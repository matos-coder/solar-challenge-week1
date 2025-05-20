# Exploratory Data Analysis (EDA) – Solar Challenge Week 1

This folder contains the EDA notebook for the Benin solar dataset as part of Task 2: Data Profiling, Cleaning & EDA.

## Objective

Profile, clean, and explore each country’s solar dataset end-to-end so it’s ready for comparison and region-ranking tasks.

## Workflow Overview

The notebook follows these main steps:

1. **Summary Statistics & Missing-Value Report**
   - Uses `df.describe()` to summarize numeric columns.
   - Reports missing values and flags columns with >5% nulls.

2. **Outlier Detection & Basic Cleaning**
   - Detects outliers using Z-scores (|Z| > 3) for key columns (GHI, DNI, DHI, ModA, ModB, WS, WSgust).
   - Imputes missing values in key columns with the median.
   - Removes rows with outliers.
   - Exports the cleaned DataFrame to `../data/benin_clean.csv` (not committed to git).

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

## How to Reproduce

1. Ensure you have the required dependencies installed (see `requirements.txt` in the project root).
2. Place the raw data file (`benin-malanville.csv`) in the `../data/` directory.
3. Open and run the notebook `benin_eda.ipynb` step by step.

**Note:**  
- Cleaned data is exported to `../data/benin_clean.csv` but is not tracked by git (see `.gitignore`).
- All code sections are explained with markdown cells, including references to external documentation and statistical methods.

## References

References for statistical methods and plotting functions are included as markdown cells within the notebook for each relevant section.

## Key Performance Indicators (KPIs) Addressed

- Proactivity to self-learn (references provided in notebook)
- EDA techniques to understand data and discover insights
- Demonstrating statistical understanding using suitable distributions and plots


## Cross-Country Comparison  
Key findings:  
- Benin has the highest solar potential.  
- Statistical significance confirmed via ANOVA (p < 0.05).  