#!/usr/bin/env python

import numpy as np

np.set_printoptions(precision=3)


def DH_transform(theta, d, a, alpha):
    transform = np.array([[np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(alpha)*np.sin(theta), a*np.cos(theta)],
                          [np.sin(theta), np.cos(alpha)*np.cos(theta), -
                           np.sin(alpha)*np.cos(theta), a*np.sin(theta)],
                          [0, np.sin(alpha), np.cos(alpha), d],
                          [0, 0, 0, 1]])
    return transform


def FK(theta, d, a, alpha):

    links_number = theta.shape[0]

    fk = np.eye(4)
    trans = np.zeros((4, 4, links_number))

    for i in range(links_number):
        trans[:, :, i] = DH_transform(theta[i], d[i], a[i], alpha[i])
        fk = np.matmul(fk, trans[:, :, i])

    return fk
