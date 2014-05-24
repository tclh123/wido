# coding=utf-8

from flask import Flask

# TODO: use SQLAlchemy ?


def create_app():
    """Create the app instance."""
    app = Flask(__name__, template_folder="templates")
    # app.config.from_pyfile("app.cfg")

    # whats that?
    # set the secret key.  keep this really secret:
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    # initialize extensions
    # db.init_app(app)

    return app

app = create_app()


# views

import json

from flask import request, redirect, jsonify

from wido.models.timeline import Timeline
from wido.models.home import Home


@app.route('/timeline')
def timeline():
    owner_uid           = request.args.get('owner_uid', 1659177872)
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
    owner_uid           = request.args.get('owner_uid', 1659177872)
    owner_access_token  = request.args.get('owner_access_token', '2.007xjRoBZNmGKBf13ad83cd2fVtNOD')
    start               = int(request.args.get('start', 0))
    limit               = int(request.args.get('limit', 3))

    ss = Home.get(owner_access_token, owner_uid, start, limit)
    return jsonify(statuses=ss)
