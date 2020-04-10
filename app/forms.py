from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired


class PoemForm(FlaskForm):
    title = StringField('Титул', validators=[DataRequired()])
    text = TextAreaField('Текст', validators=[DataRequired()])
    submit = SubmitField('Додати')


class HumoresqueForm(FlaskForm):
    title = StringField('Титул', validators=[DataRequired()])
    text = TextAreaField('Текст', validators=[DataRequired()])
    submit = SubmitField('Додати')