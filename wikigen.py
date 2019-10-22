import random

def readsqr(path):
    wikisqr=[]
    for line in open(path):
        wikisqr.append([int(i) for i in line.rstrip().split(',')])
    return wikisqr


def gen():
    wikisqr=[]
    prime=[[i for i in range(0,128)] for _ in range(128)]
    for j in range(128):
        random.shuffle(prime[j])
        wikisqr.append(prime[j])
    print(wikisqr)
    return wikisqr

def backup(conf_path,wikisqr,name="default:"):
    path=open(conf_path).readlines()[1].rstrip()
    tar=open(path+'\\'+name,'w')
    for i in range(0,128):
        output=''
        for j in range(0,128):
            output+=','+str(wikisqr[i][j])
        print(output[1:],file=tar)
    tar.close()
    return True
