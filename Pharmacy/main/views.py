from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main import MenuObject
Menu = MenuObject.Menu

def passwordBefore(request, node):
    return render(request, node.name.replace(" ", "")+".html", {'name': node.name})
def passwordAfter(request, node):
    if request.POST.get("password", "") == "GRACE":
        return HttpResponseRedirect("/main/"+node.options[-1].name.replace(" ", "")+"/")
    return HttpResponseRedirect("/main/"+node.name.replace(" ", "")+"/")

def shiftNumberBefore(request, node):
    return render(request, node.name.replace(" ", "")+".html", {'name': node.name})
def shiftNumberAfter(request, node):
    if request.POST.get("shiftNumber", "") == "1":
        return HttpResponseRedirect("/main/"+node.options[-1].name.replace(" ", "")+"/")
    return HttpResponseRedirect("/main/"+node.name.replace(" ", "")+"/")

def addNewItemBefore(request, node):
    return render(request, node.name.replace(" ", "")+".html", {'name': node.name})
def addNewItemAfter(request, node):
    if "back" in request.POST:
        return HttpResponseRedirect("/main/"+node.options[0].name.replace(" ", "")+"/")

    itemCode = request.POST.get("itemCode", "")
    supplierName = request.POST.get("supplierName", "")
    itemDescription = request.POST.get("itemDescription", "")
    unit = request.POST.get("unit", "")
    ofUnitPack = request.POST.get("ofUnitPack", "")
    salePrice = request.POST.get("salePrice", "")
    tax = request.POST.get("tax", "")
    discount = request.POST.get("discount", "")
    type = request.POST.get("type", "")
    minimum = request.POST.get("minimum", "")

    return HttpResponseRedirect("/main/"+node.name.replace(" ", "")+"/")

if True:
    Password = Menu("Password", [], passwordBefore, passwordAfter)
    ShiftNum = Menu("Shift Number", [Password], shiftNumberBefore, shiftNumberAfter)
    MainMenu = Menu("Main Menu", [ShiftNum])

    MasterFile = Menu("Master File", [MainMenu])
    ReceivingIn = Menu("Receiving In", [MainMenu])
    SaleOut = Menu("Sale - Out", [MainMenu])
    Cashier = Menu("Cashier", [MainMenu])
    Bank = Menu("Bank", [MainMenu])
    Reports = Menu("Reports", [MainMenu])
    ReIndexTheFiles = Menu("Re Index The Files", [MainMenu])
    AddQuantityForItems = Menu("Add Quantity For Items", [MainMenu])


    AddNewItem = Menu("Add New Item", [MasterFile], addNewItemBefore, addNewItemAfter)
    EditOldItem = Menu("Edit Old Item", [MasterFile])
    EditCompanyName = Menu("Edit Company Name", [MasterFile])
    ChangePrice = Menu("Change Price", [MasterFile])
    EditMasterFile = Menu("Edit MasterFile", [MasterFile])
    CheckQuantities = Menu("Check Quantities", [MasterFile])
    PharmacyValue = Menu("Pharmacy Value", [MasterFile])
    ChangeCode = Menu("Change Code", [MasterFile])
    BackupTheFiles = Menu("Backup The Files", [MasterFile])

    OutNormalMovement = Menu("Out (Normal Movement)", [SaleOut])
    HealthInsurance = Menu("Health Insurance", [SaleOut])
    SaleOnCreditAndDept = Menu("Sale On Credit And Dept", [SaleOut])

    MoneyOut1 = Menu("Money Out 1", [Cashier])
    MoneyIn1 = Menu("Money In 1", [Cashier])

    MoneyOut2 = Menu("Money Out 2", [Bank])
    MoneyIn2 = Menu("Money In 2", [Bank])
    PayACheque = Menu("Pay A Cheque", [Bank])
    EditACheque = Menu("Edit A Cheque", [Bank])
    DeleteACheck = Menu("Delete A Check", [Bank])

    ReportsForMasterFile = Menu("Reports For MasterFile", [Reports])
    ReportsForRecieving = Menu("Reports For Recieving", [Reports])
    ReportsForSale = Menu("Reports For Sale", [Reports])
    ReportsForCashier = Menu("Reports For Cashier", [Reports])
    ReportsForBank = Menu("Reports For Bank", [Reports])



    Password.addOptions([ShiftNum])
    ShiftNum.addOptions([MainMenu])
    MainMenu.addOptions([MasterFile, ReceivingIn, SaleOut, Cashier, Bank, Reports, ReIndexTheFiles, AddQuantityForItems])

    MasterFile.addOptions([AddNewItem, EditOldItem, EditCompanyName, ChangePrice, EditMasterFile, CheckQuantities, PharmacyValue, ChangeCode, BackupTheFiles])
    SaleOut.addOptions([OutNormalMovement, HealthInsurance, SaleOnCreditAndDept])
    Cashier.addOptions([MoneyOut1, MoneyIn1])
    Bank.addOptions([MoneyOut2, MoneyIn2, PayACheque, EditACheque, DeleteACheck])
    Reports.addOptions([ReportsForMasterFile, ReportsForRecieving, ReportsForSale, ReportsForCashier, ReportsForBank])


    allMenus = [Password, ShiftNum, MainMenu, 
    MasterFile, ReceivingIn, SaleOut, Cashier, Bank, Reports, ReIndexTheFiles, AddQuantityForItems, #MainMenu
    AddNewItem, EditOldItem, EditCompanyName, ChangePrice, EditMasterFile, CheckQuantities, PharmacyValue, ChangeCode, BackupTheFiles, #MasterFile
    OutNormalMovement, HealthInsurance, SaleOnCreditAndDept, #SaleOut
    MoneyOut1, MoneyIn1, #Cashier
    MoneyOut2, MoneyIn2, PayACheque, EditACheque, DeleteACheck, #Bank
    ReportsForMasterFile, ReportsForRecieving, ReportsForSale, ReportsForCashier, ReportsForBank #Reports
    ]

def main(request):
    name = request.path.replace("/main/", "").replace("/", "")
    for menu in allMenus:
        if menu.name.replace(" ", "") == name:
            currentNode = menu
            break

    if request.method == 'POST':
        if currentNode.afterFunc == None:
            return currentNode.moveNode(int(request.POST.get("option", "")))
        else:
            return currentNode.afterFunc(request, currentNode)

    if currentNode.beforeFunc == None:
        return render(request, "Main.html", {'name': currentNode.name, 'options': ["Back"]+[option.name for option in currentNode.options[1:]]})
    else:
        return currentNode.beforeFunc(request, currentNode)


