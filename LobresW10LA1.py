LobresFlavor=input("Enter Pizza Flavor (Hawaiian/Pepperoni/Cheese): ").lower()

match LobresFlavor:
     case "hawaiian":
         print("You Selected Hawaiian")

         LobresSize = input("Enter Size (Small/Medium/Large):").lower()

         match LobresSize:
             case "small":
                 LobresPrice = 250
             case"medium":
                 LobresPrice = 350
             case "large":
                 LobresPrice = 450

             case _:
                 LobresPrice=0
                 print("Invalid")

     case"pepperoni":
         print("You Selected Pepperoni")

         LobresSize = input("Enter Size (Small/Medium/Large):").lower()

         match LobresSize:
             case "small":
                 LobresPrice = 350
             case "medium":
                 LobresPrice = 550
             case "large":
                 LobresPrice = 1000

             case _:
                 LobresPrice=0
                 print("Invalid")

     case"cheese":
         print("You Selected Cheese")

         LobresSize = input("Enter Size (Small/Medium/Large):").lower()

         match LobresSize:
             case "small":
                 LobresPrice = 200
             case "medium":
                 LobresPrice = 400
             case "large":
                 LobresPrice = 550

             case _:
                 LobresPrice=0
                 print("Invalid")

if LobresPrice > 0:
    print("Pizza Price:" , LobresPrice)