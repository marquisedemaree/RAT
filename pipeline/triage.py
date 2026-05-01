def triage_scans(scans_df):
    '''
    Sorts scans in-place by predicted hemorrhage probability in descending order.
    INPUT:      scans_df (Pandas DataFrame): Scan info with predictions.
                    Columns: (file_name, scan_id, file_path, hemorrhage_probability, label).
    '''

    # 1: Sort scans_df by hemorrhage_probability in descending order
    scans_df.sort_values(by="hemorrhage_probability", ascending=False, inplace=True)
    
    # 2: Reset index to reflect new order
    scans_df.reset_index(drop=True, inplace=True)
