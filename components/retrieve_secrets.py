# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/
 
import boto3
from botocore.exceptions import ClientError
import json

def get_secret():
 
    secret_name = "cognitosm"
    region_name = "us-east-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = boto3.client(
        service_name='secretsmanager',
        region_name="us-east-2",
        aws_access_key_id="ASIAXDA7ANJKY2CRCICL",
        aws_secret_access_key="FUWfTDCtwqjUoh2I7ngr9ZqwFeEa6IHDIITS5eRv",
        aws_session_token="IQoJb3JpZ2luX2VjEFMaCXVzLWVhc3QtMSJGMEQCICgVc3S79blSRiKYMyQFGEz87OaXNkUrs80fH/lVYPGqAiBESMFEOHK4JdL80hzx4nifwsjq9HWHDrsDYtoBr4TjNSqVAwi8//////////8BEAAaDDQ4NzU0MzgyNzAyOSIM/8Hf18V7nZg1DR7jKukCwKPIJSo6iuSksIbk7ZdLLqieR9oGCFep8JXITra42ojysGMI0fCocjE2bbbnagAAbMetNhAJoPO3JY2vAuzoRt0R3w2ufyOZDvluz0uPGR4FhXg1OuJEZl6eBhBqBcq7HzpvSYmMvTOkIQ76HBMPqw4RJE3IXMQpAT8vzPSN8Rdh/e7xyryc5ATBBOOLqYolb6Fn99iiDSVhRPOumXFON/MoJ6z+HDxRdAN88w9jrpT3tjQVomd7KDlcLQdOwz29DcLEK5bGPvIuDBYhjVprsEr1HNqDTCm99iSTdjdlJ8ttgUBMtFnINv1abrTIr2iJZlQFfrmYJke1siIdN6bmHo+MvpuQYjhyYnODEJOrZcN240F5hJ52gSwhm8Ljx4ipJD8MtY6U1sNlqqvztRS/BE8aX+j5jBX4U4FJgHO3fKExXci3wLIKVS7N5/Ln5Vten8HMg4AjL3BZVdUCbxPzz4pirNF25y8sxjDK6surBjqnAQ0aaS9xiT6rjTRtQfRgUO9HqTZ/61FTbdwlJ1ckChcS0Wx3+0ReyzbFJXw6sZix9GU9DrUP/dbm3OPTA1LS29YwnuLrMm2WCJ4/NYXEY8J4SeRP3XLb4ujJ+8tJmMTrjlXeP+rz/C2BuVwaQGy605DsIMawzYd9PG10jGq5mYfEAWZQLggE2L8iBlBZSGLaXw8RZXkwisqYZew6i+tiaxHGhi5aCX3m"
    )
 
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e
 
    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']
    # print(secret["COGNITO_DOMAIN"])
    # print(secret["COGNITO_DOMAIN"])
    
    processed=json.loads(secret)
    return processed
    # Your code goes here.
