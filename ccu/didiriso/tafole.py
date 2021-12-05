from kivy.app import App as Tshebediso
from kivy.uix.boxlayout import BoxLayout as SeemoKN
from kivy.lang import Builder as Moagi

import requests as dikopo

URL = "http://192.168.8.102:8000"

	
Moagi.load_string('''
<Tafole>:
	id: fes_kgo
	RecycleView:
		viewclass: "CustLabel"
		id: lefatse_tafole
		RecycleGridLayout:
			id: slt
			cols: 4
			default_size: (None, 250)
			default_size_hint: (1, None)
			size_hint_y: None
			height: self.minimum_height
			spacing: 1
			
<CustLabel@Label>:
	bcolor: (1,1,1,1)
	canvas.before:
		Color:
			rgba: root.bcolor
		Rectangle:
			size: self.size
			pos: self.pos
''')


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
difane = []
dibelas = []
ditulo = []	
fneng = []

bbasebedisi1 = []
metshireletsi1 = []
difane1 = []
dibelas1 = []
ditulo1 = []	
fneng1 = []

class Tafole(SeemoKN):
	def __init__(nna, table, **kwargs):
		super().__init__(**kwargs)
		CHOICES = ['basebedisi', 'manollo', 'intanete']
		if table in CHOICES:
			if table == "basebedisi":
				nna.simoloha(nna.lata_basebedisi())
		
			elif table == "manollo":
				nna.simoloha(nna.lata_basebedisi())
		
			elif table == "intanete":
				nna.simoloha(nna.lata_basebedisi())
		
		else:
			raise TypeError("Choice not in %s. Pick one of these tables" % (CHOICES))
			
		
	def simoloha(nna, table):
		bas = table
		
		print(bas, ': ', type(bas))
		#print(bas[0], ': ', type(bas[0]))
		#print(bas[0][1], ':', type(bas[0][1]))
		#print(bas[0][1][1], ':', type(bas[0][1][1]))
		col_titles = []
		counter = 0
		for i in bas:
			col_titles.append(bas[counter][0])
			counter +=1
		row_len = len(col_titles)
		nna.columns = row_len
		print(row_len)
		ttafole = []
		for t in col_titles:
			ttafole.append({'text':t, 'size_hint_y': None, 'height': 50, 'bcolor': (.06, .45, .45,1)})
		print(metshireletsi)
		for u in range(len(difane)):
			for r in range(row_len):
				#print(bas[r][1][u+1], ': ', type(bas[r][1][u+1]))
				ttafole.append({'text': str(bas[r][1][u+1]), 'size_hint_y':None,
				'height': 30, 'bcolor': (.06, .25, .25,1)})
		
		print(ttafole)
		nna.ids.slt.cols = nna.columns
		nna.ids.lefatse_tafole.data = ttafole
		
			
	def lata_basebedisi(nna):
		basebedisi = lata_basebedisi()
		for mosebedisi in basebedisi:
			metshireletsi.append(mosebedisi['username'])
			difane.append(mosebedisi['last_name'])
			fneng.append(mosebedisi['last_login'])
			if mosebedisi['is_superuser'] == True:
				ditulo.append('Mongodi')
			elif mosebedisi['is_staff'] == True:
				ditulo.append('Mobopi')
			else:
				ditulo.append('Mosebedisi')
			belas = mosebedisi['email']
			if len(belas) > 10:
				belas = belas[-10:]
			dibelas.append(belas)
		#print(ditulo)
		botelele = len(metshireletsi)
		idx = 0
		mmetshireletsi = {}
		ddifane = {}
		ddibelas = {}
		dditulo = {}
		ffneng = {}
		while idx < botelele:
			mmetshireletsi[idx + 1] = metshireletsi[idx]
			ddifane[idx + 1] = difane[idx]
			ddibelas[idx + 1] = dibelas[idx]
			dditulo[idx + 1] = ditulo[idx]
			ffneng[idx + 1] = fneng[idx]
			
			idx +=1
			
		bbasebedisi.append(("basebedisi" ,mmetshireletsi))
		bbasebedisi.append(("difane" ,ddifane))
		bbasebedisi.append(("dibelas", ddibelas))
		bbasebedisi.append(("ditulo", dditulo))
		bbasebedisi.append(("fneng", ffneng))
		
		return bbasebedisi


'''
class TTafole(Tshebediso):
	def build(nna):
		return Tafole()
	
if __name__=="__main__":
	TTafole().run()




x = lata_basebedisi()
y = lata_pv()
z = lata_man()
print(x)
print(y)
print(z)
'''
