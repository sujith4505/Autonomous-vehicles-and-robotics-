
def fuse_sensor_data(camera_data, lidar_data):
    # Dummy fusion logic: combine confidence scores
    fused_data = []
    for c_obj, l_obj in zip(camera_data, lidar_data):
        fused_score = (c_obj['confidence'] + l_obj['confidence']) / 2
        fused_data.append({'object': c_obj['object'], 'fused_confidence': fused_score})
    return fused_data

# Example input data
camera_data = [{'object': 'car', 'confidence': 0.85}]
lidar_data = [{'object': 'car', 'confidence': 0.80}]

fused = fuse_sensor_data(camera_data, lidar_data)
print("Fused Sensor Data:", fused)
