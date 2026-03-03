## Expense tracker project

expenses = [] ##list of expenses in form of dictionary

print("🎍💸💸💸  Welcome to Expense Tracker : 💸💸💸🎍")

while True:
    print("\n📋📋📋 MENU 📋📋📋")  
    print("\n ➕ 1.Add Expense")
    print("\n 🕶️ 2.View all expenses")
    print("\n 💯 3.View Total Expenses")
    print("\n 🚪 4.Exit")

    choice = int(input("\n 🔢 Please Enter your choice: \n"))

## Add Expense Code
    if(choice==1):
        date = input("\n 📅 Enter date: \n")
        category = input("\n 📊 Please enter category of expense(e.g. food, travel etc.) : \n")
        description = input("\n 📇 Enter more details or description: \n")
        amount = float(input("\n 🤑 Enter the Amount : \n"))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("\n ✅✅✅Expenses added successfully!! ✅✅✅")


## View all expenses code
    elif(choice==2):
        if(len(expenses)==0):
            print("\n ⛔ No expense added, Go and do some shopping!!")
        else:
            print("\n 💰💰 Your All Expenses: 💰💰 ")
            count = 1
            for eachexp in expenses:
                print(f"Expense {count} -> {eachexp["date"]}, {eachexp["category"]}, {eachexp["description"]}, {eachexp["amount"]}")
                count=count+1




## View Total Spendings/Expenses code
    elif (choice==3):
        total = 0
        for eachexp in expenses:
            total = total + eachexp["amount"]

        print("\n 💯💯 Total Expense = ", total)

## EXIT code
    elif(choice==4):
        print("\n 🤟🤟 Thanks for using Expense Tracker!! 🤟🤟 ")
        break

    else:
        print("\n 🦘🦘 Invalid Choice!! 🦘🦘")




   



