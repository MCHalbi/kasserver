import zeep
import json
from typing import List, Union, Dict
import lxml

Query = Dict[str, Union[str, Dict]]

class KasApiClient:
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

        return self.call_kas_api(request)

    def call_kas_api(self, request: Query):
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
