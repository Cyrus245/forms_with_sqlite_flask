from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


# creating the flask form
class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    rating = FloatField('Rating',
                        validators=[DataRequired(), NumberRange(min=1, max=10, message="value must be from 1 to 10")])
    submit = SubmitField('Add')
