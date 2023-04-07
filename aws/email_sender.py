import boto3, os, json

SENDER = os.environ["SENDER"]
EMAIL_SUBJECT = os.environ["EMAIL_SUBJECT"]

ses = boto3.client("ses")

def send_email(input):
    recipient = event["Input"]["email"]
    message = event["Input"]["message"]
    ses.send_email(
        Source=SENDER,
        Destination={"ToAddresses": [recipient]},
        Message={
            "Subject": {EMAIL_SUBJECT},
            "Body": {"Text": {"Data": message}},
        },
    )
    print('Message: [' + message + '] sent successfully to: ' + recipient)


def lambda_handler(event, context):
    attachment = {}
    print("Received event: " + json.dumps(event))
    try:
        input = event["Input"]
        send_email(input)
        return "Success"
    except Exception as e:
        print("Exception when sending reports")
        print(e)
        return "Fail"