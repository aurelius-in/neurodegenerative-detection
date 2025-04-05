import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df, column):
    """
    Plot the distribution of a specified column using a histogram and kernel density estimate (KDE).

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        column (str): The column name to plot.

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, color='blue')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def plot_correlation_heatmap(df):
    """
    Plot a heatmap of the correlation matrix for the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.show()

def plot_scatter(df, x_column, y_column, hue=None):
    """
    Create a scatter plot between two numerical columns, with an optional categorical hue.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        x_column (str): The column name for the x-axis.
        y_column (str): The column name for the y-axis.
        hue (str, optional): The column name for color encoding. Defaults to None.

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_column, y=y_column, hue=hue, palette='viridis', alpha=0.7)
    plt.title(f'Scatter Plot of {y_column} vs {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.legend(title=hue)
    plt.grid(True)
    plt.show()

def plot_categorical_count(df, column):
    """
    Plot the count of occurrences for each category in a categorical column.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        column (str): The categorical column name to plot.

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=column, palette='Set2')
    plt.title(f'Count of Categories in {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

def plot_pairwise_relationships(df, columns):
    """
    Plot pairwise relationships between specified columns.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        columns (list): List of column names to include in the pair plot.

    Returns:
        None
    """
    sns.pairplot(df[columns], diag_kind='kde', markers='+', plot_kws={'alpha': 0.6})
    plt.suptitle('Pairwise Relationships', y=1.02)
    plt.show()
