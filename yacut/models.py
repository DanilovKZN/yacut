from datetime import datetime

from flask import url_for

from . import db
from .random_generator import get_unique_short_id


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(300), nullable=False)
    short = db.Column(db.String(16), default=get_unique_short_id())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'jump_short_link',
                short_link=self.short,
                _external=True
            )
        )

    def from_dict(self, data):
        setattr(self, 'original', data['url'])
        setattr(self, 'short', data['custom_id'])
