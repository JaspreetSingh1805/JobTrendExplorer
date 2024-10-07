# import os
# import pandas as pd

# # Specify the folder where your CSV files are located
# folder_path = 'C:\\Users\\VIRENDER\\OneDrive\\Desktop\\CSV'


# # Create an empty list to store each DataFrame
# all_data = []

# # Loop through each file in the folder
# for file in os.listdir(folder_path):
#     if file.endswith('.csv'):
#         # Read the CSV file into a DataFrame
#         file_path = os.path.join(folder_path, file)
#         df = pd.read_csv(file_path)
#         all_data.append(df)

# # Concatenate all DataFrames into one
# combined_data = pd.concat(all_data, ignore_index=True)

# # Save the combined data into a single CSV file
# combined_data.to_csv('combined_file.csv', index=False)

# print("All CSV files have been combined into 'combined_file1.csv")



