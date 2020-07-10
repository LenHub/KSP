import numpy as np 

G = 6.67430*10**(-11)  #m^3.kg^-1.s^-2
 

def altitudes(R,M,T):
	"""Renvoie l'alitude de l'orbite géostationnaire et
	le periastre et l'apoastre de l'orbite de transfert permettant de placer 3 satellites sur
	l'orbite stationnaire
	Prend en entrée la masse le rayon et la période de rotation sidérale de l'astre concerné"""
	Tt = 2*T/3

	Rs = (T**2*G*M/(4*(np.pi)**2))**(1/3)  #Rayon de l'orbite statiionnaire (Rs = R + Hs avec Hs l'altitude de l'orbite stationnaire)

	At = (Tt**2*G*M/(4*(np.pi)**2))**(1/3) #Demi grand axe de l'orbite de transfert

	Hs = Rs - R

	Pe = 2*(At - R) - Hs

	print("""
		Rayon de l'orbite stationnaire: {}

		Apoastre de l'orbite de transfert: {}

		Pésiastre de l'orbite de transfert: {}

		""".format(Hs, Hs, Pe))


R_Kerbin = 600000 #m
M_Kerbin = 5.2915158*10**22 #kg
T_Kerbin = 21549.425 #s

altitudes(R_Kerbin, M_Kerbin, T_Kerbin)


