def evaluate_model(scans_df):
    '''
    Evaluates RAT performance by calculating average hemorrhage positions.
    INPUT:      - scans_df (Pandas DataFrame): Columns: (scan_id, label).
    OUTPUT:     - metrics (dict): {"fifo_avg": float, "rat_avg": float}.
    '''

    def compute_avg_positions(positions):
        if len(positions) == 0:
            return 0.0
        return sum(positions) / len(positions)

    # 1: FIFO positions based on scan_id
    fifo_positions = (
        scans_df.loc[scans_df["label"] == 1, "scan_id"] + 1
    ).tolist()

    # 2: RAT positions based on DataFrame order
    rat_positions = (
        scans_df.index[scans_df["label"] == 1] + 1
    ).tolist()

    # 3: Compute average positions for FIFO and RAT
    metrics = {
        "fifo_avg": compute_avg_positions(fifo_positions),
        "rat_avg": compute_avg_positions(rat_positions),
    }

    return metrics
