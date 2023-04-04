import boto3, json, os

def lambda_handler(event, context):
    print(json.loads(event['body']))
    data = json.loads(event['body'])
    data['timeDelay'] = int(data['timeDelay'])
    checks = []
    checks.append('message' in data)
    checks.append(type(data['timeDelay']) == int)
    checks.append('option' in data)
    if False in checks:
        response = {
            "statusCode": 400,
            "headers": {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin':'*',
                'Access-Control-Allow-Methods': 'POST',
                'Access-Control-Allow-Credentials': 'true',
                'Content-Type': 'application/json'
            },
            "body": json.dumps( { "Status": "Success", "Reason": "Input failed validation" } )
        }
    else: 
        response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin':'*',
                'Access-Control-Allow-Methods': 'POST',
                'Access-Control-Allow-Credentials': 'true',
                'Content-Type': 'application/json'
            },
            "body": json.dumps( {"Status": "Success"} )
        }
    return response
