from github import Github
from flask import Flask
import base64
import sys
import yaml
import json

app = Flask(__name__)
#/v1/<filename>
@app.route('/v1/<filename>')
def config(filename):
    path = sys.argv[1].split("/")
    try:
        git = Github()
    except:
        return "Bad Credentials!"
    else:
        try:
            user = git.get_user(path[3])
        except:
            return "User not found!"
        else:
            try:
                repo = user.get_repo(path[4])
            except:
                return "Repositoryy not found!"
            else:
                files = repo.get_contents('/')
                for i in files:
                    file_format = str(i.name)
                    extension = file_format.split(".")
                    if (file_format ==filename):
                        if (extension[1] == "yml" ):
                            contents = (i.content.decode('base64'))
                            return yaml.dump(contents, default_flow_style=False)
                        elif (extension[1] == "json"):
                            contents = (i.content.decode('base64'))
                            return json.dumps(contents)
if __name__=="__main__":
    app.run(debug= True,host='0.0.0.0')
