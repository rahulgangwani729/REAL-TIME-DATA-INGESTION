import json
from datetime import datetime
import boto3


def check_duration(start_date, end_date):
    start_date1 = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date1 = datetime.strptime(end_date, '%Y-%m-%d').date()

    diff = (end_date1 - start_date1).days

    if diff > 1:
        return True
    
    return False


def lambda_handler(event, context):
    try:
        
        print("Event: ", event)
    
        data = json.loads(event[0]['body'])
    
        print("Data: ", data)
    
        start_date_str = data['startDate']
        end_date_str = data['endDate']
    
        check = check_duration(start_date_str, end_date_str)
    
        if check:
            print("Record satisfy condition of duration greater than 1 day.")
            
            return {
                'statusCode': 200,
                'body': json.dumps(data)
                }
        else:
            print("Record will be skipped as condition not satisfied of duration less than or equal to 1 day.")
            
            return {
                'statusCode': 200,
                'body': 'None'
                }
                
    except Exception as e:
        
        print(f"exception occured in Filter Airbnb Bookings lambda function, error = {e}")
