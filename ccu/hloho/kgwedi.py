import datetime
from rhythm0 import *

ditshwantso = ['../0c.png', '../1q.png','../2g.png', '../3f.png', 
'../3g.png','../4q.png','../5c.png','../6a.png']

#letsatsi_lekano = (69, 6252)

class almanaka0:
	def __init__(nna):
		nna.letsatsi_lekano = (6252, 69)
		nna.kgwedi = 27.3 #27.3 #29.5 
		nna.kgwedi_hora = nna.kgwedi*24
		#nna.kgwedi_motsotswana = nna.kgwedi*24*60
		#nna.karolo = nna.kgwedi_motsotswana/len(ditshwantso)
		nna.karolo = nna.kgwedi_hora/len(ditshwantso)

	def nako(nna, selemo, letsatsi_selemo):
		nako_fetele = ((letsatsi_selemo - nna.letsatsi_lekano[1])\
				+ (selemo - nna.letsatsi_lekano[0]))*24 # fetola ho dihora
		#print(int(nako_fetele/24), '|', letsatsi_selemo)
		karolo_kgwedi = (nako_fetele/nna.karolo) % len(ditshwantso)
		return ditshwantso[int(karolo_kgwedi)] #nepo e wile kahore ha ka kenya dihora

    

if __name__=="__main__":
	almanaka = almanaka()
	selemo, letsatsi_selemo = almanaka.mapping(datetime.date.today())
	u = almanaka0()
	for i in range(0,96):
		print(u.nako(selemo, letsatsi_selemo - i))

