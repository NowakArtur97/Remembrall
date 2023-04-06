import os, cfnresponse, boto3, urllib

FILE_NAME = os.environ['FILE_NAME']
BUCKET_NAME = os.environ['BUCKET_NAME']
VALUES_TO_REPLACE = os.environ['VALUES_TO_REPLACE'].split(",")
VALUES_TO_BE_REPLACED = os.environ['VALUES_TO_BE_REPLACED'].split(",")

TMP_FILE_PATH = '/tmp/' + FILE_NAME

s3 = boto3.resource('s3')

def download_file():
  BUCKET = s3.Bucket(BUCKET_NAME)
  BUCKET.download_file(FILE_NAME, TMP_FILE_PATH)

def read_file():
    with open(TMP_FILE_PATH, 'r') as file:
      filedata = file.read()
    return filedata

def reaplce_values_in_file(filedata):
    for index, toReplace in enumerate(VALUES_TO_REPLACE):
      toBeReplaced = VALUES_TO_BE_REPLACED[index]
      filedata = filedata.replace(toReplace, toBeReplaced)
      print("Chaned value from: " + toReplace + " to: " + toBeReplaced)

def save_new_values_to_file(filedata):
    with open(TMP_FILE_PATH, 'w') as file:
      file.write(filedata)

def upload_updated_file_to_s3():
    s3.Object(BUCKET_NAME, FILE_NAME).put(Body=open(TMP_FILE_PATH, 'rb').read())

def lambda_handler(event, context):
    download_file()
    filedata = read_file()
    reaplce_values_in_file(filedata)
    save_new_values_to_file(filedata)
    upload_updated_file_to_s3()