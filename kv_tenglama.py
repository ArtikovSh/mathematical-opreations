# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 00:54:16 2024

@author: Shohrux
"""

a = float(input("a ning qiymatini kiriting: "))
b = float(input("b ning qiymatini kiriting: "))
c = float(input("c ning qiymatini kiriting: "))
d = b**2-4*a*c
if d<0:
    xyarim1 = -b/(2*a)
    e = (2*a)
    if e-int(e)==0:
        print(f"Ushbu tenglamaning yechimlari:\n x1={xyarim1}+({-d}^(1/2)*i)/{int(e)}, x2={xyarim1}-({-d}^(1/2)*i)/{int(e)}.")
    else:
        print(f"Ushbu tenglamaning yechimlari:\n x1={xyarim1}+({-d}^(1/2)*i)/{e}, x2={xyarim1}-({-d}^(1/2)*i)/{e}.")
else:
    xbir = (-b+d**(1/2))/(2*a)
    xikki = (-b-d**(1/2))/(2*a)
    if xbir-int(xbir)==0 and xikki-int(xikki)!=0:
        print(f"Ushbu tenglamaning yechimlari:\n x1={int(xbir)}, x2={xikki}.")
    elif xikki-int(xikki)==0 and xbir-int(xbir)!=0:
        print(f"Ushbu tenglamaning yechimlari:\n x1={xbir}, x2={int(xikki)}.")
    elif xbir-int(xbir)==0 and xikki-int(xikki)==0:
        print(f"Ushbu tenglamaning yechimlari:\n x1={int(xbir)}, x2={int(xikki)}.")
    elif xbir-int(xbir)!=0 and xikki-int(xikki)!=0:
        print(f"Ushbu tenglamaning yechimlari:\n x1={xbir}, x2={xikki}.")