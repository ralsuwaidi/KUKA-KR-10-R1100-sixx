#!/usr/bin/env python

from fk import FK
import unittest
import numpy as np

class Test_FK(unittest.TestCase):
	def test_zero_configuration(self):
		# Joint variables
		theta = np.array(np.deg2rad([0, -90, 0, 0, 0, 0]))
		# Table of DH parameters
		d = np.array([0.4, 0, 0, 0.515, 0, 0.08])
		a = np.array([0.025, 0.560, 0.035, 0, 0, 0])
		alpha = np.array(np.deg2rad([-90, 0, -90, 90, -90, 0]))

		fk = FK(theta, d, a, alpha)

		result = np.array([[0, 0, 1, 0.62],
				   [0, -1, 0, 0],
				   [1, 0, 0, 0.995],
				   [0, 0, 0, 1]])

		flag = np.array_equal(fk, result) 
                self.assertEqual(flag, True, "ERROR!")

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun("arm_tests", 'test_add', Test_FK)
