import json
from fnmatch import fnmatch
def match(actual, expected):
    return fnmatch(actual, expected)

def getUrl(page):
    with open("resources/pages.json", 'r') as file:
        data = json.load(file)
        return data[page]

def getCreds(profile):
    with open("resources/users.json", 'r') as file:
        data = json.load(file)
        return data[profile]

def getError(error):
    with open("resources/errors.json", 'r') as file:
        data = json.load(file)
        return data[error]
