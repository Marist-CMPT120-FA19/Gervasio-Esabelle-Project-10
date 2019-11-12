#Esabelle Gervasio
def censor(stringlist, censoredstring):
    for j in censoredstring():
        cesnoredstring.split()
    for i in range(len(stringlist)):
            censor="*"*len(j)
            stringlist[i]=stringlist[i].replace(j, censor)
    return stringlist

def main ():
    file = input("Please enter the name of the file you want censored. ")
    censoredfile = input("Please enter the name of the file with words to be censored. ")

    outfilewrite = input("Please enter the name of the file to write to. ")
    outfile = open(outfilewrite, 'w')
    
    infile = open(file,'r')
    original=infile.readlines()
    infile2 = open(censoredfile,'r')
    censoredlist=infile2.read()
    
    newcensor=censor(original, censoredlist)
    outfile.writelines(newcensor)
    print("File printed to", outfilewrite)
    
    infile.close()
    censoredfile.close()
    outfile.close()
main()
