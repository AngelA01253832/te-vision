from opcua import Client
from time import sleep
from CodeLector import Reader
import threading

client = Client("opc.tcp://localhost:4840")

class DataChangeHandler(object):
    def __init__(self):
        self.startNode: bool = False
        self.finishNode: bool = False
        self.isBoxReaded: bool = False
        self.reader = Reader(self.visionCallback)
        self.reader_thread = None

    def datachange_notification(self, node, val, data):
        print(f"Change state value in node: {node}")
        print(f"New value: {val}")
        # Update state
        if node == self.startNode:
            self.startNode = val
            self.startProcess()

        elif node == self.finishNode:
            self.finishNode = val
            self.finishProcess()

    def startProcess(self):
        if self.startNode:
            if self.reader_thread is None or not self.reader_thread.is_alive():
                self.reader_thread = threading.Thread(target=self.reader.realTime)
                self.reader_thread.start()
        else:
            print("Start value: False")

    def finishProcess(self):
        if self.finishNode:
            if self.reader_thread is not None and self.reader_thread.is_alive():
                self.reader.stop()
                self.reader_thread.join()
        else:
            print("Finish value: False")

    def visionCallback(self, content):
        print(f"QR detected, Content: {content}")
        # Send 1
        readNode.set_value(1)
        sleep(1)  # Esperar 1 segundo
        # Send 0
        readNode.set_value(0)

try:
    client.connect()
    print("Connection to OPC-UA server established successfully")

    # Create subscription object
    handler = DataChangeHandler()
    subscription = client.create_subscription(500, handler)

    # Get start node
    startNode = client.get_node("ns=1;s=Start")
    handler.startNode = startNode.nodeid
    handleStart = subscription.subscribe_data_change(startNode)

    # Get read node
    readNode = client.get_node("ns=3;s=ReadNode")

    # Get finish node
    finishNode = client.get_node("ns=2;s=Finish")
    handler.finishNode = finishNode.nodeid
    handleFinish = subscription.subscribe_data_change(finishNode)

    input("Press Enter to stop the client...")

finally:
    subscription.unsubscribe(handleStart)
    subscription.unsubscribe(handleFinish)
    client.disconnect()

    print("Connection to OPC-UA server disconnected successfully")
