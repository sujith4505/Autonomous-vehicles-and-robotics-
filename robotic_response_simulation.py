
import time
import random

def simulate_robotic_response():
    command = random.choice(['MOVE_FORWARD', 'STOP', 'TURN_LEFT'])
    start = time.perf_counter()
    
    # Simulate actuator processing delay
    time.sleep(random.uniform(0.01, 0.05))
    
    end = time.perf_counter()
    return command, round((end - start) * 1000, 2)

# Run 5 control tests
for _ in range(5):
    cmd, latency = simulate_robotic_response()
    print(f"Command: {cmd}, Latency: {latency} ms")
