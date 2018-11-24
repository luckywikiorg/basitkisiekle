# libler

import time
import os
import sys



kisiler = []



def girisbanneri():
	print("""
	
    | 	    BıgData     |
    
						  """)
	print("")

def menu():
	print("""

		1| Kişi Ekle
		2| Kişileri Görüntüle

		""")
	
	print("")

def secimmenu():
	
	menusecim = input(">_ ")

	if menusecim == "1":
		kisiekle = input("Kişiyi Ekle >_  ")
		kisiler.append(kisiekle)
		print("Kişi Eklendi!")
		print("")
		secimmenu()
	if menusecim == "2":
		print(kisiler)
		secimmenu()



print("")

girisbanneri()

menu()

secimmenu()




	
