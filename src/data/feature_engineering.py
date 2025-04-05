import pandas as pd
import numpy as np

def add_interaction_features(df):
    """
    Create interaction features by multiplying pairs of numerical features.

    Args:
        df (pd.DataFrame): DataFrame containing the dataset.

    Returns:
        pd.DataFrame: DataFrame with new interaction features added.
    """
    df['feature1_feature2'] = df['feature1'] * df['feature2']
    df['feature3_feature4'] = df['feature3'] * df['feature4']
    # Add more interaction features as needed
    return df

def encode_categorical_features(df):
    """
    Encode categorical features using one-hot encoding.

    Args:
        df (pd.DataFrame): DataFrame containing the dataset.

    Returns:
        pd.DataFrame: DataFrame with categorical features encoded.
    """
    categorical_cols = ['categorical_column1', 'categorical_column2']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    return df

def scale_features(df):
    """
    Scale numerical features to have zero mean and unit variance.

    Args:
        df (pd.DataFrame): DataFrame containing the dataset.

    Returns:
        pd.DataFrame: DataFrame with scaled numerical features.
    """
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    numerical_cols = ['numerical_column1', 'numerical_column2']
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    return df

def main():
    # Define file paths
    input_path = '../../data/interim/cleaned_data.csv'
    output_path = '../../data/processed/feature_engineered_data.csv'

    # Load cleaned data
    df = pd.read_csv(input_path)

    # Apply feature engineering functions
    df = add_interaction_features(df)
    df = encode_categorical_features(df)
    df = scale_features(df)

    # Save the feature-engineered data
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    main()
