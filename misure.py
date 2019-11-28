from ordine2 import *



prova = Calcolo()
prova.setMisure([6.7,10.2,3.1],[3,1,2],13.5)
#diz = prova.ciclo(prova.m, prova.nM, prova.mF)
print(prova.arrayMisure(prova.m, prova.nM))
#print(str(diz["b"][0]) + '\n' + str(diz["s"][0]) + '\n' + str(prova.avanzo()[0]))
print(prova.numeroL(prova.nM, prova.mF))
print(prova.permutazioni(prova.m, prova.nM))
#print(prova.best(16))
#print(prova.somme(0))
#print(prova.avanzo(0))
#print(prova.permutazioni(prova.m, prova.nM)[0])
#c = len(prova.permutazioni(prova.m, prova.nM))
#print(c)
diz = prova.ciclo()
print(diz)
#prova.salvaMisure(diz)
max = prova.massimo(diz)
#min = prova.minimo(diz)
#print("taglio avanzo massimo: " + str(max[0]) + " avanzo massimo: "+ str(max[1]) + "\ntaglio avanzo minimo: " + str(min[0]) + " avanzo minimo: " + str(min[1]))
taglioAvanzo=prova.trovaMisura(2,diz)
#print(taglioAvanzo)
for i in taglioAvanzo["r"]:
    print("\navanzo: "+ str(i) + " taglio: "+ str(taglioAvanzo["t"][taglioAvanzo["r"].index(i)])+"\n")




