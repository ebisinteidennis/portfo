from flask import Flask, render_template, url_for, redirect,request
import csv

app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/work.html')
def work():
    return render_template('work.html')

@app.route('/works.html')
def works():
    return render_template('works.html')


def write_to_csv(data):
    with open('database.csv', mode='a') as database1:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database1, delimiter=',', newline='', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong. Try Again!'
