from lxml import etree
import difflib
import os
import math

def compTitle(stra, strb):
    tab1 = stra.lower()
    tab2 = strb.lower()
    if len(tab1) <= len(tab2):
        tab1 = tab1.split(" ")
        tab2 = tab2.split(" ")
    else:
        tab = tab2
        tab2 = tab1.split(" ")
        tab1 = tab.split(" ")

    x = 0
    poid = 0
    for i in tab1:
        if any(char.isdigit() for char in i):
            p=10
        else:
            p=1
        poid+=p
        for j in tab2:
            seq = difflib.SequenceMatcher(a=i, b=j)
            c = seq.ratio() * 100
            if c>80:
                x=x+p
    print (x,'\n', poid,'\n', x*100/poid)

def compPrice(priceHIGH,priceLOW):
    if priceLOW > priceHIGH:
        a = priceHIGH
        priceHIGH = priceLOW
        priceLOW = a
    diff = float((1-((priceHIGH-priceLOW)/priceHIGH))*100)
    print (diff)

def compEtat(etat1,site1,etat2,site2):
    # list_status[0] ==> eBay
    # list_status[1] ==> Priceminister
    # list_status[2] ==> cdiscount
    list_status = [["Neuf", "Reconditionné par le fabricant", "Reconditionné par le vendeur", "Occasion", "Pour pièces détachées/ne fonctionne pas"], ["Neuf", "Comme Neuf", "Très Bon Etat", "Bon Etat", "Etat Correct", "Hors Service"], ["Produit Neuf", "Reconditionné", "Comme neuf","Très Bon Etat", "Bon Etat", "Etat correct"]]
    etat1 = float((len(list_status[site1])-list_status[site1].index(etat1))/len(list_status[site1]))
    etat2 = float((len(list_status[site2])-list_status[site2].index(etat2))/len(list_status[site2]))
    diff_etat = float((1-math.fabs(etat1-etat2))*100)
    return diff_etat


print(compEtat("Pour pièces détachées/ne fonctionne pas", 0, "Hors Service", 1))



b = []
key_words = os.listdir("Big_Data")
print (key_words)

for i in key_words:
    if '_' in i:
        a = int(i.index('_'))
        c = i[:a]
        if not c in b:
            b.append(c)
        print(b)
sites = ['_CD.qaz','_PM.qaz','_EBAY.qaz']
for i in b:
    for j in range(len(sites)):
        for h in range(len(sites)-j-1):
            h += j+1
            print(i + sites[j],    "ET"    ,i + sites[h]) #i et j sites compares
            tree = etree.parse("Big_Data/"+ i + sites[j])
            b = tree.xpath("/prods/prod/Name")
            d = tree.xpath("/prods/prod/price/price_seller")
            f = tree.xpath("/prods/prod/Etats_Produit")
            tree = etree.parse("Big_Data/"+ i + sites[h])
            c = tree.xpath("/prods/prod/Name")
            e = tree.xpath("/prods/prod/price/price_seller")
            g = tree.xpath("/prods/prod/Etats_Produit")


            for proda in b:
                for prodb in c:
                    print (proda.text, '    ET    ', prodb.text)
                    compTitle(proda.text, prodb.text)


            for prixa in d:
                for prixb in e:
                    try:
                        compPrice(float(prixa.text), float(prixb.text))
                    except:
                        print("error")
                    print (prixa.text, '    ET    ', prixb.text)


            for etatA in f:
                for etatB in g:
                    q = ''
                    w = ''
                    try:
                        if sites[j] == '_EBAY.qaz':
                            q = 0
                        if sites[j] == '_PM.qaz':
                            q = 1
                        if sites[j] == '_CD.qaz':
                            q = 2
                        if sites[h] == '_EBAY.qaz':
                            w = 0
                        if sites[h] == '_PM.qaz':
                            w = 1
                        if sites[h] == '_CD.qaz':
                            w = 2
                    except:
                        print("error")
                    print (etatA.text,q, '    ET    ', etatB.text,w)
                    try:
                        print(compEtat(etatA.text, q, etatB.text, w))
                    except:
                        print("error")
