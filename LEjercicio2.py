print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------- Ejercicio 3 ----------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
#Ejercicio3
# Los arrays `u` y `v` representan dos series en funcion del tiempo `t`.
# Calcule la covarianza entre `u` y `v` e imprima su valor.

import numpy as np
import matplotlib.pylab as plt
u = np.array([12.,45.,6.,78.,34.,22.,-10.,31.,-27.])
v = np.array([3.,11.,1.3,37.,11.,6.,-23.,7.,7.])


def covarianza(u,v):
	A=np.zeros((len(u)))
	for i in range(1,len(u)):
		for j in range(1,len(u)):	
			a=u[i]-np.mean(u)
			b=v[j]-np.mean(v)	
			ab=a*b
			A[i]=(np.sum(ab))/(len(u)-1)
	return A

print covarianza(u,v)
