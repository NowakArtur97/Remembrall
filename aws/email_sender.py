import boto3, os, json

SENDER = os.environ["SENDER"]
EMAIL_SUBJECT = os.environ["EMAIL_SUBJECT"]

ses = boto3.client("ses")

def send_email(input):
    recipient = input["email"]
    message = input["message"]
    ses.send_email(
        Source=SENDER,
        Destination={"ToAddresses": [recipient]},
        Message={
            "Subject": {"Data": EMAIL_SUBJECT},
            "Body": {"Text": {"Data": message}},
        },
    )
    print('Message: [' + message + '] successfully sent to: ' + recipient)

def lambda_handler(event, context):
    attachment = {}
    print("Received event: " + json.dumps(event))
    try:
        input = event["Input"]
        send_email(input)
        return "Success"
    except Exception as e:
        print("Exception when sending email")
        print(e)
        return "Fail"
