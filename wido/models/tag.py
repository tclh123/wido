# coding=utf-8

from wido.ext import db

from wido.models.user_tag import UserTag


class Tag(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Unicode(100), nullable=False)

    def __repr__(self):
        return ('<Tag(id=%r, parent_id=%r, name=%r)>'
                % (self.id, self.parent_id, self.name))

    def users_with_tag(self):
        uts = UserTag.query.filter(UserTag.tag_id == self.id)
        return uts

    def children(self):
        tags = Tag.query.filter(Tag.parent_id == self.id)
        return tags

    def as_dict(self):
        return dict(id=self.id,
                    parent_id=self.parent_id,
                    name=self.name)
