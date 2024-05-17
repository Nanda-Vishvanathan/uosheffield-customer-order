import mysql.connector
import boto3
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def establish_connection():
    logger.info("Fetching SSM parameters")
    # Fetching SSM parameters
    ssm_client = boto3.client('ssm')
    db_host = ssm_client.get_parameter(
        Name='uos_db_host', WithDecryption=True)['Parameter']['Value']
    db_name = ssm_client.get_parameter(
        Name='uos_db_name', WithDecryption=True)['Parameter']['Value']
    db_password = ssm_client.get_parameter(
        Name='uos_rds_password', WithDecryption=True)['Parameter']['Value']
    db_username = ssm_client.get_parameter(
        Name='uos_rds_username', WithDecryption=True)['Parameter']['Value']
    try:
        # Connect to the RDS database
        logger.info("Establishing connection to the uos db")
        connection = mysql.connector.connect(
                            host=db_host,
                            user=db_username,
                            password=db_password,
                            database=db_name)
        logger.info("Connection established with uos db")
        return connection
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }


def execute_sql_query(query_statement, customer_id=None):
    # SQL query to fetch all customer and order data
    logger.info("Executing Query")
    connection = establish_connection()
    cursor = connection.cursor()

    # Execute the SQL query
    if customer_id:
        cursor.execute(query_statement, (customer_id,))
    else:
        cursor.execute(query_statement)
    logger.info("Query executed successfully & fetching results!")
    # Fetch all rows from the result set
    result_data = cursor.fetchall()
    # Committing & Closing connection
    connection.commit()
    connection.close()
    return result_data
