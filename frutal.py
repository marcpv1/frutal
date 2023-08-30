import random
import numpy as np
import sys

def resultat(tirada):
 if tirada==1:
    return "groc"
 if tirada==2: 
    return "verd"
 if tirada==3: 
    return "blau"
 if tirada==4: 
    return "vermell"
 if tirada==5: 
    return "cistell"
 if tirada==6: 
    return "corb"

NomesResultat="0"
Corb=2

if (len(sys.argv)>1):
    NomesResultat = sys.argv[1]

if (len(sys.argv)>2):
    Corb = int(sys.argv[2])

arbre = np.array([4,4,4,4])
arbreBuit = np.array([0,0,0,0])

arbre_es_buit = (arbre == arbreBuit).all()

if NomesResultat=="0": print("VALORS INICIALS")
if NomesResultat=="0": print(arbre)
if NomesResultat=="0": print "Corb: " , Corb

while (arbre_es_buit==False) and (Corb>0):

 tirada = (random.randint(1,6))

 if NomesResultat=="0": print
 if NomesResultat=="0": print("Dau tirat. Ha sortit " + resultat(tirada))

 if tirada==1 or tirada==2 or tirada==3 or tirada==4: 
    if arbre[tirada-1]>0:
       arbre[tirada-1]=arbre[tirada-1]-1

 if tirada==5:
   if arbre[0]>0:
      arbre[0]=arbre[0]-1
   if arbre[1]>0:
      arbre[1]=arbre[1]-1
   if arbre[2]>0:
      arbre[2]=arbre[2]-1
   if arbre[3]>0:
      arbre[3]=arbre[3]-1

 if tirada==6:
     Corb=Corb-1

 if NomesResultat=="0": print("Arbres: ")
 if NomesResultat=="0": print(arbre)
 if NomesResultat=="0": print "Corb: " , Corb

 arbre_es_buit = (arbre == arbreBuit).all()

if (arbre_es_buit==True):
   print("VICTORIA DELS JUGADORS")

if (Corb==0):
   print("VICTORIA DEL CORB")
