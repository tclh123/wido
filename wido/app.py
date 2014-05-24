# coding=utf-8

from flask import Flask

from wido.ext import db
from wido.config import DATABASE_URI, SQLALCHEMY_DATABASE_URI

# TODO: use SQLAlchemy ?


def create_app():
    """Create the app instance."""
    app = Flask(__name__, template_folder="templates")

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

    # whats that?
    # set the secret key.  keep this really secret:
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    # initialize extensions
    db.init_app(app)

    return app

app = create_app()


# views

from flask import request, redirect, jsonify

from wido.models.timeline import Timeline
from wido.models.home import Home
from wido.models.rec import Rec
from wido.models.video_url import VideoURL
from wido.models.tag import Tag


@app.route('/timeline')
def timeline():
    owner_uid           = int(request.args.get('owner_uid', 1659177872))
    owner_access_token  = request.args.get('owner_access_token', '2.007xjRoBZNmGKBf13ad83cd2fVtNOD')
    since_id            = request.args.get('since_id', 0)
    max_id              = request.args.get('max_id', 0)
    count               = request.args.get('count', 20)
    page                = request.args.get('page', 1)
    t = Timeline.get(owner_uid, owner_access_token,
                     since_id, max_id, count, page)
    return jsonify(**t.r)


@app.route('/home')
def home():
    owner_uid           = int(request.args.get('owner_uid', 1659177872))
    owner_access_token  = request.args.get('owner_access_token', '2.007xjRoBZNmGKBf13ad83cd2fVtNOD')
    start               = int(request.args.get('start', 0))
    limit               = int(request.args.get('limit', 3))

    # print owner_uid, type(owner_uid)
    # print owner_access_token, type(owner_access_token)

    ss = Home.get(owner_access_token, owner_uid, start, limit)
    return jsonify(statuses=ss)


@app.route('/friends')
def bilateral():
    owner_uid           = int(request.args.get('owner_uid', 1659177872))
    owner_access_token  = request.args.get('owner_access_token', '2.007xjRoBZNmGKBf13ad83cd2fVtNOD')
    start               = int(request.args.get('start', 0))
    limit               = int(request.args.get('limit', 3))

    ss = Home.get_bi(owner_access_token, owner_uid, start, limit)
    return jsonify(statuses=ss)


@app.route('/rec')
def rec():
    owner_access_token  = request.args.get('owner_access_token', '2.007xjRoBZNmGKBf13ad83cd2fVtNOD')
    start               = int(request.args.get('start', 0))
    limit               = int(request.args.get('limit', 3))

    statuses = Rec.get(owner_access_token, start, limit)
    return jsonify(statuses=statuses)


@app.route('/video_url')
def video_url():
    owner_access_token  = request.args.get('owner_access_token', '2.007xjRoBZNmGKBf13ad83cd2fVtNOD')
    urls                = request.args.getlist('urls')

    maps = VideoURL.expand(owner_access_token, urls)
    return jsonify(maps=maps)


@app.route('/tags')
def tags():
    parent = request.args.get('parent', 0)

    tags = Tag.query.filter(Tag.parent_id == parent)
    return jsonify(tags=[tag.as_dict() for tag in tags])


@app.route('/user_with_tag')
def user_with_tag():
    tag_id = request.args.get('tag_id', 0)

    tag = Tag.query.get(tag_id)
    if not tag:
        return jsonify({})
    uts = tag.users_with_tag()
    return jsonify(users=[ut.as_dict() for ut in uts])
