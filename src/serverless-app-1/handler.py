import boto3
import json
import os

#   Environment Variables
EVENT_BRIDGE_SOURCE = os.environ['EVENT_BRIDGE_SOURCE']
EVENT_BUS_NAME = os.environ['EVENT_BUS_NAME']


def main(event, context):
    body = {
        "message": "Successfully sent to EventBridge",
        "input": event
    }

    put_event()

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def put_event():
    client = boto3.client('events')
    try:
        detail = {
            "key": "value"
        }
        response = client.put_events(
            Entries=[
                {
                    'Source': EVENT_BRIDGE_SOURCE,
                    'DetailType': 'test',
                    'Detail': json.dumps(detail),
                    'EventBusName': EVENT_BUS_NAME
                }
            ]
        )
        print(response)
        print('Sent message to EventBridge')
    except Exception as e:
        print(e)
        print('Failed to send message to EventBridge')
