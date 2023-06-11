import httpx
import asyncio

class AsyncFetcher:
    def __init__(self, url) -> None:
        self.url = url

    async def postRequest(self, data):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(self.url, data=data)
                return response
        except Exception as error:
            print(error)
            return None

url = 'https://reqres.in/api/users'

fetcher = AsyncFetcher(url)
data = {
    "name": "morpheus",
    "job": "leader"
}
response = asyncio.run(fetcher.postRequest(data))
print(response.json())
