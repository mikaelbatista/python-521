
import flask
import docker

from services.login_required import login_required


blueprint = flask.Blueprint('docker', __name__)

@blueprint.route('/docker', methods=[ 'GET', 'POST' ])
@login_required
def _docker():

    conn = docker.DockerClient()

    context = {
        'title': 'Python | Sysadmin',
        'containers': conn.containers.list(all=True) 
    }

    return flask.render_template('docker.html', context=context)

@blueprint.route('/docker/<containerid>/start', methods=[ 'GET' ])
def start_container(containerid):

    conn = docker.DockerClient()

    container = conn.containers.get(containerid)
    container.restart()

    return flask.redirect('/docker')
    
@blueprint.route('/docker/<containerid>/stop', methods=[ 'GET' ])
def stop_container(containerid):
    
    conn = docker.DockerClient()

    container = conn.containers.get(containerid)
    container.stop()

    return flask.redirect('/docker')