"""
The Facade design pattern provides a simplified interface to a complex subsystem. It acts as a high-level interface that makes the subsystem easier to use by hiding its complexities. 
Here's an explanation of the Facade pattern and a simple Python example:
## Facade Design Pattern ##
The Facade pattern:
- Provides a unified interface to a set of interfaces in a subsystem
- Defines a higher-level interface that makes the subsystem easier to use
- Wraps a complicated subsystem with a simpler interface
Key benefits:
- Simplifies the usage of complex systems
- Decouples the client from the subsystem's components
- Promotes loose coupling between subsystems

Python Example
Here's a simple Python example demonstrating the Facade pattern:
"""


# Complex subsystem classes
class CPU:
    def freeze(self):
        print("CPU: Freezing...")

    def jump(self, address):
        print(f"CPU: Jumping to address {address}")

    def execute(self):
        print("CPU: Executing...")


class Memory:
    def load(self, address, data):
        print(f"Memory: Loading data {data} at address {address}")


class HardDrive:
    def read(self, sector, size):
        print(f"HardDrive: Reading sector {sector} with size {size}")

# Facade


class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load(0, "boot data")
        self.cpu.jump(0)
        self.cpu.execute()


if __name__ == "__main__":
    # Client code
    computer = ComputerFacade()
    computer.start()

"""
In this example:
1. We have complex subsystem classes (CPU, Memory, HardDrive) with their specific operations.
2. The ComputerFacade class provides a simplified interface to start the computer. It encapsulates the complexity of working with the subsystem components.
3. The client code only needs to interact with the ComputerFacade, without knowing the details of the subsystem.
"""
