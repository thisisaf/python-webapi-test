from flask import Flask, render_template, request

app = Flask(__name__,
             template_folder='templates',
             static_folder='')

records = [
    {
        'id': 1,
        'title': 'Administrator',
        'salary': 25000,
        'currency': '£',
        'short-description': 'This is a description of the job',
        'posted': '2023-01-01'
    },
    {
        'id': 2,
        'title': 'Barman',
        'salary': 30000,
        'currency': '£',
        'short-description': 'This is a description of the job',
        'posted': '2023-02-01'
    },
    {
        'id': 3,
        'title': 'Cleaner',
        'salary': 99000,
        'currency': '$',
        'short-description': 'This is a description of the job',
        'posted': '2023-03-01'
    },
    {
        'id': 4,
        'title': 'Data Scientist',
        'salary': 35000,
        'currency': '£',
        'short-description': 'This is a description of the job',
        'posted': '2023-04-01'
    }
]


@app.route('/')
def home():
    return render_template('index.html', records=records)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
