#!/usr/bin/env python
# coding=utf-8

""" A WSGI app for dev.  """

from wido.app import app
from wido.config import APP_PORT

if __name__ == "__main__":
    app.debug = True

    app.run(host='0.0.0.0', port=APP_PORT)
