
# Somador on/off

## Autor:

**Nome:** Diogo Pinto Araújo

**Id:** a100544

## Trabalho a efetuar:

O programa em Python tinha de fazer o seguinte:

1. Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
2. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
3. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
4. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

## Trabalho efetuado:

Optei por usar o método findall para identificar todas as instâncias de uma expressão regular específica no arquivo fornecido como entrada. A expressão regular que escolhi para utilizar no findall foi `r'(on|off|-?[0-9]+|=)'`, que busca todas as ocorrências de on, off, =, além de sequências de dígitos que podem ser negativas ou positivas.

Efetuei o parsing de todos esses comandos potenciais adicionando-os a uma lista organizada cronologicamente, conforme foram aparecendo no texto.

Com essa lista em mãos, implementei um loop for para iterar sobre cada comando e determinar que tipo de operação precisava ser realizada. Cada vez que um sinal de igual era encontrado, uma mensagem era exibida no terminal indicando o resultado atual. Ao final do processo, o resultado final também era exibido.

Este método proporcionou-me uma abordagem eficiente para analisar e processar os comandos presentes no texto de entrada.

**Para correr o programa:** 

O input é feito através de um ficheiro na pasta do tpc chamado `input.txt` onde se devera colocar o input destinado!

```python3 code.py```
