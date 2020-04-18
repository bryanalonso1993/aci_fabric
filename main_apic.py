#!/usr/env/bin/python3.6.9
import requests
import json


class ApiRestAci(object):
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self.header = {'content-type': 'application/json'}
        self.url = "https://"+self.ip+"/api/node/"
        self.token = requests.post("https://"+self.ip+"/api/aaaLogin.json",data=json.dumps({
                "aaaUser": {
                    "attributes": {
                        "name": self.username,
                        "pwd": self.password
                    }
                }
            }), headers=self.header, verify=False).json()['imdata'][0]['aaaLogin']['attributes']['token']

    def get_data_aci(self, data_method):
        response_data = requests.get(self.url+data_method,
                                     cookies={'APIC-cookie': self.token},
                                     headers=self.header,
                                     verify=False)
        if response_data.status_code == 200:
            return response_data.json()['imdata']
        else:
            return "Bad Response ACI ... {} ... error ... {}".format(response_data.status_code, response_data.json())

    def post_data_aci(self, data_method):
        response_data = requests.post(self.url+data_method,
                                      cookies={'APIC-cookie': self.token},
                                      headers=self.header,
                                      verify=False
                                      )
        if response_data.status_code == 200:
            print("succesfull operation : {}, response server : {}".format(response_data.status_code,
                                                                           response_data.json()))
        else:
            return "Bad Operation ACI ...{}".format(response_data.status_code)

    def put_data_aci(self, data_method):
        response_data = requests.put(self.url+data_method,
                                     cookies={'APIC-cookie': self.token},
                                     headers=self.header,
                                     verify=False
                                     )
        if response_data.status_code == 200:
            print("succesfull operation : {}, response server : {}".format(response_data.status_code,
                                                                           response_data.json()))
        else:
            return "Bad Operation ACI ...{}".format(response_data.status_code)
    
    def delete_data_aci(self, data_method):
        response_data = requests.put(self.url+data_method,
                                     cookies={'APIC-cookie': self.token},
                                     headers=self.header,
                                     verify=False
                                     )
        if response_data.status_code == 200:
            print("succesfull operation : {}, response server : {}".format(response_data.status_code,
                                                                           response_data.json()))
        else:
            return "Bad Operation ACI ...{}".format(response_data.status_code)