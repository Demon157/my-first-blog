import json
json_str = '{ "hello": "world"} '
r = json.loads(json_str)

print(r)
