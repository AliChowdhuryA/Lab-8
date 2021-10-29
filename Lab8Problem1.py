import time
import math
from datetime import datetime
#Variable declaration
firstName = ' '
lastName = ' '
firstLast = ' '

#

#step1
firstName = input("Input firstName: ")
#step2
lastName = input("Input lastName: ")

#step3
print("Hello", firstName.lower(), lastName.upper())

#step4
print('\n\n')

#step5
firstLast = firstName + " " + lastName
#step 6
print("Sliced firstLast: "+ firstLast.removeprefix(firstName))
#step7
print("Replace: ", firstLast.replace(lastName, lastName+" Wayne Student"))
#step8
print('"Start by doing what\'s necessary; then do what\'s possible; and suddenly you are doing the impossible - Francis of Assisi"')
#step 9
var1 = 0.1
var2 = 1.1
#step 10
addVar = var1+var2
multVar = var1*var2
subVar = var1-var2
divVar = var1/var2
#step11
print(var1,'+',var2,'=',addVar)
varOutput = (str(var1) + " * " + str(var2) + " = " + str(multVar))
print(varOutput)
print(f"{var1} - {var2} = {subVar}")
print("{}/{}={}".format(var1,var2,divVar))

#step 12
sq_root = math.sqrt(multVar)
print("The square root of ", round(multVar,2)," = ", round(sq_root,2))

#step 13
intMonth = datetime.now().strftime("%B")
intDay = datetime.now().day

#step 14
print(f"Today is {intDay} of the month {intMonth}")





time.sleep(2)
