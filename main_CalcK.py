#used to calculate K values for a given SENT geoemetry
import math

P = 100 # [N]
a = 30 # [mm]
W = 60 # [mm]
B = 60 # [mm]
Bn = 60
#Bn = W-2*(0.05*B) # [mm]
poisson = 0.3
E = 207000 # [MPa]

tj = [1.197, -2.133, 23.886, -69.051, 100.462, -41.397, -36.137, 51.215, -6.607, -52.322, 18.574, 19.465]
G=0
print("------------------")
#print("exponents: ")
for i, value in enumerate(tj):
    G = G + value * (a/W)**i
    #print(i)

K = P * math.sqrt(math.pi*a) / (math.sqrt(B*Bn)*W )
K = K * G

J = K**2 * (1-poisson**2) / E

print("K [MPa sqrt(mm)] = ", K)
print("J [MPa mm] = ", J)
print("Clamp width [mm] = ", W*4)
print("Daylight [mm] = ", W*10)
print("Total length [mm] = ", W*10 + 2*W*4)
print("Beff [mm] = ", math.sqrt(B*Bn) )