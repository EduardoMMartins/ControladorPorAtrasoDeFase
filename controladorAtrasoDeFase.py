#Código do Projeto de Controladores por Atraso de Fase


#Importando Funções
import numpy as np
import control.matlab as ml
import matplotlib.pyplot as plt
import math
import scipy
from scipy.interpolate import interp1d
from control import *

#Definindo Margem de Fase desejada 
pmd = 45 #[VALOR ADICIONADO]

#Definindo g(s) 
num = np.array([1]) #[VALOR ADICIONADO]
den = np.polymul(np.array([1,0]),np.array([1,2])) #[VALOR ADICIONADO]
g = ml.tf(num,den)
print("Função de Transferência G(s): ", g)

#Definindo K
ess = 5/100 #[VALOR ADICIONADO]
kv = 1/ess #Sistema do tipo 1 // [EQUAÇÃO ADICIONADA]
k = 2*kv #[EQUAÇÃO ADICIONADA]
print("K = ", k)

#Definir G1(s)
g1 = k*g
print("Função de Transferência G1(s): ", g1)
mag,phase,w = ml.bode(g1)

#Calculando a Margem de Ganho e Fase
gm,pm,wg,wp = margin(g1)
print("Margem de Ganho: ", gm)
#pm = math.ceil(pm) #Arredonda o valor da Margem de Fase para cima
print("Margem de Fase: ", pm)

#Definindo Angulo de Fase 
anguloAvanco = 5 #[ADICIONAR VALOR DE 5º A 12º]
phim = -180 + pmd + anguloAvanco
print("Valor do Ângulo de Fase: ", phim)

#Definindo Wc
def myFunction(x):
    return x

myFunction2 = np.vectorize(myFunction)

wq = interp1d(myFunction2(phase), w)
wc = wq(np.deg2rad(phim))
print("Wc = ", wc)

#Definindo magc
def myFunctionMag(x):
    return 20*math.log10(x)

myFunctionMag2 = np.vectorize(myFunctionMag)

magq = interp1d(w,myFunctionMag2(mag))
magc = magq(wc)
print("magc = ", magc)

#Definindo alpha 
alpha = 10**(magc/20)
print("Alpha: ", alpha) 

#Definindo o Período (T)
t = 10/wc
print("Período (T): ", t)

#Definindo frequêcia do zero (Wz)
wz = 1/t
print("Frequência do zero (wz): ", wz)

#Definindo frequência do polo (Wp)
wp = wz/alpha
print("Frequência do Polo (Wp): ", wp)

#Definindo valor de Beta (B)
beta = 1/(wp*t)
print("Beta (B): ", beta)

#Definindo a Função de Transferência do Compensador (Gc)
bt = beta*t
numc = np.array([t, 1])
denc = np.array([bt, 1])
gCompensador = k*ml.tf(numc,denc)
print("Função de Transferência do Compensador: ", gCompensador)

#Iterando as Funções de Transferências
gIterada = gCompensador*g
print("Função de Tranferência Iterada: ", gIterada)
magIt,phaseIt,wIt = ml.bode(gIterada)

#Calculando a Margem de Fase da Função de Transferência Iterada
gmIt,pmIt,wgIt,wpIt = margin(gIterada)
print("Margem de Fase da FT Iterada: ", pmIt)
print("Margem de Fase Desejada: ", pmd)
print("Diferença entre a Margem de Fase Desejada e a Obtida: ", pmd - pmIt)