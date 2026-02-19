"""
Example data collector script for Dazal Black project.

This script demonstrates how to structure a data collection module.
"""

def collect_sample_data():
    """
    Collect sample data.
    
    Returns:
        list: A list of sample data items
    """
    sample_data = [
        {"id": 1, "name": "Sample 1", "value": 100},
        {"id": 2, "name": "Sample 2", "value": 200},
        {"id": 3, "name": "Sample 3", "value": 300},
    ]
    return sample_data


def save_data(data, filename="data/sample_output.json"):
    """
    Save data to a file.
    
    Args:
        data: The data to save
        filename: The output filename
    """
    import json
    import os
    
    # Create data directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Data saved to {filename}")


def main():
    """Main function to run the data collection process."""
    print("Starting data collection...")
    data = collect_sample_data()
    print(f"Collected {len(data)} items")
    
    # Uncomment the line below to save data
    # save_data(data)
    
    print("Data collection complete!")
    return data


if __name__ == "__main__":
    main()
