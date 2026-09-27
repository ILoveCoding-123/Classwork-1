from abc import ABC, abstractmethod

# 1. Create an abstract base class for a Smart Device
class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name

    # Define an abstract method that every subclass must implement
    @abstractmethod
    def execute_command(self):
        pass

    # A common method shared by all devices
    def get_status(self):
        return f"{self.name} is connected to the Command Center."


# 2. Inherit and override the abstract method for a Smart Light
class SmartLight(SmartDevice):
    def execute_command(self):
        return f"💡 {self.name}: Setting brightness to 80% and turning on warm white light."


# 3. Inherit and override the abstract method for a Smart Thermostat
class SmartThermostat(SmartDevice):
    def execute_command(self):
        return f"🌡️ {self.name}: Adjusting temperature to 72°F (22°C)."


# 4. Inherit and override the abstract method for a Smart Speaker
class SmartSpeaker(SmartDevice):
    def execute_command(self):
        return f"🔊 {self.name}: Streaming your favorite morning playlist at volume 5."


# === Main Execution demonstrating Polymorphism ===
if __name__ == "__main__":
    print("--- Initializing Smart Device Command Center ---\n")

    # Create a list containing different types of smart devices
    devices = [
        SmartLight("Living Room Light"),
        SmartThermostat("Main Hallway Thermostat"),
        SmartSpeaker("Kitchen Speaker")
    ]

    # Demonstrate Polymorphism: Loop through any device and call the same method name
    for device in devices:
        print(device.get_status())
        print(device.execute_command())
        print("-" * 50)