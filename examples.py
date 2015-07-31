# -*- coding: utf-8 -*-

from symbols import *
import numpy as np

a = np.array([1.0, 2.0, dontcare, 3.0])

print a + 2.0
print a * 2.0
print 2.0 + a
print 2.0 * a

print True == dontcare == True
print False == dontcare == False
print True == False
print True - dontcare == True
print dontcare + False == False