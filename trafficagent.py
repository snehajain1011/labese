import time
import random

class TrafficSensorAgent:
    def __init__(self):
        self.traffic_level = 'low'

    def detect_traffic(self):
        # Simulate traffic detection: randomly set to high or low
        self.traffic_level = random.choice(['high', 'low'])
        return self.traffic_level

class TrafficLightController:
    def __init__(self):
        self.current_light = 'red'
        self.light_states = ['red', 'yellow', 'green']
        self.state_index = 0

    def get_current_light(self):
        return self.current_light

    def change_light(self, traffic_level):
        if traffic_level == 'high':
            # If traffic is high, keep green if possible, or change to green
            if self.current_light == 'green':
                pass  # Stay green
            else:
                self.current_light = 'green'
        elif traffic_level == 'low':
            # If traffic is  toolow, cycle to next state
            self.state_index = (self.state_index + 1) % len(self.light_states)
            self.current_light = self.light_states[self.state_index]

def main():
    sensor = TrafficSensorAgent()
    controller = TrafficLightController()

    print("Traffic Light Controller Simulation")
    print("Current Light: Red")

    for _ in range(10):  # Simulate 10 cycles
        traffic = sensor.detect_traffic()
        print(f"Traffic detected: {traffic}")
        controller.change_light(traffic)
        print(f"Current Light: {controller.get_current_light()}")
        time.sleep(1)  # Wait 1 second for simulation
       
if __name__ == "__main__":
    main()
print(f"which light")
