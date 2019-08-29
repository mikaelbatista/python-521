import logging

import flask
import ldap3


blueprint = flask.Blueprint('auth', __name__)

@blueprint.route('/sign-in', methods=[ 'GET', 'POST' ])
def sign_in():

    context = {
        'title': 'Python | Sysadmin',
    }

    EMAIL = 'admin@admin'
    PASSWORD = 'admin'

    if flask.request.method == 'POST':

        email = flask.request.form.get('email')
        password = flask.request.form.get('password')

        if email == EMAIL and password == PASSWORD:
            logging.info('Usuário logado')
        else:
            logging.warning('Falha na autenticação' + email)
            
    return flask.render_template('sign-in.html', context=context)