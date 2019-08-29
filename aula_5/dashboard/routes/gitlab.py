
import flask
import requests


blueprint = flask.Blueprint('gitlab', __name__)

@blueprint.route('/gitlab', methods=[ 'GET', 'POST' ])
def gitlab():

    users = requests.get('http://localhost:8000/api/v4/users', headers={
        'Private-Token': 'uUmZe2QZGuvoATevamxu'
    })
    
    projects = requests.get('http://localhost:8000/api/v4/projects', headers={
        'Private-Token': 'uUmZe2QZGuvoATevamxu'
    })

    context = {
        'title': 'Python | Sysadmin',
        'users': users.json() if users.status_code == 200 else [],
        'projects': projects.json() if projects.status_code == 200 else [],
    }

    return flask.render_template('gitlab.html', context=context)


@blueprint.route('/gitlab/<projectid>', methods=[ 'GET', 'POST' ])
def get_commits(projectid):

    url = 'http://localhost:8000/api/v4/projects/{}/repository/commits'.format(projectid)

    commits = requests.get(url, headers={
        'Private-Token': 'uUmZe2QZGuvoATevamxu'
    })

    context = {
        'title': 'Python | Sysadmin',
        'commits': commits.json() if commits.status_code == 200 else []
    }

    return flask.render_template('gitlab_commits.html', context=context)










    