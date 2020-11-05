def main(event, context):
    body = {
        "message": "Called from EventBridge",
        "input": event
    }

    return body
