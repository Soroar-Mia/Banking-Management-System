class Bank:
    account_number_counter=100000
    def __init__(self):
        self.accounts = {}
        self.bank_balance = 0
        self.bank_withdrawal=0
        self.bank_deposit=0
        self.loan_feature = True
        self.total_loan_amount = 0

    @classmethod
    def generate_account_number(self):
        id = self.account_number_counter
        self.account_number_counter += 1
        return id

    def create_account(self,email,password, initial_balance):
        if email not in self.accounts:
            account_number = Bank.generate_account_number()
            self.accounts[account_number] = {'balance':initial_balance,'deposit':0,'withdrawal':0,'loan':0,'transfer':0}
            self.accounts[email] = password
            self.bank_balance += initial_balance
            print(f"Account {account_number} created with an initial balance of {initial_balance}.")
        else:
            print("Account already exists.")

    def deposit(self, account_number,email,password,amount):
        if account_number in self.accounts:
            if self.accounts[email]==password:
                self.accounts[account_number]['balance'] += amount
                self.bank_balance += amount
                self.bank_deposit += amount
                self.accounts[account_number]['deposit'] += amount
                print(f"Deposited {amount} to account {account_number}.")
            else:
                print("Wrang Password.")
        else:
            print("Account does not exist.")

    def withdraw(self, account_number,email,password,amount):
        if account_number in self.accounts:
            if self.accounts[email]==password:
                if self.accounts[account_number]['balance'] >= amount:
                    self.accounts[account_number]['balance'] -= amount
                    self.bank_balance -= amount
                    self.bank_withdrawal +=amount
                    self.accounts[account_number]['withdrawal'] +=amount
                    print(f"Withdrew {amount} from account {account_number}.")
                else:
                    print("Bank is bankrupt. Cannot withdraw.")
            else:
                print("Wrang Password.")
        else:
            print("Account does not exist.")

    def transfer(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            if self.accounts[from_account]['balance'] >= amount:
                self.accounts[from_account]['balance'] -= amount
                self.accounts[from_account]['transfer'] += amount
                self.accounts[to_account]['balance'] += amount
                print(f"Transferred {amount} from account {from_account} to account {to_account}.")
            else:
                print("Bank is bankrupt. Cannot transfer.")
        else:
            print("One or both of the accounts do not exist.")

    def take_loan(self, account_number,email,password):
        if account_number in self.accounts:
            if self.accounts[email]==password:
                if self.loan_feature:
                    total_balance = self.accounts[account_number]['balance']
                    loan_amount = total_balance * 2
                    if loan_amount < self.bank_balance:
                        self.accounts[account_number]['balance'] += loan_amount
                        self.accounts[account_number]['loan'] += loan_amount
                        self.total_loan_amount += loan_amount
                        self.bank_balance -=loan_amount
                        print(f"Loan of {loan_amount} granted to account {account_number}.")
                    else:
                        print("Bank is bankrupt. Cannot Loan.")
                else:
                    print("Loan feature is currently off.")
            else:
                print("Wrang Password.")
        else:
            print("Account does not exist.")



    def check_balance(self, account_number,email,password):
        if account_number in self.accounts:
            if self.accounts[email]==password:
                balances = self.accounts[account_number]['balance']
                print(f"Account {account_number} has a balance of {balances}.")
            else:
                print("Wrang Password.")
        else:
            print("Account does not exist.")
    

    def check_bank_balance(self, account_number,email,password):
        if account_number in self.accounts:
            if self.accounts[email]==password:
                balances = self.bank_balance
                print(f"total available balance of the bank {balances}.")
            else:
                print("Wrang Password.")
        else:
            print("Account does not exist.")
    

    def check_bank_loan_balance(self, account_number,email,password):
        if account_number in self.accounts:
            if self.accounts[email]==password:
                balances = self.total_loan_amount
                print(f"total loan amount of the bank {balances}.")
            else:
                print("Wrang Password.")
        else:
            print("Account does not exist.")
    
    def user_transaction_history(self, account_number,email,password):
        if account_number in self.accounts:
            if self.accounts[email]==password:
                balance = self.accounts[account_number]['balance']
                deposit = self.accounts[account_number]['deposit']
                withdrawal = self.accounts[account_number]['withdrawal']
                loan = self.accounts[account_number]['loan']
                transfer = self.accounts[account_number]['transfer']
                print(f"Transaction history for account {account_number}: Balance={balance}, Deposit={deposit}, Withdrawal={withdrawal}, Lone={loan}, Transfer={transfer}")
            else:
                print("Wrang Password.")
        else:
            print("Account does not exist.")

    def bank_transaction_history(self, account_number,email,password):
        if account_number in self.accounts:
            if self.accounts[email]==password:
                balance = self.bank_balance
                deposit = self.bank_deposit
                withdrawal = self.bank_withdrawal
                loan = self.total_loan_amount
                print(f"Transaction history for Bank: Balance={balance}, Deposit={deposit}, Withdrawal={withdrawal}, Lone={loan}")
            else:
                print("Wrang Password.")
        else:
            print("Account does not exist.")




class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, email, password, initial_balance):
        self.bank.create_account(email, password, initial_balance)

    def bank_transaction_history(self, account_number,email,password):
        self.bank.bank_transaction_history(account_number,email,password)

    def toggle_loan_feature(self, status):
        self.bank.loan_feature = status
        if status:
            print("Loan feature is now ON.")
        else:
            print("Loan feature is now OFF.")

    def check_bank_loan_balance(self, account_number,email,password):
        self.bank.check_bank_loan_balance(account_number,email,password)

    def check_bank_balance(self, account_number,email,password):
        self.bank.check_bank_balance(account_number,email,password)

class User:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, email, password, initial_balance):
        self.bank.create_account(email, password, initial_balance)

    def deposit(self, account_number,email,password,amount):
        self.bank.deposit(account_number,email,password,amount)

    def withdraw(self, account_number,email,password,amount):
        self.bank.withdraw(account_number,email,password,amount)

    def transfer(self, from_account, to_account, amount):
        self.bank.transfer(from_account, to_account, amount)

    def take_loan(self, account_number,email,password):
        self.bank.take_loan(account_number,email,password)
    
    def check_balance(self, account_number,email,password):
        self.bank.check_balance(account_number,email,password)

    def user_transaction_history(self, account_number,email,password):
        self.bank.user_transaction_history(account_number,email,password)

    
    
# Example usage of the banking management system

bank = Bank()

user = User(bank)
admin = Admin(bank)

admin.create_account('admin@gmail.com', '1234', 10000000)

user.create_account('user@gmail.com', '1234', 11100)
user.create_account('user2@gmail.com', '1234', 11100)
user.create_account('user3@gmail.com', '1234', 10000)
user.create_account('user4@gmail.com', '1234', 10000)
user.create_account('user5@gmail.com', '1234', 10000)

admin.create_account('admin@gmail.com', '1234', 10000000)

user.deposit(100001,'user@gmail.com', '1234',1000)
user.withdraw(100001,'user@gmail.com', '1234',1000)

user.transfer(100001,100002,500)

user.take_loan(100001,'user@gmail.com', '1234')
admin.toggle_loan_feature(True)

user.check_balance(100001,'user@gmail.com', '1234')
admin.check_bank_balance(100000,'admin@gmail.com', '1234')
admin.check_bank_loan_balance(100000,'admin@gmail.com', '1234')

user.user_transaction_history(100001,'user@gmail.com', '1234')
admin.bank_transaction_history(100000,'admin@gmail.com', '1234')




