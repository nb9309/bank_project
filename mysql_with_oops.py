# creating account
import mysql.connector as mc

class bank:
    @classmethod
    def select_pin(cls):
        try:
            conn = mc.connect(host='localhost', user='root', passwd='naresh', database='bank')
            cur_obj = conn.cursor()
            cur_obj.execute("select pin from account")
            cls.lst_pin = []
            for i in cur_obj.fetchall():
                for j in i:
                    cls.lst_pin.append(j)
        except mc.DatabaseError as db:
            print('error in database is: ', db)
    @classmethod
    def balence_enquiry(cls):
        try:
            conn = mc.connect(host='localhost', user='root', passwd='naresh', database='bank')
            cur_obj = conn.cursor()
            pin = int(input('enter your pin to check balence: '))
            if pin in bank.lst_pin:
                cur_obj.execute("select balence from account where pin= %d" %pin)
                cls.lst = 0
                for i in cur_obj.fetchall():
                    for j in i:
                        cls.lst=cls.lst+j
                print('balence: ',cls.lst)
            else:
                print('incorrect pin' )
                exit()
        except mc.DatabaseError as db:
            print('error in database is: ', db)
        except ValueError:
            print('enter only numbers')


    def create_account(self):
        while 9:
            self.acno = int(input('enter account number: '))
            self.cnane = input('enter coustemer name: ')
            self.bal = float(input('enter balence: '))
            self.pin = int(input('enter pin: '))
            try:
                conn = mc.connect(host='localhost',user='root',passwd='naresh',database='bank')
                cur_obj = conn.cursor()
                #cur_obj.execute('create table account(acno int, name varchar(10),balence float, pin int)')
                cur_obj.execute("insert into account values(%d,'%s',%f,'%s')" %(self.acno,self.cnane,self.bal,self.pin))
                print('account created successfully')
                conn.commit()
                n = input('do you want to create another account(yes/no): ')
                if n == 'no':
                    break
            except mc.DatabaseError as db:
                print('error in database is: ',db)
            except ValueError:
                print('enter only numbers')

class hyd:
    @staticmethod
    def deposit_money():
        try:
            depo = float(input('enter deposit money: '))
            balen = bank.lst+depo
            pin = int(input('enter your pin to deposit money: '))
            if pin in bank.lst_pin:
                conn = mc.connect(host='localhost', user='root', passwd='naresh', database='bank')
                cur_obj = conn.cursor()
                # cur_obj.execute('create table account(acno int, name varchar(10),balence float, pin int)')
                cur_obj.execute("update account set balence=%f where pin = %d" %(balen,pin))
                if cur_obj.rowcount == 1:
                    print('money is deposited to your account')
                else:
                    print('insufficent fund')
                conn.commit()
            else:
                print('incorrect pin ----> try again')
                exit()
        except mc.DatabaseError as db:
            print('error in database is: ', db)
        except ValueError:
            print('enter only numbers')

    @staticmethod
    def withdraw_money():
        try:
            conn = mc.connect(host='localhost', user='root', passwd='naresh', database='bank')
            cur_obj = conn.cursor()
            withdramoney = float(input('enter withdraw money: '))
            balen = bank.lst-withdramoney
            pin = int(input("enter your pin to withdraw money: "))
            if pin in bank.lst_pin:
                cur_obj.execute("update account set balence=%f where pin = %d" %(balen,pin))
                if cur_obj.rowcount == 1:
                    print('money is withdrwan from your account')
                else:
                    print('insufficent fund')
                conn.commit()
            else:
                print('incorrect pin ---> try again')
                exit()
        except mc.DatabaseError as db:
            print('error in database is: ', db)
        except ValueError:
            print('enter only numbers')

    @staticmethod
    def view_all_customer_data():
        try:
            con = mc.connect(host='localhost', user='root', passwd='naresh',database='bank')
            cur_obj = con.cursor()
            cur_obj.execute('select * from account')
            print('accno\t    name\t  bal\t   pin')
            for i in cur_obj:
                for j in i:
                    print(j,end='\t')
                print()
        except mc.DatabaseError as db:
            print('error in database is: ',db)

    @staticmethod
    def search_customer_data():
        try:
            conn = mc.connect(host='localhost', user='root', passwd='naresh', database='bank')
            cur_obj = conn.cursor()
            cur_obj.execute("select name from account")
            lst_name = []
            for i in cur_obj.fetchall():
                for j in i:
                    lst_name.append(j)
            cname = input('enter name to get data: ')
            if cname in lst_name:
                cur_obj.execute("select * from account where name='%s'" %cname)
                for i in cur_obj:
                    for j in i:
                        print(j)
            else:
                print("given name don't have account")
        except mc.DatabaseError as db:
            print('error in database is: ', db)

    @staticmethod
    def update_pin():
        try:
            conn = mc.connect(host='localhost', user='root', passwd='naresh', database='bank')
            cur_obj = conn.cursor()
            cur_obj.execute("select name from account")
            lst_name = []
            for i in cur_obj.fetchall():
                for j in i:
                    lst_name.append(j)
            cname = input('enter name for pin update: ')
            if cname in lst_name:
                pin = int(input('enter pin to update: '))
                cur_obj.execute("update account set pin=%d where name = '%s'" %(pin,cname))
                print('pin updated successfully')
                conn.commit()
            else:
                print('check your name ---> try again')
        except mc.DatabaseError as db:
            print('error in database is: ', db)

s = bank()
bank.select_pin()

while 9:
    ask = input('what do you what today(create account/ deposit money/ withdraw money/ view all customer data/ balence enquiry/ search customer data/ pin update/ work completed): ')

    if ask.strip() == 'view all customer data':
        hyd.view_all_customer_data()
    elif ask.strip() == 'create account':
        s.create_account()
    elif ask.strip() == 'balence enquiry':
        s.balence_enquiry()
    elif ask.strip() == 'withdraw money':
        s.balence_enquiry()
        hyd.withdraw_money()
        s.balence_enquiry()
    elif ask.strip() == 'deposit money':
        s.balence_enquiry()
        hyd.deposit_money()
        s.balence_enquiry()
    elif ask.strip() == 'search customer data':
        hyd.search_customer_data()
    elif ask.strip() == 'pin update':
        hyd.update_pin()
    elif ask.strip() == 'work completed':
        print('thank you ---> visit again')
        break
    else:
        print('enter available option correctly')