

import requests as dikopo

URL = "http://192.168.8.102:8000"



def lata_tshebiso(): # lebitso, lekunutu):
	'''This function fetches the information from the database'''
	url = "%s/manollo/lenane_bas/" % (URL)
	#hloho = {'Authorization': "Token %s" % (lata_senotlolo(lebitso, lekunutu))}
	karabo = dikopo.get(url)#, headers=hloho)
	return karabo.json()
	
x = lata_tshebiso()
print(x)
