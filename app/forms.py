from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class PoemForm(FlaskForm):
    title = StringField('Титул', validators=[DataRequired()])
    text = TextAreaField('Текст', validators=[DataRequired()])
    submit = SubmitField('Додати')


class HumoresqueForm(FlaskForm):
    title = StringField('Титул', validators=[DataRequired()])
    text = TextAreaField('Текст', validators=[DataRequired()])
    submit = SubmitField('Додати')


class SearchForm(FlaskForm):
    search_field = TextAreaField('Ключ', validators=[DataRequired(), Length(min=2, max=60)])
    submit = SubmitField('Знайти')