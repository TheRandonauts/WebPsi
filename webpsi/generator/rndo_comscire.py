from webpsi.generator.base import Generator
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class Randonautica_QRNG(Generator, id='rndo', bit_numbering=Generator.BitNumbering.UNKNOWN):
    def get_bytes(self, length):
        url = os.environ.get("RNDO_URL")
        token = os.environ.get("RNDO_API_KEY")
        session = requests.Session()
        session.headers.update({'Authorization': f'Bearer {token}'})
        try:
            response = session.get(f'{url}?length={length}')
            print(response)
            response.raise_for_status()
            json = response.json()
            print(json['result']['entropy'])
            return bytes.fromhex(json['result']['entropy'])
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)
