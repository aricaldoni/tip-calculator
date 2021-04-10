#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

# Welcome message
print("Welcome to the tip calculator.")

# prompts
bill = float(input("What is the total bill?: "))
tip = int(input("What percentage tip are you giving? 10, 12 or 15?: "))
people = float(input("How many people are spliting the bill?: "))

# Math
bill_with_tip = tip / 100 * bill + bill
result = bill_with_tip / people
#Round the bill
final = "{:.2f}".format(result)

# Finale
print(f"Each person should pay ${final}")