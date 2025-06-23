import pandas as pd
import numpy as np

def create_dummy_study_data(name="dummy_data.csv", seed=42, num_samples=100, min_value=0.5, max_value=12):
    """
    Create a dummy dataset of study hours and corresponding percentiles.
    
    Parameters:
    - name: Name of the CSV file to save the data.
    - seed: Random seed for reproducibility.
    - num_samples: Number of samples to generate.
    - min_hours: Minimum study hours.
    - max_hours: Maximum study hours.
    
    Returns:
    - None
    """
    # Set a seed for reproducibility
    np.random.seed(seed)

    # Generate random study times between min_hours and max_hours
    field1 = np.round(np.random.uniform(min_value, max_value, num_samples), 2)

    # Generate percentiles based on a loose correlation to study time
    # Add some noise to make it more realistic
    noise = np.random.normal(0, 10, num_samples)
    field2 = np.clip((field1 * 7) + noise, 1, 100).astype(int)

    # Create the DataFrame
    df = pd.DataFrame({
        'Time Studied (hours)': field1,
        'Percentile Reached': field2
    })

    # Save to CSV
    df.to_csv("data/" + name, index=False)

create_dummy_study_data()