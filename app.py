from flask import Flask, render_template, redirect,url_for
from flask_bootstrap import Bootstrap
from models import db, Book
from form import BookForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'  # Replace with your secret key
# creating the database uri
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///crud_sqlite.db"
Bootstrap(app)
# initialize the app with flask_sqlAlchemy extension
db.init_app(app)

# creating database tables
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_books():
    """This route handler adds books to the database"""
    form = BookForm()
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        rating = form.rating.data
        new_book = Book(title=title.title(), author=author.title(), rating=rating)
        db.session.add(new_book)
        db.session.commit()
        # redirecting to the home page
        return redirect(url_for('home'))

    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
