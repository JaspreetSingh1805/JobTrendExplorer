import pandas as pd
import re

df= pd.read_csv("combined_file.csv")
pd.options.display.max_rows=50999
# for i in df['Title'].unique():
#     for k in ['software', "developer", "Software", "Developer"]:
#         if str(k) in i:
#             print(f"*{i} software Develper")
#     else:
#         print(i)
# import pdb
# pdb.set_trace()
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
    r'ping': 'Ping Engineer',
    r'principal': 'Principal Engineer',
    r'ci/cd': 'Software Developer',
    r'electronics': 'Electronics Engineer',
    r'sap': 'Product Manager',
    r'analytics': 'Software Developer',
    r'program': 'Program Manager',
    r'assistant': 'Assistant',
    r'accountant': 'Accountant',
    r'Media': 'Media Relations Manager',
    r'Research': 'R&D Engineer',
    r'President': 'Vice President (VP) ',
    r'manager': 'Manager',
    r'Data Science,Analyst': 'software developer',
    r'director': 'Director',
    r'engineer': 'Engineer',
    
}

# Function to clean the title using the dictionary
def clean_title(title):
    if isinstance(title, str):
        for pattern, new_title in title_mappings.items():
            if re.search(pattern, title, re.IGNORECASE):
                return new_title
    return title


df['title'] = df['title'].apply(clean_title)
print(df['title'].tail(10000))
