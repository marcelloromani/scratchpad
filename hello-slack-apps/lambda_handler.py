from base64 import b64decode
from urllib.parse import parse_qs


def parse_event_body(event: dict) -> dict:
    if event['isBase64Encoded']:
        body = b64decode(event['body']).decode()
    else:
        body = event['body']
    qs = parse_qs(body)
    return qs


def get_args_string_from_event(event: dict) -> str:
    return parse_event_body(event)['text'][0]


def parse_args(args: str) -> (str, str):
    elements = args.strip().split()
    if len(elements) < 2:
        raise ValueError("Two args are required: <animal> <message>")
    animal, rest = elements[0], elements[1:]
    rest = " ".join(rest)
    return animal, rest


def handler(event, context):
    # print(json.dumps(event))

    app_args = get_args_string_from_event(event)
    animal, message = parse_args(app_args)

    response_body = f"{animal}: {message}"

    response = {"statusCode": 200, "body": response_body}
    return response
