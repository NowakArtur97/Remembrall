import boto3, json, os

def validateData(data):
    checks = []
    checks.append('message' in data)
    checks.append(type(data['timeDelay']) == int)
    checks.append('option' in data)
    if data['option'] in ['email', 'both']:
        checks.append(data['email'] != "")
    return checks

def lambda_handler(event, context):
    print("Received request: ")
    print(json.loads(event['body']))
    data = json.loads(event['body'])
    data['timeDelay'] = int(data['timeDelay'])
    checks = validateData(data)
    if False in checks:
        print("Input failed validation")
        response = {
            "statusCode": 400,
            "body": json.dumps( { "Status": "Success", "Reason": "Input failed validation" } )
        }
    else:
        response = {
            "statusCode": 200,
            "body": json.dumps( {"Status": "Success"} )
        }
    return response
