# coding=utf-8

from wido.ext import db


class UserTag(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    user_name = db.Column(db.Unicode(100), nullable=False)
    tag_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return ('<UserTag(id=%r, user_id=%r, tag_id=%r)>'
                % (self.id, self.user_id, self.tag_id))

    def as_dict(self):
        return dict(id=self.id,
                    user_id=self.user_id,
                    user_name=self.user_name,
                    tag_id=self.tag_id)
