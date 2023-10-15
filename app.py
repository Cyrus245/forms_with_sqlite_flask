from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from models import db, Book
from form import BookForm, RatingForm

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
    """This route handler return home page"""
    all_book = db.session().query(Book).all()

    return render_template('index.html', all_book=all_book)


@app.route('/edit/<b_id>', methods=['GET', 'POST'])
def edit(b_id):
    """This route handler updates the book rating"""
    rating_form = RatingForm()
    # querying selected book based on a primary key
    selected_book = Book.query.get(b_id)
    if rating_form.validate_on_submit():
        # changing the rating
        changed_rating = rating_form.rating.data
        selected_book.rating = changed_rating
        # committing to the db
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('Edit Rating.html', form=rating_form, current_rating=selected_book.rating,
                           book_title=selected_book.title)


@app.route('/add', methods=['GET', 'POST'])
def add_books():
    """This route handler adds books to the database"""
    form = BookForm()
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        rating = form.rating.data
        # creating a new entry to the db
        new_book = Book(title=title.title(), author=author.title(), rating=rating)
        db.session.add(new_book)
        db.session.commit()
        # redirecting to the home page
        return redirect(url_for('home'))

    return render_template('add.html', form=form)


@app.route('/delete/<b_id>', )
def delete(b_id):
    """This route decorator deletes the selected book"""
    book_to_delete = Book.query.get(b_id)
    if book_to_delete:
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
