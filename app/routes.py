from flask import redirect, render_template, url_for, request
from app import app, db
from app.forms import PoemForm, HumoresqueForm
from app.models import Poem, Humoresque


@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', title='Про Автора')


@app.route('/poems/<int:page_num>')
def poems(page_num):
    poems = Poem.query.paginate(per_page=5, page=page_num, error_out=True)
    return render_template('poems.html', title='Вірші',  poems=poems)


@app.route('/humoresques/<int:hum_page_num>')
def humoresques(hum_page_num):
    humoresques = Humoresque.query.paginate(per_page=5, page=hum_page_num, error_out=True)
    return render_template('humoresques.html', title='Гуморески',  humoresques=humoresques)


@app.route('/add_poem', methods=['POST', 'GET'])
def add_poem():
    form = PoemForm()
    if form.validate_on_submit():
        poem = Poem(title=form.title.data, text=form.text.data)
        db.session.add(poem)
        db.session.commit()
        return redirect(url_for('add_poem'))
    return render_template('add_poem.html', title="Add poem", form=form)


@app.route('/add_humoresque', methods=['POST', 'GET'])
def add_humoresque():
    form = HumoresqueForm()
    if form.validate_on_submit():
        humoresque = Humoresque(title=form.title.data, text=form.text.data)
        db.session.add(humoresque)
        db.session.commit()
        return redirect(url_for('add_humoresque'))
    return render_template('add_humoresque.html', title="Add humoresque", form=form)