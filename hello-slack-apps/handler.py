import json


def hello(event, context):
    print(json.dumps(event))

    response = {"statusCode": 200, "body": ""}
    return response
