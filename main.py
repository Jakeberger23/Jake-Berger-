try:
  grade = int(input("Enter your grade "))
  if(100 >= grade >= 90):
    print("Your Grade is an A")
  if(89 >= grade >= 80):
    print("Your Grade is a B")
  if(79 >= grade >= 70):
    print("Your Grade is a C")
  if(69 >= grade >= 65):
    print("Your Grade is a D")
  if(grade < 65): 
    print("Your Grade is a F ")
except: 
  print("Must be a number") 