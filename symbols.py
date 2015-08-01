# -*- coding: utf-8 -*-
""" NICERPYTHON | SYMBOLS
    
    constants and symbols
"""

class _DontCare(object):
    def __lt__(self, other):
        return True
    
    def __gt__(self, other):
        return True
    
    def __eq__(self, other):
        return True
    
    def __add__(self, other):
        return other
    
    def __sub__(self, other):
        return -other
    
    def __mul__(self, other):
        return other

    def __pow__(self, p):
        return self
    
    def __floordiv__(self, other):
        return 1//other
    
    def __div__(self, other):
        return 1/other
    
    def __mod__(self, other):
        return 0
    
    def __and__(self, other):
        return True
    
    def __or__(self, other):
        return True
    
    def __xor__(self, other):
        return True
    
    # # #
    def __rlt__(self, other):
        return True
    
    def __rgt__(self, other):
        return True
    
    def __req__(self, other):
        return True
    
    def __radd__(self, other):
        return other
    
    def __rsub__(self, other):
        return other
    
    def __rmul__(self, other):
        return other

    def __rpow__(self, p):
        return p
    
    def __rfloordiv__(self, other):
        return other
    
    def __rdiv__(self, other):
        return other
    
    def __rmod__(self, other):
        return 0
    
    def __rand__(self, other):
        return True
    
    def __ror__(self, other):
        return True
    
    def __rxor__(self, other):
        return True

    # # # 
        
    def __str__(self):
        return "dontcare"
    
    def __repr__(self):
        return "dontcare"

dontcare = _DontCare()
