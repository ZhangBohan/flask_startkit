#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from werkzeug.contrib.fixers import ProxyFix
from src.common import app

app.wsgi_app = ProxyFix(app.wsgi_app)
app.run(port=9000)