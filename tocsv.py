
def text2csv(screenname):
    #print(screenname)
    t=""
    for s in screenname:
       if(s!=',' and s!='\n'):
           t=t+s
    print(t)

    data_file =open(r'C:\\Users\\HASHIM MUHAMMED\\Downloads\\Xcheck-master\\Xcheck-master\\FakeNews\\fakenewsFE\\data.csv','w+')
    
    data_file.write('text, \n'+t+',')
