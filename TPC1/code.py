
# Opening the file
file = open("emd.csv", "r")

# Data fields
modalidades = set()
totalAtletas = 0
aptosCount = 0
idadeMaisAlta = 0
atletaDict = {} # key: age, value: list of lists with info

auxCount = 0

## Organizing the data into the fields ##
for line in file:
    lineInfo = line.strip().split(",")
    
    if auxCount > 0:
        auxCount += 1
        
        # Extracting the data
        id = lineInfo[0]
        nomeCompleto = lineInfo[3] + " " + lineInfo[4]
        idade = int(lineInfo[5])
        modalidade = lineInfo[8]
        clube = lineInfo[9]
        isApto = lineInfo[12]
        
        
        ## Updating the data fields ##
        
        # Updating the highest age
        if idade > idadeMaisAlta:
            idadeMaisAlta = idade
            
        # Updating total athlete number
        totalAtletas += 1
        
        # Updating the modalities set
        modalidades.add(modalidade)
        
        # Updating the aptos count
        if isApto == "true":
            aptosCount += 1
            
        # Adding the athlete to the dictionary
        if idade not in atletaDict:
            atletaDict[idade] = []
            
        atletaDict[idade].append([nomeCompleto, modalidade, clube])
    
    else:
        auxCount += 1    
        
        

# Calculating apt percentage
aptPercentage = (aptosCount / totalAtletas) * 100
totalApt = aptosCount

# Calculating non apt percentage
nonAptPercentage = (100 - aptPercentage)
totalNonApt = totalAtletas - aptosCount



## Handling the results ##

# Creating results file
results = open("results.txt", "w")

# Writing the modalities ordered
results.write("------------------------------------------------")
results.write("\n\n")

results.write(f"Modalidades: ")
results.write("\n\n")

modalidades = sorted(modalidades)
for modalidade in modalidades:
    results.write(f"-> {modalidade} ")
    results.write("\n")

results.write("\n")
results.write("------------------------------------------------")
results.write("\n\n")

# Writing the apt an non apt percentages
results.write(f"Atletas aptos: {str(aptPercentage)}% ({totalApt}) ")
results.write("\n\n")

results.write(f"Atletas inaptos: {str(nonAptPercentage)}% ({totalNonApt}) ")
results.write("\n\n")

results.write("------------------------------------------------")
results.write("\n\n")


# Writing the athletes age window

results.write("Escaloes: ")
results.write("\n\n")

start = 0
end = 0
for start in range(0, idadeMaisAlta+1,5):
    
    end = start + 4
    
    flag = False
    
    for age in atletaDict:
        if age >= start and age <= end:
            flag = True
            break
    
    if flag is True: 
        results.write(f"[{start}-{end}] : ")
        results.write("\n")
        results.write("\n")

        auxList = []

        currentAge = start
        for currentAge in range(start, end+1):
            if currentAge in atletaDict:
                for atleta in atletaDict[currentAge]:
                    auxList.append([atleta[0], atleta[2]])
        
        auxList = sorted(auxList, key=lambda athlete: athlete[0])
        for item in auxList:
            results.write(f"-> {item[0]} / {item[1]}")
            results.write("\n")
        
        results.write("\n")
        results.write(f"Numero de atletas neste escalao: {len(auxList)}")     
            
        results.write("\n\n\n")    
        
results.write("------------------------------------------------")        
print("Resultados guardados no ficheiro 'results.txt'")    