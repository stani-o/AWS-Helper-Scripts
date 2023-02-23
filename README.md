# AWS Helper Scripts
This repository contains helper scripts for working with AWS services. These scripts are provided as-is and are not officially supported by AWS. Please note that the use of these scripts is at your own risk and I am not responsible for any issues that may arise from their use.

## Requirements
The scripts in this repository require the following software to be installed:

- Python 3.x
- AWS SDK for Python (Boto3)

## Usage
Each script in this repository is designed to perform a specific task. Please review the source code and any accompanying documentation before running the scripts.

To use the scripts in this repository, you will need to configure your AWS credentials. You can do this by creating an IAM user with the necessary permissions and configuring your AWS CLI or SDK with the user's access key and secret key. Please refer to the AWS documentation for more information on setting up IAM users.

## Scripts

### s3_restore.py
Restores all versioned deleted objects in an S3 bucket. The script first lists all the deleted versions of objects in the bucket, and then restores each deleted version using the copy_object method of the Boto3 S3 client.

## Disclaimer
These scripts are provided as-is and are not officially supported by AWS. I am not responsible for any issues that may arise from their use. Please use these scripts at your own risk and always test them in a non-production environment before using them in a production environment.

## Contributing
If you would like to contribute to this repository, please fork the repository and submit a pull request. I welcome contributions and feedback from the community.

## License
This repository is licensed under the MIT license. See the LICENSE file for more information.

## Contact
If you have any questions or concerns about this repository, please contact me in linkedin.
