# Methalox-CEA-Performance-Analyzer

## Overview
This repository contains a comprehensive computational simulation and data processing pipeline for analyzing the theoretical performance of a liquid bipropellant rocket engine using data derived from the NASA Chemical Equilibrium with Applications (CEA) software. 

The simulation models a modern **Liquid Oxygen / Liquid Methane (Methalox)** propulsion system—the propellant architecture powering next-generation launch vehicles like SpaceX Starship. The engine performance was simulated across an operational matrix of Oxidizer-to-Fuel ($O/F$) ratios (2.0 to 6.0) and high-pressure chamber conditions (30 atm to 100 atm).

## Simulation Scope & Core Physics
The software engine and data pipeline evaluate key rocket propulsion phenomena:
1.  **Chemical Equilibrium & Adiabatic Flame Temperature ($T_c$):** Simulates the maximum thermal energy release across varying mixture ratios and pressure boundaries.
2.  **Performance Metrics ($I_{sp}$ & $c^*$):** Computes specific impulse ($I_{sp}$) and characteristic velocity ($c^*$) to evaluate overall motor efficiency.
3.  **Dissociation & Species Mass Fractions:** Tracks primary combustion products ($CO_2, H_2O, CO, H_2$) and minor dissociation species ($O, O_2, H, OH$) to analyze how high chamber pressures suppress chemical dissociation and promote recombination.
4.  **Optimum Mixture Ratio Analysis:** Numerically determines the divergence between the mixture ratio that maximizes chamber temperature ($O/F \approx 3.8$) versus the ratio that maximizes specific impulse ($O/F \approx 3.2$), proving how exhaust molecular weight ($\mathcal{M}$) dictates performance.

## Repository Architecture
The project is structured as a modular software pipeline:
*   `main.py`: The top-level executive script managing data ingestion and execution flow.
*   `src/cea_parser.py`: A data engineering script utilizing Regular Expressions (`re`) to parse complex unformatted simulation text blocks into clean Pandas dataframes.
*   `src/data_visualizer.py`: An automated visualization suite utilizing `matplotlib` to render publication-ready thermodynamic and chemical species dashboards.
*   `data/`: Directory containing the structured simulation datasets (`CEA_Results.xlsx`).

## Key Thermodynamic Findings
*   **The Molecular Weight Trade-Off:** While stoichiometric mixtures maximize thermal energy ($T_c$), running slightly fuel-rich introduces unburnt low-mass species ($H_2$ and $CO$) into the exhaust. Because $I_{sp} \propto \sqrt{T_c / \mathcal{M}}$, reducing the exhaust molecular weight yields higher specific impulse, shifting peak efficiency away from maximum temperature.
*   **Chamber Pressure Effects:** Increasing chamber pressure up to 100 atm actively suppresses the dissociation of $CO_2$ and $H_2O$, converting more chemical energy into sensible heat and boosting performance metrics.


<img width="3000" height="1800" alt="Plot5_Optimization" src="https://github.com/user-attachments/assets/e648183a-7a1b-4dfb-967d-45763edbb39a" />
<img width="3000" height="1800" alt="Plot3_MainSpecies_100atm" src="https://github.com/user-attachments/assets/7f596246-f72d-4615-992b-8efc5078c4c8" />
<img width="3000" height="1800" alt="Plot3_MainSpecies_80atm" src="https://github.com/user-attachments/assets/8a7c95e0-7da4-4b5c-afab-28fa8d5025f6" />
<img width="3000" height="1800" alt="Plot3_MainSpecies_60atm" src="https://github.com/user-attachments/assets/d5eb497f-2078-4be8-9158-20c4473d6321" />
<img width="3000" height="1800" alt="Plot3_MainSpecies_30atm" src="https://github.com/user-attachments/assets/bc08a4d4-5f9a-4144-aef3-bd830f47bf0f" />
<img width="3000" height="1800" alt="Plot2B_Cstar" src="https://github.com/user-attachments/assets/9bfb4c1f-43fe-44ef-bd1c-e062d0b24fc0" />
<img width="3000" height="1800" alt="Plot2A_Isp" src="https://github.com/user-attachments/assets/d970a817-066c-46f1-b12d-b8bbbd832b8c" />
<img width="3000" height="1800" alt="Plot1_Tc_vs_OF" src="https://github.com/user-attachments/assets/b8fb134b-cc9e-4c20-930a-7b1dc341b2be" />


## How to Run
1. Clone the repository to your local machine.
2. Ensure Python, Pandas, and Matplotlib are installed.
3. Execute the pipeline from the root directory:
   ```bash
   python main.py
