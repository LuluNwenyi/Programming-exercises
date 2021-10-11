# Temperature conversion
'''
    If the user enters 1, ask the user to "Enter a celsius value:". 
    Else, ask the user to "Enter a Fahrenheit value:".
'''

selection = "1. Celsius to Farenheit" + "\n" + "2. Farenheit to Celsius" + "\n"
print (selection + "Enter an option: ")

selected = input()

if selected == "1":
    print("Enter a celsius value: ")
    celsius = input()
    farenheit = (float(celsius) * 9/5) + 32
    print("The farenheit value is: " + str(farenheit))

elif selected == "2":
    print("Enter a farenheit value: ")
    farenheit = input()
    celsius = (float(farenheit) - 32) * 5/9
    print("The celsius value is: " + str(celsius))
    
else:
    print("Please enter a valid option")
