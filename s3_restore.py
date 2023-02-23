import boto3

# Replace "BUCKET_NAME" with your S3 bucket name
bucket_name = "BUCKET_NAME"

# Create an S3 client
s3 = boto3.client('s3')

# Get a list of all version deleted objects in the S3 bucket
versions = s3.list_object_versions(
    Bucket=bucket_name,
    Prefix='',
    MaxKeys=1000,
)

# Restore each version deleted object in the S3 bucket
for version in versions['Versions']:
    # Get the object key and version ID
    object_key = version['Key']
    version_id = version['VersionId']

    # Copy the object to restore the deleted version
    s3.copy_object(
        Bucket=bucket_name,
        CopySource={
            'Bucket': bucket_name,
            'Key': object_key,
            'VersionId': version_id
        },
        Key=object_key,
    )

    # Print the object key and version ID of the restored object
    print(f'Restored object: {object_key}, version ID: {version_id}')
