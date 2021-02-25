# 5. Property Tax
# A county collects property taxes on the assessment value of property, which is 60 percent of
# the property’s actual value. For example, if an acre of land is valued at $10,000,
# its assessment value is $6,000. The property tax is then 72¢ for each $100 of the assessment value.
# The tax for the acre assessed at $6,000 will be $43.20. Write a program that asks for the
# actual value of a piece of property and displays the assessment value and property tax.

actValueToAssesRate = 0.60
taxRate = 0.0072

def main():
    propertyActValue = float(input("Enter the actual value of property, UAH: "))
    print("The assessment value of property, UAH:", format(propertyAssesValue(propertyActValue), '.2f'))
    print("Property tax, UAH:", format(taxProperty(propertyActValue), '.2f'))


def propertyAssesValue(propertyActValue):
    propertyAssesValue = propertyActValue * actValueToAssesRate
    return propertyAssesValue


def taxProperty(propertyActValue):
    taxProperty = propertyAssesValue(propertyActValue) * taxRate
    return taxProperty


main()
