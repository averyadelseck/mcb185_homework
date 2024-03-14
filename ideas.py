import dogma 

prot = 'IIIIIIIIIIIIICLFCMKRNRKNRKIMRQSFSYVYIMRNRNRNRNRNRNNRNRNRNRNRNNRNRNRNRNRNNRNRNRNRNRNKNRKRN'

def tmfinder(prot):
    spcan = []
    finprot = []  
    sp = prot[:30]
    if 'P' in prot:
        return 'Proline found'
    for i in range(len(sp) - 8 + 1):
        ssp = sp[i:i+8]
        avhb = dogma.avghydrobit(ssp)
        print(i, avhb)
        if avhb >= 2.5: 
            spcan.append(ssp) 
            #ask later if there is a way to 'continue' but to just leave the loop previous, like break or somthing else similar

    for candidate in spcan:
        tr = prot[30:]
        for j in range(len(tr) - 11 + 1):  
            tm_region = tr[j:j+11]
            print(tm_region)
            avhb = dogma.avghydrobit(tm_region)
            print(j, avhb) 
            if avhb >= 2.0: 
                finprot.append(prot) 
                

    return finprot

print(tmfinder(prot))
