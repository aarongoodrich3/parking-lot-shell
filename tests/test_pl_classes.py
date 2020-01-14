import unittest
from pl_classes import ParkingLot, Vehicle

class TestParkingLotMethods(unittest.TestCase):
    '''Test ParkingLot and Vehicle classes'''

    def test_create_parking_lot_with_expected_number_of_slots(self):
        '''Ensure parking_lot_size dict is created with proper keys when ParkingLot obejct created'''
        parking_lot_size = 6
        parking_lot = ParkingLot(parking_lot_size)
        self.assertEqual(len(parking_lot.parking_lot_spaces), parking_lot_size)
        self.assertIsNone(parking_lot.parking_lot_spaces[1])
        self.assertIsNone(parking_lot.parking_lot_spaces[parking_lot_size])
        self.assertRaises(KeyError, lambda: parking_lot.parking_lot_spaces[0])
        self.assertRaises(KeyError, lambda: parking_lot.parking_lot_spaces[parking_lot_size+1])

    def test_park_returns_slot_key_if_slot_is_empty_and_none_if_all_slots_taken(self):
        '''Ensure park function fills slots in proper order and None is slots are full'''
        parking_lot_size = 2
        parking_lot = ParkingLot(parking_lot_size)
        park_return_variable = parking_lot.park("ka-01-hh-1234" , "white")
        self.assertEqual(park_return_variable, 1)
        park_return_variable = parking_lot.park("ka-01-hh-1234" , "white")
        self.assertEqual(park_return_variable, 2)
        park_return_variable = parking_lot.park("ka-01-hh-1234" , "white")
        self.assertIsNone(park_return_variable)

    def test_park_creates_vehicle_with_correct_variable_formatting(self):
        '''Ensures registration numbers are always uppercase and colors are always capialized'''
        parking_lot_size = 1
        parking_lot = ParkingLot(parking_lot_size)
        parking_lot.park("ka-01-hh-1234", "white")
        self.assertEqual(parking_lot.parking_lot_spaces[1].registration_number, "KA-01-HH-1234")
        self.assertEqual(parking_lot.parking_lot_spaces[1].color, "White")

    def test_leave_returns_true_if_slot_exists_and_false_otherwise(self):
        '''Ensures 'leave' only works if called on an actual parking slot'''
        parking_lot_size = 2
        parking_lot = ParkingLot(parking_lot_size)
        self.assertTrue(parking_lot.leave(1))
        self.assertTrue(parking_lot.leave(2))
        self.assertFalse(parking_lot.leave(0))
        self.assertFalse(parking_lot.leave(3))

    def test_leave_converts_strings_to_integer(self):
        '''Ensures 'leave' will convert properly formatted string to an integer'''
        parking_lot_size = 2
        parking_lot = ParkingLot(parking_lot_size)
        self.assertTrue(parking_lot.leave("1"))

    def test_find_matches_returns_list_of_correct_vehicle_attributes_or_parking_slots(self):
        '''Ensures vehicle attribute searches return the correct information'''
        parking_lot_size = 6
        parking_lot = ParkingLot(parking_lot_size)
        for x in range(6):
            parking_lot.park("AK-01-HH-1234", "White")
        self.assertEqual(parking_lot.find_matches("AK-01-HH-1234","registration_number","slot"),[1,2,3,4,5,6])
        self.assertEqual(parking_lot.find_matches("White","color","slot"),[1,2,3,4,5,6])
        self.assertEqual(parking_lot.find_matches("whit","color","slot"),[])
        self.assertEqual(parking_lot.find_matches("White","color","registration_number"),["AK-01-HH-1234"]*6)


if __name__ == '__main__':
    unittest.main()