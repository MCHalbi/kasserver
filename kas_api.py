import zeep
import json
from typing import List, Union, Dict
import lxml

Query = Dict[str, Union[str, Dict]]

class KasApi:
    def __init__(self, kas_login: str, kas_password: str):
        self._client = zeep.Client("./KasApi.wsdl")
        self._kas_login = kas_login
        self._kas_password = kas_password

    def get_mailforwards(self, mail_forward = None):
        action = "get_mailforwards"

        request = self.create_query(
            action=action,
            mail_forward=mail_forward
        )

        response = self.call_api(request)
        result = self.convert_response(response)

        return result

    def convert_response(self, response):
        request = self.convert_request(response)
        print(request)

        return response

    def convert_request(self, response):
        converter = Converter()
        result = converter.convert(response[0])

        return result


    def call_api(self, request: Query):
        return self._client.service.KasApi(json.dumps(request))

    def create_query(self, action: str, **params) -> Query:
        request = {
            "kas_login": self._kas_login,
            "kas_auth_type": "plain",
            "kas_auth_data": self._kas_password,
            "KasRequestType": action,
        }

        filtered_params = {
            key: value for key, value in params.items() if value is not None
        }

        if filtered_params:
            request["KasRequestParams"] = filtered_params

        return request

class Converter:
    def convert(self, input_object):
        print(f"{input_object=}")
        print(f"{type(input_object)=}, {'key' in input_object=}, {len(input_object) == 2=}")
        if (
            len(input_object) == 2
            and "key" in input_object
            and "value" in input_object):
            return {input_object["key"]: self.convert(input_object["value"])}

        return input_object
