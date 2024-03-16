import ply.lex as lex
import json
import re
from datetime import date
from prettytable import PrettyTable
import sys

tokens = (
    "LISTAR",
    "MOEDA",
    "SELECIONAR",
    "SALDO",
    "SAIR"    
)

saldoMachine = 0

def printTable(data):
    header = ["Código", "Nome", "Quantidade", "Preço"]
    items = []
    # Iterating over the data
    for value in data:
        # Getting the code and the name
        code = value["cod"]
        name = value["nome"]
        quantity = value["quant"]
        price = str(value["preco"]) + "€"
        
        if quantity > 0:
            # Appending the stock list with the data
            items.append([code, name, quantity, price])
    
    # Printing the table
    table = PrettyTable(header)
    for item in items:
        table.add_row(item)
    print(table)    

def calcularTroco():
    # Define the coins and their values in cents
    coins = {"2e": 200, "1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}
    
    # Calling the global variable
    global saldoMachine
    
    # Calculating the change in cents
    saldoCent = saldoMachine * 100
    
    trocoStr = ""
    # For each coin, starting from the highest value
    for coin, value in sorted(coins.items(), key=lambda item: item[1], reverse=True):
        # Calculate how many coins of this type can be given
        count = saldoCent // value
        if count > 0:
            # Subtract the value of these coins from the total change
            saldoCent -= count * value
            # Add this information to the result string
            trocoStr += f"{count}x {coin}, "
    
    # Remove the last comma and space from the result string
    trocoStr = trocoStr.rstrip(", ")
    trocoStr += "."
    
    return trocoStr
        
def calcularSaldo():
    
    # Calling the global variable
    global saldoMachine
    
    saldoToStr = ""
    
    # Calculating the change
    if len(str(saldoMachine)) > 1:
        if str(saldoMachine).split(".")[1] == "0":
            saldoToStr = str(saldoMachine).split(".")[0] + 'e'
        elif len(str(saldoMachine).split(".")[1]) == 1:
            saldoToStr = str(saldoMachine).split(".")[0] + 'e' + str(saldoMachine).split(".")[1] + '0c'
        else:
            saldoToStr = str(saldoMachine).split(".")[0] + 'e' + str(saldoMachine).split(".")[1] + 'c'
    else:
        if saldoMachine != 0:
            saldoToStr = str(saldoMachine) + 'e'

    return saldoToStr   

# Done
def t_LISTAR(t):
    r'LISTAR'
    
    # Getting the stock from the lexer
    stock = t.lexer.stock
        
    # Printing the stock
    print("maq:")
    printTable(stock)
    
    return t
    
#Done
def t_MOEDA(t):
    r'MOEDA.+'
    
    # Calling the global variable
    global saldoMachine
    
    # Adding the money to the machine
    moedas = re.findall(r'(1e|2e|50c|20c|10c|5c|2c|1c)', t.value)
    
    for moeda in moedas:
        if moeda == "1e":
            saldoMachine += 1
        elif moeda == "2e":
            saldoMachine += 2
        elif moeda == "50c":
            saldoMachine += 0.50
        elif moeda == "20c":
            saldoMachine += 0.20
        elif moeda == "10c":
            saldoMachine += 0.10
        elif moeda == "5c":
            saldoMachine += 0.05
        elif moeda == "2c":
            saldoMachine += 0.02
        elif moeda == "1c":
            saldoMachine += 0.01
    
    # Calculating the change
    saldoToStr = calcularSaldo()
    
    # Printing the balance-
    print(f"maq: Saldo = {saldoToStr}")
    
    return t

# Done
def t_SELECIONAR(t):
    r'SELECIONAR\s[A-Z]{1}[0-9]+'
    
    # Calling the global variable
    global saldoMachine
    
    # Getting the item code
    itemID = re.match(r'SELECIONAR ([A-Z]{1}[0-9]+)', t.value).group(1)
 
    # Getting the stock from the lexer
    stock = t.lexer.stock
    
    item = None
    for artigo in stock:
        if artigo["cod"] == itemID:
            item = artigo
            break
    
    if item == None:
        print(f"maq: Não existe o item \"{itemID}\" na maquina.")
        return t
    
    else:
        if item["quant"] == 0:
            print(f"maq: Não tem stock do item \"{itemID}\".")
            return t
        
        else:
            # Searching for the item in the stock   
            itemPrice = item["preco"]
            
            # Verifying if the user has enough money
            if itemPrice > saldoMachine:
                print(f"maq: Não tem saldo suficiente para comprar o item {itemID}.")
                print(f"maq: Saldo = {calcularSaldo()}; Pedido = {itemPrice}")
            else:
                item["quant"] -= 1
                saldoMachine -= itemPrice
                saldoMachine = round(saldoMachine, 2)
                print(f"maq: Pode retirar o produto dispensado \"{item['nome']}\" .")   
                print(f"maq: Saldo = {calcularSaldo()}") 
                
                file = open("stock.json", "w")
                json.dump({"stock": stock}, file)
            
# Done
def t_SALDO(t):
    r'SALDO'
    
    # Calculating the change
    saldoToStr = calcularSaldo()
    
    # Printing the balance
    if saldoToStr == "":
        print("maq: Saldo = 0e")
    else:
        print(f"maq: Saldo = {saldoToStr}")
    
    return t
    
# Done
def t_SAIR(t):
    r'SAIR'
    
    # Calculating the change
    trocoToString = calcularTroco()
    
    # Printing the change
    if trocoToString == ".":
        print("maq: Não tem troco a devolver. Até à próxima.")
    else:     
        print(f"maq: Pode retirar o troco: {trocoToString}")
        print("maq: Até à próxima.")
        
    # Exiting the program
    sys.exit()
        
# Done
def main():   
    # Gretting the user with default message 
    print(f"\nmaq: {date.today()}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    
    # Creating the lexer
    lexer = lex.lex()
    
    # Infinite loop so the user can input multiple commands
    while True:
        try:
            # Opening the stock file
            with open("stock.json", "r") as file:
                # Loading stock from json file
                stock = json.load(file)
                # Storing the stock info in a variable inside the lexer
                lexer.stock = stock['stock']
            
            # Reading the intructions from the user
            inputText = input(">> ")
            
            # Parsing the input
            lexer.input(inputText)
            
            # Getting the first token
            toke = lexer.token()
            
        except EOFError:
            break

t_ignore = " \t"
        
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_error(t):   
    print(f"maq: Comando inválido: {t}")
    t.lexer.skip(1000)

if "__main__" == __name__:
    main()        