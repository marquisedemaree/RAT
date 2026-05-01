import torch
from rsna.model import RSNADenseNet121


def load_rsna_model(checkpoint_path):
    '''
    Loads a pre-trained RSNADenseNet121 model from a checkpoint file.
    INPUT:      - checkpoint_path (str): Path to the checkpoint file.
    OUTPUT:     - model (RSNADenseNet121): The loaded model.
    '''

    # 1: Load the checkpoint and extract the state_dict
    checkpoint = torch.load(checkpoint_path, map_location="cpu")
    state_dict = checkpoint["state_dict"]

    # 2: Remove "module." prefix from state_dict keys if present (for DataParallel compatibility)
    clean_state_dict = {
        key.replace("module.", ""): value
        for key, value in state_dict.items()
    }

    # 3: Initialize the model, load the state_dict, and set to evaluation mode
    model = RSNADenseNet121()
    model.load_state_dict(clean_state_dict)
    model.eval()

    return model

def predict_hemorrhage_probability(model, image_tensor):
    """
    Runs inference on a preprocessed image tensor.
    INPUT:      - model (RSNADenseNet121): The pre-trained model for inference.
                - image_tensor (torch.Tensor): Preprocessed image tensor.
                    Shape: [1, 3, 512, 512].
    OUTPUT:     - probability (float): Predicted probability of intracranial hemorrhage.
    """

    # Run the model in inference mode (no gradient calculation)
    with torch.no_grad():
        logits = model(image_tensor)
        probability = torch.sigmoid(logits)

    return  probability[0][0].item()
