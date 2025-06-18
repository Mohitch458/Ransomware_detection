import boto3
import logging

def upload_to_s3(file_path, bucket_name, s3_key):
    """Upload a file to AWS S3"""
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        logging.info(f"Uploaded {file_path} to S3 bucket {bucket_name}")
    except Exception as e:
        logging.error(f"Error uploading file to S3: {e}")

def download_from_s3(bucket_name, s3_key, download_path):
    """Download a file from AWS S3"""
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, s3_key, download_path)
        logging.info(f"Downloaded {s3_key} from S3 to {download_path}")
    except Exception as e:
        logging.error(f"Error downloading file from S3: {e}")

# Example usage
upload_to_s3('/path/to/important_file.txt', 'my-bucket', 'important_file.txt')
download_from_s3('my-bucket', 'important_file.txt', '/path/to/downloaded_file.txt')
