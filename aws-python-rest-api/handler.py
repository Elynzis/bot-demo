import json

def _build_response(status_code, body):
    return  {
        "statusCode": status_code,
        "body": json.dumps(body)
    }

def hello(event, context):
    body = {
        "message": "Hello World",
    }
    return _build_response(200, body)
 
def _mock_db(org_id):
    # mocking database repository

    if org_id == 1:
        return "CTO"
    else:
        return "BOT"
    
def get_org(event, context):
    # get organization name from given id
    org_id = event.get("pathParameters").get("org_id")
    
    try:
        org_id = int(org_id)
        body = {
            "organization": _mock_db(org_id=org_id)
        }
        return _build_response(200, body)

    except ValueError as e:
        return _build_response(400, {"error": "org_id must be integer"})