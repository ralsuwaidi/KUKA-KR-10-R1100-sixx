#!/usr/bin/env python

import rosunit
import unittest
from fk import FK
import numpy as np


class testFK(unittest.TestCase):

    # Set the precision
    decimal = 3

    # Table of DH parameters
    d = np.array([0.4, 0, 0, 0.515, 0, 0.08])
    a = np.array([0.025, 0.560, 0.035, 0, 0, 0])
    alpha = np.array(np.deg2rad([-90, 0, -90, 90, -90, 0]))

    def test_zero_configuration(self):
        # Joint variables
        theta = np.array(np.deg2rad([0, 0, 0, 0, 0, 0]))

        # calculate forward kinematics
        fk = FK(theta, self.d, self.a, self.alpha)

        # desired result
        result = np.array([[1, 0, 0, 0.62],
                           [0, -1, 0, 0],
                           [0, 0, -1, -0.195],
                           [0, 0, 0, 1]])

        # compare numpy arrays
        np.testing.assert_array_almost_equal(
            fk, result, self.decimal, 'Zero configuration test was failed!')

    def test_second_joint(self):
        # Joint variables
        theta = np.array(np.deg2rad([0, -90, 0, 0, 0, 0]))

        # calculate forward kinematics
        fk = FK(theta, self.d, self.a, self.alpha)

        # desired result
        result = np.array([[0, 0, 1, 0.62],
                           [0, -1, 0, 0],
                           [1, 0, 0, 0.995],
                           [0, 0, 0, 1]])

        # compare numpy arrays
        np.testing.assert_array_almost_equal(
            fk, result, self.decimal, 'Second joint test was failed!')


if __name__ == '__main__':
    rosunit.unitrun('arm_tests', 'test_forward_kinematics', testFK)
