import json
import uuid
import random
from faker import Faker
from datetime import datetime, date
import boto3

queue_url = 'https://sqs.us-east-1.amazonaws.com/730335310416/AirbnbBookingQueue'

sqs_client = boto3.client('sqs')
fake = Faker()

def mock_data_generator():
    bookingId = str(uuid.uuid4())
    userId = random.randint(1, 100)
    propertyId = random.randint(101, 1001)
    location = f'{fake.city()}, {fake.country()}'

    start_date = date(2023, 6, 1)
    end_date = date.today()

    start_date1 = fake.date_between_dates(date_start=start_date, date_end=end_date)
    end_date1 = fake.date_between_dates(date_start=start_date1, date_end=end_date)

    startDate = start_date1.strftime('%Y-%m-%d')
    endDate = end_date1.strftime('%Y-%m-%d')

    price = round(random.uniform(20,200), 1)

    result_dict = {
        "bookingId": bookingId,
        "userId": userId,
        "propertyId": propertyId,
        "location": location,
        "startDate": startDate,
        "endDate": endDate,
        "price": price
        }

    return result_dict


def lambda_handler(event, context):
    try:

        print("Event: ", event)

        for i in range(20):
            d = mock_data_generator()
            print(d)

            res = sqs_client.send_message(QueueUrl=queue_url, MessageBody=json.dumps(d))

            print("Response: ", res)

        return {
            'statusCode': 200,
            'body': json.dumps("Message Published to SQS !!!")
        }
    
    except Exception as e:
        
        print(f"exception occured in Produce Airbnb Booking Data lambda function, error = {e}")
