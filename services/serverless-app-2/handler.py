import json


def hello(event, context):
    response = {
        "statusCode": 200,
        "body": "Numba 2 works!"
    }

    return response
