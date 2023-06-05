from opcua import Client
import asyncio

client = Client("opc.tcp://localhost:4840")

class DataChangeHandler(object):
    def datachange_notification(self, node, val, data):
        print(f"Cambio de datos detectado en el nodo:{node}")
        print(f"New value:{val}")

try:
    client.connect()
    print("Connection OPC-UA established successfully")
    handler = DataChangeHandler()
    subscription = client.create_subscription(500, handler)
    start = client.get_node("ns=1;s=Start")
    finish = client.get_node("ns=2;s=Finish")
    handleStart = subscription.subscribe_data_change(start)
    handleFinish = subscription.subscribe_data_change(finish)

    input("Press Enter to stop the client...")

finally:
    subscription.unsubscribe(handleStart)
    subscription.unsubscribe(handleFinish)
    client.disconnect()
    
    print("Connection OPC-UA disconnected successfully")