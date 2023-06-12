#Dependencies import
from opcua import Server 
import time

server = Server()
def handle_node_change(node, value, data):
    if node == isBoxReadedNode:
        print("Change in isBoxReadedNode!")
        print(f"Nuevo valor:{value}")
root = server.get_objects_node()

#Start node
startNode = root.add_variable("ns=1;s=Start", "Start", False)
#Finish node
finishNode = root.add_variable("ns=2;s=Finish", "Finish", False)
#isBoxReaded node
isBoxReadedNode = root.add_variable("ns=3;s=ReadNode", "ReadNode", False)
isBoxReadedNode.set_writable()

#getBoxesNode
getBoxesNode = root.add_variable("ns=4;s=getBoxesNode", "getBoxesNode", False)
server.start()
print("Servidor OPC UA iniciado")

try:
    while True:
        startNode.set_value(False)
        finishNode.set_value(False)
        getBoxesNode.set_value(False)
        print("Start server")
        time.sleep(15)
        print(f"Init states - start: {startNode.get_value()}, finish: {finishNode.get_value()}, boxes: {getBoxesNode.get_value()}, StatusBox: {isBoxReadedNode.get_value()}")
        startNode.set_value(True)
        finishNode.set_value(False)
        print(f"On vision system - start: {startNode.get_value()}, finish: {finishNode.get_value()}, boxes: {getBoxesNode.get_value()}, StatusBox: {isBoxReadedNode.get_value()}")
        time.sleep(30)
        print('api init')
        startNode.set_value(False)
        getBoxesNode.set_value(True)
        print('api finish')
        print(f"E3 - start: {startNode.get_value()}, finish: {finishNode.get_value()}, boxes: {getBoxesNode.get_value()}, StatusBox: {isBoxReadedNode.get_value()}")
        time.sleep(10)
        startNode.set_value(False)
        finishNode.set_value(True)
        print(f"E4 - start: {startNode.get_value()}, finish: {finishNode.get_value()}, boxes: {getBoxesNode.get_value()}, StatusBox: {isBoxReadedNode.get_value()}")
        time.sleep(5)

finally:
    server.stop()
    print("Servidor OPC UA detenido")
