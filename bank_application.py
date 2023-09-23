import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="thanu@123", database="bank_management")

def openAcc():
    n = input("Enter the name:")
    ac = input("Enter the account number:")
    db = input("Enter the date of birth:")
    add = input("Enter the address:")
    cn = input("Enter the contact number:")
    ob = input("Enter the opening balance:")
    data1 = (n, ac, db, add, cn, ob)
    data2 = (n, ac, ob)
    sql1 = 'INSERT INTO account VALUES(%s, %s, %s, %s, %s, %s)'
    sql2 = 'INSERT INTO amount VALUES(%s, %s, %s)'
    x = mydb.cursor()
    x.execute(sql1, data1)
    x.execute(sql2, data2)
    mydb.commit()
    print("Data entered successfully...")
    main()

def depoAmt():
    amount = input("Enter the amount you want to deposit:")
    ac = input("Enter the account number:")
    a = 'SELECT balance FROM amount WHERE accno = %s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    final = x.fetchone()
    t = final[0] + float(amount)  # Convert amount to float
    sql = 'UPDATE amount SET balance = %s WHERE accno = %s'
    d = (t, ac)
    x.execute(sql, d)
    mydb.commit()
    print("Amount deposited successfully.")
    main()

def withdrawAmt():
    amount = input("Enter the amount you want to withdraw:")
    ac = input("Enter the account number:")
    a = 'SELECT balance FROM amount WHERE accno = %s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    final = x.fetchone()
    t = final[0] - float(amount)  # Convert amount to float
    sql = 'UPDATE amount SET balance = %s WHERE accno = %s'
    d = (t, ac)
    x.execute(sql, d)
    mydb.commit()
    print("Amount withdrawn successfully.")
    main()

def balanceAmt():
    ac = input("Enter the account number:")
    a = 'SELECT * FROM amount WHERE accno = %s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    print("Balance for account:", ac, "is", result[-1])
    main()

def customerDetails():
    ac = input("Enter the account number:")
    a = 'SELECT * FROM account WHERE accno = %s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    final = x.fetchone()
    for i in final:
        print(i)
    main()

def closeAcc():
    ac = input("Enter the account number:")
    sql1 = 'DELETE FROM account WHERE accno = %s'
    sql2 = 'DELETE FROM amount WHERE accno = %s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(sql1, data)
    x.execute(sql2, data)
    mydb.commit()
    print("Account closed successfully.")
    main()

def main():
    while True:
        print(""" 1. Open new account
                 2. Deposit amount
                 3. Withdraw amount
                 4. Balance amount
                 5. Display customer details
                 6. Close an account
                 7. Exit""")
        choice = int(input("Enter the task you want to perform: "))
        if choice == 1:
            openAcc()
        elif choice == 2:
            depoAmt()
        elif choice == 3:
            withdrawAmt()
        elif choice == 4:
            balanceAmt()
        elif choice == 5:
            customerDetails()
        elif choice == 6:
            closeAcc()
        elif choice == 7:
            print("Exiting the application.")
            break
        else:
            print("Invalid Choice. Try Again.")

if __name__ == "__main__":
    main()
