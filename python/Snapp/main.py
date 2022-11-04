import requests
import json
##############
url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
number = input("Enter your number: ")
body = {"cellphone": str(number)}
r = requests.post(url, data=json.dumps(body), headers={
                  'content-type': 'application/json'})
##############
url_aut = "https://app.snapp.taxi/api/api-passenger-oauth/v2/auth"
token_usr = input("Enter your token: ")
body_auth = {
    "grant_type": "sms_v2",
    "client_id": "ios_sadjfhasd9871231hfso234",
    "client_secret": "23497shjlf982734-=1031nln",
    "cellphone": str(number),
    "token": str(token_usr),
    "referrer": "pwa",
    "device_id": "4725509f-536b-43c8-8ef3-088eada9b502",
    "secure_id": "4725509f-536b-43c8-8ef3-088eada9b502"
}

response_auth = requests.post(
    url_aut, data=json.dumps(body_auth), headers={'content-type': 'application/json'})
#######
url_profile = "https://app.snapp.taxi/api/api-base/v2/passenger/profile"
headers_with_token = {
    'content-type': 'application/json',
    'Authorization': 'Bearer '+response_auth.json()["access_token"]
}
print('Bearer '+response_auth.json()["access_token"])
payload={}
request_profile = requests.get(url_profile, headers=headers_with_token)
print(request_profile.request.headers)
print(request_profile.json())
