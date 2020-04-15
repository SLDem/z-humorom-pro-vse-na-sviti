from flask import redirect, render_template, url_for, session, request
from app import app, db
from app.forms import PoemForm, HumoresqueForm, SearchForm
from app.models import Poem, Humoresque
from werkzeug.datastructures import MultiDict

@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', title='З Гумором Про Все На Світі')


@app.route('/poems/<int:page_num>')
def poems(page_num):
    poems = Poem.query.paginate(per_page=5, page=page_num, error_out=True)
    return render_template('poems.html', title='Вірші',  poems=poems)


@app.route('/humoresques/<int:hum_page_num>')
def humoresques(hum_page_num):
    humoresques = Humoresque.query.paginate(per_page=5, page=hum_page_num, error_out=True)
    return render_template('humoresques.html', title='Гуморески',  humoresques=humoresques)


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():

        poems_by_title = Poem.query.filter(Poem.title.like('%' + form.search_field.data + '%'))
        poems_by_text = Poem.query.filter(Poem.text.like('%' + form.search_field.data + '%'))

        humoresques_by_title = Humoresque.query.filter(Humoresque.title.like('%' + form.search_field.data + '%'))
        humoresques_by_text = Humoresque.query.filter(Humoresque.text.like('%' + form.search_field.data + '%'))

        poems = poems_by_title.union(poems_by_text)
        humoresques = humoresques_by_title.union(humoresques_by_text)

        return render_template('search.html', poems=poems, humoresques=humoresques, form=form, title='Пошук')
    return render_template('search.html', form=form, title='Пошук')


# adding and deleting content
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


@app.route('/delete_poem/<int:poem_id>')
def del_poem(poem_id):
    poem = Poem.query.filter_by(id=poem_id).first_or_404()
    db.session.delete(poem)
    db.session.commit()
    return redirect(url_for('about'))


@app.route('/delete_hum/<int:hum_id>')
def del_hum(hum_id):
    hum = Humoresque.query.filter_by(id=hum_id).first_or_404()
    db.session.delete(hum)
    db.session.commit()
    return redirect(url_for('about'))
