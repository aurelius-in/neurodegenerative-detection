import os
import json
import pandas as pd

def load_json(filepath):
    """
    Load a JSON file and return its content.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        dict: Parsed content of the JSON file.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, filepath):
    """
    Save data to a JSON file.

    Args:
        data (dict): Data to be saved.
        filepath (str): Path to the JSON file.

    Returns:
        None
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_csv(filepath):
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the CSV data.
    """
    return pd.read_csv(filepath)

def save_csv(dataframe, filepath):
    """
    Save a pandas DataFrame to a CSV file.

    Args:
        dataframe (pd.DataFrame): DataFrame to be saved.
        filepath (str): Path to the CSV file.

    Returns:
        None
    """
    dataframe.to_csv(filepath, index=False)

def ensure_directory_exists(directory):
    """
    Ensure that a directory exists; if not, create it.

    Args:
        directory (str): Path to the directory.

    Returns:
        None
    """
    os.makedirs(directory, exist_ok=True)
