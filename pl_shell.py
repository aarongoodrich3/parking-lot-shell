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

    @exception_decorator
    def do_park(self, s):
        slot = self.parking_lot.park(*s.split())
        if slot:
            print(f"Allocated slot number: {slot}")
        else:
            print("Sorry, parking lot is full")

    @exception_decorator
    def do_leave(self, s):
        if self.parking_lot.leave(s):
            print(f"Slot number {s} is free")
        else:
            print("That slot doesn't exist in this parking lot")
    
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