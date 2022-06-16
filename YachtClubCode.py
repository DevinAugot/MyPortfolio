# Preparing Program for St.John's Marina and Yacht Club

# Author : Devin Augot

# Date: 2022-05-23

# Define Constants

Date = "2022-05-23"
HST_RATE = .15
EVEN_NUM_SITE = 80.00  # per month
ODD_NUM_SITE = 120.00  # per month
WEEKLY_CLEAN = 50.00  # per month
VID_SUR = 35.00  # per month

# Input Statements

SiteNum = int(input("Enter The Client’s Site Number: "))
MemName = input("Enter The Member’s Name: ")
StreetAdd = input("Enter Member’s street Address: ")
City = input("Enter Member’s City: ")
Prov = input("Enter Member’s Province: ")
PostCode = input("Enter Member’s postal code: ")
PhoneNum = input("Enter Member’s Phone Number: ")
CellNum = input("Enter Member’s Cellphone Number: ")
MemType = input("Enter the Membership Type: ").upper()
AltMembers = int(input("Enter the number of alternate members allowed access: "))
SiteClean = input("Weekly site cleaning Y or N: ").upper()
VidSur = input("Video Surveillance add on Y or N: ").upper()

print()

# Calculations

if SiteNum % 2 == 0:
    SiteCharge = EVEN_NUM_SITE + (AltMembers * 5.00)
else:
    SiteCharge = ODD_NUM_SITE + (AltMembers * 5.00)

if (SiteClean == "Y") and (VidSur == "Y"):
    ExtraCharge = WEEKLY_CLEAN + VID_SUR
    SiteClean = "Yes"
    VidSur = "Yes"


elif (SiteClean == "N") and (VidSur == "Y"):
    ExtraCharge = VID_SUR
    SiteClean = "No"
    VidSur = "Yes"

elif (SiteClean == "Y") and (VidSur == "N"):
    ExtraCharge = WEEKLY_CLEAN
    SiteClean = "Yes"
    VidSur = "No"




else:
    ExtraCharge = 0.00
    SiteClean = "No"
    VidSur = "No"

if MemType == "S":
    MonthlyDues = 75.00
    MemType = "Standard"


elif MemType == "E":
    MonthlyDues = 150.00
    MemType = "Executive"


else:
    MonthlyDues = 0.00


SubTotal = SiteCharge + ExtraCharge
SalesTax = SubTotal * HST_RATE
TotMthCharge = SubTotal + SalesTax
TotalMonthlyFee = MonthlyDues + TotMthCharge
TotalYearlyFee = TotalMonthlyFee * 12
MonthlyPay = (TotalYearlyFee + 59.99) / 12
CancelFee = (SiteCharge * 12) * .60

# Print Statements

print("{:^40s}".format("St. John’s Marina & Yacht Club"))
print("{:^40s}".format("Yearly Membership Receipt"))
print("_" * 40)
print()
print("Client Name and Address: ")
print()
print("{:<24}".format(MemName))
print("{:<24}".format(StreetAdd))
print(f"{City}, {Prov} {PostCode}")
print()
print(f"Phone: {PhoneNum}(H)")
print(f"       {CellNum}(C)")
print()
print(f"Site #:{SiteNum:>3d} Member type:{MemType:>15s}")
print()
print(f"Alternate members:                   {AltMembers}")
print(f"Weekly Site Cleaning:              {SiteClean}")
print(f"Video Surveillance:                 {VidSur}")
print()
SiteChargeDsp = "${:,.2f}".format(SiteCharge)
print(f"Site Charges:{SiteChargeDsp:>25s}")
ExtraChargeDsp = "${:,.2f}".format(ExtraCharge)
print(f"Extra Charges:{ExtraChargeDsp:>24s}")
print((" " * 24), ("-" * 13))
SubTotalDsp = "${:,.2f}".format(SubTotal)
print(f"Subtotal:{SubTotalDsp:>29s}")
SalesTaxDsp = "${:,.2f}".format(SalesTax)
print(f"Sales tax(HST):{SalesTaxDsp:>23s}")
print((" " * 24), ("-" * 13))
TotMthChargeDsp = "${:,.2f}".format(TotMthCharge)
print(f"Total monthly charges:{TotMthChargeDsp:>16s}")
MonthlyDuesDsp = "${:,.2f}".format(MonthlyDues)
print(f"Monthly Dues:{MonthlyDuesDsp:>25s}")
print((" " * 24), ("-" * 13))
TotalMonthlyFeeDsp = "${:,.2f}".format(TotalMonthlyFee)
print(f"Total monthly fees:{TotalMonthlyFeeDsp:>19s}")
TotalYearlyFeeDsp = "${:,.2f}".format(TotalYearlyFee)
print(f"Total yearly fees:{TotalYearlyFeeDsp:>20s}")
print()
MonthlyPayDsp = "${:,.2f}".format(MonthlyPay)
print(f"Monthly payment:{MonthlyPayDsp:>22s}")
print("_" * 40)
print()
print(f"Issued:{Date}")
print("HST Reg No: 549-33-5849-4720-9885")
print()
CancelFeeDsp = "${:,.2f}".format(CancelFee)
print(f"Cancellation fee:{CancelFeeDsp:>21s}")


