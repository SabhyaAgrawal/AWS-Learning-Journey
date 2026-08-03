"""
Project: Launch an Amazon EC2 Instance using Python (Boto3)

Description:
This script launches a new EC2 instance in AWS using the Boto3 SDK.

Prerequisites:
- AWS CLI configured (`aws configure`)
- Python 3.x
- Boto3 installed (`pip install boto3`)
"""

import boto3

# Create an EC2 client
ec2 = boto3.client("ec2", region_name="ap-south-1")

# Launch EC2 instance
response = ec2.run_instances(
    ImageId="ami-0f58b397bc5c1f2e8",  # Replace with a valid AMI ID for your region
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=1,
    KeyName="your-key-pair-name",
    SecurityGroupIds=[
        "sg-xxxxxxxxxxxxxxxxx"
    ],
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "Python-EC2-Instance"
                }
            ]
        }
    ]
)

instance_id = response["Instances"][0]["InstanceId"]

print(f"EC2 Instance launched successfully!")
print(f"Instance ID: {instance_id}")# TODO
