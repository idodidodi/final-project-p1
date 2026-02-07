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
    PASSWORD: {os.environ.get('DB_PASSWORD')}
    """
    
if __name__ == '__main__':
    app.run(debug=True)
