import zeep
import json
from typing import List, Union, Dict, Any
import lxml
from dataclasses import dataclass

@dataclass(frozen=True)
class KasAuth:
    login: str
    passphrase: str
    type: str

    def __iter__(self) -> dict:
        return iter(
            [
                ("kas_login", self.login),
                ("kas_auth_type", self.type),
                ("kas_auth_data", self.passphrase),
            ]
        )

@dataclass(frozen=True)
class KasApiQuery:
    auth: KasAuth
    action: str
    params: Dict[str, Any]

    def json(self):
        query_dict = dict(self.auth) | {"KasRequestType": self.action}

        filtered_params = {
            key: value for key, value in self.params.items() if value is not None
        }

        if filtered_params:
            query_dict["KasRequestParams"] = filtered_params

        return json.dumps(query_dict)

class KasApiClient:
    def __init__(self, kas_login: str, kas_password: str):
        self._client = zeep.Client("./KasApi.wsdl")
        self._auth = KasAuth(kas_login, kas_password, "plain")

    def get_mailforwards(self, mail_forward = None):
        action = "get_mailforwards"

        query = self.create_query(
            action=action,
            mail_forward=mail_forward
        )

        return self.call_kas_api(query)

    def call_kas_api(self, query: KasApiQuery):
        return self._client.service.KasApi(query.json())

    def create_query(self, action: str, **params) -> KasApiQuery:
        return KasApiQuery(self._auth, action, params)

class KasApiResponse:
    def __init__(self, request_time, request_type, request_parameters):
        self._request_time: int = request_time
