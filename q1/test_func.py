# -*- coding: utf-8 -*-

import unittest
import itertools
from q1 import *

class TestFunc(unittest.TestCase):
    """Test q1.py"""

    def test_allocate_subnet_to_gateway(self):
        """Test method allocate_subnet_to_gateway(a, b)"""

        self.assertEqual({}, allocate_subnet_to_gateway(2,0))
        self.assertEqual({'GW0': [], 'GW1': []}, allocate_subnet_to_gateway(0,2))
        self.assertEqual({'GW0': ['Subnet0']}, allocate_subnet_to_gateway(1, 1))
        self.assertEqual({'GW0': ['Subnet0'], 'GW1': []}, allocate_subnet_to_gateway(1,2))
        self.assertEqual({'GW0': ['Subnet0'], 'GW1': [], 'GW2': []}, allocate_subnet_to_gateway(1,3))
        self.assertEqual({'GW0': ['Subnet0'], 'GW1': [], 'GW2': [], 'GW3': [], 'GW4': []}, allocate_subnet_to_gateway(1,5)) 
        self.assertEqual({'GW0': ['Subnet0'], 'GW1': ['Subnet1'], 'GW2': [], 'GW3': [], 'GW4': [], 'GW5': []}, allocate_subnet_to_gateway(2,6))
        self.assertEqual({'GW0': ['Subnet0'], 'GW1': ['Subnet1'], 'GW2': ['Subnet2'], 'GW3': [], 'GW4': []}, allocate_subnet_to_gateway(3,5))
        self.assertEqual({'GW0': ['Subnet0'], 'GW1': ['Subnet1'], 'GW2': ['Subnet2'], 'GW3': ['Subnet3'], 'GW4': ['Subnet4']}, allocate_subnet_to_gateway(5, 5))
        self.assertEqual({'GW0': ['Subnet0', 'Subnet5', 'Subnet7'], 'GW1': ['Subnet1', 'Subnet6', 'Subnet8']}, allocate_subnet_to_gateway(6,2))
        self.assertEqual({'GW0': ['Subnet0', 'Subnet5', 'Subnet6', 'Subnet7', 'Subnet8']}, allocate_subnet_to_gateway(5,1))
        self.assertEqual({'GW0': ['Subnet0', 'Subnet3'], 'GW1': ['Subnet1', 'Subnet4'], 'GW2': ['Subnet2']}, allocate_subnet_to_gateway(5,3))
        self.assertEqual({'GW0': ['Subnet0', 'Subnet6', 'Subnet8', 'Subnet10'], 'GW1': ['Subnet1', 'Subnet7', 'Subnet9']}, allocate_subnet_to_gateway(7,2))

if __name__ == '__main__':
    unittest.main()
