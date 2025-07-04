
import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(file_name, bucket_name, object_name=None):
    """Upload a file to an S3 bucket"""
    s3 = boto3.client('s3')

    if object_name is None:
        object_name = file_name

    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print(f"✅ Upload Successful: {object_name}")
    except FileNotFoundError:
        print("❌ The file was not found")
    except NoCredentialsError:
        print("❌ Credentials not available")

# Example usage
if __name__ == "__main__":
    # Replace these with your own details
    file_name = "sample.csv"  # The file you want to upload
    bucket_name = "your-s3-bucket-name"
    object_name = "folder_in_bucket/sample.csv"  # Optional path in bucket

    upload_to_s3(file_name, bucket_name, object_name)

