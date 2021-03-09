#import firebase_admin
#from firebase_admin import auth

#default_app = firebase_admin.initialize_app(cred)
#print(default_app.name)

#To find the token to your device, upon installating the companion_app to your device,
#check the debug console on android studio and look for "D/TAG: the token refreshed: ...". 
#The following string is your device token, take that and assign it to this file's registration_token variable.
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
#import firebase_messaging

if not firebase_admin._apps:
    cred = credentials.Certificate("<INSERT PATH TO SERVICE JSON>")
    firebase_admin.initialize_app(cred)

#default_app = firebase_admin.initialize_app()

# This registration token comes from the client FCM SDKs.
registration_token = '<INSERT REGISTRATION DEVICE TOKEN HERE>'

# See documentation on defining a message payload.
message = messaging.Message(
    notification=messaging.Notification(
        title='ALERT FROM NERF SENTRY',
        body='Your Nerf Sentry detected a possible intruder and was signaled to fire.'
    ),
    #data={
    #    'score': '850',
    #    'time': '2:45',
    #},
    token=registration_token,
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)

