#reilly kurth
#program #4
#3/3/2025

class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title
    def get_name(self):
        return self.__name
    def get_id_number(self):
        return self.__id_number
    def get_department(self):
        return self.__department
    def get_job_title(self):
        return self.__job_title

def main():
    employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

   
    print(f"Name: {employee1.get_name()}, ID Number: {employee1.get_id_number()}, "
          f"Department: {employee1.get_department()}, Job Title: {employee1.get_job_title()}")
    print(f"Name: {employee2.get_name()}, ID Number: {employee2.get_id_number()}, "
          f"Department: {employee2.get_department()}, Job Title: {employee2.get_job_title()}")
    print(f"Name: {employee3.get_name()}, ID Number: {employee3.get_id_number()}, "
          f"Department: {employee3.get_department()}, Job Title: {employee3.get_job_title()}")


if __name__ == "__main__":
    main()