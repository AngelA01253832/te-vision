from opcua import Client
from time import sleep
from CodeLector import Reader
import threading
import asyncio

client = Client("opc.tcp://localhost:4840")

class DataChangeHandler(object):
    def __init__(self):
        self.startNode : bool = False
        self.finishNode : bool = False
        self.isBoxReaded : bool = False
        self.reader = Reader()
        self.counter : int = 0
        self.reader_thread = None

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
        

    def startProcess(self):
        if self.startNode == True:
            self.reader_thread = threading.Thread(target=self.reader.realTime)
            self.reader_thread.start()

        else:
            print("Start value: False")

    def finishProcess(self):
        if self.finishNode == True:
            if self.reader_thread is not None and self.reader_thread.is_alive():
                self.reader.stop()
                self.reader_thread.join()
        
            # self.reader_thread = threading.Thread(target=self.reader.stop)
            # self.reader_thread.stop()
            # self.reader_thread.join()
            #self.reader.stop()
        else:
            print("Finish value: False")

def visionCallback(content):
    print(f"QR detected, Content:{content}")
    #Send 1
    readNode.set_value(1)
    sleep(1)  # Esperar 1 segundo
    # Send 0

try:
    client.connect()
    print("Connection OPC-UA established successfully")
    #Create subscription object
    handler = DataChangeHandler()
    subscription = client.create_subscription(500, handler)
    #Start node
    startNode = client.get_node("ns=1;s=Start")
    handleStart = subscription.subscribe_data_change(startNode)

    readNode = client.get_node("ns=3;s=ReadNode") 
    
    #Finish node
    finishNode = client.get_node("ns=2;s=Finish")
    handleFinish = subscription.subscribe_data_change(finishNode)

    input("Press Enter to stop the client...")

finally:
    subscription.unsubscribe(handleStart)
    subscription.unsubscribe(handleFinish)
    client.disconnect()
    
    print("Connection OPC-UA disconnected successfully")