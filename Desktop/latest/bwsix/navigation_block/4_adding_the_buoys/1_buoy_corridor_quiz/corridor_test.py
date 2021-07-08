# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 01:38:56 2021

@author: JO20993
"""
import numpy as np
import matplotlib.pyplot as plt

import hashlib

def my_hash(data):
    if not isinstance(data, str):
        d2 = data.tobytes()
    else:
        d2 = data.encode("UTF-8")
        
    return hashlib.md5(d2).hexdigest()

def round_and_report(data, n):
    d2 = np.rint(data * 10**n).astype(np.int32)
    return my_hash(d2)
    

A = np.array([[ 10.6,  23.3], [-36.1, -18.7], [ 49.7, -37.2], [-32.1,  25.3], [ 16.2,  28.4],
              [-40.3, -44.1], [ 46.2,  11.7], [-41.3,   6.1], [ 11.7,  46.4], [  7.4, -12.9],
              [ -4.8, -29.8], [  6.9, -30.5], [  8.4,  -2.4], [  1.8,  32.3], [ 23.2, -43.1],
              [ 17.2,  14.3], [ 32.8, -29.6], [ 11.7,  11.8], [-19.9,  37.2], [  9.0,  48.2],
              [ -5.8, -37.4], [  0.9,  -6.8], [ 41.6,  20.9], [ 39.1,   8.9], [ 13.7, -15.8]])

G = np.array([[ 32.4, -19.5], [-19.2, -29.9], [-23.5,  15.1], [-34.5, -11.1], [ 14.8,  34.8],
              [-43.6,  -8.6], [-16.8,  22.1], [ -2.6,  29.9], [-40.9,  37.5], [ 27.7,  27.2],
              [-43.7,   9.4], [ 29.2, -22.6], [-12.9,  35.3], [ 17.9,  25.4], [ -8.3, -17.9],
              [-12.8, -22.5], [ 18.0,   8.2], [ 47.0,  -8.4], [-17.0,  46.7], [ 32.6, -19.5],
              [ 32.3,   5.7], [ 21.9,  38.0], [ -0.4,   1.2], [ 14.9, -15.7], [ 12.3,  -3.5]])

R = np.array([[-37.6,  48.0], [ -4.8, -38.3], [ 32.0, -32.5], [-26.9,  20.5], [ 21.8, -35.2],
              [-10.6,  30.3], [ 31.0,  29.6], [ 35.8, -20.3], [-34.1,  18.6], [ 23.4, -35.2],
              [-23.3, -11.8], [  0.4,  15.7], [ 25.2, -43.3], [-28.9,  17.4], [ 39.7,  26.2],
              [ 31.6,  11.0], [  9.1,  35.5], [ 13.3,  36.8], [ -8.4,  15.7], [ 40.5, -42.0],
              [ 18.0, -41.7], [-29.1,  33.8], [  2.2,  22.1], [ 36.2,  26.9], [ 17.7,   5.5]])

incount = 0
Ntest = R.shape[0]
incorridor = np.zeros((Ntest,1), dtype=bool)
for i in range(Ntest):
    GR = np.array((R[i,0]-G[i,0], R[i,1]-G[i,1]))
    GA = np.array((A[i,0]-G[i,0], A[i,1]-G[i,1]))
    RA = np.array((A[i,0]-R[i,0], A[i,1]-R[i,1]))
    
    GRGA = np.dot(GR, GA)
    GRRA = np.dot(GR, RA)
    
    if (GRGA*GRRA < 0):
        print(f"{i}: in the corridor ( {GRGA}, {GRRA} )")
        incorridor[i] = True
        incount += 1
    
    doPlot = False
    if (doPlot):
        plt.plot(R[i,0], R[i,1], 'ro')
        plt.plot(G[i,0], G[i,1], 'go')
        plt.plot(A[i,0], A[i,1], 'yo')
        plt.axis('equal')
        plt.show()
    

print(f"MD5 hash = {my_hash(incorridor)}")