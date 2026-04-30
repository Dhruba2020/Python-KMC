class Device:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = "off"

    def turn_on(self):
        if self.status == "on":
            print(f"Device {self.device_id} is already ON")
        else:
            self.status = "on"
            print(f"Device {self.device_id} turned ON")

    def turn_off(self):
        if self.status == "off":
            print(f"Device {self.device_id} is already OFF")
        else:
            self.status = "off"
            print(f"Device {self.device_id} turned OFF")

class SmartDevice(Device):
    def __init__(self, device_id, connectivity):
        super().__init__(device_id)
        self.connectivity = connectivity
        self.connected = False

    def connect(self):
        if self.connected:
            print(f"{self.device_id} already connected via {self.connectivity}")
        else:
            self.connected = True
            print(f"{self.device_id} connected using {self.connectivity}")


class SmartThermostat(SmartDevice):
    def __init__(self, device_id, connectivity, temperature=20, mode="cool"):
        super().__init__(device_id, connectivity)
        self.temperature = temperature
        self.mode = mode

    def set_temperature(self, temp):

            if temp < 10 or temp > 40:
                raise ValueError("Temperature must be between 10 and 40")

            self.temperature = temp
            print(f"Temperature set to {self.temperature}")




obj = SmartThermostat ()
obj.set_temperature (20)
object.display ()

















            
