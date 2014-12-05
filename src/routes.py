from common import app
from flask import render_template
from common import cache, cached

@app.route('/hello_world')
def hello_world():
    app.logger.debug('hello world')
    return 'Hello World!'


@app.route('/')
def root():
    msg = 'Hello World!!!'
    return render_template('index.jinja2', msg=msg)


@app.route('/cache_test')
@cached(timeout=10)
def cache_test():
    app.logger.info('without cache')
    return 'Hello World~~~'
