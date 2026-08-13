from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Flask App</title>
    </head>

    <body>

        <h1>Hello from Flask!</h1>

        <p>This is my first Flask application.</p>

        <button onclick="alert('Hello!')">
            Click Me
        </button>

    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run(debug=True)