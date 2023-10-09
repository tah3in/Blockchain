import hashlib as hasher

# contains rows
merkel=[]

def merkel_tree(data,x="notclear",one=False):
    global merkel
    #clear merkel list jast when call of major blockchain this function
    if x=='clear':
        merkel=[]
    #append one row to one row
    merkel.append(data) 
    data_out=[]
    #counter
    a=-1
    #hash(user entered Trasactions)
    if one==True:
        lists=[]
        for i in data:
            lists.append(hasher.sha256(i.encode('utf-8')).hexdigest())
        data=lists
        merkel.append(data)
        one=False
    #hash( hash user entered Trasactions)
    for i in data:
        a+=1
        if a%2!=0:
            data_out.append(hasher.sha256(F"{data[a-1]}".encode('utf-8')+F"{data[a]}".encode('utf-8')).hexdigest())

        elif a==len(data)-1:
            data_out.append(hasher.sha256(F"{data[a]}".encode('utf-8')+F"{data[a]}".encode('utf-8')).hexdigest())
    
    #run when reached root
    if len(data_out)>1:
        #recursive function for hash rows
        merkel_tree(data_out,x='notclear')
        # merkel=[]
    else:
        merkel.append(data_out)
    if x=='clear':
        test=merkel
        merkel=[]
    else:
        test=merkel
    return test
    


def rootmerkel(data):
    return merkel_tree(data)[-1][0]
