from flask import Flask, render_template, request
from pymongo import MongoClient


app = Flask(__name__)

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')
db = client['Job_listing']  # Database name
collection = db['Job_data']  # Collection name

@app.route('/')
def index():
    # Fetch unique job titles and cities for dropdowns
    job_titles = collection.distinct('title')  # Get distinct job titles
    cities = collection.distinct('extracted_cities')  # Get distinct cities

    # Print job titles in the Flask console
    print("Job Titles in Dropdown: ", job_titles)

    # Render the index page with dropdown data
    return render_template('index.html', job_titles=job_titles, cities=cities)


@app.route('/filter', methods=['POST'])
def filter_data():
    # Get the selected title and city from the form submission
    title = request.form.get('title')
    city = request.form.get('extracted_cities')

    # Build the query based on selected filters
    query = {}
    if title and title != "All":
        query['title'] = title
    if city and city != "All":
        query['extracted_cities'] = city

    # Fetch matching documents from MongoDB
    jobs = collection.find(query)

    # Convert the cursor to a list of dictionaries
    job_list = []
    for job in jobs:
        job['_id'] = str(job['_id'])  # Convert ObjectId to string for JSON compatibility
        job_list.append(job)

    # Render the results page and pass the filtered job data
    return render_template('result.html', data=job_list)

if __name__ == '__main__':
    app.run(debug=True)




