from abc import ABC, abstractmethod

class ElectronicDevice(ABC):
    
    @abstractmethod
    def battery_life(self):
        pass

class Smartphone(ElectronicDevice):
    # Implement the battery_life method for the Smartphone class
    def battery_life(self):
        return "The smartphone has a battery life of 12 hours."

class Laptop(ElectronicDevice):
    # Implement the battery_life method for the Laptop class
    def battery_life(self):
        return "The laptop has a battery life of 8 hours."

class Smartwatch(ElectronicDevice):
    # Implement the battery_life method for the Smartwatch class
    def battery_life(self):
        return "The smartwatch has a battery life of 24 hours."

def display_battery_life(device):
    # Call the battery_life method of the given device object and print the returned string
    print(device.battery_life())

# Test your implementation
smartphone = Smartphone()
laptop = Laptop()
smartwatch = Smartwatch()

display_battery_life(smartphone)
display_battery_life(laptop)
display_battery_life(smartwatch)
