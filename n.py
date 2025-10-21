cadena=input("dame la cadena de caracteres entre comillas por favor")
acum=0
dicc={}
for c in cadena:
    if c in dicc:
       dicc[c]+=1
    else:
        dicc[c]=1
    
      
print (dicc)    
