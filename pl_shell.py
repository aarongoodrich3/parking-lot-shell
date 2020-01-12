import cmd, sys
from decorators import exception_decorator
from pl_classes import ParkingLot, Vehicle

class ParkingLotShell(cmd.Cmd):
    intro = "Welcome to the Parking Lot Shell. For detailed information on available commands, type 'help' into the prompt.\n"\
            "For more information on a specific command type 'help [command]'\n"\
            "ex: help park"
    prompt = "(PL_Shell) "
    parking_lot = None

    def emptyline(self):
        """ Overrides empty line function in parent class.
            When return key is pressed on an empty line, the prompt will simply break to a new line. """
        pass

    @exception_decorator
    def do_create_parking_lot(self, s):
        self.parking_lot = ParkingLot(s)
        print(f"Created a parking lot with {s} slots")

    def help_create_parking_lot(self):
        print("Creates a ParkingLot object. Expects a single integer as an argument which represents\n"\
              "the number of parking slots the parking lot can accomodate\n"\
              "ex: create_parking_lot 6")

    @exception_decorator
    def do_park(self, s):
        slot = self.parking_lot.park(*s.split())
        if slot:
            print(f"Allocated slot number: {slot}")
        else:
            print("Sorry, parking lot is full")

    def help_park(self):
        print("Creates a Vehicle object and adds it to the nearest available parking slot in the lot\n"\
              "Expects 2 arguments: The vehicle registration number and the vehicle color, listed in order\n"\
              "ex: park KA-01-HH-9999 White")

    @exception_decorator
    def do_leave(self, s):
        if self.parking_lot.leave(s):
            print(f"Slot number {s} is free")
        else:
            print("That slot doesn't exist in this parking lot")

    def help_leave(self):
        print("If a vehicle is in a parking slot, this command empties it.\n"
              "Expects 1 argument: a single integer representing the parking slot\n"\
              "ex: leave 4")
    
    @exception_decorator
    def do_status(self, s):
        try:
            if FILE_OUTPUT:
                status_delimiter = "    "
            else:
                status_delimiter = "\n"
        except NameError:
            status_delimiter = "\n"
        print(f"Slot No.{status_delimiter}Registration No{status_delimiter}Colour")
        for slot in sorted(self.parking_lot.parking_lot_spaces.keys()):
            if self.parking_lot.parking_lot_spaces[slot]:
                print(f"{slot}{status_delimiter}{self.parking_lot.parking_lot_spaces[slot].registration_number}"\
                      f"{status_delimiter}{self.parking_lot.parking_lot_spaces[slot].color}")

    def help_status(self):
        print("Prints vehicle information on all occupied parking slots\n"\
              "Expects no arguments\n"
              "ex: status")

    @exception_decorator
    def do_registration_numbers_for_cars_with_colour(self, s):
        matches = self.parking_lot.find_matches(s.strip().capitalize() , "color", "registration_number")
        print_match_results(matches)

    def help_registration_numbers_for_cars_with_colour(self):
        print("Prints all vehicle registration numbers associated with a vehicle color\n"
              "Expects one argument: the vehicle color\n"
              "ex: help_registration_numbers_for_cars_with_colour White")

    @exception_decorator
    def do_slot_numbers_for_cars_with_colour(self, s):
        matches = self.parking_lot.find_matches(s.capitalize() , "color", "slot")
        print_match_results(matches)

    def help_slot_numbers_for_cars_with_colour(self):
        print("Prints all parking lot slots associated with a vehicle color\n"
              "Expects one argument: the vehicle color\n"
              "ex: lot_numbers_for_cars_with_colour White")

    @exception_decorator
    def do_slot_number_for_registration_number(self, s):
        matches = self.parking_lot.find_matches(s.upper(), "registration_number", "slot")
        print_match_results(matches)

    def help_slot_number_for_registration_number(self):
        print("Prints parking lot slot associated with a vehicle registration number\n"
              "Expects one argument: the vehicle registration number\n"
              "ex: slot_number_for_registration_number KA-01-HH-3141")

def print_match_results(matches):
    if matches:
        print(*matches,sep=", ")
    else:
        print("Not found")

if __name__ == '__main__':
    pl_shell = ParkingLotShell()
    if len(sys.argv) == 1:
        FILE_OUTPUT = False
        pl_shell.cmdloop()
    else:
        FILE_OUTPUT = True
        with open(sys.argv[1], 'r') as pl_file:
            for line in pl_file:
                pl_shell.onecmd(line)