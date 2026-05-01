# RAT
AI-assisted prioritization of CT scans to accelerate detection of intracranial hemorrhage.
## Getting Started
These instructions will help you run RAT locally for demo and evaluation.
### Prerequisites
- Python 3.9+
- pip
### Installation
1. Clone the repository: `git clone https://github.com/your-username/rat.git`
2. Change the directory to RAT: `cd rat`
3. Install dependencies: `pip install -r requirements.txt`
## Usage
Run the full RAT pipeline: `python main.py`
This will:
1. Load demo CT scans  
2. Run hemorrhage prediction using a DenseNet121 model  
3. Reorder scans by predicted risk  
4. Evaluate triage performance  
5. Generate output visualizations  
