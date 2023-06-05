from opcua import Client
import asyncio

class OPCUASubscriber:
    def __init__(self, server_url):
        self.server_url = server_url
        self.client = None
        self.subscription = None

    async def connect(self):
        self.client = Client(self.server_url)
        await self.client.connect()

    async def disconnect(self):
        if self.client is not None:
            await self.client.disconnect()

    def data_changed_handler(self, node, data):
        print("Cambio de datos detectado en el nodo:", node, "Nuevo valor:", data)

    async def subscribe_to_node(self, node_id):
        if self.client is None:
            raise Exception("No se ha establecido la conexión con el servidor OPC UA.")

        self.subscription = await self.client.create_subscription(100, self.data_changed_handler)
        node = await self.client.get_node(node_id)
        handle = await self.subscription.subscribe_data_change(node)

    async def unsubscribe_from_node(self):
        if self.subscription is not None:
            await self.subscription.unsubscribe_all()
            
subscriber = OPCUASubscriber("opc.tcp://localhost:4840")

async def main():
    await subscriber.connect()
    await subscriber.subscribe_to_node("ns=1;s=Start")

    # Realizar otras operaciones mientras espera cambios de datos...

    await subscriber.unsubscribe_from_node()
    await subscriber.disconnect()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


# class Handler(object):
#     def changeNotification(self, node, val, data):
#         if val == True:
#             print("True")
#         else:
#             print("false")
            
# class Client:
#     def __init__(self) -> None:
#         self.client : Client = Client("opc.tcp://localhost:4840")
#         self.startNode : str = "ns=1,s=Start"
#         self.finishNode : str = "ns=2,s=Finish"
#     def main(self):
#         try:
#             self.client.connect()
#         except:
#             print("Connection error")
#         else:
#             start = client.get_node(self.startNode)
            
#             handler = Handler()
#             sub = client.create_subscription(500,handler)
#             handle = sub.subscribe_data_change(handler)

# client = Client("opc.tcp://localhost:4840")
# startNode  = "ns=1,s=Start"

# try:
#     client.connect()
# except:
#     print("Connection error")
# else:
#     start = client.get_node(startNode)
            
#     handler = Handler()
#     sub = client.create_subscription(500,handler)
#     handle = sub.subscribe_data_change(handler)
