#Create a program that ask user to input name and age.
# Print error message when the input is not valid. Set your own definition of valid name and valid age.

try:
     var1 = (input("Please input name "))
        
except:
    print("Try again")  
    
while True:    
    try:   
        var2 = int(input("Please input age "))
        break
    except:
        print("Try again")       
    
data = []
data.append(("name", var1))
data.append(("age - {var2}"))

print(data)



# Store all the collected information into array. After every input, ask the user if want to input another entry.
# When “Yes”, ask the user again for input. Do it until the user respond “No”. When the user responded “No”, display the name and age of the oldest person.
# Use the array in checking who is the oldest.