from http import HTTPStatus
import random

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage, check_inique_short_url
from .models import URLMap
from .views import check_symbols, SYMBOLS


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()

    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')

    if 'url' not in data:
        raise InvalidAPIUsage(
            '"url" является обязательным полем!', HTTPStatus.BAD_REQUEST
        )

    if 'custom_id' not in data or data['custom_id'] is None:
        data['custom_id'] = ''.join(random.choices(SYMBOLS, k=6))

    custom_id = data['custom_id']

    if len(custom_id) > 16 or not check_symbols(custom_id):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки', HTTPStatus.BAD_REQUEST
        )

    if check_inique_short_url(custom_id):
        raise InvalidAPIUsage(
            (f'Имя "{custom_id}" уже занято.'), HTTPStatus.BAD_REQUEST
        )

    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if not url:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url.original}), HTTPStatus.OK