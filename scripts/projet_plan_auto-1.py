#importation des bibliotheques necessaires 
from pyautocad import Autocad,APoint,aDouble

#ouverture du fichier txt
data=open("../data/dato.txt","r")

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
acad=Autocad(create_if_not_exists=True,visible=True)

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

#ajout du cadre
    
#recuperation des valeurs extremes
xmax=max(x)
xmin=min(x)
ymax=max(y)
ymin=min(y)

print("le max des x est :",xmax)
print("le min des x est :",xmin)
print("le max des y est :",ymax)
print("le min des y est :",ymin)

#insertion
ajl=60
aju=40
cadre1=aDouble(xmin-ajl,ymax+aju,0,xmax+ajl,ymax+aju,0,xmax+ajl,ymin-aju,0,xmin-ajl,ymin-aju,0,xmin-ajl,ymax+aju,0) #definition des coordonees 
acad.model.AddPolyline(cadre1)

#deuxieme cadre
aK=70
cadre2=aDouble(xmin-aK,ymax+aK,0,xmax+aK,ymax+aK,0,xmax+aK,ymin-aK,0,xmin-aK,ymin-aK,0,xmin-aK,ymax+aK,0) #definition des coordonees 
acad.model.AddPolyline(cadre2)

#ajout des differents textes
#cotatation 1
tmat=2
cot1=APoint(xmin-ajl,ymax+aK-3)
acad.model.AddText(u'{}'.format("ODRE NATIONAL DES GEOMETRES EXPERT"),cot1,tmat)
 
 #cotation 2
tmat=2
cot2=APoint(xmin-ajl,ymax+aK-8)
acad.model.AddText(u'{}'.format("CABINET XVIX"),cot2,tmat)
tmat=2
cot3=APoint(xmin-ajl,ymax+aK-13)
acad.model.AddText(u'{}'.format("ROLL-UP"),cot3,tmat)

#COTATION 4 et 5
wid1=10
cot4=APoint(xmax-wid1,ymax+aK-3)
mt1=acad.model.AddMText(cot4,wid1,"REGION: CENTRE")
mt1.Height=2

#cot 6
tmat=2
cot2=APoint(xmin-ajl,ymin-aK+13)
acad.model.AddText(u'{}'.format("Bornee leve et dresse par"),cot2,tmat)
tmat=2
cot3=APoint(xmin-ajl,ymin-aK+8)
acad.model.AddText(u'{}'.format("ELOUNDOU ABEGA"),cot3,tmat)
tmat=2
cot3=APoint(xmin-ajl,ymin-aK+3)
acad.model.AddText(u'{}'.format("JEAN JOVANICK"),cot3,tmat)

wid1=22
cot5=APoint(xmax-wid1,ymax+aK-8)
mt2=acad.model.AddMText(cot5,wid1,"ARRONDISSEMENT: OBALA")
mt2.Height=2


#creation du tableau de coordonnees 
entet=['MAT','X','Y']
t=1
tmat=1.25
aj=10
for i in range(0,len(entet)):
    entete=aDouble(xmax+aj+10*i,(ymin+ymax)/2,0,xmax+aj+10*i+10,(ymin+ymax)/2,0,xmax+aj+10*i+10,(ymin+ymax)/2-5,0,xmax+aj+10*i,(ymin+ymax)/2-5,0,xmax+aj+10*i,(ymin+ymax)/2,0)
    acad.model.AddPolyline(entete)
    lab=APoint(xmax+aj+10*i+t,(ymax+ymin)/2-5+t)
    acad.model.AddText(u'{}'.format(entet[i]),lab,tmat)

xdep=xmax+aj
ydep=(ymax+ymin)/2-5
val=[]
for i in range(0,len(x)):
    val=[name[i],x[i],y[i]]
    for j in range (0,len(entet)):
        entete= aDouble(xdep+10*j,ydep-5*i,0,xdep+10*j+10,ydep-5*i,0,xdep+10*j+10,ydep-5-5*i,0,xdep+10*j,ydep-5-5*i,0,xdep+10*j,ydep-5*i,0)
        acad.model.AddPolyline(entete)
        lab=APoint(xdep+10*j+t,ydep-5*i+t-5)
        acad.model.AddText(u'{}'.format(val[j]),lab,tmat)
