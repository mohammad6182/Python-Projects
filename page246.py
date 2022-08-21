
# parent class employye

class Employee:

    name = "John"
    rank = "M-11"
    schedule = "MJ2"

    def workShiftInfo(self):
        entry_name = input("What is your name?")
        entry_rank = input("what is your ranking code?")
        entry_schedule = input("what is your Schedule Code?")
        if(entry_name == self.name and entry_schedule == self.schedule):
            print("Thank you for coming in for your shift, {}".format(entry_name))
        else:
            print("There is no work schedule for today, Please talk to your manager {}".format(entry_name))



#parent class customer

class Customer:
    name = "Mark Jones"
    order_id = "T-1221"
    state = "Californi"


    def orderStatus(self):
        entry_name = input("please enter your name: >>>")
        entry_order_id = input("Order Id: ")
        entry_state = input("Destination: ")
        if(entry_name==self.name and entry_order_id==self.order_id):
            print("Your order has been sent and further information will be send to your email address")
        else:
            print("We cannot find your order information, please give us 24 hour to update your order status or call us")
    




#child class Group1

class Group1(Employee):
    hour_work = 40
    department = "HR"
    Access_code = "1221"

    def workShiftInfo(self):
        entry_name = input("what is your name?")
        entry_department = input("Department:  ")
        entry_access_code = input("what is your access code?")
        if(entr_name ==self.name and entry_access_code == self.Access_code):
            print("Welcome {} , yourshift is starting now".format(entry_name))
        else:
            print(" {}, please talk to a manager about your shift.".format(entry_name))



#child class order
class Order(Customer):
    order_date = "02/01/2022"
    order_code = "334434"

    def orderStatus(self):
        entry_id = input("Order ID:  ")
        entry_date = input("When did you submit your order?")
        entry_code = input("what is your order code?")
        if(entry_id == self.order_id and entry_code == self.ordr_code):
            print("Your order has been submited")
        else:
            print("We cannot find your order, please contact customer service")
            
    
    






























            
            
                                  





































        
    

    
