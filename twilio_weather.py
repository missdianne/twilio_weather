import json
import requests
import sys
import urllib

from twilio.rest import TwilioRestClient

print "Starting twilio_weather.py"

try:
    u = "http://api.openweathermap.org/data/2.5/weather?id=5380748&APPID=b508c75277d46d54e2029f51cf3b17c8"
    r = requests.get(u)
    j = json.loads(r.text)
except:
    sys.stderr.write("Couldn't load current conditions\n")

temperature = j['main']['temp']

conditions = j['weather'][0]['description']

text_message_body = conditions[0].lower()+conditions[1:]


# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "AC9f2d249ff39b2bd8eefd3bac0b6d7fb7"
AUTH_TOKEN = "7da95cf2670be3ed3ac555f87af236b4"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    body="Good morning! Today's weather is "+text_message_body+" with a chance of meatballs!", 
    to="+14089660143",
    from_="+15623747477",
)

print message.sid
