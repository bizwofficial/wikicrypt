try:
    import os
    import wikigen
    import cry_v1
except Exception:
    print('Important files missed.\n\nPress ENTER to exit.')
    a=input()
    exit()

os.system('@title Welcome to wikicrypt')
welcome='''
wikicrypt 0.1b Author:President Bridgman

For more details, read README or visit https://www.github.com/bizwofficial/wikicrypt

MENU
1. Encrypt
2. Decrypt
3. Generate wiki-sqr
4. Exit
'''
print(welcome)
sgn=True
choi=['1','2','3','4']
conf_path='.\\config'
while sgn:
    ch=input('wikicrypt>')
    if ch in choi:
        sgn=False

if ch==choi[0]:
    pro='''
    ENCRYPT
    1. Use existed wiki-sqr
    2. Use new wiki-sqr
    '''
    print(pro)
    sgn=True
    choi=['1','2']
    while sgn:
        en=input('encrypt>')
        if en in choi:
            sgn=False
    if en==choi[0]:
        file_path=input('Original File Path>')
        wikisqr_path=input('Wiki-sqr Path>')
        key=input('Set a key>>')
        os.system('@cls')
        print('Processing ...')
        square=wikigen.readsqr(wikisqr_path)
        osqr=cry_v1.decry_sqr(square,key)
        cry_v1.cry(conf_path,file_path,osqr,key)
    else:
        file_path=input('Original File Path>')
        wikisqr_storage_name=input('Name your new wiki-sqr>')
        key=input('Set a key>>')
        os.system('@cls')
        print('Processing ...')
        osqr=wikigen.gen()
        square=cry_v1.cry_sqr(osqr,key)
        wikigen.backup(conf_path,square,wikisqr_storage_name)
        cry_v1.cry(conf_path,file_path,osqr,key)
elif ch==choi[1]:
    file_path=input('Encrypted File Path>')
    wikisqr_path=input('Wiki-sqr Path>')
    key=input('Enter your key>>')
    os.system('@cls')
    print('Processing ...')
    square=wikigen.readsqr(wikisqr_path)
    osqr=cry_v1.decry_sqr(square,key)
    cry_v1.decry(conf_path,file_path,osqr,key)
elif ch==choi[2]:
    wikisqr_storage_name=input('Name your new wiki-sqr>')
    key=input('Enter your key>>')
    os.system('@cls')
    print('Processing ...')
    osqr=wikigen.gen()
    square=cry_v1.cry_sqr(osqr,key)
    wikigen.backup(conf_path,square,wikisqr_storage_name)
else:
    exit()
print('Succeeded.')
a=input()
