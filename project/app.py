from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

file_path = 'analyzed_data.csv'
df = pd.read_csv(file_path)

@app.route('/')
def index():
    titles = df['Title'].dropna().unique().tolist()
    locations = df['Locations'].dropna().unique().tolist()
    return render_template('index.html', titles=titles, locations=locations)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    selected_title = request.form.get('title')
    selected_location = request.form.get('location')
    
    filtered_df = df[(df['Title'] == selected_title) & (df['Locations'] == selected_location)]

    filtered_data = filtered_df.to_dict(orient='records')
    
    return render_template('result.html', data=filtered_data)

if __name__ == '__main__':
    app.run(debug=True,port=8000)