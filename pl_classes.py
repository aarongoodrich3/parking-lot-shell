class ParkingLot:
    def __init__(self,number_of_spaces):
        self.parking_lot_spaces = {}
        for slot in range(1, int(number_of_spaces) + 1):
            self.parking_lot_spaces[slot] = None

    def park(self, registration_number, color):
        for slot in sorted(self.parking_lot_spaces.keys()):
            if self.parking_lot_spaces[slot] == None:
                self.parking_lot_spaces[slot] = Vehicle(registration_number.upper(), color.capitalize())
                return slot
        return None

    def leave(self, spot_number):
        if int(spot_number) in list(self.parking_lot_spaces.keys()): 
            self.parking_lot_spaces[int(spot_number)] = None
            return True
        else:
            return False

    def find_matches(self, s, vehicle_attr, search_for):
        matches = []
        for slot in sorted(self.parking_lot_spaces.keys()):
            if self.parking_lot_spaces[slot] == None:
                continue
            if getattr(self.parking_lot_spaces[slot], vehicle_attr) == s:
                if search_for == "slot":
                    matches.append(slot)
                elif search_for == "registration_number":
                    matches.append(self.parking_lot_spaces[slot].registration_number)
                elif search_for == "color":
                    matches.append(self.parking_lot_spaces[slot].color)
        return matches

class Vehicle:
    def __init__(self,registration_number,color):
        self.registration_number = registration_number
        self.color = color