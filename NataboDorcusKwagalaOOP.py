class student:
    def __init__(self, Student_name, Registration_number, Course_name, Year, Semester):
        self.Student_name = Student_name
        self.Registration_number = Registration_number
        self.Course_name = Course_name
        self.Year = Year
        self.Semester =Semester
        
    def display_info(self):
        print(f"Student_name: {self.Student_name}, Registration_number: {self.Registration_number}, Course_name: {self.Course_name}, Year: {self.Year}, Semester: {self.Semester}")
        
Student=[
    student("Namwanga Shammie", "BSIT23040", "Bachelor of Science in Information Technology", "2", "1"),
    student("Aine John","BSCS22005", "Bachelor of Sceince in Computer Science", "3", "2"),
    student("Nabirye Shine", "BSDA23015", "Bachelor Of Science in Data Science and Analytics", "2","1"),
]


for student in Student:
    student.display_info()