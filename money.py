import json as js

def monthlyIncome(name):
    with open(f'{name}.json', 'r') as file:
        income = js.load(file)
    profit=0
    for item in income[0]["months"]:
        profit+=item
    
    return income[0]["months"], profit, income[0]["months"][-1]

