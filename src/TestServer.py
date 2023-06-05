from opcua import Server 
import time

server = Server()

root = server.get_objects_node()
start = root.add_variable("ns=1;s=Start", "Start", False)
finish = root.add_variable("ns=2;s=Finish", "Finish", True)
server.start()
print("Servidor OPC UA iniciado")


while True:
    start.set_value(True)  
    finish.set_value(False)
    time.sleep(3) 
    start.set_value(False) 
    finish.set_value(True)
    time.sleep(3) 

