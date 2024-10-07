import pandas as pd

# Load the CSV file
df = pd.read_csv('modified_new5location.csv')

# Fill NaN values in the 'extracted_skills' column with a default value (e.g., 'Not Specified')
df['extracted_skills'].fillna('NaN', inplace=True)
df['Timings'].fillna('NaN', inplace=True)

# Save the modified DataFrame back to a CSV file
df.to_csv('modified_new6location.csv', index=False)

print("NaN values in 'extracted_skills' column have been filled.")
