from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp


class UrlForm(FlaskForm):
    original_link = URLField(
        'Ваша неэстетичная ссылка',
        validators=[
            DataRequired(message='Обязательное поле.'),
            Length(1, 400),
            URL(require_tld=True, message=('Неправильный URL.'))
        ]
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16),
            Optional(),
            Regexp(r'^[A-Za-z0-9]+$')
        ]
    )
    submit = SubmitField('Создать')
