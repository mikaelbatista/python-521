import json


class Git:

    def __init__(self, user, password, repo, *args, **kwargs):
        self.user = user
        self.password = password
        self.repo = repo

    def commit(self):
        print('Comitando')

class Config:

    def __init__(self, app, version, *args, **kwargs    ):
        self.app = app
        self.version = version

if __name__ == "__main__":
    

    settings = {}
    with open('settings.json') as f:
        settings = json.loads(f.read())

    print(settings)

    git = Git(**settings.get('git'))
    config = Config(**settings.get('config'))

    print(git.user, git.password, git.repo)    
    print(config.app, config.version)
    
    git.commit()
