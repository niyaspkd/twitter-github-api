import json
import requests
from oauthlib import oauth2
key='ol2PmNbIKEntIGSHcPooa2KXm'
secret='6QZwEnU8zjnmtk90OQrmWqNhCEExLdYhpGxcbM5pxWVBYxdEW0'
access='2806936872-WKzGa0CONWb1RNwtOYqjyvSFRQiKRhNOV0wWXG7'
asecret='jVV2SDHmbSCJ1o6Nm1uA6xCbOnsH2l0HcarK89r79Mg87'
consumer=oauth2.Consumer(key=key,secret=secret)
token=oauth2.Token(key=access,secret=asecret)
client=oauth2.Client(consumer,token)
timel="http://api.twitter.com/1.1/statuses/home_timeline.json"
response,data=client.request(timel)
tw=json.loads(data)
print tw

