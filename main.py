import base64
import sendgrid
import os
from sendgrid.helpers.mail import *
import json

def handle_email_message(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    
    # Convert the raw message string into a dict
    message_dict = json.loads("[" + pubsub_message + "]")[0]

    # Set the API Key so we can null check it
    API_KEY = os.environ.get('SENDGRID_API_KEY')

    if (API_KEY != None):
        sg = sendgrid.SendGridAPIClient(api_key=API_KEY)
        from_email = Email(message_dict["from"])
        to_email = To(message_dict["to"])
        subject = message_dict["subject"]
        content = Content("text/plain", message_dict["text"])
        mail = Mail(from_email, to_email, subject, content)
        sg.client.mail.send.post(request_body=mail.get())
        return 200
    else:
        return 500