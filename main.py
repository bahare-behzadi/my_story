from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

response = requests.get("https://api.npoint.io/471e5bffdccebfaded78")
posts = response.json()
day = datetime.datetime.today().day
year = datetime.datetime.today().year
month = datetime.datetime.now().strftime("%B")
@app.route('/')
def home():
    length = len(posts)
    return render_template("index.html", posts=posts, len=length, day=day, month=month, year=year)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/<int:num>')
def post(num):
    return render_template('post.html', num=num-1, posts=posts)

if __name__ == "__main__":
    app.run(debug=True)