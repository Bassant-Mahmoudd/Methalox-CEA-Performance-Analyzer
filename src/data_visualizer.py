import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel File
file_path = 'data/CEA_Results.xlsx'
try:
    df = pd.read_excel(file_path)
    print("Data loaded successfully.")
except FileNotFoundError:
    print(f"Error: Could not find '{file_path}'.")
    exit()

plt.style.use('seaborn-v0_8-whitegrid')
target_pressures = [30, 60, 80, 100]

# PLOT 1: Adiabatic Flame Temp (Tc) vs O/F
plt.figure(figsize=(10, 6))
for p in target_pressures:
    subset = df[df['Pressure_ATM'] == p]
    if not subset.empty:
        plt.plot(subset['O/F'], subset['Tc (K)'], marker='o', markersize=4, label=f'{p} atm')
plt.title('Adiabatic Flame Temperature ($T_c$) vs. Mixture Ratio', fontsize=14)
plt.xlabel('Oxidizer/Fuel Ratio (O/F)', fontsize=12)
plt.ylabel('Chamber Temperature (K)', fontsize=12)
plt.legend(title='Chamber Pressure')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.savefig('Plot1_Tc_vs_OF.png', dpi=300)
plt.close()

# PLOT 2: Performance (Isp)
plt.figure(figsize=(10, 6))
for p in target_pressures:
    subset = df[df['Pressure_ATM'] == p]
    if not subset.empty:
        plt.plot(subset['O/F'], subset['Isp (m/s)'], marker='o', markersize=4, label=f'{p} atm')
plt.title('Specific Impulse ($I_{sp}$) vs. Mixture Ratio', fontsize=14)
plt.xlabel('O/F', fontsize=12)
plt.ylabel('Isp (m/s)', fontsize=12)
plt.legend(title='Pressure')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.savefig('Plot2A_Isp.png', dpi=300)
plt.close()

# PLOT 3: Performance (C*)
plt.figure(figsize=(10, 6))
for p in target_pressures:
    subset = df[df['Pressure_ATM'] == p]
    if not subset.empty:
        plt.plot(subset['O/F'], subset['C* (m/s)'], linewidth=2, label=f'{p} atm')
plt.title('Characteristic Velocity ($c^*$) vs. Mixture Ratio', fontsize=14)
plt.xlabel('O/F', fontsize=12)
plt.ylabel('c* (m/s)', fontsize=12)
plt.legend(title='Pressure')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.savefig('Plot2B_Cstar.png', dpi=300)
plt.close()

# Mass Fractions (loop for all Pressures)
for p in target_pressures:
    subset = df[df['Pressure_ATM'] == p]
    if subset.empty:
        continue

    # Main Species (H2O, CO2)
    plt.figure(figsize=(10, 6))
    plt.plot(subset['O/F'], subset['H2O'], label='$H_2O$', linewidth=2, color='blue')
    plt.plot(subset['O/F'], subset['CO2'], label='$CO_2$', linewidth=2, color='green')
    plt.title(f'Main Combustion Products at {p} atm', fontsize=14)
    plt.xlabel('Oxidizer/Fuel Ratio (O/F)', fontsize=12)
    plt.ylabel('Mass Fraction', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.savefig(f'Plot3_MainSpecies_{p}atm.png', dpi=300)
    plt.close()

    # Minor Species 1
    plt.figure(figsize=(10, 6))
    plt.plot(subset['O/F'], subset['CO'], label='$CO$', color='purple', linewidth=2)
    plt.plot(subset['O/F'], subset['O2'], label='$O_2$', color='brown', linewidth=2)
    plt.title(f'Dissociation Products ($CO, O_2$) at {p} atm', fontsize=14)
    plt.xlabel('Oxidizer/Fuel Ratio (O/F)', fontsize=12)
    plt.ylabel('Mass Fraction', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.savefig(f'Plot4_MinorSpecies_{p}atm.png', dpi=300)
    plt.close()

    # Minor Species 2
    plt.figure(figsize=(10, 6))
    plt.plot(subset['O/F'], subset['O'], label='$O$', color='purple', linewidth=2)
    plt.plot(subset['O/F'], subset['H'], label='$H$', color='brown', linewidth=2)
    plt.title(f'Dissociation Products ($O, H$) at {p} atm', fontsize=14)
    plt.xlabel('Oxidizer/Fuel Ratio (O/F)', fontsize=12)
    plt.ylabel('Mass Fraction', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.savefig(f'Plot5_MinorSpecies_{p}atm.png', dpi=300)
    plt.close()

# PLOT 4: Optimum Mixture Ratio
optimums = []
for p in target_pressures:
    sub = df[df['Pressure_ATM'] == p]
    if sub.empty: continue

    idx_max_tc = sub['Tc (K)'].idxmax()
    of_max_tc = sub.loc[idx_max_tc, 'O/F']

    idx_max_isp = sub['Isp (m/s)'].idxmax()
    of_max_isp = sub.loc[idx_max_isp, 'O/F']

    optimums.append({'Pressure': p, 'Opt_Tc': of_max_tc, 'Opt_Isp': of_max_isp})

df_opt = pd.DataFrame(optimums)

plt.figure(figsize=(10, 6))
plt.plot(df_opt['Pressure'], df_opt['Opt_Tc'], marker='o', label='Optimum O/F for Max $T_c$')
plt.plot(df_opt['Pressure'], df_opt['Opt_Isp'], marker='s', label='Optimum O/F for Max $I_{sp}$')
plt.title('Optimum Mixture Ratio vs. Chamber Pressure', fontsize=14)
plt.xlabel('Chamber Pressure (atm)', fontsize=12)
plt.ylabel('Optimum O/F Ratio', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.savefig('Plot6_Optimization.png', dpi=300)
plt.close()