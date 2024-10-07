from wordcloud import WordCloud
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd

# import pdb
# pdb.set_trace()
# Load your CSV file containing the extracted skills
df = pd.read_csv("customise2.csv")

# Combine all extracted skills into a single string
all_skills = ', '.join(df['extracted_skills'].dropna().tolist())


# Load the mask image (e.g., a star shape)
mask = np.array(Image.open("python-logo.png"))

# Create the word cloud with the mask
wordcloud = WordCloud(width=800, height=800, 
                      background_color='white', 
                      mask=mask, 
                      contour_color='pink', 
                      contour_width=5).generate(all_skills)

# Display the word cloud
plt.figure(figsize=(8, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide the axes
plt.title('Word Cloud of Extracted Skills', fontsize=20)
plt.show()
