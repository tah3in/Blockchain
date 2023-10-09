import hashlib as hasher
from merkel import rootmerkel , merkel_tree
from time import time , ctime


gensis_block=True
count_block=-1
Blocks=[]


def main():
    Data=input("Enter list Transactions into this form\t(TX,TX2,TX3,...) :\n")
    Block(convertlist(Data))

def Block(data):

    dict_block={'header:':header(data),"body:":body(data)}
    Blocks.append(dict_block)
    result=input("if you add next Block Enter Yes otherwise No :\n").lower()

    if (result=="yes"):
        main()
    else:
        print(Blocks)
        return
    
    
def header(data):
    global count_block
    global gensis_block
    count_block+=1

    if gensis_block==True:
        
        header_block={
        'rootmerkel':hasher.sha256(F"{'empty'}".encode('utf-8')).hexdigest(),
        'index': 0 ,
        'timestamp':ctime(time()),
        'pervious Blockhash' : hasher.sha256(F"{'empty'}".encode('utf-8')).hexdigest() ,
                }
        gensis_block=False
        return(header_block)
        
    else:
        header_block={
        'rootmerkel':rootmerkel(data),
        'index':count_block ,
        'timestamp':ctime(time()),
        'pervious Blockhash' : hasher.sha256(F"{Blocks[-1]}".encode('utf-8')).hexdigest() ,
                    }
        return(header_block)

def body(data):
    one=True
    return(merkel_tree(data,"clear",one))

def convertlist(text):
    list_tx=[]
    if ',' in text:
        list_tx=text.split(',')
        return(list_tx)
    else:
        raise ValueError()

if __name__ == '__main__':
    main()