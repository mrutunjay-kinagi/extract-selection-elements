import boto3

# Initialize Textract client
client = boto3.client('textract', region_name='us-east-2')

# Specify the S3 bucket name and the document key
bucket_name = 'claimlens-textract-test'
document_key = 'Completed Cyber Application Form Jan6.pdf'

# Define the parameters for the Analyze Document API call
params = {
    'DocumentLocation': {
        'S3Object': {
            'Bucket': bucket_name,
            'Name': document_key
        }
    },
    'FeatureTypes': ['TABLES']  # FORMS or TABLES
}

# Call Analyze Document API
response = client.start_document_analysis(**params)


print(response)
