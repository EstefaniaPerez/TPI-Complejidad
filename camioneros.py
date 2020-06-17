
def viaje(N, gas):
    din=[]
    dina=[]
    for i in range(0,len(gas)):
        if len(gas)-1 == i:
            if N-gas[i]<0:
                din=din+[10]
                print("hola")
            else:
                 din=din+[N-gas[i]]
                 print("hola")
        else:
            if (N-gas[i] <= 0 or N-gas[i]-gas[i+1] <= 0):
                din=din+[10]
                print("pr "+ str(din))
            else:
                din=din+[N-gas[i]]
                gas[i+1]=gas[i]+gas[i+1]
                print("pr 2"+ str(din))
                print("gas "+ str(gas))
    for i in range(0, len(din)):
        if din[i]==10:
            dina=dina+[i+1]       
    return din

N=10
gas=[2,10,5,3,1,5]
print(viaje(N,gas))


        
