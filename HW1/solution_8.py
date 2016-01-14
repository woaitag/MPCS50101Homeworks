#convert.py
# A program to convert Fahrenheit to Celsius
#by: Tiantian Zhang

def main():
    Fahrenheit=int(input("What is the Fahrenheit temperature?"))
    Celsius = Fahrenheit * 5 / 9 - 160/9
    print("The temperature is", Celsius, "degrees Celsius.")

main()
