import sqlite3


class Human:
    def __init__(self, applicant_id, applicant_name):
        self.applicant_id = applicant_id
        self.applicant_name = applicant_name

    def __str__(self) -> str:
        return f"{self.applicant_id}, {self.applicant_name}"

    def __repr__(self) -> str:
        return f"Applicant({self.__str__()})"


class Applicant(Human):
    def __init__(self, applicant_id, applicant_name, applicant_address, applicant_phone):
        Human.__init__(self, applicant_id, applicant_name)
        self.applicant_address = applicant_address
        self.applicant_phone = applicant_phone

    def __str__(self) -> str:
        return f"Id: {self.applicant_id}, name: {self.applicant_name},\naddress: {self.applicant_address}, phone: {self.applicant_phone}\n"

    def __repr__(self) -> str:
        return f"Applicant({self.__str__()})"


class ApplicantGrades(Human):
    def __init__(self, applicant_id, applicant_name, applicant_subject, applicant_grade):
        Human.__init__(self, applicant_id, applicant_name)
        self.applicant_subject = applicant_subject
        self.applicant_grade = applicant_grade

    def __str__(self) -> str:
        return f"{self.applicant_id}, {self.applicant_name}, {self.applicant_subject}, {self.applicant_grade}\n"

    def __repr__(self) -> str:
        return f"Applicant({self.__str__()})"


def get_info_by_applicant_name(applicant_name):
    with sqlite3.connect("Applicants_1.db") as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
        select * from People
        where People.Name like '%{applicant_name}%'
        """)
        result_list = cursor.fetchall()
        applicant_list = []
        for result in result_list:
            applicant_list.append(Applicant(result[0], result[1], result[2], result[3]))
    return applicant_list


def get_grades_by_applicant_name(applicant_name):
    with sqlite3.connect("Applicants_1.db") as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
        select People.Id, People.Name, Subjects.SubjectName, Grades.Grade from People
        join Grades on People.Id=Grades.ApplicantId
        join Subjects on Grades.SubjectId=Subjects.Id
        where People.Name like '%{applicant_name}%'
        """)
        result_list = cursor.fetchall()
        applicant_list = []
        for result in result_list:
            applicant_list.append(ApplicantGrades(result[0], result[1], result[2], result[3]))
    return applicant_list
