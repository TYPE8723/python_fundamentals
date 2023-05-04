with open('readsrc.txt','r') as src:
    with open('destinaton.txt','w') as dest:
        for line in src:
            dest.write(line)
            #data = src.read()
            #print(data)
            data = src.readline()
            print(data)
            #data = src.readlines()
            #print(data)
src.close()
#->https://phoenixnap.com/kb/file-handling-in-python