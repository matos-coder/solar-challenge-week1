"""
Cross-Country Solar Analysis Module

This script compares solar energy metrics across multiple countries through:
- Visual distribution analysis (boxplots)
- Descriptive statistics
- Statistical significance testing
- Country ranking by solar potential

Functions:
    load_clean_data: Loads and combines cleaned datasets
    generate_comparison_plots: Creates visualization plots
    calculate_summary_stats: Generates descriptive statistics
    perform_anova_test: Checks metric differences significance
    plot_ghi_ranking: Displays country ranking by solar potential
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os
from typing import Dict, List

# --------------------------
# Data Loading Functions
# --------------------------

def load_clean_data(countries: List[str], data_dir: str = '../data') -> pd.DataFrame:
    """
    Load and combine cleaned datasets from multiple countries
    
    Args:
        countries: List of country names (matching CSV filenames)
        data_dir: Directory containing cleaned CSV files
        
    Returns:
        Combined DataFrame with 'Country' column added
        
    Raises:
        FileNotFoundError: If any country file is missing
    """
    dfs = {}
    for country in countries:
        file_path = os.path.join(data_dir, f'{country}_clean.csv')
        if os.path.exists(file_path):
            dfs[country] = pd.read_csv(file_path)
        else:
            raise FileNotFoundError(
                f"Cleaned data for {country} not found at {file_path}. "
                "Run Task 2 EDA first."
            )
    
    return pd.concat(
        [df.assign(Country=country.capitalize()) 
         for country, df in dfs.items()],
        ignore_index=True
    )

# --------------------------
# Visualization Functions
# --------------------------

def generate_comparison_plots(df: pd.DataFrame, metrics: List[str] = ['GHI', 'DNI', 'DHI']) -> None:
    """
    Generate comparative boxplots for solar metrics
    
    Args:
        df: Combined DataFrame with 'Country' column
        metrics: List of metrics to visualize
    """
    plt.figure(figsize=(15, 5))
    
    for i, metric in enumerate(metrics, 1):
        plt.subplot(1, len(metrics), i)
        sns.boxplot(
            x='Country', 
            y=metric, 
            data=df, 
            hue='Country',
            palette='viridis', 
            legend=False
        )
        plt.title(f'{metric} Distribution')
        plt.xlabel('')  # Cleaner layout
    
    plt.tight_layout()
    plt.show()

def plot_ghi_ranking(df: pd.DataFrame) -> None:
    """
    Display country ranking by average GHI
    
    Args:
        df: Combined DataFrame containing GHI values
    """
    ghi_means = (
        df.groupby('Country')['GHI']
        .mean()
        .sort_values(ascending=False)
    )
    
    plt.figure(figsize=(8, 4))
    ghi_means.plot(
        kind='bar', 
        color=['#2ca02c', '#1f77b4', '#d62728'],
        edgecolor='black'
    )
    plt.title('Country Ranking by Average Global Horizontal Irradiance (GHI)')
    plt.ylabel('GHI (kWh/m²)')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()

# --------------------------
# Statistical Functions
# --------------------------

def calculate_summary_stats(df: pd.DataFrame, metrics: List[str]) -> pd.DataFrame:
    """
    Calculate descriptive statistics for key metrics
    
    Args:
        df: Combined DataFrame with metrics
        metrics: List of columns to analyze
        
    Returns:
        Multi-index DataFrame with mean, median, and std
    """
    return df.groupby('Country')[metrics].agg(['mean', 'median', 'std'])

def perform_anova_test(dfs: Dict[str, pd.DataFrame], metrics: List[str]) -> Dict[str, float]:
    """
    Perform ANOVA tests for metric differences between countries
    
    Args:
        dfs: Dictionary of original country DataFrames
        metrics: List of metrics to test
        
    Returns:
        Dictionary of metric:p-value pairs
    """
    results = {}
    for metric in metrics:
        groups = [df[metric].dropna() for df in dfs.values()]
        results[metric] = stats.f_oneway(*groups).pvalue
    
    return results
