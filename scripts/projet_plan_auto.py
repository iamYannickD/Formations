#importation des bibliotheques necessaires 
from pyautocad import Autocad,APoint,aDouble
import os

#ouverture du fichier txt, relativement au chemin de ce dernier
script_dir = os.path.dirname(__file__)
relative_path = os.path.join(script_dir, '../data/dato.txt')

#ouverture du fichier txt
data = open(relative_path, "r")

#Creation des differentes variables 
name=[]
x=[]
y=[]

#stockage des differentes variables 
lignes=data.readlines()
for ligne in lignes:
    print(ligne)
    name.append(ligne.split(' ')[0])
    x.append(float(ligne.split(' ')[1]))
    y.append(float(ligne.split(' ')[2]))
    #stockage des variables reussi

#instantiation de Autocad
acad=Autocad()

#realisation du plan
for i in range(0,len(x)):

    #creation des differents points
    Pac=APoint(x[i],y[i])
    Pap=APoint(x[(i+1)%len(x)],y[(i+1)%len(x)])
    
    #creation de la ligne entre les deux points 
    acad.model.AddLine(Pac,Pap)

    #creation des differentes bornes
    t=1
    borne=aDouble(x[i]-t,y[i]-t,0,x[i]-t,y[i]+t,0,x[i]+t,y[i]+t,0,x[i]+t,y[i]-t,0,x[i]-t,y[i]-t,0) #definition des coordonees 
    acad.model.AddPolyline(borne) #ajouter les polylignes

    #ajout ddes matricules des differents points
    tmat=2.5
    #defnition de la position du point
    txt=APoint(x[i]+t,y[i]+t)
    #ecriture des matricules sur les differents points
    acad.model.AddText(u'{}'.format(name[i]),txt,tmat)

