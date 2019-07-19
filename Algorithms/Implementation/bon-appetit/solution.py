def bonAppetit(bill, k, b):
    bill.pop(k)
    owed_amount = b - sum(bill) // 2
    print(owed_amount if owed_amount else "Bon Appetit")
