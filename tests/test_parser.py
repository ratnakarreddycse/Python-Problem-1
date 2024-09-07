import unittest
from main import parse_spec_file, parse_fixed_width_file

class TestFixedWidthParser(unittest.TestCase):
    
    def test_parse_spec_file(self):
        spec = parse_spec_file('spec.txt')
        expected_spec = [('FirstName', 10), ('LastName', 5), ('Address', 20), ('Age', 3)]
        self.assertEqual(spec, expected_spec)

    def test_parse_fixed_width_file(self):
        spec = [('FirstName', 10), ('LastName', 5), ('Address', 20), ('Age', 3)]
        parsed_data = parse_fixed_width_file(spec, 'fixed_width_file.txt')
        expected_data = [
            ['John', 'Smith', 'AddressHome', '43'],
            ['ABCD', 'EFG', 'Addresswork', '23'],
            ['TEST1', 'TEST1', 'Addresssssssssssssss', '111']
        ]
        self.assertEqual(parsed_data, expected_data)

if __name__ == '__main__':
    unittest.main()
