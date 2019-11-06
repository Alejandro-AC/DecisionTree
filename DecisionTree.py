
import pprint




if __name__ == "__main__":
    dirFichero = 'data/agaricus-lepiota.data'
    with open(dirFichero, 'r') as reader:
        lista= []
        
        for line in reader:
            listaux=[] 
            for elemento in line.replace("\n","").split(","):
                listaux.append(elemento)    
            lista.append(listaux)        
        pprint.pprint(lista[8900][0])