import itertools
import math
from sympy.utilities.iterables import multiset_permutations
from collections import OrderedDict
from collections import OrderedDict

class Calcolo:
    m = []
    nM = []
    mF = 0

    def setMisure(self, misure, numeroMisure, misuraFissa):  #mi permettere  di settare il valore quantita anche se privato
        self.m = misure
        self.nM = numeroMisure
        self.mF = misuraFissa

    def arrayMisure(self, m, nM):
        mT = []
        k = 0
        j=0
        for i in m:
            while k < nM[j]:
                mT.append(i)
                k+=1
            k = 0
            j+=1
        return mT

    def numeroL(self, nM, mF):
        n = math.ceil(sum(self.arrayMisure(self.m, nM))/mF)
        return n

    def permutazioni(self, m, nM):

        p = list(multiset_permutations(self.arrayMisure(m, nM)))
        return p

    def best(self,k):
        b = []
        bf = []
        p = self.permutazioni(self.m, self.nM)[k]
        n = self.numeroL(self.nM, self.mF)
        somma = 0
        best=[]
        for i in p:
            somma += i
            if somma == self.mF and len(b) < n:
                bf.append(i)
                b.append(bf)
                bf = []
                somma = 0
            elif round(somma, 1) < self.mF and len(b) < n:
                bf.append(i)
            elif round(somma, 1) > self.mF and len(b) < n:
                b.append(bf)
                somma = i
                bf = []
                bf.append(i)
            if len(b) == n-1 and p.index(i) == len(p)-1:
                b.append(bf)
            if len(b) == n:
                break
        if len(b) < n:
            return False
        else:
            return b

    def somme(self,k):
        s = []
        for i in self.best(k):
            s.append(round(sum(i),1))
        return s

    def avanzo(self,k):
        r = []
        for i in self.somme(k):
            r.append(round(self.mF-i,1))
        return r

    def ciclo(self):
        pT = self.permutazioni(self.m, self.nM)
        diz = {}
        diz["b"]=[]
        diz["s"]=[]
        diz["r"]=[]
        c = 0
        while c < len(pT):
            if self.best(c) != False:
                diz["b"] += [self.best(c)]
                diz["s"] += [self.somme(c)]
                diz["r"] += [self.avanzo(c)]
            c+=1
        return diz



    def salvaMisure(self,diz):
        with open("misure.txt") as f:
            i=0
            for line in f:
                f.write("tagli: "+str(diz["b"][i]) + " somme: " + str(diz["s"][i]) + " avanzi: " + str(diz["r"][i]+"\n"))
                i+=1

    def trovaMisura(self,misura,diz):
        tagliPossibili={"t":[],"r":[]}
        for i in diz["r"]:
            for j in i:
                if j >= misura and i not in tagliPossibili["r"]:
                    tagliPossibili["r"]+=[i]
                    index=diz["r"].index(i)
                    tagliPossibili["t"] += [diz["b"][index]]
        return tagliPossibili




