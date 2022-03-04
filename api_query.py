import base64
from distutils.command.config import config
from operator import ge
import requests
import json
import configparser

setting_config = configparser.ConfigParser()
setting_config.read('common_setting.ini')

def get_auth_admin(setting_config):
    r = requests.post(setting_config['Admin_Setting']['url']+"v2/admin/sessions/login",data={"email": setting_config['Admin_Setting']['email'],"password":setting_config['Admin_Setting']['password']})
    response = r.json()
    token_string = "%s:" % setting_config['Admin_Setting']['email'] + response['data']['token']
    token_string_bytes = token_string.encode("UTF-8")
    auth_byte = base64.b64encode(token_string_bytes)
    auth_string = auth_byte.decode("UTF-8")
    authorization = "Basic " + auth_string
    return authorization

def get_auth(setting_config):
    r = requests.post(setting_config['Portal_Setting']['url']+"v2/agent/login",data={"email": setting_config['Portal_Setting']['email'],"password":setting_config['Portal_Setting']['password']})
    response = r.json()
    token_string = "%s:" % setting_config['Portal_Setting']['email'] + response['data']['token']
    token_string_bytes = token_string.encode("UTF-8")
    auth_byte = base64.b64encode(token_string_bytes)
    auth_string = auth_byte.decode("UTF-8")
    authorization = "Basic " + auth_string
    return authorization

def create_order(config):
    auth = get_auth_admin(setting_config)
    path = "v2/merchant/orders/single?include_transactions=true"
    payload = json.dumps({
    "id": "",
    "pickup_contact_person": config['condition']['pickup_contact_person'],
    "pickup_address_line_1": config['condition']['pickup_address_line_1'],
    "pickup_address_line_2": config['condition']['pickup_address_line_2'],
    "pickup_contact_phone": config['condition']['pickup_contact_phone'],
    "pickup_latitude": {
        "lat": config['condition']['pickupp_lat'],
        "lng": config['condition']['pickupp_lng']
    },
    "pickup_longitude": {
        "lat": config['condition']['pickupp_lat'],
        "lng": config['condition']['pickupp_lng']
    },
    "pickup_zip_code": "",
    "pickup_city": "",
    "dropoff_contact_person": config['condition']['dropoff_contact_person'],
    "dropoff_address_line_1": config['condition']['dropoff_address_line_1'],
    "dropoff_address_line_2": config['condition']['dropoff_address_line_2'],
    "dropoff_contact_phone": config['condition']['dropoff_contact_phone'],
    "dropoff_latitude": {
        "lat": config['condition']['dropoff_lat'],
        "lng": config['condition']['dropoff_lng']
    },
    "dropoff_longitude": {
        "lat": config['condition']['dropoff_lat'],
        "lng": config['condition']['dropoff_lng']
    },
    "dropoff_zip_code": "",
    "dropoff_city": "",
    "width": 1,
    "length": 1,
    "height": 1,
    "weight": 1,
    "item_name": "qwertyu",
    "is_fragile": False,
    "cash_on_delivery": False,
    "cash_on_delivery_amount": "0",
    "dropoff_notes": "",
    "client_reference_number": "",
    "pickup_sms": False,
    "reliable": False,
    "has_delivery_note": False,
    "origin": "portal",
    "single_or_bulk": "single",
    "enforce_validation": True,
    "outsource_partner": "",
    "outsource_id": "",
    "convenience_store_parcel_price": "",
    "service_type": config['condition']['service_type'],
    "service_time": 0,
    "service_offering_id": config['condition']['service_offering_id'],
    "duty_type": "",
    "promo_code": "",
    "items": [],
    "is_pickupp_care": False,
    "contacts": []
    })
    headers = {
    'Authorization': auth,
    'Content-Type': 'application/json'
    }
    r = requests.post(setting_config['Portal_Setting']['url']+path,headers=headers, data=payload)
    response = r.json()
    OrderID = response["data"]["trips"][0]['order_id']
    return OrderID

def deliveryAgent(OrderID):
    auth = get_auth_admin(setting_config)
    path = "v2/admin/agents/320/trips/%s/accept" % OrderID
    headers = {
    'Authorization': auth,
    'Content-Type': 'application/json'
    }
    r = requests.put(setting_config['Setting']['url']+path, headers=headers)
    response = r.json()
    print (response)
    trip_id = response["data"]["trips"][0]['id']
    return trip_id

def enroute(trip_id):
    auth = get_auth(setting_config)
    url = "https://gateway-uat.hk.pickupp.io/v2/agent/trips/%s/enroute" % trip_id
    headers = {
    'Authorization': auth,
    'Content-Type': 'application/json'
    }
    r = requests.put(url, headers=headers)
    response = r.json()
    return response    

def dropoff(trip_id):
    auth = get_auth(setting_config)
    url = "https://gateway-uat.hk.pickupp.io/v2/agent/trips/%s/dropoff" % trip_id
    headers = {
    'Authorization': auth,
    'Content-Type': 'application/json'
    }
    r = requests.put(url, headers=headers)
    response = r.json()
    return response   

def payrolls():
    auth = get_auth_admin(setting_config)
    url = "https://gateway-uat.hk.pickupp.io/v2/admin/payrolls/confirm"
    headers = {
    'Authorization': auth,
    'Content-Type': 'application/json'
    }
    r = requests.put(url, headers=headers)
    response = r.json()
    return response   
