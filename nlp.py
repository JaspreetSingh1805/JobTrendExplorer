import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
df = pd.read_csv("customise2.csv")

# Split the skills into individual skills
# all_skills = df['extracted_skills'].str.split(',').explode().str.strip()
all_skills = df['company-name'].str.split(',').explode().str.strip()

# Get the top 20 skills by frequency
top_20_skills = all_skills.value_counts().nlargest(20)

# Plot the data
top_20_skills.plot(kind='bar', figsize=(15, 6), color='skyblue')

# Set the labels and title
plt.title('Top 20 Companies name by Frequency')
plt.xlabel('Company-name')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()


