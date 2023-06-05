#File import
from CodeLector import Reader
from AsyncFetcher import AsyncFetcher
from opcua import Client

#Create barcode reader instance
reader = Reader()
#Create barcode reader instance
fetcher = AsyncFetcher()
#Create OPC client instance
client = Client()

#OPC client
client.connect()
node = client.get_node("")
startVision = node.get_value()


client.disconnect()
#Init reader
reader.realTime()

#Get pallet summary
palletSummary = reader.getBoxes()

#Web post request
if len(palletSummary) != 0:
    fetcher.asyncRequest(palletSummary)
else:
    print("Fetching data error")
    