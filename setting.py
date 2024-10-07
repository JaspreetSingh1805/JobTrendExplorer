import pandas as pd
import re
import spacy
import numpy as np  # Import numpy for NaN handling

# Load the SpaCy model
nlp = spacy.load('en_core_web_sm')

# Define the list of skills
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
df = pd.read_csv("customise2.csv")

# Fill missing values with numpy.nan
df['Experience'] = df['Experience'].fillna(np.nan)
df['Timings'] = df['Timings'].fillna(np.nan)
df['Salary'] = df['Salary'].fillna('0')
df['Requirements'] = df['Requirements'].fillna(np.nan)
df['extracted_skills'] = df['extracted_skills'].fillna(np.nan)

# Ensure title and company names are in uppercase
df['title'] = df['title'].str.upper()
df['company-name'] = df['company-name'].str.upper()

# Split Experience into minimum and maximum experience and remove 'Yrs'
df[['minimum_experience', 'maximum_experience']] = df['Experience'].str.replace('Yrs', '').str.split('-', expand=True)

# Convert the newly created columns to numeric, with error handling
df['minimum_experience'] = pd.to_numeric(df['minimum_experience'], errors='coerce')
df['maximum_experience'] = pd.to_numeric(df['maximum_experience'], errors='coerce')

# Replace 'Permanent' with 'Full-time' in the 'Timings' column
df['Timings'] = df['Timings'].replace('Permanent', 'Full-time')

# Title mappings dictionary
title_mappings = {
    r'developer|software|python|application|it|ai/ml|data engineer|cloud|oracle|saas|machine|web|linux|devops|data scientist': 'Software Developer',
    r'business': 'Business Development',
    r'account manager': 'Account Manager',
    r'b2b': 'Sales Manager',
    r'electrical': 'Electrical Engineering',
    r'civil': 'Civil Engineering',
    r'automation': 'Automation Engineering',
    r'mechanical': 'Mechanical Engineering',
    r'piping': 'Piping Engineering',
    r'product': 'Product Engineer',
    r'site': 'Site Engineer',
    r'test': 'Testing Engineer',
    r'engineering operations|abroad': 'Engineering Operations',
    r'network': 'Network Engineer',
    r'project': 'Project Manager',
    r'process': 'Process Engineer',
    r'technical': 'Technical Engineer',
    r'supply chain': 'Supply-Chain Engineer',
    r'structural': 'Structural Engineer',
    r'lead': 'Lead Operator',
    r'staff': 'Staff Engineer',
    r'industrial': 'Operation Engineer',
    r'support': 'Support Engineer',
    r'ci/cd': 'Software Developer',
    r'electronics': 'Electronics Engineer',
    r'sap': 'Product Manager',
    r'analytics': 'Software Developer',
    r'program': 'Program Manager',
    r'assistant': 'Assistant',
    r'accountant': 'Accountant',
    r'Media': 'Media Relations Manager',
    r'Research': 'R&D Engineer',
    r'President': 'Vice President (VP)',
    r'manager': 'Manager',
    r'Data Science,Analyst': 'Software Developer',
    r'director': 'Director',
    r'engineer': 'Engineer',
    r'Human Resource': 'HR',
    r'Insurance': 'Insurance',
    r'Finance & Accounting ': 'F & A',
    r'java': 'Software Developer',
    r'Technician': 'Technician',
    r'Freelance': 'Software Developer',
    r'UI/UX': 'Software Developer',
    r'Full Stack': 'Software Developer',
    r'Azure': 'Software Developer',
    r'Consultant': 'Consultant Service',
}

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
df.to_csv("customise4.csv", index=False, encoding='utf-8-sig')

# Display the relevant columns for verification
print(df[['Experience', 'minimum_experience', 'maximum_experience', 'title', 'extracted_skills']])
