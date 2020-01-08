import unittest
from sampleFunction import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for ;get_formatted_name' function."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """DO names like 'Robby john jackson' work?"""
        formatted_name = get_formatted_name('Robby', 'john', 'jackson')
        self.assertEqual(formatted_name,'Robby Jackson John')

unittest.main()
