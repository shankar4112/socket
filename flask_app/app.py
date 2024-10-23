from flask import Flask, render_template, request
import socket
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        stream = request.form['stream']
        chemistry_mark = request.form['chemistry']
        physics_mark = request.form['physics']

        # Choose the subject based on the stream
        if stream == 'Agri':
            biology_mark = request.form['biology']
            response = send_data(biology=biology_mark, chemistry=chemistry_mark, physics=physics_mark, protocol=request.form['protocol'], stream=stream)
        else:
            math_mark = request.form['math']
            response = send_data(math=math_mark, chemistry=chemistry_mark, physics=physics_mark, protocol=request.form['protocol'], stream=stream)

        return render_template('index.html', response=response)

    return render_template('index.html', response='')

def send_data(math=None, biology=None, chemistry=None, physics=None, protocol=None, stream=None):
    data = {}
    if stream == 'Agri':
        data = {'biology': biology, 'chemistry': chemistry, 'physics': physics}
    else:
        data = {'math': math, 'chemistry': chemistry, 'physics': physics}

    server_ip = '127.0.0.1'
    if protocol == 'TCP':
        server_port = 12345
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((server_ip, server_port))
                s.sendall(json.dumps(data).encode())
                response = s.recv(1024).decode()
            return response
        except Exception as e:
            return f"Error: {e}"
    elif protocol == 'UDP':
        server_port = 12346
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.sendto(json.dumps(data).encode(), (server_ip, server_port))
                response, _ = s.recvfrom(1024)
            return response.decode()
        except Exception as e:
            return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
