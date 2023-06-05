import requests
from IBox import IBox
from decouple import config

class Fetcher:
    def __init__(self) -> None:
        self.urlApi : str = config('API_DEVELOPMENT') 
    def post(self,data : IBox) -> str:
        try:
            r = requests.post(self.urlApi, json = data)
            return r.text
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
                

