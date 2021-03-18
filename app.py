from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from covid import covid_obj

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# User.query.all()
# User.quary.filter_by(username="Sumet Jutajn").first()
class User(db.Model):
    """"Create columns to score our data"""

    # id, username, email, password

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# Only test
@app.route('/')
def home():
    """Retrieve all users from the database"""

    people = User.query.all()

    return render_template("home.html", people=people) 

@app.route('/post-details/<int:id>')
def post_details(id):
    """ Retrieve only one user(by id)"""

    person = User.query.get(id)

    return render_template("post-details.html", person=person)

# Only test
@app.route('/test')
def home_test():
    name = "Tik"
    return render_template("home-test.html", name=name) # atleast 2 argument


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/script')
def test_script():
    return render_template("test-script.html")

@app.route('/covid-table')
def covid_table():
    """ Return Covid19 data to show in a table """

    covid_data = covid_obj

    return render_template("covid-table.html",covid_data=covid_data)

if __name__ == '__main__':
    app.run(debug=True)