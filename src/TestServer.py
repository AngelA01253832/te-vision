from opcua import Server 

server = Server()
root = server.get_objects_node()

start = root.add_variable("ns=1;s=start","Start",False)
finish = root.add_variable("ns=2;s=finish","Finish",False)

server.start()