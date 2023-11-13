from typing import Dict, Any
from dataclasses import dataclass
from kasserver import KasAuth
import json


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
