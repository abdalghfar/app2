from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.contact}>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    contact = request.form['contact']
    password = request.form['password']
    new_user = User(contact=contact, password=password)
    db.session.add(new_user)
    db.session.commit()
    return 'Form submitted successfully!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
