
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



#child class quality management
            
class quality_managment(Employee):

    def workShiftInfo(self):
        badge = ''
        name = 'Alex'
        department = 'QC'
        
        
    entry_name= input("what is your name?")
    badge_number =input("Badge Number:>> ")
    entry_schedule = input("what is your schedule code?")
    if(entry_name == self.name and entry_department == self.department and badge_number == self.badge):
        print("Welcome {} , your shift is starting in 30 minutes.".format(entry_name))
    else:
        print(" {} , Please see your manager. Thank you!".format(entry_name))





if __init__ == "name":

    emp = Employee()
    emp.workShiftInfo()
    group = Group1()
    group.workShiftInfo()
    manager = quality_management()
    manager.workShiftInfo()
    
            
    
    






























            
            
                                  





































        
    

    
