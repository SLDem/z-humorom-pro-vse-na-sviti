from flask import redirect, render_template, url_for, request
from app import app, db
from app.forms import PoemForm
from app.models import Poem
from flask_paginate import Pagination, get_page_parameter


@app.route('/')
@app.route('/home')
def home():
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)
    poems = Poem.query.all()
    pagination = Pagination(page=page, total=len(poems), search=search, record_name='poems', css_framework='foundation')
    return render_template('home.html', title='Вірші',  poems=poems, pagination=pagination)


@app.route('/about')
def about():
    return render_template('about.html', title='Про Автора')


@app.route('/add_poem_password1234', methods=['POST', 'GET'])
def add_poem():
    form = PoemForm()
    if form.validate_on_submit():
        poem = Poem(title=form.title.data, text=form.text.data)
        db.session.add(poem)
        db.session.commit()
        return redirect(url_for('add_poem'))
    return render_template('add_poem.html', title="Add poem", form=form)

