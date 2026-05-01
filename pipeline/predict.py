from tqdm import tqdm
import pydicom
from rsna.preprocess import rsna_preprocess
from rsna.inference import predict_hemorrhage_probability


def get_predictions(scans_df, labels_df, model):
    '''
    Runs inference on each scan in scans_df using the provided model,
    updates the DataFrame with predictions and true labels.
    INPUT:      - scans_df (Pandas DataFrame): Scan file info.
                    Columns: (file_name, scan_id, file_path).
                - labels_df (Pandas DataFrame): Scan labels.
                    Columns: (file_name, label).
                - model (RSNADenseNet121): The pre-trained model for inference.
    '''
    
    # 1: Create a mapping from file_name to label for quick lookup
    label_map = dict(zip(labels_df["file_name"], labels_df["label"]))

    # 2: Iterate through scans_df with a progress bar
    for idx, row in tqdm(
        scans_df.iterrows(),
        total=len(scans_df),
        desc="Running inference",
        unit="scan"
    ):
        
        # 2.1: Load DICOM, preprocess, and predict hemorrhage probability
        dicom = pydicom.dcmread(row["file_path"])
        image_tensor = rsna_preprocess(dicom)
        prob = predict_hemorrhage_probability(model, image_tensor)

        # 2.2: Get true label from labels_df using file_name
        file_name = row["file_name"]
        label = label_map[file_name]

        # 2.3: Update scans_df with predicted probability and true label
        scans_df.at[idx, "hemorrhage_probability"] = prob
        scans_df.at[idx, "label"] = label
