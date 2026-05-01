from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Core paths
MODEL_PATH = BASE_DIR / "models" / "rsna_model.pth"
DEMO_FOLDER = BASE_DIR / "data" / "demo_scans"
DEMO_LABELS = BASE_DIR / "data" / "demo_labels.csv"

# Output paths
OUTPUT_DIR = BASE_DIR / "output"
TRIAGE_METRICS_OUT = OUTPUT_DIR / "triage_metrics.png"
TRIAGE_TABLE_OUT = OUTPUT_DIR / "triage_order.png"

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
