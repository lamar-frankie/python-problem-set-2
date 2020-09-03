#install requests package
import requests

#Check to see if google search is up


response = requests.get('https://api.github.com')
#simple monitoring script
if response.status_code == 200:
    print("Google Lives")
    
else:
    print("uh oh...Better switch to Bing")
