




if __name__ == "__main__":
    dirFichero = 'agaricus-lepiota.data'
    with open(dirFichero, 'r') as reader:
        for line in reader:
            for elemento in line.split(","):
                print elemento
                