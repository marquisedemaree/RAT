# RAT
**RAT - Radiology Automated Triage**<br>
AI-assisted prioritization of CT scans to accelerate detection of intracranial hemorrhage.

Project Report: http://marquisedemaree.com

## Quick Start
These instructions will help you run RAT locally for demo and evaluation.

### Prerequisites
- Git
- Python 3.10+

Not sure if you meet these requirements? Follow this guide: https://github.com/marquisedemaree/prerequisites/blob/main/README.md

### Installation
From the command line:<br>
1. Clone the repository: `git clone https://github.com/marquisedemaree/RAT.git`
2. Change the directory to RAT: `cd RAT`
3. Install dependencies: `pip install -r requirements.txt`
4. Download assets and unzip to RAT folder:
    - https://github.com/marquisedemaree/RAT/releases/download/v1.0/data.zip
    - https://github.com/marquisedemaree/RAT/releases/download/v1.0/models.zip

## Usage
Run the full RAT pipeline: `python main.py`<br>

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

## File Structure Diagram
<img width="500" height="620" alt="RAT_folder_structure" src="https://github.com/user-attachments/assets/ae6672be-b288-40fd-8777-616a63f5b838" />
