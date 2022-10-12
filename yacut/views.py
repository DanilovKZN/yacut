from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import UrlForm
from .models import URL_map
from .random_generator import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = UrlForm()
    if form.validate_on_submit():
        short_id=form.custom_id.data
        if not short_id:
            short_id = get_unique_short_id()

        if URL_map.query.filter_by(short=short_id).first() is not None:
            flash(f'Имя {short_id} уже занято!', 'danger')
            return render_template('index.html', form=form)

        Url_obj = URL_map(
            original=form.original_link.data,
            short=short_id,
        )
        db.session.add(Url_obj)
        db.session.commit()
        flash(url_for(
            'jump_short_link',
            short_link=short_id,
            _external=True),
            'result'
        )
    return render_template('index.html', form=form)


@app.route('/<string:short_link>')
def jump_short_link(short_link):
    return redirect(
        URL_map.query.filter_by(short=short_link).first_or_404().original
    )
