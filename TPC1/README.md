# TPC1: Análise de um Dataset

## Autor:

**Nome:** Diogo Pinto Araújo

**Id:** a100544

## Resumo do trabalho efetuado:  

 Este TPC foi resolvido usando um script em python onde os resultados são guardados num ficheiro "results.txt" que o próprio script cria aquando a execução do programa.

- Para guardar os dados das modalidades criei um set que será posteriormente ordenado.

- Para guardar as informações dos atletas de uma dada idade decidi criar um dicionário que guardava numa chave (sendo a chave uma qualquer idade) várias listas com informações de diferentes atletas, isto é, temos, no fundo, uma lista de listas onde as listas interiores são listas com informações acerca de um dado alteta. Guardei os dados dos atletas desta forma pois quando for preciso escrever no ficheiro informações de atletas de um certo escalão posso iterar pela lista de uma chave do dicionário, não tendo de iterar pelo dicionário todo para encontrar atletas do dado escalão, tornando assim a escrita de informação de atletas mais eficiente.

- Para descobrir as percentagens de aptos e inaptos contei o número de aptos e o número total de atletas, e no final fiz o cálculo.

- O script tem também em conta apenas os escalões que são necessários imprimir no ficheiro de resultados, ou seja, se num dado escalão não existirem atletas esse escalão não será impresso nos resultados.

- Para imprimir os atletas nos dados escalões o script faz um for loop onde itera pelos diferentes escalões, verifica se existe algum atleta nesse escalão e se não existir ignora esse escalão. Se existir, vai guardar a informação que vai ser impressa sobre cada atleta desse escalão numa lista de listas auxiliar. De seguida essa lista vai ser ordenada conforme o nome dos atletas e por fim vai ser impressa toda a informação dos atletas desse escalão.
