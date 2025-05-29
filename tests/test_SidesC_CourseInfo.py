# Cayleigh Sides
# This program tests the SidesC_CourseInfo.py program
# Tests to ensure input is cleaned of invalid characters
# Checks if information is displayed correctly or that error message is shown

import unittest
from SidesC_CourseInfo import remove_extra, info

import io
import sys

class TestCourseInfo(unittest.TestCase):

    def test_remove_extra_removes_punctuation(self):
        
        # Tests that remove_extra strips all non-alphanumeric characters from input
        self.assertEqual(remove_extra("CS101!@#"), "CS101")
        self.assertEqual(remove_extra("NT110..."), "NT110")
        self.assertEqual(remove_extra("CM241-?"), "CM241")
        self.assertEqual(remove_extra("CS102"), "CS102")    # valid input unchanged
        self.assertEqual(remove_extra("abc123"), "abc123")  # letters and digits stay

    # Tests the captured printed output and verifies correct formatting 
    def test_info_valid_course_prints_boxed_info(self):
        
        # Setup dictionaries with one course entry 
        room = {'CS101':'3004'}
        instructor = {'CS101':'Haynes'}
        time = {'CS101':'8:00 AM'}

        # Create StringIO object to capture output
        captured_output = io.StringIO()

        # Redirect stdout
        sys.stdout = captured_output

        # Call the function with a valid course
        info("CS101", room, instructor, time)

        # Reset redirect
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        # Check expected strings in output
        self.assertIn("Course: CS101", output)
        self.assertIn("Room Number: 3004", output)
        self.assertIn("Instructor: Haynes", output)
        self.assertIn("Meeting Time: 8:00 AM", output)
        self.assertIn("+------------------------+", output)  # Check box border present

    # Tests error message with invalid course input
    def test_info_invalid_course_prints_error(self):

        # Setup dictionaries with invalid course entry 
        room = {}
        instructor = {}
        time = {}

        # Create StringIO object to capture output
        captured_output = io.StringIO()

        # Redirect stdout
        sys.stdout = captured_output

        # Call the function with an invalid course
        info("INVALID", room, instructor, time)

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Check for expected error message 
        output = captured_output.getvalue()
        self.assertIn("ERROR", output)
        self.assertIn("PLEASE ENTER ONE AVAILABLE COURSE NUMBER OR 'EXIT'", output)

if __name__ == '__main__':
    unittest.main()
