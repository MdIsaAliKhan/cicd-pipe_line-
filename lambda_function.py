import boto3

sns = boto3.client('sns')

# 🔴 Replace this with your real SNS ARN
TOPIC_ARN = "arn:aws:sns:us-east-1:694630903450:smart-quote-topic"

def lambda_handler(event, context):

    # Get details safely
    detail = event.get("detail", {})
    pipeline_name = detail.get("pipeline", "Unknown Pipeline")
    state = detail.get("state", "Unknown State")

    # Decide message
    if state == "STARTED":
        message = f"🚀 Pipeline {pipeline_name} has STARTED."

    elif state == "SUCCEEDED":
        message = f"✅ Pipeline {pipeline_name} completed SUCCESSFULLY."

    elif state == "FAILED":
        message = f"❌ Pipeline {pipeline_name} has FAILED."

    else:
        message = f"ℹ️ Pipeline {pipeline_name} status: {state}"

    # Send SNS message
    sns.publish(
        TopicArn=TOPIC_ARN,
        Message=message
    )

    return {
        "statusCode": 200,
        "body": "Notification Sent"
    }