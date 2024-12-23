# python-webapi-test

## Overview

This project is a simple Python web API that serves a static HTML page. The API is built using Flask, and the HTML page is served using the Flask `send_from_directory` function.


## Example

When you navigate to `http://127.0.0.1:5000`, you should see the content of `index.html` displayed in your web browser. When you navigate to `http://127.0.0.1:5000/api/data`, you should receive a JSON response with sample data.

This project is a simple Python web API that serves a static HTML page. The API is built using Flask, and the HTML page is served using the Flask `send_from_directory` function.

## Files

- `app.py`: The main Python file that sets up the Flask web server and defines the API endpoints.
- `index.html`: The static HTML page that is served by the Flask web server.

## Requirements

- Python 3.x
- Flask

## Setup

1. Clone the repository:
    ```sh
    git clone /home/afm/Git/python-webapi-test
    cd python-webapi-test
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the Flask web server:
    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000` to view the static HTML page.

## API Endpoints

- `GET /`: Serves the `index.html` file.

## Example

When you navigate to `http://127.0.0.1:5000`, you should see the content of `index.html` displayed in your web browser.

## License

This project is licensed under the MIT License.