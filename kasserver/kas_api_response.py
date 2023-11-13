from dataclasses import dataclass
from typing import Dict, Any
import zeep


@dataclass
class KasApiRequest:
    time: int
    type: str
    parameters: Dict[str, Any]

    @staticmethod
    def from_raw_response(raw_response: List):
        pass

    def convert(raw_response: List):
        native_python_response = zeep.helpers.serialize_object(raw_response, dict)
        return recursive_convert(native_python_response)

    def recursive_convert(response_node):
        if (native_python_response)

