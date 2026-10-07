import re
import pandas as pd


def parse_cea_output(text_data):
    rows = []
    # Split the massive file into blocks based on "Pin ="
    case_blocks = text_data.split('Pin =')

    # Regex patterns that adapt to 2 or 3 columns automatically
    patterns = {
        "Pressure_PSI": r"^\s+([\d\.]+)\s+PSIA",
        "O/F": r"O/F=\s+([\d\.]+)",
        "Tc (K)": r"T, K\s+([\d\.]+)",
        "Isp (m/s)": r"Isp, M/SEC.+\s([\d\.]+)",
        "C* (m/s)": r"CSTAR, M/SEC.+\s([\d\.]+)",
        "H2O": r"\*H2O\s+([\d\.\-eE]+)",
        "CO2": r"\*CO2\s+([\d\.\-eE]+)",
        "CO": r"\*CO\s+([\d\.\-eE]+)",
        "OH": r"\*OH\s+([\d\.\-eE]+)",
        "H2": r"\*H2\s+([\d\.\-eE]+)",
        "O2": r"\*O2\s+([\d\.\-eE]+)",
        "O": r"\*O\s+([\d\.\-eE]+)",
        "H": r"\*H\s+([\d\.\-eE]+)",
    }

    for block in case_blocks[1:]:
        row_data = {}
        p_match = re.search(patterns["Pressure_PSI"], block)

        # Extract Pressure
        if p_match:
            try:
                psi = float(p_match.group(1))
                # Convert PSI to ATM roughly
                if 430 < psi < 450:
                    row_data["Pressure_ATM"] = 30
                elif 720 < psi < 750:
                    row_data["Pressure_ATM"] = 50
                elif 870 < psi < 900:
                    row_data["Pressure_ATM"] = 60
                elif 1000 < psi < 1050:
                    row_data["Pressure_ATM"] = 70
                elif 1160 < psi < 1190:
                    row_data["Pressure_ATM"] = 80
                elif 1300 < psi < 1350:
                    row_data["Pressure_ATM"] = 90
                elif 1450 < psi < 1480:
                    row_data["Pressure_ATM"] = 100
                else:
                    row_data["Pressure_ATM"] = psi
            except ValueError:
                continue

        # Extract Data with Error Handling
        for name, pattern in patterns.items():
            if name == "Pressure_PSI": continue
            match = re.search(pattern, block)
            if match:
                try:
                    row_data[name] = float(match.group(1))
                except (IndexError, ValueError):
                    print(f"Warning: Issue parsing {name} in a block.")
                    row_data[name] = 0.0
            else:
                row_data[name] = 0.0

        if "O/F" in row_data:
            rows.append(row_data)

    df = pd.DataFrame(rows)
    return df


if __name__ == '__main__':
    raw_cea_output = """ """  # Paste raw CEA text output inside these quotes
    df_results = parse_cea_output(raw_cea_output)
    print(df_results.to_string())
    excel_filename = "CEA_Results.xlsx"
    df_results.to_excel(excel_filename, index=False)