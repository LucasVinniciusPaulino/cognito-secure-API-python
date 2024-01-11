import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Items')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        id = body['id']
        price = body['price']

        response = table.put_item(
            Item={
                'id': id,
                'price': price
            }
        )

        statusCode = 200
        responseBody = json.dumps('Item inserido com sucesso!')

    except Exception as e:
        statusCode = 500
        responseBody = json.dumps(str(e))

    response = {
        'statusCode': statusCode,
        'body': responseBody
    }

    return response
