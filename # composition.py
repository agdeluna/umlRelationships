# composition.py

class House:
    class _Room: # Inner class representing part of the house
        def __init__(self, room_type):
            self.room_type = room_type

    def __init__(self, address, room_type):
        self.address = address
        self.bedroom = self._Room(room_type) # Composition (Lifecycle is tied to House)

    def display_house(self):
        print(f"House at {self.address} contains a {self.bedroom.room_type}.")

if __name__ == "__main__":
    house = House("123 Main St", "Master Bedroom")
    house.display_house()
