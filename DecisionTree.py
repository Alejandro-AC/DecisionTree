
import pprint






if __name__ == "__main__":
    dirFichero = 'data/agaricus-lepiota.data'
    with open(dirFichero, 'r') as reader:
        lista= []
        i=0
        listaEntropia=[]
        for y in range(24):
            listaEntropia.append(0)
            
        
        for line in reader:
            listaux=[] 
            for elemento in line.replace("\n","").split(","):
                listaux.append(elemento)
                
            lista.append(listaux)        
        #pprint.pprint(lista[8900][0])
        for elemento in lista:
            if elemento[1]=='b':
                if elemento[0]=='p':
                    listaEntropia[0]=listaEntropia[0]+1
                else:
                    listaEntropia[1]=listaEntropia[1]+1
                    
        print(listaEntropia[0])
        print(listaEntropia[1])