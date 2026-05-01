# RAT
AI-assisted prioritization of CT scans to accelerate detection of intracranial hemorrhage.
## Getting Started
These instructions will help you run RAT locally for demo and evaluation.
### Prerequisites
- Python 3.9+
- pip
### Installation
1. Clone the repository: `git clone https://github.com/marquisedemaree/RAT.git`
2. Change the directory to RAT: `cd rat`
3. Install dependencies: `pip install -r requirements.txt`
4. Download assets: `python setup_demo.py`
## Usage
Run the full RAT pipeline: `python main.py`
This will:
1. Load demo CT scans  
2. Run hemorrhage prediction using a DenseNet121 model  
3. Reorder scans by predicted risk  
4. Evaluate triage performance  
5. Generate output visualizations  
## Features
- AI-Powered Triage: Uses a custom DenseNet121 model to estimate hemorrhage probability from CT scans  
- Automated Workflow Optimization: Reorders scans to prioritize high-risk cases  
- Medical Image Processing: Includes full DICOM preprocessing pipeline with Hounsfield Unit normalization  
- Performance Evaluation: Compares FIFO vs RAT triage efficiency using clinically meaningful metrics  
- Visualization Outputs: Generates triage charts and ranked scan tables for clear interpretation
