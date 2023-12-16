q = print("What is the capital of India?")
options = ["UP", "MP", "Delhi", "Mumbai"]
print(options)
q1 = input("").lower()  # Convert the input to lowercase

money = 0

if q1 == "delhi":
    print("Correct answer!!")
    money += 10000
    print(money)
else:
    print("ouufff!!")
    money -= 1000
    print(money)
    print("Apka safar yahi khatam hua")
    exit()

print("Agla sawaal")
qq = input("Who is the Prime Minister of India?")
options = ["Pappu", "Narendra Modi", "Indira Gandhi", "Amit Shah"]
q2 = input("").lower()  # Convert the input to lowercase

if q2 == "narendra modi" or q2 == "modi":
    print("Correct answer!!")
    money += 10000
    print(money)
else:
    print("oufff!!")
    money -= 1000
    print(money)
    print("Apka safar yahi khatam hua")
    exit()
