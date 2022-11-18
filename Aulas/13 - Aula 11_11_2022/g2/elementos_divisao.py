dividendo, divisor = input().split()
dividendo, divisor = int(dividendo), int(divisor)

quociente = dividendo // divisor
resto = dividendo % divisor

#print("dividendo -", dividendo)
print("dividendo - {}".format(dividendo))
print("divisor - {}".format(divisor))
print("quociente - {}".format(quociente))
print("resto - {}".format(resto))