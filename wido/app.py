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


@app.route('/timeline')
def timeline():
    return r
