'''


                           Relationship Diagram:

                                Employee
                                    |
              ---------------------------------------------
              |              |              |             |
             Cook          Server        Janitor        Manager
             ---
              |
           Sous_Chef
             ---  
              |                                             
             Chef


'''

class Employee:
    def __init__(self, name, address, phoneNumber, ssn, bankAcountNumber):
        self.name = name;
        self.address = address;
        self.phoneNumber = phoneNumber;
        self.ssn = ssn;
        self.bankAccountNumber = bankAcountNumber;
    
    def get_name(self):
        return ("Name: " + self.name);
    
    def get_address(self):
        return ("Address: " + self.address);
    
    def get_phoneNumber(self):
        return ("Phone number: " + self.phoneNumber);
    
    def get_ssn(self):
        return ("Social Security Number: " + self.ssn);
    
    def get_bankAccountNumber(self):
        return ("Bank Account Number: " + str(self.bankAccountNumber));
    
    def set_name(self, name):
        self.name = name;
    
    def set_address(self, address):
        self.address = address;
    
    def set_phoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber;
    
    def set_ssn(self, ssn):
        self.ssn = ssn;
        
    def set_bankAccountNumber(self, bankAccountNumber):
        self.bankAccountNumber = bankAccountNumber;


class Cook(Employee):
    def __init__(self, name, address, phoneNumber, ssn, bankAccountNumber,
                 yearsOfRelevantExperience):
        super().__init__(name, address, phoneNumber, ssn, bankAccountNumber);
        self.yearsOfRelevantExperience = yearsOfRelevantExperience;
        
    def get_yearsOfRelevantExperience(self):
        return ("Years of relevant experience: " + str(self.yearsOfRelevantExperience));
    
    def set_yearsOfRelevantExperience(self, yearsOfRelevantExperience):
        self.yearsOfRelevantExperience = yearsOfRelevantExperience;


class Sous_Chef(Cook):
    def __init__(self,name, address, phoneNumber, ssn, bankAccountNumber,
                 yearsOfRelevantExperience, institutionAttended, speciality):
        super().__init__(name, address, phoneNumber, ssn, bankAccountNumber, yearsOfRelevantExperience);
        self.institutionAttended = institutionAttended;
        self.speciality = speciality;
    
    def get_institutionAttended(self):
        return ("Institution Attended: " + self.institutionAttended);
    
    def get_speciality(self):
        return ("Speciality: " + self.speciality);
    
    def set_institutionAttended(self, institutionAttended):
        self.institutionAttended = institutionAttended;
    
    def set_speciality(self, speciality):
        self.speciality = speciality;


class Chef(Sous_Chef):
    def __init__(self, name, address, phoneNumber, ssn, bankAccountNumber,
                 yearsOfRelevantExperience, institutionAttended, speciality,
                 numOfAwards, numOfTvShowsFeaturedOn):
        super().__init__(name, address, phoneNumber, ssn, bankAccountNumber,
                 yearsOfRelevantExperience, institutionAttended, speciality);
        self.numOfAwards = numOfAwards;
        self.numOfShowsFeaturedOn = numOfTvShowsFeaturedOn;
        
    def get_numOfAwards(self):
        return ("Number of awards: " + str(self.numOfAwards));

    def get_numOfTvShowsFeaturedOn(self):
        return ("Number of tv shows featured on: " + str(self.numOfShowsFeaturedOn));
    
    def set_numOfAwards(self, numOfAwards):
        self.numOfAwards = numOfAwards;
    
    def set_numOfTvShowsFeaturedOn(self, numOfTvShowsFeaturedOn):
        self.numOfShowsFeaturedOn = numOfTvShowsFeaturedOn;

      
class Server(Employee):
    def __init__(self, name, address, phoneNumber, ssn, bankAcountNumber,
                 yearsOfRelevantExperience, numOfPositiveFeedback, numOfComplaints):
        super().__init__(name, address, phoneNumber, ssn, bankAcountNumber);
        self.yearsOfRelevantExperience = yearsOfRelevantExperience;
        self.numOfPositiveFeedback = numOfPositiveFeedback;
        self.numOfComplaints = numOfComplaints;
    
    def get_yearsOfRelevantExperience(self):
        return ("Years of relevant experience: " + str(self.yearsOfRelevantExperience));
    
    def get_numOfPositiveFeedback(self):
        return ("Number of positive feedback: " + str(self.numOfPositiveFeedback));
    
    def get_numOfComplaints(self):
        return ("Number of complaints: " + str(self.numOfComplaints));
    
    def set_yearsOfRelevantExperience(self, yearsOfRelevantExperience):
        self.yearsOfRelevantExperience = yearsOfRelevantExperience;
        
    def set_numOfPositiveFeedback(self, numOfPositiveFeedback):
        self.numOfPositiveFeedback = numOfPositiveFeedback;
    
    def set_numOfComplaints(self, numOfComplaints):
        self.numOfComplaints = numOfComplaints;
    

class Janitor(Employee):
    def __init__(self, name, address, phoneNumber, ssn, bankAcountNumber,
                 yearsOfRelevantExperience, yearsOfMaintenanceTraining):
        super().__init__(name, address, phoneNumber, ssn, bankAcountNumber);
        self.yearsOfRelevantExperience = yearsOfRelevantExperience;
        self.yearsOfMaintenanceTraining = yearsOfMaintenanceTraining;
    
    def get_yearsOfRelevantExperience(self):
        return ("Years of relevant experience: " + str(self.yearsOfRelevantExperience));
    
    def get_yearsOfMaintenanceTraining(self):
        return ("Years of maintenance training: " + str(self.yearsOfMaintenanceTraining));
    
    def set_yearsOfRelevantExperience(self, yearsOfRelevantExperience):
        self.yearsOfRelevantExperience = yearsOfRelevantExperience;
    
    def set_yearsOfMaintenanceTraining(self, yearsOfMaintenanceTraining):
        self.yearsOfMaintenanceTraining = yearsOfMaintenanceTraining;


class Manager(Employee):
    def __init__(self, name, address, phoneNumber, ssn, bankAcountNumber,
                 yearsOfRelevantExperience, tertiaryDegree, NumOfEmployeesManaged):
        super().__init__(name, address, phoneNumber, ssn, bankAcountNumber);
        self.yearsOfRelevantExperience = yearsOfRelevantExperience;
        self.tertiaryDegree = tertiaryDegree;
        self.NumOfEmployeesManaged = NumOfEmployeesManaged;
    
    def get_yearsOfRelevantExperience(self):
        return ("Years of relevant experience: " + str(self.yearsOfRelevantExperience));
    
    def get_tertiaryDegree(self):
        return ("Tertiary degree: " + self.tertiaryDegree);
    
    def get_NumOfEmployeesManaged(self):
        return ("Number of employees managed: " + str(self.NumOfEmployeesManaged));
    
    def set_yearsOfRelevantExperience(self, yearsOfRelevantExperience):
        self.yearsOfRelevantExperience = yearsOfRelevantExperience;
    
    def set_tertiaryDegree(self, tertiaryDegree):
        self.tertiaryDegree = tertiaryDegree;
        
    def set_NumOfEmployeesManaged(self, NumOfEmployeesManaged):
        self.NumOfEmployeesManaged = NumOfEmployeesManaged;
          
          
class Main():
    def __init__(self):
        self.main();
    
    def employee(self):
        employee_doe = Employee("John doe", "123 Main Street", "112-233-4445",
                                 "123-32-1111", 777888999);
        print("Employee Class\n---------------\n")
        print("Get\n---")
        print(employee_doe.get_name());
        print(employee_doe.get_address());
        print(employee_doe.get_phoneNumber());
        print(employee_doe.get_ssn())
        print(employee_doe.get_bankAccountNumber());
        print();
        
        print("Set\n---")
        employee_doe.set_name("Jane doe");
        employee_doe.set_address("123 Broadway Street");
        employee_doe.set_phoneNumber("666-777-8888");
        employee_doe.set_ssn("111-22-3333");
        employee_doe.set_bankAccountNumber(444555666);
        
        print(employee_doe.get_name());
        print(employee_doe.get_address());
        print(employee_doe.get_phoneNumber());
        print(employee_doe.get_ssn())
        print(employee_doe.get_bankAccountNumber());
        print("\n--------------------------------------------\n");  
    
    def cook(self):
        cook_doe = Cook("John doe", "123 Main Street", "112-233-4445",
                         "123-32-1111", 777888999, 10);
        print("Cook Class\n---------------\n")
        print("Get\n---")
        print(cook_doe.get_name());
        print(cook_doe.get_address());
        print(cook_doe.get_phoneNumber());
        print(cook_doe.get_ssn())
        print(cook_doe.get_bankAccountNumber());
        print(cook_doe.get_yearsOfRelevantExperience());
        print();
        
        cook_doe.set_name("Jane doe");
        cook_doe.set_address("123 Broadway Street");
        cook_doe.set_phoneNumber("666-777-8888");
        cook_doe.set_ssn("111-22-3333");
        cook_doe.set_bankAccountNumber(444555666);
        cook_doe.set_yearsOfRelevantExperience(15);
        
        print("Set\n---")
        print(cook_doe.get_name());
        print(cook_doe.get_address());
        print(cook_doe.get_phoneNumber());
        print(cook_doe.get_ssn())
        print(cook_doe.get_bankAccountNumber());
        print(cook_doe.get_yearsOfRelevantExperience());
        print("\n--------------------------------------------\n");
        
    def sousChef(self):
        sousChef_doe = Sous_Chef("John doe", "123 Main Street", "112-233-4445",
                                  "123-32-1111", 777888999, 10, "NYU", "Sous Chef");
        print("Sous_Chef Class\n---------------\n")
        print("Get\n---")
        print(sousChef_doe.get_name());
        print(sousChef_doe.get_address());
        print(sousChef_doe.get_phoneNumber());
        print(sousChef_doe.get_ssn())
        print(sousChef_doe.get_bankAccountNumber());
        print(sousChef_doe.get_yearsOfRelevantExperience());
        print(sousChef_doe.get_institutionAttended());
        print(sousChef_doe.get_speciality());
        print();
        
        sousChef_doe.set_name("Jane doe");
        sousChef_doe.set_address("123 Broadway Street");
        sousChef_doe.set_phoneNumber("666-777-8888");
        sousChef_doe.set_ssn("111-22-3333");
        sousChef_doe.set_bankAccountNumber(444555666);
        sousChef_doe.set_yearsOfRelevantExperience(15);
        sousChef_doe.set_institutionAttended("CUNY");
        sousChef_doe.set_speciality("Under Chief");
        
        print("Set\n---")
        print(sousChef_doe.get_name());
        print(sousChef_doe.get_address());
        print(sousChef_doe.get_phoneNumber());
        print(sousChef_doe.get_ssn())
        print(sousChef_doe.get_bankAccountNumber());
        print(sousChef_doe.get_yearsOfRelevantExperience());
        print(sousChef_doe.get_institutionAttended());
        print(sousChef_doe.get_speciality());
        print("\n--------------------------------------------\n");
        
    def chef(self):
        chef_doe = Chef("John doe", "123 Main Street", "112-233-4445",
                         "123-32-1111", 777888999, 10, "NYU", "Executive Chef",
                         13, 20);
        print("Chef Class\n---------------\n")
        print("Get\n---")
        print(chef_doe.get_name());
        print(chef_doe.get_address());
        print(chef_doe.get_phoneNumber());
        print(chef_doe.get_ssn())
        print(chef_doe.get_bankAccountNumber());
        print(chef_doe.get_yearsOfRelevantExperience());
        print(chef_doe.get_institutionAttended());
        print(chef_doe.get_speciality());
        print(chef_doe.get_numOfAwards());
        print(chef_doe.get_numOfTvShowsFeaturedOn());
        print();
        
        chef_doe.set_name("Jane doe");
        chef_doe.set_address("123 Broadway Street");
        chef_doe.set_phoneNumber("666-777-8888");
        chef_doe.set_ssn("111-22-3333");
        chef_doe.set_bankAccountNumber(444555666);
        chef_doe.set_yearsOfRelevantExperience(15);
        chef_doe.set_institutionAttended("CUNY");
        chef_doe.set_speciality("Under Chief");
        chef_doe.set_numOfAwards(5);
        chef_doe.set_numOfTvShowsFeaturedOn(10);
        
        print("Set\n---")
        print(chef_doe.get_name());
        print(chef_doe.get_address());
        print(chef_doe.get_phoneNumber());
        print(chef_doe.get_ssn())
        print(chef_doe.get_bankAccountNumber());
        print(chef_doe.get_yearsOfRelevantExperience());
        print(chef_doe.get_institutionAttended());
        print(chef_doe.get_speciality());
        print(chef_doe.get_numOfAwards());
        print(chef_doe.get_numOfTvShowsFeaturedOn());
        print("\n--------------------------------------------\n");
        
    def server(self):
        server_doe = Server("John doe", "123 Main Street", "112-233-4445",
                         "123-32-1111", 777888999, 5, 100, 10);
        print("Server Class\n---------------\n")
        print("Get\n---")
        print(server_doe.get_name());
        print(server_doe.get_address());
        print(server_doe.get_phoneNumber());
        print(server_doe.get_ssn())
        print(server_doe.get_bankAccountNumber());
        print(server_doe.get_yearsOfRelevantExperience());
        print(server_doe.get_numOfPositiveFeedback());
        print(server_doe.get_numOfComplaints());
        print();
        
        server_doe.set_name("Jane doe");
        server_doe.set_address("123 Broadway Street");
        server_doe.set_phoneNumber("666-777-8888");
        server_doe.set_ssn("111-22-3333");
        server_doe.set_bankAccountNumber(444555666);
        server_doe.set_yearsOfRelevantExperience(15);
        server_doe.set_numOfPositiveFeedback(200);
        server_doe.set_numOfComplaints(5);
        
        print("Set\n---")
        print(server_doe.get_name());
        print(server_doe.get_address());
        print(server_doe.get_phoneNumber());
        print(server_doe.get_ssn())
        print(server_doe.get_bankAccountNumber());
        print(server_doe.get_yearsOfRelevantExperience());
        print(server_doe.get_numOfPositiveFeedback());
        print(server_doe.get_numOfComplaints());
        print("\n--------------------------------------------\n");
        
    def janitor(self):
        janitor_doe = Janitor("John doe", "123 Main Street", "112-233-4445",
                         "123-32-1111", 777888999, 7, 3);
        print("Janitor Class\n---------------\n")
        print("Get\n---")
        print(janitor_doe.get_name());
        print(janitor_doe.get_address());
        print(janitor_doe.get_phoneNumber());
        print(janitor_doe.get_ssn())
        print(janitor_doe.get_bankAccountNumber());
        print(janitor_doe.get_yearsOfRelevantExperience());
        print(janitor_doe.get_yearsOfMaintenanceTraining());
        print();
        
        janitor_doe.set_name("Jane doe");
        janitor_doe.set_address("123 Broadway Street");
        janitor_doe.set_phoneNumber("666-777-8888");
        janitor_doe.set_ssn("111-22-3333");
        janitor_doe.set_bankAccountNumber(444555666);
        janitor_doe.set_yearsOfRelevantExperience(9);
        janitor_doe.set_yearsOfMaintenanceTraining(5);
        
        print("Set\n---")
        print(janitor_doe.get_name());
        print(janitor_doe.get_address());
        print(janitor_doe.get_phoneNumber());
        print(janitor_doe.get_ssn())
        print(janitor_doe.get_bankAccountNumber());
        print(janitor_doe.get_yearsOfRelevantExperience());
        print(janitor_doe.get_yearsOfMaintenanceTraining());
        print("\n--------------------------------------------\n");
        
    def manager(self):
        manager_doe = Manager("John doe", "123 Main Street", "112-233-4445",
                         "123-32-1111", 777888999, 7, "Buniess Management", 50);
        print("Manager Class\n---------------\n")
        print("Get\n---")
        print(manager_doe.get_name());
        print(manager_doe.get_address());
        print(manager_doe.get_phoneNumber());
        print(manager_doe.get_ssn())
        print(manager_doe.get_bankAccountNumber());
        print(manager_doe.get_yearsOfRelevantExperience());
        print(manager_doe.get_tertiaryDegree());
        print(manager_doe.get_NumOfEmployeesManaged());
        print();
        
        manager_doe.set_name("Jane doe");
        manager_doe.set_address("123 Broadway Street");
        manager_doe.set_phoneNumber("666-777-8888");
        manager_doe.set_ssn("111-22-3333");
        manager_doe.set_bankAccountNumber(444555666);
        manager_doe.set_yearsOfRelevantExperience(9);
        manager_doe.set_tertiaryDegree("Business Adminstration");
        manager_doe.set_NumOfEmployeesManaged(100);
        
        print("Set\n---")
        print(manager_doe.get_name());
        print(manager_doe.get_address());
        print(manager_doe.get_phoneNumber());
        print(manager_doe.get_ssn())
        print(manager_doe.get_bankAccountNumber());
        print(manager_doe.get_yearsOfRelevantExperience());
        print(manager_doe.get_tertiaryDegree());
        print(manager_doe.get_NumOfEmployeesManaged());
        print("\n--------------------------------------------\n");
        
    def main(self):
        self.employee();
        self.cook();
        self.sousChef();
        self.chef();
        self.server();
        self.janitor();
        self.manager();
        
Main();