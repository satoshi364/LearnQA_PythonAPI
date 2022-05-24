import json

string_as_json_format = '{"answer": "Hello, Ninja"}'
obj = json.loads(string_as_json_format)
print(obj['answer'])