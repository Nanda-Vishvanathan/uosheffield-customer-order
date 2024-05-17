import boto3
import get_customer_data
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(f"Event: {event}")
    if event['httpMethod'] == 'GET':
        # Check if the path is /customers & # Check if it's a GET request
        if event['path'] == '/customers':
            logger.info("Invoke customers api")
            result = get_customer_data.get_all_customers()
            return result
        # Check if the path is /customer & # Check if it's a GET request
        elif event['path'] == '/customer':
            logger.info("Invoke customer api")
            customer_id = event['queryStringParameters']['id']
            result = get_customer_data.get_customer_by_id(customer_id)
            return result
        else:
            return {
                    'statusCode': 404,
                    'body': 'Resource not found'
                    }
    else:
        return {
                'statusCode': 405,
                'body': 'Method not allowed'
                }
