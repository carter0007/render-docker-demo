from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Привіт з Docker на Render!"
