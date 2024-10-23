import socket
import json

def calculate_cutoff(marks):
    if 'biology' in marks:
        # Agri stream formula: Biology, Physics, Chemistry, Mathematics all divided by 2
        return (int(marks['biology']) / 2) + (int(marks['chemistry']) / 2) + (int(marks['physics']) / 2) + (int(marks.get('math', 0)) / 2)
    else:
        # General stream formula: Math, Chemistry, Physics, each divided by 2
        cut=(int(marks['math'])  + (int(marks['chemistry']) + (int(marks['physics'])/2)))
        return cut

server_ip = '127.0.0.1'
server_port = 12345  # TCP port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_server:
    tcp_server.bind((server_ip, server_port))
    tcp_server.listen(1)
    print(f"TCP server listening on {server_ip}:{server_port}")
    
    while True:
        conn, addr = tcp_server.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024)
            if not data:
                break
            marks = json.loads(data.decode())
            cutoff = calculate_cutoff(marks)
            response = f'Cutoff is: {cutoff:.2f}'
            conn.sendall(response.encode())
            print(f"Sent response: {response}")
