# Exploratory Data Analysis (EDA) – Solar Challenge Week 1

This folder contains the EDA notebooks for the Benin, Sierra Leone, and Togo solar datasets as part of Task 2: Data Profiling, Cleaning & EDA, and the cross-country comparison analysis.

## Objective

Profile, clean, and explore each country’s solar dataset end-to-end so it’s ready for comparison and region-ranking tasks. Then, compare countries to identify the best regions for solar potential.

## Workflow Overview

The workflow is divided into two main stages:

### 1. Country-Level EDA (per-country notebooks)

Each country notebook (e.g., `benin_eda.ipynb`, `sierraleone_eda.ipynb`, `togo_eda.ipynb`) follows these steps:

1. **Summary Statistics & Missing-Value Report**
   - Uses `df.describe()` to summarize numeric columns.
   - Reports missing values and flags columns with >5% nulls.
2. **Outlier Detection & Basic Cleaning**
   - Detects outliers using Z-scores (|Z| > 3) for key columns (GHI, DNI, DHI, ModA, ModB, WS, WSgust).
   - Imputes missing values in key columns with the median.
   - Removes rows with outliers.
   - Exports the cleaned DataFrame to `../data/<country>_clean.csv` (not committed to git).
3. **Time Series Analysis**
   - Plots GHI, DNI, DHI, and Tamb vs. Timestamp to observe trends and anomalies.
4. **Cleaning Impact**
   - Groups by the 'Cleaning' flag and compares average ModA & ModB values pre/post-cleaning.
5. **Correlation & Relationship Analysis**
   - Shows a heatmap of correlations between key variables.
   - Scatter plots for WS, WSgust, WD vs. GHI; RH vs. Tamb and RH vs. GHI.
6. **Wind & Distribution Analysis**
   - Wind rose plot for wind speed/direction.
   - Histograms for GHI and WS.
7. **Temperature & Humidity Analysis**
   - Scatter plots and bubble charts to explore the relationship between RH, Tamb, and GHI.

### 2. Cross-Country Comparison (compare_countries.ipynb)

The `compare_countries.ipynb` notebook and `src/compare_countries.py` module provide a workflow to compare solar potential across all countries:

1. **Data Loading**
   - Loads cleaned data for each country and combines them into a single DataFrame with a 'Country' column.
2. **Metric Distribution Visualization**
   - Generates boxplots and other visualizations for key solar metrics (GHI, DNI, DHI) to compare distributions across countries.
3. **Descriptive Statistics**
   - Calculates summary statistics (mean, median, standard deviation, etc.) for each metric and country.
4. **Statistical Significance Testing**
   - Performs ANOVA tests to determine if observed differences in solar metrics between countries are statistically significant.
5. **Country Ranking**
   - Visualizes and ranks countries by average GHI (Global Horizontal Irradiance), highlighting regions with the highest solar potential.
6. **Key Observations**
   - Summarizes main findings, such as which country has the highest median GHI, variability in readings, and notable distribution patterns.

## How to Reproduce

1. Ensure you have the required dependencies installed (see `requirements.txt` in the project root).
2. Place the raw data files (e.g., `benin-malanville.csv`, `sierraleone-bumbuna.csv`, `togo-dapaong_qc.csv`) in the `../data/` directory.
3. Run each country EDA notebook step by step to generate cleaned data.
4. Run `compare_countries.ipynb` to perform the cross-country analysis.

**Note:**  
- Cleaned data is exported to `../data/<country>_clean.csv` but is not tracked by git (see `.gitignore`).
- All code sections are explained with markdown cells, including references to external documentation and statistical methods.
- The codebase and notebooks include expanded inline comments and docstrings to clarify complex operations and support reproducibility.

## References

References for statistical methods and plotting functions are included as markdown cells within the notebooks and as docstrings in the supporting Python modules for each relevant section.

## Key Performance Indicators (KPIs) Addressed

- Proactivity to self-learn (references provided in notebook)
- EDA techniques to understand data and discover insights
- Demonstrating statistical understanding using suitable distributions and plots
- Ability to synthesize and compare data across regions
- Use of statistical testing to support conclusions
- Clear documentation and reproducibility of analysis


