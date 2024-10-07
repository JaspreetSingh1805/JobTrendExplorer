import pandas as pd

# Load the CSV file
df = pd.read_csv('new4location.csv')

# Function to keep only one city from the 'extracted_cities' column
def keep_one_city(cities):
    if pd.isna(cities):
        return cities  # If NaN, return as is
    city_list = cities.split(",")  # Split by comma if there are multiple cities
    return city_list[0]  # Return the first city in the list

# Apply the function to the 'extracted_cities' column
df['extracted_cities'] = df['extracted_cities'].apply(keep_one_city)

# Save the modified CSV file
df.to_csv('modified_new4location.csv', index=False)

print("Updated CSV file saved as 'modified_new4location.csv'.")
