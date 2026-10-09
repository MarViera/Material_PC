import base64

message = "Los estudiantes de LSTI van a aprobar PC"
message_bytes = message.encode('ascii') #bytes
print(message_bytes)
base64_bytes = base64.b64encode(message_bytes) #objeto base64
print(base64_bytes) #bytes
base64_message = base64_bytes.decode('ascii') #str

print(type(base64_message),"-->",base64_message) 
