# =====================================================================
# Main Execution Script: NASA CEA Propulsion Data Pipeline
# Project: Methalox Rocket Engine Performance & Dissociation Analysis
# =====================================================================

import os
import sys

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from cea_parser import parse_cea_output
from data_visualizer import generate_visualizations


def main():
    print("--- 1. Initializing NASA CEA Data Pipeline ---")

    # Path configurations
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)
    excel_path = os.path.join(data_dir, "CEA_Results.xlsx")

    # Check if dataset exists, otherwise run parser on raw template
    if not os.path.exists(excel_path):
        print("Processed dataset not found. Running parser...")

        # Placeholder or raw text integration point
        raw_cea_output = """ 
        # Paste or stream your raw NASA CEA text output here if re-parsing from scratch, 
        # or ensure 'CEA_Results.xlsx' is pre-loaded into the data directory.
        """

        if raw_cea_output.strip() == "":
            print("[INFO] No raw text block provided in main.py.")
            print("[INFO] Please place your pre-parsed 'CEA_Results.xlsx' inside the /data/ directory,")
            print("[INFO] or paste your raw text into raw_cea_output to execute the RegEx pipeline.")
            return

        df_results = parse_cea_output(raw_cea_output)
        df_results.to_excel(excel_path, index=False)
        print(f"Successfully generated dataset at: {excel_path}")
    else:
        print(f"Found existing dataset at: {excel_path}")

    print("\n--- 2. Executing Data Visualization Engine ---")
    # This triggers the plotting suite inside data_visualizer.py
    # (Ensure data_visualizer.py points to 'data/CEA_Results.xlsx')
    import data_visualizer

    print("\nPipeline execution complete! Check output directory for generated plots.")


if __name__ == "__main__":
    main()