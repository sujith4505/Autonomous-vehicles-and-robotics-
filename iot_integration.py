# iot_integration.py

import serial
import time
import random
import requests
import threading

# ---------- Serial Communication with Arduino ----------
def read_from_arduino(port='COM3', baud_rate=9600):
    try:
        ser = serial.Serial(port, baud_rate)
        time.sleep(2)  # Wait for connection to establish
        print("Connected to Arduino.")

        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').rstrip()
                print(f"Received from Arduino: {data}")
    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except KeyboardInterrupt:
        print("Stopped reading from Arduino.")

# ---------- Simulated Sensor Data ----------
def get_fake_environmental_data():
    return {
        "temperature": round(random.uniform(15, 35), 2),
        "humidity": round(random.uniform(30, 70), 2),
        "location": "HomeLab",
        "sensorStatus": "OK"
    }

# ---------- Send Data to Server ----------
def send_data_to_server(url):
    sensor_data = get_fake_environmental_data()
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=sensor_data, headers=headers)
        if response.status_code == 200:
            print("Data sent successfully!")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

# ---------- Main ----------
if __name__ == "__main__":
    # Start Arduino reading in a separate thread
    arduino_thread = threading.Thread(target=read_from_arduino, args=('COM3', 9600))
    arduino_thread.daemon = True
    arduino_thread.start()

    # Replace with your actual endpoint
    server_url = "http://your-server-ip-or-domain/api/data"

    # Periodically send data
    try:
        while True:
            send_data_to_server(server_url)
            time.sleep(10)  # Send every 10 seconds
    except KeyboardInterrupt:
        print("Program terminated.")
