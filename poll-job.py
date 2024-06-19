import boto3
import json

# Initialize Textract client
client = boto3.client('textract', region_name='us-east-2')


# Call Analyze Document API
response = client.get_document_analysis(JobId='9737c68d65d879b76a0256bed1ca04381a9000cbdfec820ce5fbe7470e225a23')

# Print the detected text and other elements
print(json.dumps(response))
