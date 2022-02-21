from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime
import base64

class MpesaC2BCredentials:
    consumer_key = 'Ez4umg995u17jWJ63XhnaBDZAJVfj2Mu'
    consumer_secret = 'TIogVGbMVdgVGAvn'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    r = requests.get(MpesaC2BCredentials.api_URL, auth=HTTPBasicAuth(MpesaC2BCredentials.consumer_key, MpesaC2BCredentials.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']


class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379"
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    data_to_encode = Business_short_code + passkey + lipa_time
    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')













