import matplotlib.pyplot as plt
from config import TRIAGE_METRICS_OUT, TRIAGE_TABLE_OUT


def plot_triage_simulation(metrics, ax=None):
    '''
    Plots the triage simulation results.
    INPUT:      - metrics (dict): Performance metrics for FIFO and RAT.
                    Entries: {"fifo_avg": float, "rat_avg": float}.
                - ax (matplotlib.axes.Axes): Axes object to plot on.
    '''

    # 1: Create bar chart comparing FIFO and RAT average positions
    if ax is None:
        ax = plt.gca()

    # 2: Prepare data for plotting
    labels = ["FIFO", "RAT"]
    values = [metrics["fifo_avg"], metrics["rat_avg"]]

    # 3: Create bar chart
    bars = ax.bar(labels, values, color="#dc3545")
    ax.set_title("Average Hemorrhage Queue Position", fontsize=16)
    ax.tick_params(axis="x", labelsize=16)
    ax.set_ylim(0, 60)

    # 4: Add value labels on top of bars
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.02,
            f"{value:.2f}",
            ha="center",
            va="bottom",
            fontsize=16
        )

def save_triage_chart(metrics, file_name=TRIAGE_METRICS_OUT):
    '''
    Saves the triage simulation chart to a file.
    INPUT:      - metrics (dict): Performance metrics for FIFO and RAT.
                    Entries: {"fifo_avg": float, "rat_avg": float}.
                - file_name (str): Name of the file to save the chart to.
    '''

    # 1: Create figure and plot triage simulation results
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    plot_triage_simulation(metrics, ax=ax)
    plt.tight_layout()

    # 2: Save the figure to a file
    plt.savefig(file_name, dpi=300, bbox_inches="tight")
    plt.close(fig)

    # 3: Print confirmation message
    print(f"✅ Saved triage results to {file_name}")

def save_rat_triage_table(scans_df, file_name=TRIAGE_TABLE_OUT):
    '''
    Saves the RAT triage table to a file.
    INPUT:      - scans_df (Pandas DataFrame): Scan data.
                    Columns: (file_name, scan_id, file_path, hemorrhage_probability, label).
                - file_name (str): Name of the file to save the table to.
    '''

    # 1: Create a copy of scans_df for the table and reset index
    table_df = scans_df.copy().reset_index(drop=True)

    # 2: Calculate queue position and change in queue position for each scan
    table_df["queue_position"] = table_df.index + 1
    table_df["change_in_queue_position"] = (
        table_df["scan_id"] - table_df["queue_position"]
    )

    # 3: Select columns for the table
    table_df = table_df[
        [
            "queue_position",
            "scan_id",
            "change_in_queue_position",
            "hemorrhage_probability",
            "label"
        ]
    ].copy()

    # 4: Format "change_in_queue_position" with +/-
    table_df["change_in_queue_position"] = table_df[
        "change_in_queue_position"
    ].map(lambda x: f"{x:+d}")

    # 5: Format "hemorrhage_probability" to 3 decimal places
    table_df["hemorrhage_probability"] = table_df[
        "hemorrhage_probability"
    ].map(lambda x: f"{x:.3f}")

    # 6: Create figure and axis for the table
    fig, ax = plt.subplots(figsize=(12, max(4, len(table_df) * 0.45)))
    ax.axis("off")
    ax.set_title("RAT Triage Order", fontsize=16)

    # 7: Create the table with formatted data
    table = ax.table(
        cellText=table_df.values,
        colLabels=[
            "Queue Position",
            "Scan ID",
            "Change",
            "Hemorrhage Probability",
            "Label"
        ],
        cellLoc="center",
        loc="upper center"
    )

    # 8: Style the table
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.6)

    # 9: Color header row and positive cases
    for col in range(len(table_df.columns)):
        cell = table[(0, col)]
        cell.set_facecolor("#dc3545")
        cell.set_text_props(color="white", weight="bold")

    # 10: Color rows based on label (red for positive, white for negative)
    for row in range(len(table_df)):
        is_positive = scans_df.iloc[row]["label"] == 1
        for col in range(len(table_df.columns)):
            cell = table[(row + 1, col)]
            if is_positive:
                cell.set_facecolor("#f8d7da")
            else:
                cell.set_facecolor("white")

    # 11: Adjust layout and save the figure to a file
    plt.tight_layout()
    plt.savefig(file_name, dpi=300, bbox_inches="tight")
    plt.close(fig)

    # 12: Print confirmation message
    print(f"✅ Saved RAT triage table to {file_name}")

def visualization(metrics, scans_df):
    '''
    Visualizes the triage performance results.
    INPUT:      - metrics (dict): Performance metrics for FIFO and RAT.
                    Entries: {"fifo_avg": float, "rat_avg": float}.
                - scans_df (Pandas DataFrame): Scan data.
                    Columns: (file_name, scan_id, file_path, hemorrhage_probability, label).
    '''

    # 1: Plot triage simulation results and save chart
    save_triage_chart(metrics)

    # 2: Save RAT triage table with scan details
    save_rat_triage_table(scans_df)
