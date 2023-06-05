from opcua import Client

class ClientOpc:
    def __init__(self):
        self.client = Client("opc.tcp://192.168.0.241:49320")
        self.state = False
        self.channel = 2
        self.channelName = "Channel1.Device1.Entradapy"
    def handleChange(self,node, isStarted, data):
        if isStarted == 0:
            self.state == False
        else:
            self.state = True

        if self.state: 
            print("Programa iniciado")
        else:
            print("Programa detenido")

    def runClient(self):
        try:
            self.client.connect()
            node = self.client.get_node(f"ns={self.channel};s={self.channelName}") 
            handler = node.subscribe_data_change(self.handleChange)

            input("Presiona Enter para salir...\n")

        finally:
            self.client.disconnect()

opcServer = ClientOpc()
opcServer.runClient() 