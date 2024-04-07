
# TPC6: Analisador Sintático

## Autor:

**Nome:** Diogo Pinto Araújo

**Id:** a100544

## Trabalho efetuado:  

**O que se pretende:**

Garantir a prioridade de operadores, garantir que é LL(1) e calcular look aheads.

```
? a
b = a * 2 / (27 - 3)
! a + b
c = a * b / (a / b)
```
**Resolução do tpc**
```
T =  {'?', '=', '*', '/', '-', '!', '+', '(', ')', Var, Num}

N = {Start, Expression, Exp1, Exp2, Operation, Op}

S = Start

P = {

    Start -> '?' Var                LA = {'?'}
        | '!' Expression            LA = {'!'}   
        | Var '=' Expression        LA = {Var}   

    Expression -> Exp1 Operation    LA = {'(', Var, Num}    

    Exp1 -> Exp2 Op                 LA = {'(', Var, Num}
    
    Operation -> '+' Expression     LA = {'+'}     
            | '-' Expression        LA = {'-'}  
            | &                     LA = {')', $}

    Exp2 -> '(' Expression ')'      LA = {'('}
        | Var                       LA = {Var}
        | Num                       LA = {Num}
    
    Op -> '*' Exp1                  LA = {'*'}
        | '/' Exp1                  LA = {'/'}
        | &                         LA = {'+', '-', ')', $}

}
```