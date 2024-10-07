# from flask import Flask, render_template, request, redirect, url_for
# from pymongo import MongoClient
# import matplotlib
# import matplotlib.pyplot as plt
# import os
# from collections import Counter

# matplotlib.use('Agg')

# app = Flask(__name__)

# client = MongoClient('mongodb://localhost:27017/')
# db = client['Job_listing']
# collection = db['Job_data']

# CHART_FOLDER = 'static/charts'
# if not os.path.exists(CHART_FOLDER):
#     os.makedirs(CHART_FOLDER)

# @app.route('/')
# def index():
#     pipeline = [
#         {"$group": {"_id": "$title", "count": {"$sum": 1}}},
#         {"$sort": {"count": -1}},
#         {"$limit": 250}
#     ]
#     title_data = list(collection.aggregate(pipeline))
#     titles = [item['_id'] for item in title_data]  
#     locations = collection.distinct('extracted_cities')

#     return render_template('index.html', titles=titles, locations=locations)

# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#     selected_title = request.form.get('title').strip()
#     selected_location = request.form.get('extracted_cities').strip()

#     filtered_data = list(collection.find(
#         {
#             'title': {"$regex": f"^{selected_title}$", "$options": "i"},
#             'extracted_cities': {"$regex": f"^{selected_location}$", "$options": "i"}
#         },
#         {'_id': 0}  
#     ))

#     if filtered_data:
#         columns_to_plot = ['extracted_skills', 'minimum_experience', 'maximum_experience', 'company-name']
#         chart_paths = {}

#         for column in columns_to_plot:
#             column_data = [job.get(column) for job in filtered_data if job.get(column)]
            
#             if column_data:
#                 value_counts = Counter(column_data).most_common(10)

#                 labels = [str(item[0]) for item in value_counts]
#                 sizes = [item[1] for item in value_counts]

#                 plt.figure(figsize=(10, 6))
#                 plt.bar(labels, sizes, color='skyblue')
#                 plt.xlabel(column.replace('_', ' '))
#                 plt.ylabel('Count')
#                 plt.title(f'Top 10 {column.replace("_", " ")} Distribution')

#                 plt.xticks(rotation=45, ha='right', fontsize=10)

#                 plt.tight_layout()

#                 chart_filename = f'{column}_bar_chart.png'
#                 chart_path = os.path.join(CHART_FOLDER, chart_filename)
#                 plt.savefig(chart_path)
#                 plt.close()  

#                 chart_paths[column] = chart_path

#         return render_template('result.html', data=filtered_data, chart_paths=chart_paths)

#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True, port=8000)


# Add new updated code 

from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
import matplotlib
import matplotlib.pyplot as plt
import os
from collections import Counter

matplotlib.use('Agg')

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

client = MongoClient('mongodb://localhost:27017/')
db = client['Job_listing']
collection = db['Job_data']

CHART_FOLDER = 'static/charts'
if not os.path.exists(CHART_FOLDER):
    os.makedirs(CHART_FOLDER)

@app.route('/')
def index():
    pipeline = [
        {"$group": {"_id": "$title", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 250}
    ]
    title_data = list(collection.aggregate(pipeline))
    titles = [item['_id'] for item in title_data]
    locations = collection.distinct('extracted_cities')

    return render_template('index.html', titles=titles, locations=locations)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    selected_title = request.form.get('title').strip()
    selected_location = request.form.get('extracted_cities').strip()

    # Debug: Print selected values
    print(f"Selected Title: {selected_title}, Selected Location: {selected_location}")

    # Query the MongoDB collection
    filtered_data = list(collection.find(
        {
            'title': {"$regex": f"^{selected_title}$", "$options": "i"},
            'extracted_cities': {"$regex": f"^{selected_location}$", "$options": "i"}
        },
        {'_id': 0}
    ))

    # Debug: Print filtered data length
    print(f"Filtered Data Length: {len(filtered_data)}")

    if filtered_data:
        columns_to_plot = ['extracted_skills', 'minimum_experience', 'maximum_experience', 'company-name']
        chart_paths = {}

        for column in columns_to_plot:
            column_data = [job.get(column) for job in filtered_data if job.get(column)]

            if column_data:
                value_counts = Counter(column_data).most_common(10)

                labels = [str(item[0]) for item in value_counts]
                sizes = [item[1] for item in value_counts]

                plt.figure(figsize=(10, 6))
                plt.bar(labels, sizes, color='skyblue')
                plt.xlabel(column.replace('_', ' '))
                plt.ylabel('Count')
                plt.title(f'Top 10 {column.replace("_", " ")} Distribution')

                plt.xticks(rotation=45, ha='right', fontsize=10)

                plt.tight_layout()

                chart_filename = f'{column}_bar_chart.png'
                chart_path = os.path.join(CHART_FOLDER, chart_filename)
                plt.savefig(chart_path)
                plt.close()

                chart_paths[column] = chart_path

        return render_template('result.html', data=filtered_data, chart_paths=chart_paths)

    # Flash a message if no data is found
    flash('No data found for the selected title and location.', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=8000)
