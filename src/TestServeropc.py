from opcua import Server 
import time

server = Server()

def handle_node_change(node, value, data):
    if node == isBoxReadedNode:
        print("Change in isBoxReadedNode!")
        print(f"Nuevo valor: {value}")

root = server.get_objects_node()

# Start node
startNode = root.add_variable("ns=1;s=Start", "Start", False)

# Finish node
finishNode = root.add_variable("ns=2;s=Finish", "Finish", False)

# isBoxReaded node
isBoxReadedNode = root.add_variable("ns=3;s=ReadNode", "ReadNode", False)
isBoxReadedNode.set_writable()

# isBoxReadedNode.subscribe_data_change(handle_node_change)

server.start()
print("Servidor OPC UA iniciado")

while True:
    print("Inicie")
    time.sleep(10)
    print(f"E1 - start: {startNode.get_value()}, finish: {finishNode.get_value()}")
    startNode.set_value(True)
    finishNode.set_value(False)
    print(f"E2 - start: {startNode.get_value()}, finish: {finishNode.get_value()}")
    time.sleep(5)
    startNode.set_value(False)
    finishNode.set_value(True)
    print(f"E3 - start: {startNode.get_value()}, finish: {finishNode.get_value()}")
    time.sleep(5)
