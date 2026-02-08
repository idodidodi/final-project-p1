from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/hello")
def hello():
    return f"""
    ENV: {os.environ.get('APP_ENV')}<br>
    MESSAGE: {os.environ.get('APP_MESSAGE')}<br>
    PORT: {os.environ.get('FLASK_RUN_PORT')}<br>
    PASSWORD: {os.environ.get('DB_PASSWORD')}
    """

@app.route("/health/live")
def live():
    return "OK", 200

@app.route("/health/ready")
def ready():
    return "READY", 200
    
if __name__ == '__main__':
    app.run(debug=True)
