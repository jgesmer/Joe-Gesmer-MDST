import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt


a = [1, 2, 3, 4, 5, 6]

print(a[3:6])

#exerise one

i = 0
bigList = []
for i in range(20):
    bigList.append(i+1)

print (bigList)

#exercise 2
print("Now exercise 2")
evenList = list(range(1,101))

i = 0 
for i in range(100):
    if evenList[i] % 2 == 0:
        print(evenList[i])
#exercise 3

print("now exercise 4")
x = 2
y = 3

def multiplier(x,y):
    return x / y

#exercise 4

print("Now exercise 5")

Input = ("I like milkshakes")
print(Input.upper())

#exercise 6

z = 0 
print("now exercise 7")
fizzBuzzList = list(range(1,31))
for z in range(30):
    if (fizzBuzzList[z] % 3 == 0 and fizzBuzzList[z] % 5 == 0):
        print("fizzbuzz")
    elif (fizzBuzzList[z] % 3 == 0):
        print("fizz")
    elif (fizzBuzzList[z] % 5 == 0):
        print("buzz")
    else:
        print(fizzBuzzList[z])

#exercise 8

print("Now exercise 10")
thisDict = {"Gyro" : 9, "Burger" : 9, "Greek salad" : 8, "Philly Steak" : 10}

#exercise 9

print("Now exercise 10")
df = pd.read_csv("../data/starbucks.csv")
type(df)

print(df[df["calories"] > 400])

#exercise 10

print("Output calories, sugar, and protein of every 40th row")
print(df.iloc["sugar", "calories", "protein"::40])



print("Now exercise 11")

print(df[df["vitamin c"] > df["iron"]])

#exercise 11

print("now exercise 12")


# t = 0
# sum = 0 
# d2f = df["calories"]
# for t in range(244):
#     sum += df["calories"]


print ("The average calories for all drinks is")
print(df["calories"].mean())

#exercise 12

print("Now exercise 13")

print(df["beverage_category"].unique())
print("there are 9 different types of beverages")

#exercise 13

print("Now exercise 14")

# dfCoffee = df.set_index('coffee')
# dfCoffee.head()
# dfCoffee.loc['coffee']
# dfCoffee.loc['coffee', ["calories"]]

#print(df.groupby(['beverage_category'])['coffee','calories'].mean())


# print(plt.hist(df["calories"], bins = 8))

data = pd.read_csv('../data/starbucks.csv')
beverages = data['beverage_category']
calories = data['calories']

bins = ['coffee','classic espresso drinks', 'signature espresso drinks', 'tazo tea drinks', 'shaken iced beverages',
'smoothies', 'frapuccino blended coffee', 'frapuccino light blended coffee', 'frapuccino blended crme']
plt.hist(beverages, bins = bins, edgecolor = 'black', log = True)

plt.title('calories per beverage')
plt.xlabel('beverages')
plt.ylabel('calories')
plt.show()

#df["beverage"].plot.hist(edgecolor = 'black', alpha = 0.8, title = "calories per drink")

    
# calories = data['calories']
# bins2 = [50,100,150,200,250,300,250,400,450,500,550,600]
# plt.hist(calories, bins = bins2, edgecolor = 'black')
# plt.title('calories based on grams of fat')
# plt.xlabel('calories')
# plt.ylabel('grams of fat')
# plt.show()




print("average number of calories per beverage type")

# print("coffee: ")
# print(df.iloc["coffee"].mean())
# print("classic espresso drinks: ")
# print(df.iloc["classic espresso drinks"].mean())
# print("signature espresso drinks: ")
# print(df.iloc["signature espresso drinks"].mean())
# print("tazo tea drinks: ")
# print(df.iloc["tazo tea drinks"].mean())
# print("shacken iced beverages: ")
# print(df.iloc["shacken iced beverages"].mean())
# print("smoothies: ")
# print(df.iloc["smoothies"].mean())
# print("frapuccino blended coffee: ")
# print(df.iloc["frappucino blended coffee"].mean())
# print("frapuccino light blended coffee: ")
# print(df.iloc["frapuccino light blended coffee"].mean())
# print("frappucino light blended crme: ")
# print(df.iloc["frappucino light blended crme"].mean())

print("now exercise 15")

df["caffeine per calories"] = df["caffeine"] / df["calories"]
df.head()




print("now exercise 16")

x = data["calories"]
y = data["total fat"]

plt.scatter(x ,y, s = 50, c = "green", edgecolor = 'black')
plt.title("calories graphed againt total fat of drinks")
plt.xlabel("calories")
plt.ylabel("total fat in grams")
plt.show()

