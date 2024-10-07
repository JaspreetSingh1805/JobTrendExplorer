import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("new1location.csv")



# Ensure 'Capital_Cities' and 'title' columns are clean and have proper values
df['Capital_Cities'] = df['Capital_Cities'].fillna('Not a Capital')
df['title'] = df['title'].fillna('Unknown')

# Exclude rows where the city is "Not a Capital"
filtered_df = df[df['Capital_Cities'] != 'Not a Capital']

# Group by 'Capital_Cities' and 'title' and count the occurrences
city_job_counts = filtered_df.groupby(['Capital_Cities', 'title']).size().reset_index(name='count')

print(city_job_counts)

# For each city, find the job with the maximum count
most_common_jobs = city_job_counts.loc[city_job_counts.groupby('Capital_Cities')['count'].idxmax()]

print(most_common_jobs)

# Sort by count and get the top 20 results
top_20_most_common_jobs = most_common_jobs.sort_values(by='count', ascending=False).head(20)


# Display the top 20 most common jobs in each city
print(top_20_most_common_jobs)

top_20_most_common_jobs.to_csv("top_20_most_common_jobs_in_cities.csv", index=False)

plt.figure(figsize=(15, 8))
top_20_most_common_jobs.plot(kind='barh', x='Capital_Cities', y='count', color='skyblue', legend=False)

font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

plt.title('Top 20 Cities with Most Common Jobs', fontdict=font1)
plt.xlabel('Number of Jobs', fontdict=font2)
plt.ylabel('City', fontdict=font2)
plt.tight_layout()


plt.grid(color='green', linestyle='--', linewidth=0.5)

plt.show()
