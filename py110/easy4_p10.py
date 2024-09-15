'''
input: int (id), list (of dicts {id: int, movement: str, quantity: int})
output: bool (T or F is item available)

explicit rules:
- return True only if quantity > 0
- movement value determines if quant increases or decreases

implicit rules:
- 

questions:
- 

data structures:
- list of dicts
- 

algorithm:
1. use id to get list of dicts

'''
def transactions_for(id, transactions):
    return [transaction for transaction in transactions
            if transaction['id'] == id]

def is_item_available(id, transactions):
    product_transactions = transactions_for(id, transactions)
    total = 0

    for transaction in product_transactions:
        if transaction['movement'] == 'in':
            total += transaction['quantity']
        else:
            total -= transaction['quantity']
    
    return total > 0

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True
