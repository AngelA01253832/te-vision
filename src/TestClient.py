from array import array
import json
from opcua import Client
from time import sleep
from CodeLector import Reader
import threading
from decouple import config
import datetime
from Fetcher import AsyncFetcher

import asyncio
config
client = Client(config('OPC_ENDPOINT'))
FetcherPallet = AsyncFetcher(config('WEB_API_PALLET'))
FetcherBoxes = AsyncFetcher(config('WEB_API_BOXES'))

class DataChangeHandler(object):

    def __init__(self, Callback):
        self.startNode : bool = False
        self.finishNode : bool = False
        self.isBoxReaded : bool = False
        self.reader = Reader(Callback)
        self.counter : int = 0
        self.readerThread = None

    def datachange_notification(self, node, val, data):
        print(f"Change state value in node:{node}")
        print(f"New value:{val}")
        # Update state
        if node == startNode:
            self.startNode = val
            self.startProcess()

        elif node == finishNode:
            self.finishNode = val
            self.finishProcess()

        elif node == getBoxesNode:
            self.getBoxesNode = val
            self.getBoxes()
        

    def startProcess(self):
        if self.startNode:
            if self.readerThread is None or not self.readerThread.is_alive():
                self.readerThread = threading.Thread(target=self.reader.realTime)
                self.readerThread.start()

        else:
            print("Start value: False")

    def getBoxes(self):
        if self.getBoxesNode:
            arrayBoxes = self.reader.getContentList()
            today = datetime.date.today()
            todayParse = today.strftime('%Y-%m-%dT%H:%M:%S.000Z')
 
            payload = {
                "date" : todayParse,
                "status" : "completed",
                "time" : 120,
                "noStopEmergency" : 0,
                "userId" : "clihuvji30000wc500smn5hfu"
            }
            
            palletResponse = asyncio.run(FetcherPallet.postRequest(payload))
            palletId = palletResponse.json()['data']['pallet']['id']
            
            if palletId:
                for box in arrayBoxes:
                    vendorCodeParse = str(box["vendorCode"])
                    box["palletId"] = palletId
                    box["vendorCode"] = vendorCodeParse
                boxResponse = asyncio.run(FetcherBoxes.postRequest(arrayBoxes))
            
                print(boxResponse.json())

        else:
            pass
    def finishProcess(self):
        if self.finishNode == True:
            if self.readerThread is not None and self.readerThread.is_alive():
                self.reader.stop()
                self.readerThread.join()
        else:
            print("Finish value: False")

def Callback(content):
    print(f"QR detected, Content:{content}")
    isBoxReadedNode.set_value(True)
    sleep(1)
    isBoxReadedNode.set_value(False)

try:
    client.connect()
    print("Connection OPC-UA established successfully")
    #Create subscription object
    handler = DataChangeHandler(Callback)
    subscription = client.create_subscription(500, handler)
    #Start node
    startNode = client.get_node("ns=1;s=Start")
    handleStart = subscription.subscribe_data_change(startNode)

    #get boxes node
    getBoxesNode = client.get_node("ns=4;s=getBoxesNode")
    handleBoxes = subscription.subscribe_data_change(getBoxesNode)

    isBoxReadedNode = client.get_node("ns=3;s=ReadNode") 
    
    #Finish node
    finishNode = client.get_node("ns=2;s=Finish")
    handleFinish = subscription.subscribe_data_change(finishNode)

    input("Press Enter to stop the client...")

finally:
    subscription.unsubscribe(handleStart)
    subscription.unsubscribe(handleBoxes)
    subscription.unsubscribe(handleStart)
    client.disconnect()
    
    print("Connection OPC-UA disconnected successfully")