
import sys
import os
import time
import logging 
import flask
import requests

from routes.auth import blueprint as auth_blueprint
from routes.jenkins import blueprint as jenkins_blueprint
from routes.docker import blueprint as docker_blueprint
from routes.gitlab import blueprint as gitlab_blueprint


FORMAT_STRING = '''
%(asctime)s | %(levelname)s | %(filename)s | %(message)s

'''.replace('/n', '').strip()

DATE_FORMAT_STRING = '''
%d/%m/%Y %H:%M:%S
'''.replace('/n', '').strip()

opts = {
    'filename': 'app.log',
    'level': int(os.getenv('DEBUG LEVEL') or 0),
    'format': FORMAT_STRING,
    'datefmt': DATE_FORMAT_STRING
}

logging.basicConfig(**opts)

app = flask.Flask(__name__)

app.secret_key = 'secret'

app.register_blueprint(auth_blueprint)
app.register_blueprint(jenkins_blueprint)
app.register_blueprint(docker_blueprint)
app.register_blueprint(gitlab_blueprint)

@app.route('/')
def index():

    res = requests.get('https://gen-net.herokuapp.com/api/users/')
    
    users = res.json() if res.status_code == 200 else []

    def extract(u):
        return u

    context = {
        'title': 'Python | Sysadmin',
        'users': [ extract(u) for u in users ]
    }

    return flask.render_template('index.html', context=context)

if __name__ == "__main__":

    root_module = os.path.abspath(os.path.curdir)
    sys.path.append(root_module)

    logging.info('iniciando aplicação')

    app.run(host='0.0.0.0')