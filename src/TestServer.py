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

#isBoxReadedNode.subscribe_data_change(handle_node_change)

server.start()
print("Servidor OPC UA iniciado")

try:
    while True:
        startNode.set_value(False)
        finishNode.set_value(False)
        getBoxesNode.set_value(False)
        print("Start server")
        time.sleep(10)
        print(f"Init states - start: {startNode.get_value()}, finish: {finishNode.get_value()}, boxes: {getBoxesNode.get_value()}")
        startNode.set_value(True)
        finishNode.set_value(False)
        print(f"On vision system - start: {startNode.get_value()}, finish: {finishNode.get_value()}, boxes: {getBoxesNode.get_value()}")
        time.sleep(20)
        print('api')
        startNode.set_value(False)
        getBoxesNode.set_value(True)
        print(f"E3 - start: {startNode.get_value()}, finish: {finishNode.get_value()}, boxes: {getBoxesNode.get_value()}")
        time.sleep(10)
        startNode.set_value(False)
        finishNode.set_value(True)
        print(f"E4 - start: {startNode.get_value()}, finish: {finishNode.get_value()}, boxes: {getBoxesNode.get_value()}")
        time.sleep(5)

finally:
    server.stop()
    print("Servidor OPC UA detenido")
    
# while True:
#     #print(isBoxReadedNode.get_value())
#     print("Start server")
#     time.sleep(10)
#     print(f"Init states - start: {startNode.get_value()}, finish: {finishNode.get_value()} , boxes: {getBoxesNode.get_value()}")
#     startNode.set_value(True)  
#     finishNode.set_value(False)  
#     print(f"On vision system - start: {startNode.get_value()}, finish: {finishNode.get_value()}, boxes: {getBoxesNode.get_value()}")
#     time.sleep(60) 
#     print('api')
#     startNode.set_value(False)
#     getBoxesNode.set_value(True)
#     print(f"E3 - start{startNode.get_value()}, finish{finishNode.get_value()}, boxes: {getBoxesNode.get_value()}")
#     time.sleep(20) 
#     startNode.set_value(False)
#     finishNode.set_value(True)
    # print("Inicie")
    # time.sleep(10)
    # print(f"E1 - start{startNode.get_value()}, finish{finishNode.get_value()}")
    # startNode.set_value(True)  
    # finishNode.set_value(False)  
    # print(f"E2 - start{startNode.get_value()}, finish{finishNode.get_value()}")
    # time.sleep(10) 
    # startNode.set_value(False)
    # finishNode.set_value(True)
    # print(f"E3 - start{startNode.get_value()}, finish{finishNode.get_value()}")
    # time.sleep(5) 
    # startNode.set_value(False)
    # finishNode.set_value(False)
