from kivy.app import App as Tshebediso
from kivy.uix.boxlayout import BoxLayout as SeemoKN


import requests as dikopo

URL = "http://192.168.8.102:8000"

	


def lata_basebedisi():#lebitso, lekunutu):
	'''This function fetches the information from the database'''
	url = "%s/manollo/lenane_bas/" % (URL)
	#hloho = {'Authorization': "Token %s" % (lata_senotlolo(lebitso, lekunutu))}
	karabo = dikopo.get(url)#, headers=hloho)
	return karabo.json()

def lata_pv():#lebitso, lekunutu):
	'''This function fetches the information from the database'''
	url = "%s/manollo/lenane_pv/" % (URL)
	#hloho = {'Authorization': "Token %s" % (lata_senotlolo(lebitso, lekunutu))}
	karabo = dikopo.get(url)#, headers=hloho)
	return karabo.json()

def lata_man():#lebitso, lekunutu):
	'''This function fetches the information from the database'''
	url = "%s/manollo/lenane_tshebiso/" % (URL)
	#hloho = {'Authorization': "Token %s" % (lata_senotlolo(lebitso, lekunutu))}
	karabo = dikopo.get(url)#, headers=hloho)
	return karabo.json()

bbasebedisi = []
metshireletsi = []
mabitso = []
difane = []
dibelas = []
ditulo = []	
fneng = []

class FHloho(SeemoKN):
	def __init__(nna, **kwargs):
		super().__init__(**kwargs)
		
def lata_basebedisi():
	basebedisi = lata_basebedisi()
	for mosebedisi in basebedisi:
		metshireletsi.append(mosebedisi['username'])
		mabitso.append(mosebedisi['first_name'])
		difane.append(mosebedisi['last_name'])
		fneng.append(mosebedisi['last_login'])
		if mosebedisi['is_superuser'] == True:
			ditulo.append('Mongodi')
		elif mosebedisi['is_staff'] == True:
			ditulo.append('Mobopi')
		else:
			ditulo.append('Mosebedisi')
		dibelas.append(mosebedisi['email'])
	#print(ditulo)
	botelele = len(mabitso)
	idx = 0
	mmetshireletsi = {}
	mmabitso = {}
	ddifane = {}
	ddibelas = {}
	dditulo = {}
	ffneng = {}
	while idx < botelele:
		mmetshireletsi[idx + 1] = metshireletsi[idx]
		mmabitso[idx + 1] = mabitso[idx]
		ddifane[idx + 1] = difane[idx]
		ddibelas[idx + 1] = dibelas[idx]
		dditulo[idx + 1] = ditulo[idx]
		ffneng[idx + 1] = fneng[idx]
		
		idx +=1
		
	bbasebedisi.append(("basebedisi" ,mmetshireletsi))
	bbasebedisi.append(("mabitso" ,mmabitso))
	bbasebedisi.append(("difane" ,ddifane))
	bbasebedisi.append(("dibelas", ddibelas))
	bbasebedisi.append(("ditulo", dditulo))
	bbasebedisi.append(("fneng", ffneng))
	
	return bbasebedisi
	
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
