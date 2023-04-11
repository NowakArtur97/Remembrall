import boto3, json, os

sm = boto3.client('stepfunctions')
STATE_MACHINE_ARN = os.environ["STATE_MACHINE_ARN"]

def validateData(data):
    checks = []
    checks.append('message' in data)
    checks.append(type(data['timeDelay']) == int)
    checks.append('notificationType' in data)
    if data['notificationType'] in ['email', 'both']:
        checks.append(data['email'] != "")
    if data['notificationType'] in ['sms', 'both']:
        checks.append(data['phoneNumber'] != "")
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
        sm.start_execution(stateMachineArn=STATE_MACHINE_ARN, input=json.dumps(data))
        response = {
            "statusCode": 200,
            "body": json.dumps( {"Status": "Success"} )
        }
    return response
