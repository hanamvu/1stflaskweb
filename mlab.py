import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds149144.mlab.com:49144/c4e11_namvh15
host = "ds149144.mlab.com"
port = 49144
db_name = "c4e11_namvh15"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
