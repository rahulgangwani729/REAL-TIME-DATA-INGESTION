import json
import boto3
from datetime import datetime


def lambda_handler(event, context):
    try:
        s3_client = boto3.client('s3')
        
        bucket = 'lambda-to-s3-airbnb-booking-records'
        file_name = 'airbnb_booking_' + datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + '.json'
        
        print("Event: ", event)
        
        data = event[0]['body']
        
        print("Data: ", data)
        
        if data != 'None':
            
            res = s3_client.put_object(Body=data, Bucket=bucket, Key=file_name)
            
            print("Response: ", res)
                
            print("Successfully saved in S3 !!!")
        
        else:
            
            print("Data None, skipped")
            
    except Exception as e:
        print(f"exception occured in Process Filtered Bookings lambda function, error = {e}")
