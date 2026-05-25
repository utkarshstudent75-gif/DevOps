# This code uses the boto3 library to interact with Amazon S3. It creates a client for S3, retrieves the access control list (ACL) for a specified bucket, and prints the response. Make sure to replace 'utkarsh-demo-bucket-1234567890' with the name of your actual S3 bucket.
import boto3

client = boto3.client('s3')

#here's how you can create a bucket using boto3, but it's commented out to avoid accidental bucket creation. Uncomment and run it if you want to create a new bucket.

#response = client.create_bucket(
    #Bucket='utkarsh-demo-bucket-1234567890',
#)

#here's how you can list all buckets in your S3 account, but it's commented out to avoid unnecessary API calls. Uncomment and run it if you want to see the list of your buckets.

#response = client.list_buckets()

#here's how you can retrieve the ACL for a specific bucket.

response = client.get_bucket_acl(
    
    Bucket='utkarsh-demo-bucket-1234567890',
    
)

print(response)