from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
app = Flask(__name__)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:passsword@localhost:5432/as6db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

@app.route('/sign_in', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        mobile_number = request.form['mobile_number']
  
        participant = User(name=name, surname=surname, email=email, mobile_number= mobile_number)
        db.session.add(participant)
        db.session.commit()
        return render_template("index.html")
    else:
        return render_template('sign_in.html')

@app.route('/spring_course', methods=['GET'])
def display_users():
    users = User.query.all()
    return render_template("spring_course.html", users=users)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    user = User.query.filter_by(id=id).first()

    if request.method == 'POST':
        user.name = request.form['name']
        user.surname = request.form['surname']
        user.email = request.form['email']
        user.mobile_number = request.form['mobile_number']

        db.session.commit()
        return render_template("index.html")
    else:
        return render_template('update.html', user=user)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return render_template("index.html")

@app.route('/spring_course')
def list_users():
    sort_field = request.args.get('sort')
    sort_order = request.args.get('order', 'asc')
    filter_field = request.args.get('filter')
    filter_value = request.args.get('value')
    search_field = request.args.get('search_field')
    search_value = request.args.get('search_value')

    query = User.query

    if sort_field:
        if sort_order == 'desc':
            query = query.order_by(desc(sort_field))
        else:
            query = query.order_by(sort_field)
    if filter_field and filter_value:
        query = query.filter(getattr(User, filter_field) == filter_value)
    if search_field and search_value:
        query = query.filter(getattr(User, search_field).contains(search_value))

    users = query.all()
    return render_template('spring_course.html', users=users)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/sign_in")
def sign_in():
    return render_template("sign_in.html")

@app.route("/spring_course")
def spring_course():
    return render_template("spring_course.html")

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
