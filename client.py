import socket 
import concurrent.futures

target_host = "0.0.0.0"
target_port = 8888

def task(n):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, target_port))

    client.send("v cool".encode())

    resp = client.recv(4096)
    
    
    print(resp.decode())
    return resp.decode()



with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    results = executor.map(task, range(20))

for i in results:
    print(i)