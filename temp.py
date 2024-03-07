
def convert_temp():
    F = float(input("Insert fahrenheit:"))
    C = convert_to_celsius(F)
    K = convert_to_kelvin(C)
    print(f"celsius = {round(C, 4)}")
    print(f"kelvin ={round(K, 4)}")
    
def convert_to_celsius(F):
  C = (5/9) * (F -32)
  return C
    
def convert_to_kelvin(C):
  K = C + 273.15
  return K

convert_temp()