from flask import Flask, render_template, request

app = Flask(__name__)

records = [
    {
        'name': 'Alice',
        'age': 25
    },
    {
        'name': 'Bob',
        'age': 30
    },
    {
        'name': 'Charlie',
        'age': 35
    },
]


@app.route('/')
def home():
    return render_template('index.html', records=records)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
