import pandas as pd

# Load the CSV file
df = pd.read_csv("new1location.csv")

# Ensure 'Capital_Cities' and 'title' columns are clean and have proper values
df['Capital_Cities'] = df['Capital_Cities'].fillna('Not a Capital')
df['title'] = df['title'].fillna('Unknown')

# Exclude rows where the city is "Not a Capital"
filtered_df = df[df['Capital_Cities'] != 'Not a Capital']

print(filtered_df)

# Group by 'Capital_Cities' and 'title' and count the occurrences
city_job_counts = filtered_df.groupby(['Capital_Cities', 'title']).size().reset_index(name='count')

print(city_job_counts)

# For each city, find the job with the maximum count
most_common_jobs = city_job_counts.loc[city_job_counts.groupby('Capital_Cities')['count'].idxmax()]

# Display the most common job in each city
print(most_common_jobs)

# Save the result to a CSV file if needed
most_common_jobs.to_csv("most_common_jobs_in_cities.csv", index=False)

# Plotting the most common job in each city (optional)
import matplotlib.pyplot as plt

plt.figure(figsize=(15, 6))
most_common_jobs.plot(kind='barh', x='Capital_Cities', y='count', color='skyblue', legend=False)

font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

# Set labels and title
plt.title('Most Common Jobs in Each City', fontdict=font1)
plt.xlabel('Number of Jobs', fontdict=font2)
plt.ylabel('City', fontdict=font2)
plt.tight_layout()

# Add grid for readability
plt.grid(color='green', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()
