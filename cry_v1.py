def loopkey(key):
    while True:
        for i in key:
            yield i

def cry(conf_path,origin_path,wikisqr,key):
    origin=open(origin_path).read()
    name=origin_path.split('\\')[-1]        #with alternative part
    code=''
    keygetter=loopkey(key)
    for c in origin:
        key_unit=next(keygetter)
        code+=chr(wikisqr[ord(key_unit)][ord(c)])
    tar_folder=open(conf_path).readlines()[2].strip()
    tar=open(tar_folder+'\\'+name,'w')
    print(code,file=tar)
    tar.close()
    return True

def cry_sqr(wikisqr,key):
    keygetter=loopkey(key)
    new=[]
    for line in wikisqr:
        temp=[]
        for col in line:
            ky=ord(next(keygetter))
            temp.append(ky+col)
        new.append(temp)
    return new

def decry(conf_path,code_path,wikisqr,key):
    code=open(code_path).read()
    name=code_path.split('\\')[-1]      #with alternative part
    origin=''
    keygetter=loopkey(key)
    for c in code:
        key_unit=next(keygetter)
        origin+=chr(wikisqr[ord(key_unit)].index(ord(c)))        #for dever: check 'find'!!!
    tar_folder=open(conf_path).readlines()[3].strip()
    tar=open(tar_folder+'\\'+name,'w')
    print(origin,file=tar)
    tar.close()
    return True

def decry_sqr(wikisqr,key):
    keygetter=loopkey(key)
    new=[]
    for line in wikisqr:
        temp=[]
        for col in line:
            key=ord(next(keygetter))
            temp.append(col-key)
        new.append(temp)
    return new

