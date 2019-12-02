# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:42:14 2019

@author: narendra
"""

import cv2

def process(foto):
    mean = foto.mean()
    foto[foto>mean]= 0
    return foto