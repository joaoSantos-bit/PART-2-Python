import unittest
from license_plates_validator import validate
import json
import os

class TestLicensePlateValidator(unittest.TestCase):
    
    def setUp(self):

        """Set up test environment by creating mock configuration files."""
        self.json_file_standard = 'brasil.cnf'
        with open(self.json_file_standard, 'w') as file:
            json.dump({"length": 6, "letters": 3, "numbers": 3}, file)
        
        self.json_file_no_numbers = 'brasil_no_numbers.cnf'
        with open(self.json_file_no_numbers, 'w') as file:
            json.dump({"length": 6, "letters": 3}, file)
        
        self.json_file_no_letters = 'brasil_no_letters.cnf'
        with open(self.json_file_no_letters, 'w') as file:
            json.dump({"length": 6, "numbers": 3}, file)

    def tearDown(self):

        """Clean up after tests by removing mock configuration files."""
        os.remove(self.json_file_standard)
        os.remove(self.json_file_no_numbers)
        os.remove(self.json_file_no_letters)

    def test_valid_license_plate(self):

        """Test case where the license plate matches the standard constraints."""
        self.assertTrue(validate(self.json_file_standard, 'ABC123'))
    
    def test_invalid_length(self):

        """Test case where the license plate length doesn't match the constraint."""
        self.assertFalse(validate(self.json_file_standard, 'AB1234'))
        self.assertFalse(validate(self.json_file_standard, 'ABCD1234'))
    
    def test_invalid_letters(self):

        """Test case where the license plate has incorrect number of letters."""
        self.assertFalse(validate(self.json_file_standard, 'A1C123'))
        self.assertFalse(validate(self.json_file_standard, 'AB1234'))
    
    def test_invalid_numbers(self):

        """Test case where the license plate has incorrect number of numbers."""
        self.assertFalse(validate(self.json_file_standard, 'ABCDE1'))
        self.assertFalse(validate(self.json_file_standard, 'ABC12'))
    
    def test_valid_with_no_numbers_constraint(self):

        """Test case where the JSON config does not specify a 'numbers' constraint."""
        self.assertTrue(validate(self.json_file_no_numbers, 'ABC123'))
        self.assertFalse(validate(self.json_file_no_numbers, 'ABC'))
    
    def test_valid_with_no_letters_constraint(self):

        """Test case where the JSON config does not specify a 'letters' constraint."""
        self.assertTrue(validate(self.json_file_no_letters, 'ABC123'))
        self.assertFalse(validate(self.json_file_no_letters, '123456'))
    
    def test_invalid_with_partial_constraints(self):
        
        """Test case where license plate violates remaining constraints even with missing attributes."""
        self.assertFalse(validate(self.json_file_no_letters, 'ABCDE1'))
        self.assertFalse(validate(self.json_file_no_letters, 'ABCD12'))

if __name__ == '__main__':
    unittest.main()
