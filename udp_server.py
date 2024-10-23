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
server_port = 12346  # UDP port

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_server:
    udp_server.bind((server_ip, server_port))
    print(f"UDP server listening on {server_ip}:{server_port}")
    
    while True:
        data, addr = udp_server.recvfrom(1024)
        print(f"Received data from {addr}")
        marks = json.loads(data.decode())
        cutoff = calculate_cutoff(marks)
        response = f'Cutoff is: {cutoff:.2f}'
        udp_server.sendto(response.encode(), addr)
        print(f"Sent response to {addr}: {response}")
