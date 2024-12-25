import serial
import threading
import time
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Config port
SERIAL_PORT = 'COM12'  # Attention: May be different port, so check it
BAUD_RATE = 115200
# a function
# Data which recieved from port
data = []

# start Flask and Socket
app = Flask(__name__)
socketio = SocketIO(app)

# get data from port


def read_from_serial():
    global data
    try:
        # connect  to port
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
        print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud.")
        while True:
            line = ser.readline().decode('utf-8').strip()
            print(f"Received data: {line}")

            if "Heart rate:" in line and "SpO2:" in line:
                parts = line.split("/")
                heart_rate = parts[0].split(":")[1].strip().replace("bpm", "")
                spo2 = parts[1].split(":")[1].strip().replace("%", "")

                # Add data to list
                data.append({"Heart Rate": heart_rate, "SpO2": spo2})

                # send data to client
                socketio.emit(
                    'new_data', {"Heart Rate": heart_rate, "SpO2": spo2})

            time.sleep(1)

    except serial.SerialException as e:
        print(f"Serial error: {e}")


# read data from port on another thread
serial_thread = threading.Thread(target=read_from_serial, daemon=True)
serial_thread.start()

# HTML view


@app.route('/')
def index():
    return render_template('index.html')


# Run Flask and Websocket servers
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000)
