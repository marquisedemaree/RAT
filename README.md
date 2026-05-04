# RAT
RAT - Radiology Automated Triage: AI-assisted prioritization of CT scans to accelerate detection of intracranial hemorrhage.

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

3. Create a Virtual Environment: `python3 -m venv .venv`

4. Activate Virtual Environment:
    - Mac: `python3 -m venv .venv`
    - Windows: `.venv\Scripts\activate` 

5. Install dependencies: `pip install -r requirements.txt`

6. Download assets and unzip to RAT folder:
    - https://github.com/marquisedemaree/RAT/releases/download/v1.0/data.zip
    - https://github.com/marquisedemaree/RAT/releases/download/v1.0/models.zip

## Usage
From the command line:

Run the full RAT pipeline: `python main.py`

This will:
    - Load demo CT scans  
    - Run hemorrhage prediction using a DenseNet121 model  
    - Reorder scans by predicted risk  
    - Evaluate triage performance  
    - Generate output visualizations  

## Features
- AI-Powered Triage: Uses a custom DenseNet121 model to estimate hemorrhage probability from CT scans  
- Automated Workflow Optimization: Reorders scans to prioritize high-risk cases  
- Medical Image Processing: Includes full DICOM preprocessing pipeline with Hounsfield Unit normalization  
- Performance Evaluation: Compares FIFO vs RAT triage efficiency using clinically meaningful metrics  
- Visualization Outputs: Generates triage charts and ranked scan tables for clear interpretation

## File Structure Diagram
<img width="500" height="620" alt="RAT_folder_structure" src="https://github.com/user-attachments/assets/ae6672be-b288-40fd-8777-616a63f5b838" />
