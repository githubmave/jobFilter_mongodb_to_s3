from botocore.exceptions import ClientError
import json
import os
from dotenv import load_dotenv
from pytz import timezone
from datetime import datetime

def upload_s3(s3_client,data,bucket,file_name):
    load_dotenv()
    tz_sydney = timezone(os.environ['TZ_LOCAL'])
    date=datetime.now(tz_sydney).strftime("%Y-%m-%d")

    upload_data=json.dumps(data,ensure_ascii=False)
    key=os.environ['LOAD_FOLDER_NAME'] + date + '/'+file_name
    try:
        s3_client.put_object(Bucket=bucket, Key=key, Body=upload_data)
    except ClientError as e:
        error_message=e.response['Error']['Message']
        print(error_message)    