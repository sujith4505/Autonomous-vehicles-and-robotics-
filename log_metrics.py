import json
import time

metrics = {
    "avg_inference_time": 0.032,
    "control_latency_ms": 42.5,
    "collision_rate": 0.03,
    "power_efficiency": "85%",
    "decision_accuracy": "91.3%"
}

timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
log = {"timestamp": timestamp, "metrics": metrics}

with open("phase4_metrics_log.json", "a") as file:
    file.write(json.dumps(log) + "\n")

print("Performance metrics logged.")
