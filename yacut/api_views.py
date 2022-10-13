from http import HTTPStatus
from re import match

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URL_map
from .views import get_unique_short_id


BAD_URL = 'Указано недопустимое имя для короткой ссылки'
LOST_DATA = 'Отсутствует тело запроса'
LOST_ORIGINAL_URL = '"url" является обязательным полем!'
SHORT_IN_BD = 'Такой url уже занят'
URL_NOT_FOUNDED = 'Указанный id не найден'
BAD_SHORT_URL = 'Указано недопустимое имя для короткой ссылки'
SHORT_URL = r'^[A-Za-z0-9]{1,16}$'


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()

    if not data:
        raise InvalidAPIUsage(LOST_DATA)

    if 'url' not in data or not data['url']:
        raise InvalidAPIUsage(LOST_ORIGINAL_URL)

    if 'custom_id' not in data or not data['custom_id']:
        short_id = get_unique_short_id()
        data['custom_id'] = short_id

    if not match(SHORT_URL, data['custom_id']):
        raise InvalidAPIUsage(BAD_SHORT_URL)

    if URL_map.query.filter_by(short=data['custom_id']).first() is not None:
        raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.')

    new_url = URL_map()
    new_url.from_dict(data)
    db.session.add(new_url)
    db.session.commit()
    return jsonify(new_url.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_url(short_id):
    url_in_bd = URL_map.query.filter_by(short=short_id).first()
    if not url_in_bd:
        raise InvalidAPIUsage(URL_NOT_FOUNDED, HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_in_bd.original}), HTTPStatus.OK
