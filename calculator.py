import math

# Call this method to get resistance value mapped to frequency value 
def iterate_freq():
     res=list(range(100,10000,100))
     f=freq(res)
     
     print("R(ohm)  F(kHz)")
     for i in range(len(res)):
          print(f'{res[i]}    {f[i]}')

def freq(r):
     fr=[]
     c=0.01e-6
     b=27/(27+100)
     
     fb=math.log((1+b)/(1-b))
     for i in range(len(r)):
          fr.append((1//(2*r[i]*c*fb))/1000)
     return fr

# Call this method to get frequency value mapped to resistance value 
def iterate_res():
     freq=list(range(100,10000,100))
     r=res(freq)
     
     print("F(kHz)  R(ohm)")
     for i in range(len(r)):
          print(f'{freq[i]}    {r[i]}')

def res(f):
     rs=[]
     c=0.01e-6
     b=27/(27+100)
     
     fb=math.log((1+b)/(1-b))

     for i in range(len(f)):
          rs.append((1//(2*f[i]*c*fb))/1000)
     return rs
