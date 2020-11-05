import json


def hello(event, context):
    response = {
        "statusCode": 200,
        "body": "Numba 1 works!"
    }

    return response
