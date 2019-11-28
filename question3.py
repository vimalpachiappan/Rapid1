userINPUT = {"Rick" : 85, "Amit" : 42, "George":53, "Tanya" : 60, "Linda" : 35}
print(userINPUT)

def userTOTAL(userINPUT):
    a = 0
    for i in userINPUT:
        a=a+userINPUT[i]
    return a
print("total paid: ",userTOTAL(userINPUT))
  
