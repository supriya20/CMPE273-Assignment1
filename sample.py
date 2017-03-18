from github import Github
from flask import Flask
import base64
import sys
import yaml
import json

list1 = sys.argv[1].split("/")
g = Github("supriya20", "Sup072091")
user = g.get_user(list1[3])
print user
repo = user.get_repo(list1[4])
print repo
files = repo.get_contents('/')
print files
for i in files:
    f = str(i.name)
    #print (f)
    #extension = f.split(".")
    if (f=="sample.json"):
        #contents = (i.content.decode('base64'))
        #sprint yaml.dump(contents, default_flow_style=False)
        #print yaml.dump(yaml.load(contents))
        #print contents
        contents = (i.content.decode('base64'))
        #return yaml.dump(yaml.load(contents))
        print json.dumps(contents)