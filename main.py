MAX_LINES=5 
MAX_BET=10000
MIN_BET=10
def deposit ():
    while True:
        amount=input("What would you like to deposit? ksh")
        if amount.isdigit():
            amount=int(amount)
            if amount> 0:
              break
            else:
                print("Amount should be more than 0")
        else: print ("Error ! Amount should be in digits") 
    return amount
deposit()  
def get_number_of_lines(): 
    while True:
        lines=input("how many times would you like to bet (1-"+str (MAX_LINES)+")?")
        if lines.isdigit():
            lines=int(lines)
            if 1 <=lines<=MAX_LINES:
              break
            else:
                print("a valid amount of times ")
        else: print ("Error ! Amount should be in digits") 
    return lines  
    deposit()  
def get_bet(): 
    while True:
        amount=input("How much would you like to bet? ksh")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount <= MAX_BET:
              break
            else:
                print(f"Amount must be between {MIN_BET}-{MAX_BET}")
        else: print ("Error ! Amount should be in digits") 
    return amount
def main():
      balance=deposit()
      lines = get_number_of_lines()
      print(balance,lines)
      bet=get_bet()
      total_bet=lines*bet
      print(f"You are betting {bet} on {lines} lines youre total bet is equal :ksh{total_bet}")
main()