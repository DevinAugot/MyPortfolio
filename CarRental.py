# Preparing invoice for daily car rental for the Edsel Rental Company.
# Author : Devin Augot
# Date completed: 2022-05-08

# Define system constants
DAILY_RATE = 35.00
COST_KM_TRAV = .10
HST_RATE = .15

CustName: str = input("Enter the customers name:")
CustPhoneNum = int(input("Enter the customers phone number:"))
NumDaysRent = int(input("Enter the numbers of days rented:"))
MileWhenRent = int(input("Enter the mileage when rented:"))
MileReturn = int(input("Enter the mileage when returned:"))
KiloTrav = int(input("Enter total Kilometers travelled:"))

DailyCost = (35.00 * HST_RATE) + DAILY_RATE
CostForRental = (NumDaysRent * DailyCost) + (KiloTrav * .10)
TotalCost = DailyCost + CostForRental

# Display required results
print()
print("Customers name:               ", CustName)
print("Customers Phone number:       ", CustPhoneNum)
print("Total Km Travelled:           ", KiloTrav)
print("Number of days rented:        ", NumDaysRent)
print("Miles When rented:            ", MileWhenRent)
print("Miles when returned:          ", MileReturn)
print("Kilometers travelled:         ", KiloTrav)
print("Daily cost:                   ", DailyCost)
print("Cost for rental:              ", CostForRental)
print("Total rental cost:            ", TotalCost)
