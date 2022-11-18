def fahrenheit(deg):
  result = (deg * (9 / 5)) + 32
  print(f"{deg}°C fait {result}°F")
def celcius(deg):
  result = (deg - 32) * (5 / 9)
  print(f"{deg}°F fait {result}°C")
    
while True:
  while True:
    choice = input("tapez c pour convertir en celcius, f pour fareneit")
    choice = choice.lower()
    if choice == "f":
      deg = input("Entrez une température en celcius : ")
      deg = float(deg)
      fahrenheit(deg)
      break
    elif choice == "c":
      deg = input("Entrez une température en fahrenheit : ")
      deg = float(deg)
      celcius(deg)
      break
    else:
      print("tapez c ou f")
  restart = input("tapez quit pour quitter ")
  restart.lower()
  if restart == "quit":
    break
  
  
    
      
   