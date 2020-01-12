import unittest, io
from contextlib import redirect_stdout
from pl_shell import ParkingLotShell, print_match_results

ERROR_MSG_1 = "g with vehicles"  # These are the endings of the messages created in decorators.py 
ERROR_MSG_2 = "on this command"

class TestShellMethods(unittest.TestCase):

    def test_do_create_parking_lot(self):
        pls = ParkingLotShell()
        print_out = get_print_results(pls.onecmd, "create_parking_lot 6")
        self.assertEqual(print_out,"Created a parking lot with 6 slots")

    def test_do_create_parking_lot_errors(self):
        pls = ParkingLotShell()
        print_out = get_print_results(pls.onecmd, "create_parking_lot sdfsdf")
        self.assertEqual(print_out[-15:], ERROR_MSG_2)
        print_out = get_print_results(pls.onecmd, "create_parking_lot")
        self.assertEqual(print_out[-15:], ERROR_MSG_2)
        print_out = get_print_results(pls.onecmd, "create_parking_lot 6 6 6")
        self.assertEqual(print_out[-15:], ERROR_MSG_2)

    def test_do_park(self):
        pls = ParkingLotShell()
        pls.onecmd("create_parking_lot 1")
        print_out = get_print_results(pls.onecmd, "park AK-01-HH-1234 White")
        self.assertEqual(print_out, "Allocated slot number: 1")
        print_out = get_print_results(pls.onecmd, "park AK-01-HH-1234 White")
        self.assertEqual(print_out, "Sorry, parking lot is full")

    def test_do_park_errors(self):
        pls = ParkingLotShell()
        print_out = get_print_results(pls.onecmd, "park AK-01-HH-1234 White")
        self.assertEqual(print_out[-15:], ERROR_MSG_1)
        pls.onecmd("create_parking_lot 1")
        print_out = get_print_results(pls.onecmd, "park")
        self.assertEqual(print_out[-15:], ERROR_MSG_2)
        print_out = get_print_results(pls.onecmd, "park AK-01-HH-1234 White White")
        self.assertEqual(print_out[-15:], ERROR_MSG_2)

    def test_do_leave(self):
        pls = ParkingLotShell()
        pls.onecmd("create_parking_lot 1")
        print_out = get_print_results(pls.onecmd, "leave 1")
        self.assertEqual(print_out[4:], "Slot number 1 is free")
        print_out = get_print_results(pls.onecmd, "leave 2")
        self.assertEqual(print_out[4:], "That slot doesn't exist in this parking lot")
        print_out = get_print_results(pls.onecmd, "leave 0")
        self.assertEqual(print_out[4:], "That slot doesn't exist in this parking lot")

    def test_do_leave_errors(self):
        pls = ParkingLotShell()
        print_out = get_print_results(pls.onecmd, "leave 1")
        self.assertEqual(print_out[-15:], ERROR_MSG_1)
        pls.onecmd("create_parking_lot 1")
        print_out = get_print_results(pls.onecmd, "leave")
        self.assertEqual(print_out[-15:], ERROR_MSG_2)
        print_out = get_print_results(pls.onecmd, "leave fgh")
        self.assertEqual(print_out[-15:], ERROR_MSG_2)
        print_out = get_print_results(pls.onecmd, "leave 6 6")
        self.assertEqual(print_out[-15:], ERROR_MSG_2)

    def test_do_status(self):
        pls = ParkingLotShell()
        pls.onecmd("create_parking_lot 1")
        pls.onecmd("park AK-01-HH-1234 White")
        print_out = get_print_results(pls.onecmd, "status")
        expected_results = "Slot No.\nRegistration No\nColour\n1\nAK-01-HH-1234\nWhite"
        self.assertEqual(print_out, expected_results)

    def test_do_registration_numbers_for_cars_with_colour(self):
        pls = ParkingLotShell()
        pls.onecmd("create_parking_lot 2")
        pls.onecmd("park AK-01-HH-1234 White")
        print_out = get_print_results(pls.onecmd, "registration_numbers_for_cars_with_colour White")
        self.assertEqual(print_out, "AK-01-HH-1234")
        pls.onecmd("park AK-01-HH-1234 White")
        print_out = get_print_results(pls.onecmd, "registration_numbers_for_cars_with_colour White")
        self.assertEqual(print_out, "AK-01-HH-1234, AK-01-HH-1234")
        print_out = get_print_results(pls.onecmd, "registration_numbers_for_cars_with_colour Blackish")
        self.assertEqual(print_out, "Not found")

    def test_do_registration_numbers_for_cars_with_colour_errors(self):
        pls = ParkingLotShell()
        print_out = get_print_results(pls.onecmd, "registration_numbers_for_cars_with_colour White")
        self.assertEqual(print_out[-15:], ERROR_MSG_1)

    def test_do_slot_numbers_for_cars_with_colour(self):
        pls = ParkingLotShell()
        pls.onecmd("create_parking_lot 2")
        pls.onecmd("park AK-01-HH-1234 White")
        print_out = get_print_results(pls.onecmd, "slot_numbers_for_cars_with_colour White")
        self.assertEqual(print_out, "1")
        pls.onecmd("park AK-01-HH-1234 White")
        print_out = get_print_results(pls.onecmd, "slot_numbers_for_cars_with_colour White")
        self.assertEqual(print_out, "1, 2")
        print_out = get_print_results(pls.onecmd, "slot_numbers_for_cars_with_colour Blackish")
        self.assertEqual(print_out, "Not found")

    def test_do_slot_numbers_for_cars_with_colour_errors(self):
        pls = ParkingLotShell()
        print_out = get_print_results(pls.onecmd, "slot_numbers_for_cars_with_colour White")
        self.assertEqual(print_out[-15:], ERROR_MSG_1)

    def test_do_slot_number_for_registration_number(self):
        pls = ParkingLotShell()
        pls.onecmd("create_parking_lot 2")
        pls.onecmd("park AK-01-HH-1234 White")
        print_out = get_print_results(pls.onecmd, "slot_number_for_registration_number AK-01-HH-1234")
        self.assertEqual(print_out, "1")
        pls.onecmd("park AK-01-HH-1234 White")
        print_out = get_print_results(pls.onecmd, "slot_number_for_registration_number AK-01-HH-1234")
        self.assertEqual(print_out, "1, 2")
        print_out = get_print_results(pls.onecmd, "slot_number_for_registration_number AK-01-HH-12345")
        self.assertEqual(print_out, "Not found")

    def test_do_slot_number_for_registration_number_errors(self):
        pls = ParkingLotShell()
        print_out = get_print_results(pls.onecmd, "slot_number_for_registration_number White")
        self.assertEqual(print_out[-15:], ERROR_MSG_1)

    def test_print_match_results(self):
        self.assertEqual(get_print_results(print_match_results,[]),"Not found")
        self.assertEqual(get_print_results(print_match_results,["1","2","3"]),"1, 2, 3")

def get_print_results(f,*args,**kwargs):
    out = io.StringIO()
    with redirect_stdout(out):
        f(*args,**kwargs)
    return out.getvalue()[:-1]

if __name__ == '__main__':
    unittest.main()