# Preparing program for Harry's Used Car Lot

# Author: Devin Augot

# Date: 2022-06-10

# Define Constants

import datetime

CurYear = 22
CUR_DATE = datetime.datetime.now()
HST_RATE = .15

# Input statements


while True:
    InvoiceDate = input("Enter the invoice date (YYYY-MM-DD): ")
    while True:
        CustName = input("Enter the customers first name: ").title()
        if CustName == "":
            print("Customers first Name cannot be blank please re-enter. ")
        else:
            break

    while True:
        CustLstName = input("Enter the customers last name: ").title()
        if CustLstName == "":
            print("Customers last name cannot be blank please re-enter. ")
        else:
            break
    while True:
        CustStreet = input("Enter the customers street address: ")
        if CustStreet == "":
            print("Customers street address cannot be blank please re-enter. ")
        else:
            break

    while True:
        CustPost = input("Enter the customers postal code (X9X9X9): ")
        if CustPost == "":
            print("Customers postal Code cannot be blank please re-enter. ")
        elif len(CustPost) < 6:
            print("Customers postal Code cannot be less then 6 characters please re-enter. ")
        else:
            break

    CustCity = input("Enter the customers city: ")

    CustProv = input("Enter the customers Province: ").upper()

    SalesPerName = input("Enter the salespersons name: ")

    CarMake = input("Enter the Car Make: ")

    CarModel = input("Enter the model of the car: ")

    CarYear = int(input("Enter the year of the vehicle: "))

    while True:

        PhoneNum = input("Enter the customers phone number (9999999999): ")

        if len(PhoneNum) != 10:
            print("Error. Phone Number must be 10 digits in length please re-enter.")

        else:
            break

    while True:
        PlateNum = input("Enter your licence plate number (XXX999): ").upper()

        if PlateNum == "":
            print("Licence plate number cannot be blank - please re-enter")

        elif len(PlateNum) < 6:
            print("Licence plate must be 6 characters.")

        elif PlateNum[0:3].isalpha() is False:
            print(f"Error plate number must start with 3 letters - please re-enter. ")

        elif PlateNum[3:6].isdigit() is False:
            print(f"Error plate number must end with 3 numbers - please re-enter. ")
        else:
            break

    while True:
        CarSellPrice = float(input("Enter the selling price of the car: "))

        if CarSellPrice > 50000.00:
            print("Car Sale price cannot exceed $50000.00. Please Re-enter. ")

        else:
            break

    while True:
        TradeIn = float(input("Enter the trade in value: "))

        if TradeIn > CarSellPrice:
            print("Error. Trade in value cannot exceed sale price. Please Re-enter. ")

        else:
            break

    while True:
        CCNum = input("Enter the 16 digit Credit Card Number: ")

        if len(CCNum) != 16:
            print("Error. Please enter the full 16 digits of the card number. ")

        else:
            break

    while True:
        CCExp = input("Enter the credit card expiry date (MM/YY): ")

        if CCExp[2] != "/":
            print("The month and year must be separated with a /.")
        elif int(CCExp[0:2]) < 1 or int(CCExp[0:2]) > 12:
            print("Month must be entered between 01 and 12.")
        elif int(CCExp[3:5]) < CurYear or int(CCExp[3:5]) > CurYear + 4:
            print("Year must be within 4 years of the current date.")
        else:
            break

# Calculations

    if CarSellPrice <= 5000.00:
        LicenceFee = 75.00
    elif CarSellPrice > 5000.00:
        LicenceFee = 165.00
    else:
        LicenceFee = 0.00

    if CarSellPrice < 20000.00:
        TransFee = 0.01 * CarSellPrice
    elif CarSellPrice > 20000.00:
        TransFee = (0.01 * CarSellPrice) + (0.016 * CarSellPrice)
    else:
        TransFee = 0.00

    PriceAfterTrade = CarSellPrice - TradeIn

    HstAmt = CarSellPrice * HST_RATE

    TotalSalePrice = PriceAfterTrade + HstAmt + LicenceFee + TransFee

    TradeAllowance = TradeIn

    FirstPayDate = datetime.datetime.strptime(InvoiceDate, "%Y-%m-%d")

    FirstPayDue = FirstPayDate + datetime.timedelta(days=30)

    MonthlyPay = ""  # Had to do this empty variable to fix error code "A Name "MonthlyPay" can be undefined".

    NumPay = ""  # Had to do this empty variable to fix error code "A Name "NumPay" can be undefined".

    # Financing Display output and program exit

    print(f"# Years    # Payments    Financing Fee    Total Price   Monthly Payment")
    print("-" * 70)

    for Years in range(1, 5):
        FinanceFee = 39.99 * Years
        NumPay = Years * 12
        TotalPrice = TotalSalePrice + FinanceFee
        MonthlyPay = TotalPrice / Years / 12
        TotalPriceDsp = "${:,.2f}".format(TotalPrice)
        MonthlyPayDsp = "${:,.2f}".format(MonthlyPay)
        FinanceFeeDsp = "${:,.2f}".format(FinanceFee)
        print(f" {Years:>4d}{NumPay:>13}{FinanceFeeDsp:>18s}       {TotalPriceDsp}        {MonthlyPayDsp}")
        print()

    while True:
        try:
            PayMethod = int(input("Enter the Payment Schedule you want to follow (1-4): "))
            print()
        except ValueError:  # had to use ValueError to avoid a bare exception error.
            print("Error. Payment Schedule must be between 1 and 4. Please Re-enter. ")
        else:
            if PayMethod < 1 or PayMethod > 5:
                print("Error. Payment Schedule must be between 1 and 4. Please Re-enter. ")
            else:
                break


# Print Statements

    print("{:^40s}".format("Honest Harry Car Sales"))
    print("{:^40s}".format("Used Car Sale and Receipt"))
    print()
    InvoiceDateDsp = CUR_DATE.strftime("%B %d, %Y")
    print(f"Invoice Date: {InvoiceDateDsp:>9s}")
    print(f"Receipt No: {CustName[0]}{CustLstName[0]}-{PlateNum[3:5]}-{PhoneNum[5:9]} ")
    print()
    print("Sold to:")
    print(f"     {CustName[0]}.{CustLstName:<28}")
    print(f"     {CustStreet}")
    print(f"     {CustCity},{CustProv},{CustPost:<6}")
    print()
    print("Car Details: ")
    print(f"     {CarYear} {CarMake} {CarModel}")
    print("-" * 38)
    CarSalePriceDSP = "${:,.2f}".format(CarSellPrice)
    print(f"Sale price:                 {CarSalePriceDSP:>10s}")
    TradeAllowanceDsp = "${:,.2f}".format(TradeAllowance)
    print(f"Trade Allowance:            {TradeAllowanceDsp:>10s}")
    PriceAfterTradeDsp = "${:,.2f}".format(PriceAfterTrade)
    print(f"Price after trade:          {PriceAfterTradeDsp:>10s}")
    print(" "*27, "-"*10)
    HstAmtDsp = "${:,.2f}".format(HstAmt)
    print(f"HST:                        {HstAmtDsp:>10s}")
    LicenceFeeDsp = "${:,.2f}".format(LicenceFee)
    print(f"Licence Fee:                {LicenceFeeDsp:>10s}")
    TransFeeDsp = "${:,.2f}".format(TransFee)
    print(f"Transfer Fee:               {TransFeeDsp:>10s}")
    print(" "*27, "-"*10)
    TotalSalePriceDsp = "${:,.2f}".format(TotalSalePrice)
    print(f"Total Sales Cost:           {TotalSalePriceDsp:10s}")
    print("-" * 38)
    print(f"Terms: {PayMethod}            Total payments: {NumPay}")
    MonthlyPayDsp = "${:,.2f}".format(MonthlyPay)
    print(f"Monthly payment:            {MonthlyPayDsp:>10s}")
    FirstPayDsp = (FirstPayDue.strftime("%Y-%m-%d"))
    print(f"First payment date:       {FirstPayDsp:>12}")
    print()
    print("{:^30s}".format("Honest Harry Car Sales"))
    print("{:^36s}".format("Best used cars at the best price!"))

    while True:
        print()
        Continue = input("Do you want to process another vehicle sale (Y / N): ").upper()
        print()
        if Continue == "":
            print("Must enter a Y or N to continue - Please Re-enter.")
        elif Continue != "Y" and Continue != "N":
            print("Must enter a Y or N to continue - Please Re-enter.")

        if Continue == "N":
            exit()

        else:
            break
