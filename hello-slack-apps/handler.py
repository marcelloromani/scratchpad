import json
from base64 import b64decode
from urllib.parse import parse_qs


def parse_event_body(event: dict) -> dict:
    body = b64decode(event['body']).decode()
    qs = parse_qs(body)
    return qs


def hello(event, context):
    print(json.dumps(event))

    response = {"statusCode": 200, "body": ""}
    return response
