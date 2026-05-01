import pandas as pd
from pipeline.batch_loader import load_scan_batch
from rsna.inference import load_rsna_model
from pipeline.predict import get_predictions
from pipeline.triage import triage_scans
from evaluation.model_evaluator import evaluate_model
from visualization.plots import visualization
from config import DEMO_FOLDER, DEMO_LABELS, MODEL_PATH


def main():

    # 1: LOAD DATA & MODEL
    scans_df = load_scan_batch(DEMO_FOLDER)
    labels_df = pd.read_csv(DEMO_LABELS)
    model = load_rsna_model(MODEL_PATH)
    
    # 2: PREDICT HEMORRHAGE PROBABILITIES
    get_predictions(scans_df, labels_df, model)

    # 3: TRIAGE SCANS
    triage_scans(scans_df)

    # 4: PERFORMANCE METRICS
    metrics = evaluate_model(scans_df)

    # 5: VISUALIZE RESULTS
    visualization(metrics, scans_df)

if __name__ == "__main__":
    main()
