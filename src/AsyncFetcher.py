#Dependencies import
import httpx
import asyncio
from decouple import config

#File import
from IBox import IBox


class AsyncFetcher:
    def __init__(self) -> None:
        self.urlApi : str = config('API_DEVELOPMENT') 
    async def request(self,data: IBox):
        try:
            async with httpx.AsyncClient() as client:
                r = await client.post(self.urlApi, data=data)
                print(r.text)
        except httpx.HTTPError as exc:
            print(f"HTTP Exception for {exc.request.url} - {exc}")
    def asyncRequest(self,data: IBox):
        asyncio.run(self.request(data))
