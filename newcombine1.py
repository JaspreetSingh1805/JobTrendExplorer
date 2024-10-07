import pandas as pd
import re
import spacy

# Load the SpaCy model
nlp = spacy.load('en_core_web_sm')

skills_list = [
    "Python", "Java", "SQL", "JavaScript", "HTML", "CSS", "AWS", "Node.js", "Node", 
    "Docker", "Kubernetes", "Angular", "React", "Machine Learning", "DevOps", "Web APIs",
    "Cloud", "C++", "Linux", "Git", "Agile", "Data Science", "MongoDB", "Express.js", 
    "Express js", "No SQL", "Spring Boot", "C#", "OOP", ".NET", "FastAPI", "PHP", 
    "Django", "Flask", "ASP.NET", "MySQL", "jQuery", "Ajax", "Laravel", "GIT", 
    "Phalcon", "SnowSQL", "Ethernet", "PostgreSQL", "Perl", "Ruby", "IoT", "AI", 
    "GitHub", "Data Analysis", "Digital Marketing", "Communication", "Sales", 
    "Leadership", "Management", "Event Planning", "Social Media Marketing", 
    "Media Management", "Content Marketing", "Email Marketing", "Google Ads", 
    "Interpersonal Skills", "Multitasking", "MS Office", "PowerPoint", "CQF", 
    "PRM", "MS Teams", "SAP", "TypeScript", "Cyber Security", "Problem Solving", 
    "Project Management", "Power BI", "Statistics", "AV Programming", 
    "TensorFlow", "NLP"
]

# Load your CSV file
df = pd.read_csv("customise4.csv")


title_mappings = {
    # Your existing title mappings here...
}

import pdb 

pdb.set_trace()

print(title_mappings)

# Function to clean the title using the dictionary
def clean_title(title):
    if isinstance(title, str):
        for pattern, new_title in title_mappings.items():
            if re.search(pattern, title, re.IGNORECASE):
                return new_title
    return title

# Function to extract skills from text and return as a comma-separated string
def extract_skills(text):
    if not isinstance(text, str):
        return "NaN"
    doc = nlp(text)
    extracted_skills = [token.text for token in doc if token.text in skills_list]
    return ", ".join(extracted_skills) if extracted_skills else "NaN"

# Apply functions to clean titles and extract skills
df['title'] = df['title'].apply(clean_title)
df['extracted_skills'] = df['Requirements'].apply(extract_skills)

# Save the updated DataFrame to a new CSV file
# df.to_csv("customise2.csv", index=False, encoding='utf-8-sig')

# Get the top 20 companies by job title frequency


