# Cutoff Mark Calculator with TCP/UDP Protocols

## Overview

This project is an interactive **Cutoff Mark Calculator** for **Engineering** and **Agriculture** streams. Users can input their subject marks and choose a communication protocol (**TCP** or **UDP**) to send the data to the server for cutoff calculation.

The calculator dynamically adjusts between using **Math** (for Engineering) or **Biology** (for Agriculture) based on the selected stream.

## Features

- Choose between Engineering (Math) and Agriculture (Biology) streams.
- Support for two communication protocols: **TCP** and **UDP**.
- Dynamically show or hide input fields based on the selected stream.
- Simple client-server communication using Python sockets.
- Web interface built using **Flask**.

## Project Structure

This project is organized in a single-file format. The Python file `app.py` includes the Flask application and both TCP/UDP servers.

## Prerequisites

- Python 3.x
- Flask (Install using `pip install Flask`)
- Basic understanding of Python sockets and networking.

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shankar4112/socket_programming.git
   cd cutoff-calculator
# Cutoff Mark Calculator

This project calculates the cutoff marks for Engineering and Agriculture streams, allowing users to choose between TCP and UDP protocols for communication.

## Installation

### Dependencies

To get started, install the necessary dependencies:

```bash
pip install Flask
## Running the Servers

You need to run both the TCP and UDP servers. Open two separate terminal windows:

### Terminal 1: Run the TCP Server

```bash
python app.py tcp_server
python app.py udp_server

How to Use
Choose a Stream:

Engineering: Input Math, Physics, and Chemistry marks.
Agriculture: Input Biology, Physics, and Chemistry marks.
Choose a Protocol:

Select either TCP or UDP.
Enter Marks and Calculate:

Input the marks and click "Calculate" to get the cutoff result.
Example
Engineering Stream:
Math: 85
Physics: 90
Chemistry: 80
Protocol: TCP
Result: Cutoff is 62.5

Agriculture Stream:
Biology: 92
Physics: 85
Chemistry: 88
Protocol: UDP
Result: Cutoff is 66.25

Tech Stack
Backend: Flask, Python
Frontend: HTML, CSS
Servers: Python Sockets for TCP and UDP communication
Protocols: TCP and UDP


## Tech Stack

- **Backend**: Flask, Python
- **Frontend**: HTML, CSS
- **Servers**: Python Sockets for TCP and UDP communication
- **Protocols**: TCP and UDP
