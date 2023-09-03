from flask import Flask, render_template, request
import requests
import datetime
import smtplib

app = Flask(__name__)

response = requests.get("https://api.npoint.io/471e5bffdccebfaded78")
posts = response.json()
day = datetime.datetime.today().day
year = datetime.datetime.today().year
month = datetime.datetime.now().strftime("%B")
EMAIL = "your email"
PASSWORD = "your email's app password"
smtplib.SMTP("smtp.gmail.com", port=587)


@app.route('/')
def home():
    length = len(posts)
    return render_template("index.html", posts=posts, len=length, day=day, month=month, year=year)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact',methods=["POST","GET"])
def contact():
    if request.method == 'GET':
        header = 'Contact Me'
        return render_template("contact.html", header=header)
    else:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        sent_email = f"Name: {name} with email: {email} and phon: {phone} sent you this message:\n{message}"
        header = 'Your message sent'
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:NEW MESSAGE FROM YOUR BLOG\n\n{sent_email}")

        return render_template("contact.html", header=header)


@app.route('/<int:num>')
def post(num):
    return render_template('post.html', num=num-1, posts=posts)


# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     name = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone']
#     message = request.form['message']
#     return (f"<h1>Success Sent</h1><br><h2>{name}</h2><br><h2>{email}</h2><br><h2>{phone}</h2><br><h2>{message}</h2><br>")


if __name__ == "__main__":
    app.run(debug=True)