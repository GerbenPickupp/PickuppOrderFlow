import base64
import requests
import json
import configparser

setting_config = configparser.ConfigParser()
setting_config.read('common_setting.ini')

def get_auth_portal(setting_config):
    r = requests.post(setting_config['Portal_Setting']['url']+"v2/merchant/sessions/login",data={"email": setting_config['Portal_Setting']['email'],"password":setting_config['Portal_Setting']['password']})
    response = r.json()
    token_string = "%s:" % setting_config['Portal_Setting']['email'] + response['data']['token']
    token_string_bytes = token_string.encode("UTF-8")
    auth_byte = base64.b64encode(token_string_bytes)
    auth_string = auth_byte.decode("UTF-8")
    authorization = "Basic " + auth_string
    if r.status_code == 201:
        return authorization, True
    else: 
        return authorization, False

def get_auth_admin(setting_config):
    r = requests.post(setting_config['Admin_Setting']['url']+"v2/admin/sessions/login",data={"email": setting_config['Admin_Setting']['email'],"password":setting_config['Admin_Setting']['password']})
    response = r.json()
    token_string = "%s:" % setting_config['Admin_Setting']['email'] + response['data']['token']
    token_string_bytes = token_string.encode("UTF-8")
    auth_byte = base64.b64encode(token_string_bytes)
    auth_string = auth_byte.decode("UTF-8")
    authorization = "Basic " + auth_string
    if r.status_code == 201:
        return authorization, True
    else: 
        return authorization, False

def get_auth(setting_config):
    r = requests.post(setting_config['DA_Setting']['url']+"v2/agent/login",data={"email": setting_config['DA_Setting']['email'],"password":setting_config['DA_Setting']['password']})
    response = r.json()
    token_string = "%s:" % setting_config['DA_Setting']['email'] + response['data']['token']
    token_string_bytes = token_string.encode("UTF-8")
    auth_byte = base64.b64encode(token_string_bytes)
    auth_string = auth_byte.decode("UTF-8")
    authorization = "Basic " + auth_string
    if r.status_code == 201:
        return authorization, True
    else: 
        return authorization, False

def create_order(config,type,status):
    conditionchoose = "condition_" + type
    auth, auth_status = get_auth_portal(setting_config)
    path = "v2/merchant/orders/single?include_transactions=true"
    payload = json.dumps({
        "id": "",
        "pickup_contact_person": config[conditionchoose]['pickup_contact_person'],
        "pickup_address_line_1": config[conditionchoose]['pickup_address_line_1'],
        "pickup_address_line_2": config[conditionchoose]['pickup_address_line_2'],
        "pickup_contact_phone": config[conditionchoose]['pickup_contact_phone'],
        "pickup_latitude": {
            "lat": config[conditionchoose]['pickupp_lat'],
            "lng": config[conditionchoose]['pickupp_lng']
        },
        "pickup_longitude": {
            "lat": config[conditionchoose]['pickupp_lat'],
            "lng": config[conditionchoose]['pickupp_lng']
        },
        "pickup_zip_code": "",
        "pickup_city": "",
        "dropoff_contact_person": config[conditionchoose]['dropoff_contact_person'],
        "dropoff_address_line_1": config[conditionchoose]['dropoff_address_line_1'],
        "dropoff_address_line_2": config[conditionchoose]['dropoff_address_line_2'],
        "dropoff_contact_phone": config[conditionchoose]['dropoff_contact_phone'],
        "dropoff_latitude": {
            "lat": config[conditionchoose]['dropoff_lat'],
            "lng": config[conditionchoose]['dropoff_lng']
        },
        "dropoff_longitude": {
            "lat": config[conditionchoose]['dropoff_lat'],
            "lng": config[conditionchoose]['dropoff_lng']
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
        "service_type": config[conditionchoose]['service_type'],
        "service_time": 0,
        "service_offering_id": config[conditionchoose]['service_offering_id'],
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
    if r.status_code == 201:
        OrderID = response["data"]["trips"][0]['order_id']
        return r.status_code, OrderID, True
    else:
        return r.status_code, response, False

def AssignToDeliveryAgent(OrderID, status):
    auth, auth_status = get_auth_admin(setting_config)
    path = "v2/admin/agents/%s/trips/%s/accept" % (setting_config['DA_Setting']['OrderNumber'],OrderID)
    headers = {
        'Authorization': auth,
        'Content-Type': 'application/json'
    }
    r = requests.put(setting_config['DA_Setting']['url']+path, headers=headers)
    response = r.json()
    if r.status_code == 200:    
        trip_id = response["data"]["trips"][0]['id']
        return r.status_code, trip_id, True
    else:
        return r.status_code, response, False

def enroute(trip_id, status):
    auth, auth_status= get_auth(setting_config)
    path = "v2/agent/trips/%s/enroute" % trip_id
    headers = {
        'Authorization': auth,
        'Content-Type': 'application/json'
    }
    r = requests.put(setting_config['DA_Setting']['url']+path, headers=headers)
    response = r.json()
    if r.status_code == 200:
        return r.status_code, response, True
    else:   
        return r.status_code, response, False
def dropoff_process(trip_id, status):
    auth, auth_status = get_auth(setting_config)
    path = "v2/agent/trips/%s/dropoff_process" % trip_id
    headers = {
    'Authorization': auth,
    'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "geolocation":False,
        "qr_or_passcode":False,
        "dropoff_photo":False,
        "contactless_or_unattended":True,
        "signature_photo":False,
        "cash_on_delivery":False,
        "delivery_note":False,
        "recipient_verify_code":False
    })
    r = requests.post(setting_config['DA_Setting']['url']+path, headers=headers,data=payload)
    response = r.json()
    if r.status_code == 200:
        return r.status_code, response, True
    else:   
        return r.status_code, response, False

def dropoff(trip_id, status):
    auth, auth_status = get_auth(setting_config)
    path = "v2/agent/trips/%s/dropoff" % trip_id
    headers = {
    'Authorization': auth,
    'Content-Type': 'application/json'
    }
    r = requests.put(setting_config['DA_Setting']['url']+path, headers=headers)
    response = r.json()
    if r.status_code == 200:
        return r.status_code, response, True
    else:   
        return r.status_code, response, False

def payrolls(status):
    auth, auth_status = get_auth_admin(setting_config)
    path = "v2/admin/payrolls/confirm"
    headers = {
    'Authorization': auth,
    'Content-Type': 'application/json'
    }
    r = requests.put(setting_config['Admin_Setting']['url']+path, headers=headers)
    response = r.json()
    if r.status_code == 200:
        return r.status_code, response, True
    else:   
        return r.status_code, response, False

def search_order():
    auth, auth_status = get_auth(setting_config)
    print (auth)
    path = "v2/agent/trips/new/all"
    headers = {
    'Authorization': auth,
    'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "pickup_districts_l2":"",
        "dropoff_districts_l2":"",
        "max_dimension":"",
        "min_dimension":"",
        "max_weight":"",
        "min_weight":"",
        "project_tag_id":"",
        "service_types":"",
        "city":"",
        "group":"",
        "is_warehouse":"",
        "is_bundle":"",
        "pickup_order_types":"",
        "dropoff_order_types":""
    })
    r = requests.get(setting_config['DA_Setting']['url']+path, headers=headers,data=payload)
    response = r.json()
    return r.status_code, response 

