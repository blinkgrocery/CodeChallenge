import boto3

def filesearch(bucket_name, search_substring):
    # Initialize the S3 client
    s3 = boto3.client('s3')
    # List to store matching file keys
    matching_files = []
    try:
        # List all objects in the specified bucket
        response = s3.list_objects_v2(Bucket=bucket_name)

        # Iterate through each object in the bucket
        for obj in response.get('Contents', []):
            file_key = obj['Key']

            # Process only .txt files
            if file_key.lower().endswith('.txt'):
                try:
                    # Read the file content
                    file_content = s3.get_object(Bucket=bucket_name, Key=file_key)['Body'].read().decode('utf-8')

                    # Check if the substring exists in the file content
                    if search_substring.lower() in file_content.lower():
                        matching_files.append(file_key)
                except Exception as e:
                    print(f"Error reading {file_key}: {e}")
    except Exception as e:
        print(f"Error listing objects in bucket {bucket_name}: {e}")

    return matching_files

if __name__ == "__main__":
    # Replace 'your-bucket-name' and 'your-substring' with actual values
    bucket_name = 'blinkgrocery'
    search_substring = 'Text'

    # Search for matching files
    matching_files = filesearch(bucket_name, search_substring)

    if matching_files:
        print("Matching files:")
        for file_key in matching_files:
            print(file_key)
    else:
        print("No matching files found.")
