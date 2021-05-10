import requests

from firebase import firebase

class Service():
    DATABASE = 'https://enviame-77595-default-rtdb.firebaseio.com/'
    SERVICE_ENVIAME = 'https://stage.api.enviame.io/api/s2/v2/companies/401/deliveries'
    FINDER = '/enviame/db_post'
    __firebase = None
    
    def __init__(self):
        self.__firebase = firebase.FirebaseApplication(self.DATABASE, None)
        authentication = firebase.FirebaseAuthentication('62P2zxKABaLze21VCmAJzZxtex2tYmBbBsSVF02m', 
                                                         'edwinalbertovelasco8@gmail.com', 
                                                         extra={'id': 123})
        self.__firebase.authentication = authentication

    def registed_data(self, data):
        res_envia = requests.post(url=self.SERVICE_ENVIAME, json=data,
                                  headers={
                                        'api-key': 'ea670047974b650bbcba5dd759baf1ed',
                                        'Content-Type': 'application/json',
                                        'Accept': 'application/json'
                                  })
        res_json = res_envia.json()
        res = self.__firebase.post(self.FINDER, res_json)
        
        return res

    def get_data_firebase(self):
        res = self.__firebase.get(self.FINDER, '')
        return res


DATA_ENVIAME = {"shipping_order": {
                    "n_packages": "1",
                    "content_description": "ORDEN 255826267",
                    "imported_id": "255826267",
                    "order_price": "24509.0",
                    "weight": "0.98",
                    "volume": "1.0",
                    "type": "delivery"
                },
                "shipping_origin": {
                    "warehouse_code": "401"
                },
                "shipping_destination": {
                    "customer": {
                        "name": "Bernardita Tapia Riquelme",
                        "email": "b.tapia@outlook.com",
                        "phone": "977623070"
                    },
                    "delivery_address": {
                        "home_address": {
                            "place": "Puente Alto",
                            "full_address": "SAN HUGO 01324, Puente Alto, Puente Alto"
                        }
                    }
                },
                "carrier": {
                    "carrier_code": "blx",
                    "tracking_number": ""
                }
                }
service = Service()
res = service.registed_data(data=DATA_ENVIAME)
print(res.get('name'), 'Nuevo envío guardado en Firebase')
print('', )

list_shipping = service.get_data_firebase()

print('--- listado de registros ---')
print('', )

for shipping in list(list_shipping):
    data = list_shipping.get(shipping, dict()).get('data', dict())
    print('carrier', data.get('carrier'))
    print('tracking_number', data.get('tracking_number'))
    print('identifier', data.get('identifier'))
    print('imported_id', data.get('imported_id'))
    print('',)

