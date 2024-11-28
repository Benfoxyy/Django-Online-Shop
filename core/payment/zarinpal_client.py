import requests
import json
from django.conf import settings

class ZarinPalSandbox:

    request_url = 'https://sandbox.zarinpal.com/pg/v4/payment/request.json'
    verifivation_url = 'https://sandbox.zarinpal.com/pg/v4/payment/verify.json'
    payment_url = 'https://sandbox.zarinpal.com/pg/StartPay/'
    callback_url = 'http://redreseller.com/verify'

    def __init__(self,merchant_id = settings.MERCHANT_ID):
        self.merchant_id = merchant_id

    def payment_request(self,amount,description = 'درگاه پرداخت'):
        payload = {
        "merchant_id": self.merchant_id,
        "amount": int(amount),
        "callback_url": self.callback_url,
        "description": description,
        }
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.post(self.request_url, headers=headers, data=json.dumps(payload))

        return response.json()

    def payment_verification(self,amount,authority):
        payload = {
        "merchant_id": self.merchant_id,
        "amount": int(amount),
        "authority": authority,
        }
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.post(self.verifivation_url, headers=headers, data=json.dumps(payload))

        return response.json()
    
    def generate_payment_url(self,authority):
        return self.payment_url + authority
    

# if __name__ == '__main__':
#     zarinpal = ZarinPal(merchant_id="4ced0a1e-4ad8-4309-9668-3ea3ae8e7897")
#     amount = 10000
#     data = zarinpal.payment_request(amount)
#     print(data)
#     input('next???')
#     print(zarinpal.generate_payment_url(data['data']['authority']))
#     input('next???')
#     print(zarinpal.payment_verification(amount,data['data']['authority']))