# Temperature Advisor - My First AI program

#Take temperature input from user
temp = float(input("Enter the temperature (°C):"))

# Decision rules (simple AI logic)
if temp < 10:
    print("Advice: It's very cold. wear heavy clothes.")
elif 10 <= temp <= 20:
    print("Advice: It's cool. wear a  jacket.")
elif 21 <= temp <= 30:
    print("Advice: The weather is warm and comfortable.")
else:
    print("Advice: It's hot. Drink water and stay cool.")