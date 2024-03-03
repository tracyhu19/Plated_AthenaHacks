from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # SQLite database
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Pass the required route to the decorator. 

@app.route("/") 
def input(): 
    return render_template('main.html')

@app.route("/compile") 
def intyput(): 
    db.create_all()

    return "success"

@app.route("/about.html") 
def about(): 
    return render_template('about.html')

@app.route("/locate.html") 
def locate(): 
    return render_template('locate.html')

@app.route("/upload.html") 
def upload(): 
    return render_template('upload.html')

print("Apple")
@app.route('/submit_form', methods=['POST'])
def submit_form():
    print("Inside route")
    username = request.form['username']
    email = request.form['email']
    id = request.form['id']

    new_user = User(id=id, username=username, email=email)

    db.session.add(new_user)
    db.session.commit()

    return redirect(f'index')  # Redirect to another page after submission

@app.route('/index')
def index():
    users = User.query.all()
    return render_template('index.html', users = users)


if __name__ == "__main__": 
    app.run(debug=True) 