from opcua import Client

class ClientOpc:
    def __init__(self) -> None:
        self.client = Client()
    
#Create OPC client instance
    def runServer(self):
        self.client.connect()
        node = self.client.get_node("")
        startVision = node.get_value()


client.disconnect()
