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
