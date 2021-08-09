import cmath
import math
#math.degrees(math.atan(1.18))
#x = math.sin(math.radians(y))
#print (cmath.polar(2 + 3j

def cal_complex(z,y):
    a = z*(math.cos(math.radians(y)))
    b = z*(math.sin(math.radians(y)))
    comp = complex(a,b)
    return comp

def cal_complexconj(z,y):
    a = z*(math.cos(math.radians(y)))
    b = z*(math.sin(math.radians(y)))
    comp = complex(a,b)
    return comp.conjugate()

def calculate_polar(z):
    a = z.real
    b = z.imag
    r = abs(z)
    return ((a**2+b**2)**0.5, math.degrees(math.acos(a/r) if r != 0 else 0))

def mod(z):
    a = z.real
    b = z.imag
    r = abs(z)
    return ((a**2+b**2)**0.5)

def cvtdb(z):
    a = 10*math.log(z,10)
    return a

def cvtlog(z):
    a = 10**(z/10)
    return a

taus=0
taul=0
s11 = float(input('Enter the R value for s11'))#0.75
s11angle = float(input('Enter the angle for s11'))#-120
s22 = float(input('Enter the R value for s22'))#0.6
s22angle = float(input('Enter the angle or s22'))#-70
s21 = float(input('Enter the R valye for s21'))#2.5
s21angle = float(input('Enter the angle for s21'))#80
s12 = float(input('Enter the R value or s12'))#0
s12angle = float(input('Enter the angle for s12'))#0



delta=(cal_complex(s11,s11angle)*cal_complex(s22,s22angle))-(cal_complex(s12,s12angle)*cal_complex(s21,s21angle))
deltamod = (mod(delta))
G0 = (s21**2)
Gs = (1-mod(taus)**2)**1
Gl = (1-mod(taul)**2)/(mod(1-(cal_complex(s22,s22angle)*taul))**2)
B1 = 1+(mod(s11)**2)-(mod(s22)**2)-deltamod**2
B2 = 1+(mod(s22)**2)-(mod(s11)**2)-deltamod**2
C1 = cal_complex(s11,s11angle)-(delta*cal_complexconj(s22,s22angle))
C2 = cal_complex(s22,s22angle)-(delta*cal_complexconj(s11,s11angle))
tausp =  (B1 + math.sqrt((B1**2)-4*(mod(C1**2))))/(2*C1)
tausn =  (B1 - math.sqrt((B1**2)-4*(mod(C1**2))))/(2*C1)
taulp =  (B2 + math.sqrt((B2**2)-4*(mod(C2**2))))/(2*C2)
tauln =  (B2 - math.sqrt((B2**2)-4*(mod(C2**2))))/(2*C2)
if mod(tausn) > 1:
          taus = tausp
          print('Taus =',calculate_polar(taus))
          Gs = (1-mod(taus)**2)**1
if mod(tausp) > 1:
          taus = tausn
          print('Taus =',calculate_polar(taus))
          Gs = (1-mod(taus)**2)**1
if mod(tauln) > 1:
          taul = taulp
          print('Taul =',calculate_polar(taul))
          Gl = (1-mod(taul)**2)/(mod(1-(cal_complex(s22,s22angle)*taul))**2)
if mod(taulp) > 1:
          taul = tauln
          print('Taul =',calculate_polar(taul))
          Gl = (1-mod(taul)**2)/(mod(1-(cal_complex(s22,s22angle)*taul))**2)

G0 = (s21**2)
          
if s12!=0:
    k = (1+(deltamod**2)-(s11**2)-(s22**2))/(2*mod((cal_complex(s12,s12angle)*cal_complex(s21,s21angle))))          
    print('k =',mod(k))
    if mod(k)>1:
        print('unconditoinally stable')
    if mod(k)<1:
        print('potentionally unstable')
    print('delta =',calculate_polar(delta))
    print('deltamodval',deltamod)
    
if s12==0:
    print('As s12 is 0 Value of K is infinite and amplifier is unconditionally stable')
print('B1 =',calculate_polar(B1))
print('B2 =',calculate_polar(B2))
print('C1 =',calculate_polar(C1))
print('C2 =',calculate_polar(C2))

