# Planetary Weather Classifier
#Precious Molatelo Molepo
#10/03/2026

print("Welcome to the Planetary Weather Classifier") # q(number) represents the question number 
print("-"*45)
q1 = input("Is the atmospheric temperature below 0 degrees celsius? (yes/no):\n")
if q1 == "yes":
 q2 = input("Is wind speed ≥ 40 km/h? (yes/no):\n")
 if q2 == "yes":
  print("Classification: Blizzard")
 else:
   print("Classification: Snow")
else:
 q3 = input("Is humidity high? (yes/no):\n")
 if q3 == "yes":
  q4 = input("Is there lightning observed? (yes/no):\n")
  if q4 == "yes":
   print("Classification: Thunderstorm")
  else:
   print("Classification: Rainy")
 else:
  q5 = input("Is visibility less than 1000 m? (yes/no):\n")
  if q5 == "yes":
   print("Classification: Fog")   
  else:
   q6 = input("Is wind speed >= 40 km/h? (yes/no):\n")
   if q6 == "yes":
    q7 = input("Is dust level high? (yes/no):\n")
    if q7 == "yes":
     print("Classification: Dust Storm")
    else:
     print("Classification: Windy")
   else:
    print("Classification: Clear")    
    
   
  
  