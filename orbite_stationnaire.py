 
import numpy as np 
import sys

G = 6.67430*10**(-11)  #m^3.kg^-1.s^-2
 
#Astres sous la forme (Rayon (m), Masse (kg), Période de rotation sidérale (s))
Astres = {
	'Kerbin' : (600000, 5.2915158*10**22, 21549.425),
	'Duna' : (320000, 4.5154270*10**21, 65517.859),
	'Eve' : (700000, 1.2243980*10**23, 80500.000)
	}

def altitudes(nom):
	"""Renvoie l'alitude de l'orbite géostationnaire et
	le periastre et l'apoastre de l'orbite de transfert permettant de placer 3 satellites sur
	l'orbite stationnaire
	Prend en entrée la masse le rayon et la période de rotation sidérale de l'astre concerné"""
	(R,M,T) = Astres[nom]

	#T = T/2  #décommenter pour orbite semi synchrone

	Tt = 2*T/3

	Rs = (T**2*G*M/(4*(np.pi)**2))**(1/3)  #Rayon de l'orbite stationnaire (Rs = R + Hs avec Hs l'altitude de l'orbite stationnaire)

	At = (Tt**2*G*M/(4*(np.pi)**2))**(1/3) #Demi grand axe de l'orbite de transfert

	Hs = Rs - R

	Pe = 2*(At - R) - Hs

	print("""
		Astre: {}
		Rayon de l'orbite stationnaire: {}
		Pésiastre de l'orbite de transfert: {}
		""".format(nom, Hs, Pe))




if len(sys.argv) !=2 or sys.argv[1] not in Astres:
	altitudes('Kerbin')
else:
	altitudes(sys.argv[1])
