import random

class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number  # Initializing the account_number
        self.balance = balance  # Initializing the account_balance
        self.account_type = account_type  # Initializing the account_type_(Personal/Business)

    def deposit(self, amount):
        self.balance += amount  # Update balance with deposit
        return self.balance 

    def withdraw(self, amount):
        if amount <= self.balance: # Check balance and withdraw if sufficient, return new balance.
            self.balance -= amount  
            return self.balance  
        else:
            return "Insufficient funds"  # Insufficient balance for transaction

class PersonalAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance, "Personal")  # Creating Personal_Account

class BusinessAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance, "Business")  # Initializing Business_account type

class Bank:
    def __init__(self):
        self.accounts = {}  # Creating an empty_dict to store accounts.

    def create_account(self, account_type):
        account_number = random.randint(10000, 99999)  # Generate a random account_number
        balance = 0  # Set initial = 0
        if account_type.lower() == "personal":
            account = PersonalAccount(account_number, balance)  # Creating a Personal_account_object
        elif account_type.lower() == "business":
            account = BusinessAccount(account_number, balance)  # Creating a Business_account_object
        else:
            return "Invalid account type"  #Return an error message for invalid_account type
        
        with open("accounts.txt", "a") as file:
            file.write(f"{account_number},{account_type},{balance}\n")  # Appending account_info to the file
        
        self.accounts[account_number] = account  # Adding the account to the accounts_dict
        return account_number  # return the generated account_number

    def login(self, account_number):
        with open("accounts.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if int(data[0]) == account_number:
                    account_type = data[1]
                    balance = float(data[2])
                    if account_type.lower() == "personal":
                        return PersonalAccount(account_number, balance)  # Return a Personal_account_object
                    elif account_type.lower() == "business":
                        return BusinessAccount(account_number, balance)  # Return a Business_account_object
                    else:
                        return None  # Return None for unknown_account_types
        return None  # Return None if the account number is not found

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].deposit(amount)  # Allocate amount to account
        else:
            return "Account not found"  # Return_Error: Account not found

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)  # Withdraw_amount from the account
        else:
            return "Account not found"  # Returning Error if account is not found

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]  # Remove the account from the dict
            with open("accounts.txt", "r") as file:
                lines = file.readlines()  # Read all lines from the file
            with open("accounts.txt", "w") as file:
                for line in lines:
                    if line.split(",")[0] != str(account_number):
                        file.write(line)  # Filter file (for active accounts)
            return "Account deleted"  # Return success message
        else:
            return "Account not found"  # Return error if account is not found

def main():
    bank = Bank()  # Create a Bank object
    while True:
        print("\n1. Open Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            account_type = input("Enter account type (Personal/Business): ")
            account_number = bank.create_account(account_type)  # Create a new account
            print(f"Account created successfully with number: {account_number}")
        elif choice == "2":
            account_number = int(input("Enter account number: "))
            account = bank.login(account_number)  # Access into existing account
            if account:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Delete Account")
                    print("4. Logout")
                    operation = input("Enter operation choice: ")
                    if operation == "1":
                        amount = float(input("Enter deposit amount: "))
                        print(f"New balance: {bank.deposit(account_number, amount)}")
                    elif operation == "2":
                        amount = float(input("Enter withdrawal amount: "))
                        print(f"New balance: {bank.withdraw(account_number, amount)}")
                    elif operation == "3":
                        print(bank.delete_account(account_number))  # Delete the account
                        break
                    elif operation == "4":
                        break
                    else:
                        print("Invalid operation choice.")
            else:
                print("Invalid account number.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
