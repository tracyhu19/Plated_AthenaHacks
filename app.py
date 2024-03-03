from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app3.db'  # SQLite database
db = SQLAlchemy(app)

class User(db.Model):
    fname = db.Column(db.String(80), primary_key=True)
    street = db.Column(db.String(200), unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    state = db.Column(db.String(80), unique=False, nullable=False)
    zipcode = db.Column(db.Integer, unique=False, nullable=False)

    phone = db.Column(db.Integer, unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    product = db.Column(db.String(120), unique=False, nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)
    exdate = db.Column(db.String(80), unique=False, nullable=False)
    notes = db.Column(db.String(1000), unique=False, nullable=False)

    need = db.Column(db.String(1000), unique=False, nullable=False)

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

    fname = request.form['fname']
    street = request.form['street']
    city = request.form['city']
    state = request.form['state']
    zipcode = request.form['zipcode']

    phone = request.form['phone']
    email = request.form['email']
    
    product = request.form['product']
    quantity = request.form['quantity']
    exdate = request.form['exdate']
    notes = request.form['notes']
    need = request.form['need']

    new_user = User(fname=fname, street=street, city=city, state=state, zipcode=zipcode, phone=phone, email=email, product=product, quantity=quantity, exdate=exdate, notes=notes, need=need)

    db.session.add(new_user)
    db.session.commit()

    return redirect(f'index')  # Redirect to another page after submission

@app.route('/index')
def index():
    users = User.query.all()
    return render_template('index.html', users = users)


if __name__ == "__main__": 
    app.run(debug=True) 