# 6. Patient Charges
# Write a class named Patient that has attributes for the following data:
# • First name, middle name, and last name
# • Address, city, state, and ZIP code
# • Phone number
# • Name and phone number of emergency contact
# The Patient class’s _ _init_ _ method should accept an argument for each attribute. The
# Patient class should also have accessor and mutator methods for each attribute.
# Next, write a class named Procedure that represents a medical procedure that has been
# performed on a patient. The Procedure class should have attributes for the following data:
# • Name of the procedure
# • Date of the procedure
# • Name of the practitioner who performed the procedure
# • Charges for the procedure
# The Procedure class’s _ _init_ _ method should accept an argument for each attribute.
# The Procedure class should also have accessor and mutator methods for each attribute.
# Next, write a program that creates an instance of the Patient class, initialized with sample
# data. Then, create three instances of the Procedure class, initialized with the following data:
# Procedure #1: Procedure #2: Procedure #3:
# Procedure name: Physical Exam
# Date: Today’s date
# Practitioner: Dr. Irvine
# Charge: 250.00
# Procedure name: X-ray
# Date: Today’s date
# Practitioner: Dr. Jamison
# Charge: 500.00
# Procedure name: Blood test
# Date: Today’s date
# Practitioner: Dr. Smith
# Charge: 200.00
# The program should display the patient’s information, information about all three of the
# procedures, and the total charges of the three procedures.

import patient, procedure
from datetime import datetime


def main():
    now = datetime.now()
    procList = []

    patientFirst = patient.Patient('Alex', 'Nore', 'Kor', 'Kvitucha str 30',
                                   'Kyiv', 'Kyiv region', '01001',
                                   '12345678', 'Anna', '98214566')

    procedure1 = procedure.Procedure('Physical Exam', now,
                                     'Dr. Irvine', 250.00)
    procedure2 = procedure.Procedure('X-ray', now, 'Dr. Jamison',
                                     500.00)
    procedure3 = procedure.Procedure('Blood test', now,
                                     'Dr. Smith', 200.00)
    total = procedure1.get_charge() + procedure2.get_charge() + procedure3.get_charge()

    print(patientFirst)
    print()
    print(procedure1)
    print()
    print(procedure2)
    print()
    print(procedure3)
    print()
    print("Total fee: ", total)


main()
