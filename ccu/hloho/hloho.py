from kivy.app import App as Tshebediso
from kivy.uix.boxlayout import BoxLayout as SeemoKN
from kivy.uix.scrollview import ScrollView
from kivy.uix.scatter import Scatter
#from kivy.app import runTouchApp
from kivy.clock import Clock

from didiriso.tafole import Tafole
from rhythm0 import *
from kgwedi import *

import requests as dikopo
import datetime

URL = "http://192.168.8.102:8000"

# dt = datetime.timedelta(21)

def lata_tsebiso():
	almanaka = almanaka1()
	u = almanaka0()
	selemo, letsatsi_selemo = almanaka.mapping(datetime.date.today())
	kgwedi, letsatsi_shume = almanaka.thlaloso(letsatsi_selemo)
	beke, letsatsi = almanaka.letsatsi(letsatsi_selemo)
	setswantsho = u.nako(selemo, letsatsi_selemo)
	return selemo, letsatsi_selemo, kgwedi, letsatsi_shume, beke, letsatsi, setswantsho


class FHloho(SeemoKN):
	def __init__(nna, **kwargs):
		super().__init__(**kwargs)
		
		
		selemo, letsatsi_selemo, kgwedi, letsatsi_shume, beke, letsatsi, setswantsho = lata_tsebiso()
		#print(setswantsho)
		nna.ids.kgw.source = setswantsho
		
		dikahari = nna.ids.dikahare
		table = "basebedisi"
		tafole_bas = Tafole(table=table)
		dikahari.add_widget(tafole_bas)

	
class THloho(Tshebediso):
	def build(nna):
		return FHloho()
	
if __name__=="__main__":
	THloho().run()



'''
x = lata_basebedisi()
y = lata_pv()
z = lata_man()
print(x)
print(y)
print(z)
'''
