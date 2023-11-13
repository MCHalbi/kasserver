import zeep
from kasserver import KasAuth, KasApiQuery


class KasApiClient:
    def __init__(self, kas_login: str, kas_password: str):
        self._client = zeep.Client("./KasApi.wsdl")
        self._auth = KasAuth(kas_login, kas_password, "plain")

    def get_mailforwards(self, mail_forward=None):
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
