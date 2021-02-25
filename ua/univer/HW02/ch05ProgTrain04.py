# 4. Automobile Costs
# Write a program that asks the user to enter the monthly costs for the following expenses
# incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
# maintenance. The program should then display the total monthly cost of these expenses,
# and the total annual cost of these expenses.

def main():
    print("------------------------------------------------------------------------------------------------------")
    print("Enter the monthly costs for the following expenses incurred from operating your automobile, UAH:")
    print("------------------------------------------------------------------------------------------------------")
    loanpayment = float(input("Loan payment: "))
    insurance = float(input("Insurance:    "))
    gas = float(input("Gas:          "))
    oil = float(input("Oil:          "))
    tires = float(input("Tires:        "))
    maintenance = float(input("Maintenance:  "))
    print("------------------------------------------------------------------------------------------------------")
    print("The total monthly cost of these expenses, UAH:",
          format(totalMonthExpenses(loanpayment, insurance, gas, oil, tires, maintenance), '.2f'))
    print("The total annual cost of these expenses, UAH:",
          format(totalAnnualExpenses(loanpayment, insurance, gas, oil, tires, maintenance), '.2f'))


def totalMonthExpenses(loanpayment, insurance, gas, oil, tires, maintenance):
    totalMonthExpen = loanpayment + insurance + gas + oil + tires + maintenance
    return totalMonthExpen


def totalAnnualExpenses(loanpayment, insurance, gas, oil, tires, maintenance):
    totalMonthExpen = loanpayment + insurance + gas + oil + tires + maintenance
    totalAnnualExpen = totalMonthExpen * 12
    return totalAnnualExpen


main()
