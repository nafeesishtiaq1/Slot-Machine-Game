MAX_LINES = 3

def deposit():
  while True:
    amount = input("What would you like to deposite? $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break;
      else:
        print("Amount must be greater than 0.")
    else:
      print("Please enter a number.")

  return amount

def get_number_of_lines():

def main():
    balance = deposit()

main()