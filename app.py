from flask import Flask, render_template, request
import json

app = Flask(__name__,
             template_folder='templates',
             static_folder='')

records = [
    {
        'id': 1,
        'title': 'Administrator',
        'salary': "25,000",
        'currency': '£',
        'short-description': 'Office management and coordination',
        'long-description': 'Managing office tasks, Coordinating schedules, Ensuring smooth operations.',
        'posted': '2023-01-01',
        'active': True,
        'location': 'London, UK'
    },
    {
        'id': 2,
        'title': 'Barman',
        'salary': "30,000",
        'currency': '£',
        'short-description': 'Prepare and serve drinks',
        'long-description': 'As a Barman, you will be responsible for preparing and serving drinks, maintaining the bar area, and providing excellent customer service.',
        'posted': '2023-02-01',
        'active': True,
        'location': 'New York, USA'
    },
    {
        'id': 3,
        'title': 'Cleaner',
        'salary': "99,000",
        'currency': '$',
        'short-description': 'Maintain cleanliness and hygiene',
        'long-description': 'As a Cleaner, you will be responsible for maintaining cleanliness and hygiene in various facilities, ensuring a safe and pleasant environment.',
        'posted': '2023-03-01',
        'active': True,
        'location': 'Sydney, Australia'
    },
    {
        'id': 4,
        'title': 'Data Scientist',
        'salary': "35,000",
        'currency': '£',
        'short-description': 'Analyze data and develop models',
        'long-description': 'As a Data Scientist, you will be responsible for analyzing complex data sets, developing predictive models, and providing insights to drive business decisions.',
        'posted': '2023-04-01',
        'active': True,
        'location': 'San Francisco, USA'
    }
]


@app.route('/')
def home():
    return render_template('index.html', records=records)

# @app.route('/foo/<int:id>')
# def foo(id):
#     record = next((record for record in records if record['id'] == id), None)
#     if record is None:
#         return {"error": "Record not found"}, 404
#     #return render_template('index.html', records=records)
#     return render_template('apply_details.html', record=record)

@app.route('/apply/<int:id>')
def apply(id):
    record = next((record for record in records if record['id'] == id), None)
    if record is None:
        return {"error": "Record not found"}, 404
    #TODO: Here you can add logic to handle the application process
    return render_template('apply_details.html', record=record)

@app.route('/submit_application', methods=['POST'])
def submit_application():
    name = request.form.get('name')
    email = request.form.get('email')
    about = request.form.get('about')
    linkedin = request.form.get('linkedin')
    record_id = request.form.get('record_id')
    record_title = request.form.get('record_title')
    record_currency = request.form.get('record_currency')
    record_salary = request.form.get('record_salary')
    record_location = request.form.get('record_location')
    record_long_description = request.form.get('record_long_description')
    
    submission_details = {
        'about': about,
        'name': name,
        'email': email,
        'linkedin': linkedin,
        'record_id': record_id,
        'record_title': record_title,
        'record_currency': record_currency,
        'record_salary': record_salary,
        'record_location': record_location,
        'record_long_description': record_long_description
    }

    return render_template('submitted_application.html', submission_details=submission_details)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
