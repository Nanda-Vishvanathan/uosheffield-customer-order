import db_connection
import json
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_all_customers():
    logger.info("Querying customers & orders data!")
    query_statement = (
            "SELECT customers.*, orders.order_id, orders.date, orders.amount "
            "FROM customers "
            "LEFT JOIN orders ON customers.customer_id = orders.customer_id"
    )
    result_data = db_connection.execute_sql_query(query_statement)
    actual_result = process_result(result_data)
    return actual_result


def get_customer_by_id(customer_id):
    logger.info("Querying customer data by id")
    query_statement = (
        "SELECT customers.*, orders.order_id, orders.date, orders.amount "
        "FROM customers "
        "LEFT JOIN orders ON customers.customer_id = orders.customer_id "
        "WHERE customers.customer_id = %s")
    result_data = db_connection.execute_sql_query(query_statement, customer_id)
    actual_result = process_result(result_data)
    return actual_result


def process_result(customer_data):
    logger.info("Processing the data!")
    rows = []
    for data in customer_data:
        if data:
            row_dict = {
                        'customer_id': data[0],
                        'firstname': data[1],
                        'surname': data[2],
                        'email': data[3],
                        'address': data[4],
                        'zip_code': data[5],
                        'region': data[6],
                        'status': data[7],
                        'order_id': data[8],
                        'date': data[9],
                        'amount': data[10]
                     }
        rows.append(row_dict)

    return {
            'statusCode': 200,
            'body': json.dumps(rows)
            }
