from generate_dataset import create_city_dataset
from generate_dataset_part2 import get_more_cities
import json

def combine_datasets():
    # Get the first part of the dataset
    dataset = create_city_dataset()
    
    # Add more cities from part 2
    dataset.extend(get_more_cities())
    
    # Save the combined dataset
    with open('src/dataset.json', 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
    
    print(f"Combined dataset created with {len(dataset)} cities")

if __name__ == "__main__":
    combine_datasets() 