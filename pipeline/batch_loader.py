from pathlib import Path
import pandas as pd


def load_scan_batch(folder_path):
    ''' 
    Loads scan files from a specified folder and creates a DataFrame with file info.
    INPUT:      - folder_path (str): Path to folder containing scan files.
    OUTPUT:     - df (Pandas DataFrame): For scan info.
                    Columns: (file_name, scan_id, file_path).
    '''

    # 1: Initialize list (file info) and Path object (the folder)
    rows = []
    folder = Path(folder_path)

    # 2: Iterate through folder, extract file_name and scan_id
    for file_path in folder.iterdir():
        name = file_path.stem
        if file_path.name.startswith(".") or not name.startswith("scan_"):
            continue
        scan_id = int(name.split("_")[1])
        rows.append({"file_name": name, "scan_id": scan_id, "file_path": str(file_path)})

    # 3: Create DataFrame and sort by scan_id
    df = pd.DataFrame(rows)
    df = df.sort_values("scan_id").reset_index(drop=True)

    return df
