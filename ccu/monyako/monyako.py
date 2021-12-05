from kivy.app import App as Tshebediso
from kivy.uix.boxlayout import BoxLayout as SeemoKN
from kivy.lang import Builder as Moagi

import requests as dikopo

URL = "http://192.168.8.102:8000/"


def lata_senotlolo(lebitso, lekunutu):
	# Lata senotlolo
	url = "%s/manollo/nnete/" % (URL)
	karabo = dikopo.post(url, data={'username': lebitso, 
					'password': lekunutu})
	return karabo.json()

def lata_tshebiso(lebitso, lekunutu):
	url = "%s/manollo/lenane_bas/" % (URL)
	hloho = {'Authorization': "Token %s" % (lata_senotlolo(lebitso, lekunutu))}
	karabo = dikopo.get(url, headers=hloho)
	return karabo.json()

class FMonyako(SeemoKN):
	def __init__(nna, **kwargs):
		super().__init__(**kwargs)
		
	def nnetefatsa_mosebedisi(nna):
		mosebedisi = nna.ids.lb
		lentswe = nna.ids.lk
		tsebiso = nna.ids.tsebiso
		
		lebitso = mosebedisi.text
		lekunutu = lentswe.text
		karabo = lata_tshebiso(lebitso, lekunutu)
		if karabo=={'detail': 'Invalid token header. Token string should not contain spaces.'}:
			tsebiso.text ="[color=#FF0000]Ho nale bothata ka lebitso le/kapa leunutu, leka hape.[/color]"
		else:
			tsebiso.text ="[color=#FF0000]O atlehile ho kena!!![/color]"
			nna.parent.parent.current = 'fenstere_molaoli'
			print(karabo)
		
class TMonyako(Tshebediso):
	def build(nna):
		return FMonyako()
	
if __name__=="__main__":
	TMonyako().run()
