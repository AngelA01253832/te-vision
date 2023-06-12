import httpx
import asyncio
import json
import datetime

class AsyncFetcher:
    def __init__(self, url) -> None:
        self.url = url

    async def postRequest(self, data):
        try:
            async with httpx.AsyncClient() as client:
                print(json.dumps(data))
                response = await client.post(self.url, data=json.dumps(data))
                return response
        except Exception as error:
            print(error)
            return None

# urlPallet = 'http://localhost:3000/api/pallets'
# urlBoxes = 'http://localhost:3000/api/boxes'

# today = datetime.date.today()
# todayParse = today.strftime('%Y-%m-%dT%H:%M:%S.000Z')
# arrayBoxes = [
#   {
#     "item" : "1",        
#     "description" : "fsdafas", 
#     "vendor" : "Te",      
#     "vendorCode" : "te",  
#     "prodLine":"fdasf",    
#     "palletId":"clisg2d3d000bwcuomlgsg51d"    
#   },
#   {
#     "item" : "2",        
#     "description" : "fsdafas", 
#     "vendor" : "Te",      
#     "vendorCode" : "te",  
#     "prodLine":"fdasf",    
#     "palletId":"clisg2d3d000bwcuomlgsg51d"    
#   },
#   {
#     "item" : "3",        
#     "description" : "fsdafas", 
#     "vendor" : "Te",      
#     "vendorCode" : "te",  
#     "prodLine":"fdasf",    
#     "palletId":"clisg2d3d000bwcuomlgsg51d"    
#   }
# ]

# fetcherPallet = AsyncFetcher(urlPallet)
# fetcherBoxes = AsyncFetcher(urlBoxes)

# data = {
#   "date" : todayParse,
#   "status" : "completed",
#   "time" : 250,
#   "noStopEmergency" : 0,
#   "userId" : "clihuvji30000wc500smn5hfu"
# }

# response = asyncio.run(fetcherPallet.postRequest(data))
# palletId = response.json()['data']['pallet']['id']

# for box in arrayBoxes:
#     box["palletId"] = palletId
#     box = json.dumps(box)
    
# boxResponse = asyncio.run(fetcherBoxes.postRequest(arrayBoxes))
