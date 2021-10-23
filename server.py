from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


# @app.route('/<username>/<int:p_id>')
# def hello(username=None,p_id =None):
#     return render_template('index.html', name=username, pid=p_id)

@app.route('/')
def index0():
    return render_template('index.html')


# @app.route('/blog')
# def blog():
#     return 'Hello: Blog'

@app.route('/<string:page_name>')
def pg(page_name):
    return render_template(page_name)


# @app.route('/work.html')
# def work():
#     return render_template('work.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

def txt(data):
    with open('db.txt', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = db.write(f' {email}, {subject}, {message} \n')


def excel(data):
    with open('db2.csv','a', newline='') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        spammer = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        print('/n')
        spammer.writerow([email, subject, message])


# def send(data):
#     email1 = data['email']
#     return render_template('thnx.html', email=email1)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            txt(data)
            excel(data)
        # send(data)
            return redirect('/thnx.html')
        except:
            return 'not saved to DB'
    else:
        return 'Went Wrongg'

# @app.route('/<username>')
# def hello(username=None):
#     return render_template('thnx.html', email=username)
