import pandas as pd
import joblib
import os

def load_model(model_path):
    """
    Load the trained machine learning model from a file.

    Args:
        model_path (str): Path to the saved model file.

    Returns:
        model: Loaded machine learning model.
    """
    return joblib.load(model_path)

def preprocess_input(input_data):
    """
    Preprocess the input data to match the model's expected format.

    Args:
        input_data (dict or pd.DataFrame): Raw input data.

    Returns:
        pd.DataFrame: Preprocessed data ready for prediction.
    """
    # Convert input data to DataFrame if it's a dictionary
    if isinstance(input_data, dict):
        input_data = pd.DataFrame([input_data])

    # Perform necessary preprocessing steps
    # Example: Ensure the input data has the same columns as the training data
    expected_columns = ['feature1', 'feature2', 'feature3']  # Replace with actual feature names
    input_data = input_data[expected_columns]

    # Apply any required transformations (e.g., scaling, encoding) here

    return input_data

def make_prediction(model, input_data):
    """
    Make a prediction using the loaded model and preprocessed input data.

    Args:
        model: Loaded machine learning model.
        input_data (pd.DataFrame): Preprocessed input data.

    Returns:
        np.ndarray: Model predictions.
    """
    return model.predict(input_data)

def main():
    # Define the path to the saved model
    model_path = os.path.join('models', 'random_forest_model.pkl')

    # Load the trained model
    model = load_model(model_path)

    # Example input data (replace with actual input)
    input_data = {
        'feature1': 5.1,
        'feature2': 3.5,
        'feature3': 1.4
        # Add all required features here
    }

    # Preprocess the input data
    preprocessed_data = preprocess_input(input_data)

    # Make prediction
    prediction = make_prediction(model, preprocessed_data)

    # Output the prediction
    print(f'Predicted class: {prediction[0]}')

if __name__ == "__main__":
    main()
