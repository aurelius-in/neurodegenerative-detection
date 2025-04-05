import unittest
import pandas as pd
from src.data import make_dataset

class TestMakeDataset(unittest.TestCase):

    def setUp(self):
        # Sample data to use in tests
        self.raw_data = pd.DataFrame({
            'age': [25, 30, 35, None],
            'gender': ['male', 'female', 'female', 'male'],
            'income': [50000, 60000, None, 80000]
        })

    def test_clean_data(self):
        # Assuming make_dataset has a function named clean_data
        cleaned_data = make_dataset.clean_data(self.raw_data)
        
        # Check for missing values
        self.assertFalse(cleaned_data.isnull().values.any(), "Data contains null values after cleaning")

    def test_feature_engineering(self):
        # Assuming make_dataset has a function named add_features
        featured_data = make_dataset.add_features(self.raw_data)
        
        # Check if new feature 'income_per_age' is created
        self.assertIn('income_per_age', featured_data.columns, "Feature 'income_per_age' not found in data")

if __name__ == '__main__':
    unittest.main()
