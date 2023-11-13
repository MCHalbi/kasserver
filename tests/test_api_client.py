# pylint: disable=missing-docstring
import unittest
from dotenv import load_dotenv
import os
from kasserver import KasApiClient


class KasApiClientTests(unittest.TestCase):
    def test_api_client(self):
        load_dotenv()
        client = KasApiClient(os.getenv('KAS_API_LOGIN'), os.getenv("KAS_API_PASSPHRASE"))
        raw_response = client.get_mailforwards()
        print(raw_response)
