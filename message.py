from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Details for sending the message
to_number = '+1234567890'  # Replace with the recipient's phone number
from_number = '+0987654321'  # Your Twilio phone number
message_body = 'Check out this picture!'
media_url = 'https://example.com/picture.jpg'  # URL of the picture you want to send

# Send the message
message = client.messages.create(
    body=message_body,
    media_url=[media_url],
    from_=from_number,
    to=to_number
)

print("Message SID:", message.sid)
