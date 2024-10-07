import pandas as pd
import re
import spacy

nlp = spacy.load('en_core_web_sm')


df= pd.read_csv("modified_new6location.csv")
pd.options.display.max_rows=50999
# for i in df['Title'].unique():
#     for k in ['software', "developer", "Software", "Developer"]:
#         if str(k) in i:
#             print(f"*{i} software Develper")
#     else:
#         print(i)
# import pdb
# pdb.set_trace()

df['Experience'] = df['Experience'].fillna('0')
df['extracted_skills'] = df['extracted_skills'].fillna('NaN')
df['minimum_experience'] = df['minimum_experience'].fillna('0')
df['maximum_experience'] = df['maximum_experience'].fillna('0')
df['Timings'] = df['Timings'].fillna('NaN')
df['extracted_skills'] = df['extracted_skills'].fillna('NaN')

# Fill 'Timings' with 'Not Provided' or any other relevant information

title_mappings = {
    r'developer|software|python|application|it|ai/ml|data engineer|cloud|oracle|saas|machine|web|linux|devops|data scientist|.NET': 'Software Developer',
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
    r'manager': 'Manager',
    r'Data Sciece': 'software developer',
    r'Data': 'software developer',
    r'director': 'Director',
    r'engineer': 'Engineer',
    r'Human Resource': 'HR',
    r'Insurance': 'Insurance',
    r'Finance & Accounting ': 'F & A',
    r'Governance': 'Corporate Governance',
    r'PE-SECTION': 'Engineer',
    r'java': 'Software developer',
    r'Cycle': 'Revenue Cycle Management (RCM)',
    r'head': 'Head of FP&A',
    r'Designer': 'Designer',
    r'Surface': 'PPC Manager',
    r'Salesforce': 'Force',
    r'Tax': 'Tax officer',
    r'Freelance': 'software developer',
    r'supervising':'superviser',
    r'Azure': 'software developer',
    r'Financial':'Financial Management',
    r'Delivery': 'Delivery Department',
    r'Analyst': 'Software developer',
    r'Consultant': 'Consultant Service',
    r'Chief': 'Officer',
    r'Investor': 'Finance',
    r'Trainer': 'Trainer',
    r'Investment':'Finance',
    r'OPERATION': 'Hospitality',
    r'Principle': 'Manager',
    r'Professor ': 'Law department',
    r'Technician': 'Engineer',
    r'Full Stack': 'software developer',
    r'FInance': 'Finance',
    r'agency': 'Agency',
    r'UI/UX ': 'software developer',
    
}
# print(title_mappings)
def replace_remote(cities_list):
    # Replace 'Remote' with an empty string
    updated_cities = [city.replace('Remote', '').strip() for city in cities_list]
    # print(updated_cities)
  
cities = [
    'Chandigarh', 'Remote', 'Mohali', 'Punjab', 'Bengaluru', 'Karnataka', 'Jamshedpur', 'Jharkhand', 
    'Dehradun', 'Uttarakhand', 'Nagaur', 'Rajasthan', 'Srinagar', 'Jammu and Kashmir', 'Hybrid work in Jaipur', 
    'Dum Duma', 'Assam', 'Gurugram', 'Haryana', 'Remote in Kolkata', 'West Bengal', 'Arasur', 'Coimbatore', 
    'Tamil Nadu', 'Nashik', 'Maharashtra', 'Santacruz West', 'Mumbai', 'Tilak Nagar', 'Jaipur', 
    'Remote in Mumbai Central', 'Perambur', 'Chennai', 'Pune', 'Remote in India', 'Kopar Khairane', 
    'Navi Mumbai', 'Girgaon', 'Rishikesh', 'Jharsuguda', 'Orissa', 'Surat', 'Gujarat', 'Bhubaneswar', 
    'Trivandrum District', 'Kerala', 'Hyderabad', 'Telangana', 'Kondapur', 'Chennai District', 'Harmu', 
    'Ranchi', 'Fort', 'Amritsar', 'Thiruvananthapuram', 'HITEC City', 'Noida', 'Uttar Pradesh', 'Raipur', 
    'Chhattisgarh', 'Pimpri- Chinchwad', 'Arakkonam', 'Remote in Pune', 'Raigarh Fort', 'Belgaum', 
    'Tiruvalla', 'Ahmedabad', 'Guwahati', 'RT Nagar', 'Athwa Gate', 'Madambakkam', 'CBD Belapur', 
    'Ludhiana', 'Delhi', 'Remote in Ranchi', 'Malappuram', 'Kolkata', 'Thiruvanmiyur', 'Remote in Tiruvalla', 
    'Remote in Lucknow', 'Remote in Kochi', 'Grant Road', 'Vadodara', 'Begumpet', 'Ghansoli', 'Kochi', 
    'Mahipalpur', 'Remote in Bengaluru', 'Erode', 'Brahmapur', 'Tenkasi', 'Remote in Surat', 'India', 
    'Gujrat', 'Nagar', 'Remote in Jaipur', 'Remote in Gurugram', 'Hybrid work in Tenkasi', 'Shahdol', 
    'Madhya Pradesh', 'Mansarovar', 'Bandra', 'Goa', 'Pilerne', 'Kengeri Satellite Town', 'Sitapur', 
    'Sholinganallur', 'Saravanampatti', 'Remote in Sangrur', 'Tumkur', 'Sohna', 'Noida Sector 62', 
    'Bilaspur', 'Jammu', 'Remote in Warangal', 'Shastripuram', 'Agra', 'Vijayawada', 'Andhra Pradesh', 
    'Panipat', 'Yavatmal', 'Remote in Mira Road', 'Tiruppatur', 'Yelahanka', 'Varanasi', 'Tirupati', 
    'Sangriya', 'Jodhpur', 'Indore District', 'Remote in Navi Mumbai', 'Kumta', 'Palwal', 'Shimla', 
    'Himachal Pradesh', 'Greater Noida', 'Patna', 'Bihar', 'Narela', 'Karapakkam', 'Mangalore', 
    'Viman Nagar', 'Whitefield', 'Badarpur', 'Remote in Mumbai', 'Chhatarpur', 'Shiliguri', 'Science City', 
    'Hybrid work in Delhi', 'Mira Road', 'Remote in Yelahanka New Town', 'Lucknow District', 'Indore', 
    'Ambattur', 'Thane', 'Gandhidham', 'Gopalbari', 'Sonipat', 'Remote in Dehradun', 'Janakpuri', 
    'Hybrid work in Hyderabad', 'Jorhat', 'Yeshwanthpur', 'Remote in Thiruvananthapuram', 'Karur', 
    'Domlur', 'Tiruchchirappalli', 'Ichchhapor', 'Kamrup District', 'Ujjain', 'Adajan', 'Remote in Machilipatnam', 
    'Faizabad', 'Junagadh', 'Arunachal', 'Remote in Nagpur', 'Salt Lake', 'Ranippettai', 'Malad', 
    'Marine Lines', 'Remote in Bhiwani', 'Bhiwani', 'Kovur Road', 'Shillong', 'Meghalaya', 'Jubilee Hills', 
    'Chakan', 'Samastipur', 'Banjara Hills', 'Remote in Udaipur', 'Ajmer', 'Udhana', 'Remote in Bara Banki', 
    'Hanumangarh', 'Rewari', 'Andheri', 'Visakhapatnam', 'Pantheerankavu', 'Calicut', 'Amravati', 
    'Adivaram Pudupadi', 'Sampangiramnagar', 'Kanpur', 'Remote in Chennai', 'Remote in Mohali', 'Vashi', 
    'Ottappalam', 'Tirunelveli', 'Hazira', 'Sirsa', 'KPHB Colony', 'Electronic City', 'Jamnagar', 
    'Remote in Srinagar', 'Ambala', 'Kharar', 'Remote in Patna', 'Sanjay Place', 'Hosur', 'Sangli', 
    'Udaipur', 'Daman', 'Daman and Diu', 'Alleppey', 'Cannanore', 'Ghitorni', 'Sector-1 Greater Noida PO', 
    'Delhi District', 'Remote in Ahmedabad', 'Remote in Delhi', 'Wagle Estate', 'Lucknow', 'Kishangarh', 
    'Bhankrota', 'Gachibowli', 'Dhanbad', 'Manjeri', 'Nagercoil', 'Ludhiana District', 'Agartala', 
    'Tripura', 'Faridabad', 'Mumbai District', 'Devanhalli', 'Pitampura', 'Kanchipuram', 'Remote in Nashik', 
    'T Nagar', 'Hugli', 'Medinipur', 'Nagpur', 'Pudukkottai', 'Hauz Khas', 'Kaushambi', 'Ghaziabad', 
    'Rajkot District', 'Gomtinagar', 'Remote in Tamil Nadu', 'Faridabad Sector 15', 'Remote in Chandigarh', 
    'Kaloor', 'Chhindwara', 'Badlapur', 'Angul', 'Gandhipuram', 'Madurai', 'Remote in Hyderabad', 
    'Aurangabad', 'Bais Godam', 'Mathura Road Faridabad', 'Shyam Nagar', 'HSR Layout Sector 2', 
    'Kakkanad', 'Teri', 'Sector-128 Noida', 'Narasimhanaickenpalayam', 'Tambaram', 'Dwarka', 'Narhe', 
    'Lucknow G.P.O.', 'Remote in Okhla', 'Borivali', 'Pathardi', 'Akola', 'Bhopal', 'Model Town II', 
    'Hybrid work in Bengaluru', 'Vrindavan', 'Thrissur', 'Indiranagar', 'Remote in Noida', 'Punpun', 
    'Raj Nandgaon', 'Vasanth Nagar', 'Remote in Aundh', 'Gopalpura', 'Gangtok', 'Sikkim', 'Dum Dum', 
    'Jaipur District', 'Virudunagar', 'Powai', 'Hybrid work in Navi Mumbai', 'Gudhiyari', 'Aluva', 
    'Royapettah', 'Andheri East', 'South Delhi', 'Nauroji Nagar', 'Lower Parel', 'Kalavasal', 'Sakinaka', 
    'Jayanagar', 'Badarinath', 'Remote in Bangalore City', 'Marine Drive', 'Haridwar', 'Jhandewalan', 
    'Mapuca', 'Solan', 'Faridabad NIT H.O', 'Kavundampalayam', 'Sadashivanagar', 'Gorakhpur', 'Kota', 
    'Vasai', 'Lal Chowk', 'Gaya', 'Karnal', 'Mall', 'Allahabad', 'Chandrasekharpur', 'Bikaner', 
    'Neredmet', 'Remote in Haldwani', 'Anantapur', 'Transport Nagar', 'Pollachi', 'Hisar', 'Davangere', 
    'Gautam Budh Nagar', 'Munnar', 'Tilda', 'Silvassa', 'Dadra and Nagar Haveli', 'Ultadanga Main Road', 
    'Alkapuri', 'Gulbarga', 'Ashram Road P.O', 'Patalganga', 'Coimbatore District', 'Udipi', 'Chaibasa', 
    'Shahapur', 'Borivali East', 'Vapi', 'Chembur', 'Tinsukia', 'Majura Gate', 'Gwalior', 'Kharagpur', 
    'Bhiwadi', 'Pali', 'Dhulagori', 'Howrah', 'Remote in Mathura', 'Ramanathapuram', 'Banaswadi', 
    'Gurgaon', 'Cuttack', 'Raebareli', 'Dewas', 'Sewri', 'Navi Mumbai-410703', 'Sankari', 'Amroha', 
    'Kamla Nagar', 'Vellore', 'Rohtak', 'Gujarat District', 'Ludhiana-NR', 'Navi Mumbai Sector 1', 
    'Yavatmal District', 'Shimla District', 'Tiruchirappalli District', 'Thane District', 'Navi Mumbai', 
    'Mumbai Suburban District', 'Madhya Pradesh District', 'Uttar Pradesh District', 'Punjab District', 
    'Maharashtra District', 'Bihar District', 'Telangana District', 'Kerala District', 'Andhra Pradesh District', 
    'Gujarat District', 'Odisha District', 'Rajasthan District', 'Haryana District', 'Delhi District', 
    'Tamil Nadu District', 'West Bengal District', 'Uttarakhand District', 'Jammu and Kashmir District', 
    'Chhattisgarh District', 'Jharkhand District', 'Himachal Pradesh District', 'Chandigarh District', 
    'Goa District', 'Puducherry District', 'Sikkim District', 'Tripura District', 'Arunachal Pradesh District', 
    'Assam District', 'Meghalaya District', 'Nagaland District', 'Mizoram District', 'Manipur District', 
    'Bihar District'
]



# Keywords to replace
keywords = [
    r'\bin\b', 
    r'\bHybrid work\b', 
    r'\bDistrict\b', 
    r'\bcity\b', 
    r'\bPO\b', 
    r'\bSector\b', 
    r'\bGPO\b', 
    r'\bNIT\b', 
    r'\bH\.?O\.? P\.?O\.?\b',  # Adjusted for possible variations
    r'\d+'  # Matches any numeric value
]



# Combined regex pattern
pattern = re.compile('|'.join(keywords), re.IGNORECASE)

# Replace matches with an empty string
cleaned_phrases = [pattern.sub('', phrase) for phrase in cities]

# Remove extra spaces and filter out empty strings
cleaned_phrases = [phrase.strip() for phrase in cleaned_phrases if phrase.strip()]

def extract_cities(location_text):
    if isinstance(location_text, str):  # Check if the input is a string
        doc = nlp(location_text)  # Process the text with spaCy
        cities = [ent.text for ent in doc.ents if ent.label_ == 'GPE']  # Extract cities (GPE: Geo-Political Entity)
        return ', '.join(cities)  # Join multiple cities with commas
    return ''

# Apply the function to the 'location' column and store the result in a new column 'extracted_cities'
# df['extracted_cities'] = df['Location'].apply(extract_cities)
df['extracted_cities'] = df['extracted_cities'].replace('', 'Remote')

def clean_title(title):
    if isinstance(title, str):
        for pattern, new_title in title_mappings.items():
            if re.search(pattern, title, re.IGNORECASE):
                return new_title
    return title


df['title'] = df['title'].apply(clean_title)
df.to_csv("modified_new8location.csv",index=True, encoding='utf-8-sig')
