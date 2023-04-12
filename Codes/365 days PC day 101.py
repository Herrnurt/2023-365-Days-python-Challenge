#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 23:41:50 2023

@author: boladipo
"""



## AUtomatic Wi-fi password as Qr Code



import wifi_qrcode_generator as qr



qr.wifi_qrcode('wifi name', False, "WPA", 'password')