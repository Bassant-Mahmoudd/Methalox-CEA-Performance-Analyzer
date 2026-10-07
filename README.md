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

## How to Run
1. Clone the repository to your local machine.
2. Ensure Python, Pandas, and Matplotlib are installed.
3. Execute the pipeline from the root directory:
   ```bash
   python main.py
