import time
import random
import sys
import copy
sys.setrecursionlimit(3000)

f=open("teste_sortari")
nr_teste=int(f.readline())
d={1:"Mergesort",2:"Bubblesort",3:"Countingsort",4:"Quicksort pivot mediana",5:"Quicksort pivot dreapta",6:"Radixsort baza 2",7:"Radixsort baza 10"}
for k in range(nr_teste):
    l=[int(x) for x in f.readline().split()]
    N = l[0]
    MAXI = l[1]
    print(f'Test {k + 1} (N={N},MAXI={MAXI}):')
    L=[]
    L_initial=[]
    for j in range(N):
        x=random.randint(1,MAXI)
        L.append(x)
        L_initial.append(x)
    start=time.time()
    L_sortat=sorted(L)
    stop=time.time()
    print("Sortarea nativa limbajului:",stop-start)
    for i in d.keys():
        if i==1:

            start = time.time()
            def interclasare(t, st, mij, dr):
                i = st
                j = mij+1
                aux = []  #lista cu elementele interclasate
                while i <= mij and j <= dr:
                    if t[i] <= t[j]:
                        aux.append(t[i])
                        i += 1
                    else:
                        aux.append(t[j])
                        j += 1


                aux.extend(t[i:mij+1])  #se adauga restul elementelor care nu au cu ce fi comparate
                aux.extend(t[j:dr+1])
                t[st:dr+1] = aux[:]


            def mergesort(t, st, dr): #se imparte lista pe bucati pana se ajunge la liste de lungime 1 apoi se reconstruieste cu ajutorul inteclasarii
                if st < dr:
                    mij = (dr+st) // 2
                    mergesort(t, st, mij)
                    mergesort(t, mij+1, dr)
                    interclasare(t, st, mij, dr)

            mergesort(L,0,len(L)-1)
            stop=time.time()
            print(f'{d[i]}:',stop-start,end='-')
            if L==L_sortat:
                print("Algoritm corect")
            else:
                print("Algoritm gresit")


        elif i==2:
            L =copy.deepcopy(L_initial)
            start = time.time()
            def bubble(n,L):  #algoritmul de bubble sort se bazeaza pe compararea si interschimbarea elementelor vecine

                 for i in range(n):
                    ok = 0
                     #contor ce verifica daca in fiecare parcurgere exista interschimbari
                    for j in range(n-i-1): #parcurgem pana la n-i-1, deoarece dupa prima parcurgere cel mai mare numar va fi la final ,dupa a doua, al doilea cel mai mare numar va fi penultimul s.a.m.d.,iar scaderea cu minus 1 e pentru ca nu avem cu ce compare ultimul element
                        if L[j]>L[j+1]:
                            L[j],L[j+1]=L[j+1],L[j]
                            ok+=1
                    if ok==0:
                           return L
                 return L

            if N>10**5:
                print(f'{d[i]}:ESEC(N e prea mare)')
            else:
                bubble(len(L),L)
                stop=time.time()
                print(f'{d[i]}:',stop-start,end=' ')
                if L==L_sortat:
                    print("Algoritm corect")
                else:
                    print("Algoritm gresit")

        elif i == 3:
            L = copy.deepcopy(L_initial)
            start = time.time()
            def counting(n,L):
                 maxi=max(L)
                 ap=[0 for i in range(maxi+1)] #lista ce retine frecventa elementelor din lista
                 for i in range(maxi+1):
                    ap[i]=L.count(i)

                 r=[]  #lista in care construim sirul, sortat
                 for i in range(maxi+1):
                    while ap[i]!=0: #adaugam in r elementele care  apar cel putin o data
                        r.append(i)
                        ap[i]-=1
                 return r
            if MAXI>10**5 and N>10**4:
                print(f'{d[i]}:ESEC(MAXI e prea mare)')
            else:
                L=counting(len(L),L)
                stop=time.time()
                print(f'{d[i]}:',stop-start,end="-")
                if L==L_sortat:
                    print("Algoritm corect")
                else:
                     print("Algoritm gresit")




        elif i==4:
            L = copy.deepcopy(L_initial)
            start = time.time()
            def divide(L, st, dr):

                mediana = (dr - 1 - st) // 2
                mediana = mediana + st
                #aducem mediana listei pe pozitia st
                if (L[mediana] - L[dr - 1]) * (L[st] - L[mediana]) >= 0:
                    L[st], L[mediana] = L[mediana], L[st]
                elif (L[dr - 1] - L[mediana]) * (L[st] - L[dr - 1]) >= 0:
                    L[st], L[dr - 1] = L[dr - 1], L[st]
                pivot = L[st]
                i = st + 1 #index elemente mai mari ca pivotul
                for j in range(st, dr):
                    if L[j]<pivot:
                        L[i], L[j] = L[j], L[i]
                        i += 1
                L[st], L[i - 1] = L[i - 1], L[st]
                return i - 1  #pozitia la care se afla pivotul


            def quicksort(L, st, dr):
                 if st<dr:
                    index = divide(L, st, dr)

                    quicksort(L, st, index)

                    quicksort(L, index + 1, dr)


            if N>37000:  #dupa testele mele, 37000 este cel mai mare numar la care nu se opreste programul
                print(f'{d[i]}: ESEC(stack overflow)')
            else:
                st,dr=0,len(L)

                quicksort(L,st,dr)

                stop=time.time()
                print(f'{d[i]}:',stop-start,end="-")
                if L==L_sortat:
                    print("Algoritm corect")
                else:
                    print("Algoritm gresit")
        elif i==5:
            L = copy.deepcopy(L_initial)
            start = time.time()
            def divide2(L, st, dr):
                pivot = L[dr] #alegem ca pivot ultimul element
                i = st - 1  #index pt elem<pivotul
                # se incepe de st-1 pentru ca inainte a face interschimbarea se creste cu 1, asa ca i va apartine [st,dr]
                for j in range(st, dr):
                    if L[j] < pivot: #daca un element este mai mic ca pivotul ales,
                        i += 1
                        L[i], L[j] = L[j], L[i]#interschimba un element <pivotul cu L[i](urmatorul  element din lista >pivot)
                L[i + 1], L[dr] = L[dr], L[i + 1]
                return i + 1 #pozitia la care se afla pivotul


            def quicksort2(L, st, dr):
                if st < dr:
                    pivot = divide2(L, st, dr)
                    quicksort2(L, st, pivot - 1)
                    quicksort2(L, pivot + 1, dr)


            if N>37000:
                print(f'{d[i]}:ESEC(stack overflow)')
            else:
                st, dr = 0, len(L) -1
                quicksort2(L, st, dr)
                stop = time.time()
                print(f'{d[i]}:', stop - start, end="-")

                if L == L_sortat:
                    print("Algoritm corect")
                else:
                    print("Algoritm gresit")

        elif i==6:
            L = copy.deepcopy(L_initial)
            start = time.time()
            def count2(L, ok):
                n = len(L)
                rez = [0] * n  # vector final
                fr = [0] * 2  # vector de frecventa
                for i in range(n):
                     # indexul
                    j = (L[i] >> ok) & 1 #ultimul bit al nr curent
                    fr[int(j)] += 1

                for i in range(1, 2):
                    fr[i] += fr[i - 1] #stabilim de la ce pozitie incepem fiecare 'bucket'

                for i in range(n - 1, -1, -1): #incepem de la sfarsit pt a reface lista cu elementele sortate
                    j = (L[i] >> ok) & 1
                    rez[fr[int(j)] - 1] = L[i]
                    fr[int(j)] -= 1
                for i in range(n):
                    L[i] = rez[i]



            def radix2(L):
                maxi = len(str(bin(max(L)))) - 2  #nr maxim de biti
                ok = 0  #contor pentru shiftarea bitilor
                while maxi >= 0:
                    count2(L, ok)
                    maxi -= 1
                    ok += 1
            radix2(L)
            stop=time.time()
            print(f'{d[i]}:',stop-start,end="-")

            if L==L_sortat:
                print("Algoritm corect")
            else:
                print("Algoritm gresit")


        elif i==7:
            #aceeasi implementare de RadixSort dar cu baza 10
            L = copy.deepcopy(L_initial)
            start = time.time()
            def count(L,exp):
                n=len(L)
                rez=[0]*n  #vector final
                fr=[0]*10  #vector de frecventa
                for i in range(n):
                    j=L[i]/exp  #indexul
                    fr[int(j%10)]+=1
                for i in range(1,10):
                    fr[i]+=fr[i-1]
                for i in range(n-1,-1,-1):
                    j=L[i]/exp
                    rez[fr[int(j%10)]-1]=L[i]
                    fr[int(j%10)]-=1
                for i in range(n):
                    L[i]=rez[i]


            def radix(L):
                exp=1
                maxi=max(L)
                while maxi/exp>0:
                    count(L,exp)
                    exp*=10
            if N>10**7:
                print(f'{d[i]}:ESEC(timp de executie ridicat)')
            else:
                radix(L)
                stop=time.time()
                print(f'{d[i]}:',stop-start,end="-")
                if L==L_sortat:
                    print("Algoritm corect")
                else:
                    print("Algoritm gresit")