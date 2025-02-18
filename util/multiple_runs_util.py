#! /usr/bin/env python
'''
Utility module to run multiple iterations of the genetic algorithm 
'''

from typing import List, Dict, Any
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# TODO: 3. Estadísticas descripticas del DF
def compute_row_statistics(df):
    """
    Compute the mean and variance of each row in the given DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    pd.DataFrame: A new DataFrame with two columns: 'row_Mean' and 'row_Variance'.
    """
    row_stats = pd.DataFrame({
        'row_mean': df.mean(axis=1),
        'row_variance': df.var(axis=1)
    })
    return row_stats


# TODO: 2. Graficar el DF
# TODO! Mejorar la gráfica para que visualmente se vea mejor!
def plot_row_statistics(row_stats_df, stat):
    """
    Plot a line chart for a specified statistic in the row_stats_df DataFrame.

    Parameters:
    row_stats_df (pd.DataFrame): The DataFrame containing row statistics.
    stat (str): The column to be plotted.

    Returns:
    None
    """
    if stat not in row_stats_df.columns:
        raise ValueError(f"Column '{stat}' not found in DataFrame.")

    plt.figure(figsize=(10, 5))
    plt.plot(row_stats_df.index, row_stats_df[stat], marker='o', linestyle='-', label=stat)
    plt.xlabel('Row Index')
    plt.ylabel(stat)
    plt.title(f'Line Plot of {stat}')
    plt.legend()
    plt.grid(True)
    plt.show()


# TODO: 4. Exportar el DF en diferentes formatos
# TODO! Should export only the numeric value of the fitness function 
# TODO! Verificar la carpeta donde voy a imprimir los resutlados de la simulación 
def export_results(df, param): 
    """
    Export results into an external file

    Args:
        df (pd.DataFrame): The DataFrame with the results of the simmulation 
    """
    
    # Current working directory
    cwd = Path.cwd()
    
    # Directory where the results are goint to be store 
    results_dir = cwd / param["output_dir"]
    
    # Ensure the results directory exists
    results_dir.mkdir(parents=True, exist_ok=True)
    
    # Select between: csv, xlsx, and parquet file formats 
    if param["file_format"] == "csv": 
        df.to_csv(results_dir / "results.csv", index = False)  
    elif param["file_format"] == "xlsx": 
        df.to_excel(results_dir / "results.xlsx", index = False)
    elif param["file_format"] == "parquet":
        df.to_parquet(results_dir / "results.parquet", index = False)
    else: 
        ValueError("Unsupported file format. Choose from 'csv', 'xlsx', or 'parquet'.")    