import json, requests

response = requests.get("https://api.github.com/repositories/132619461").text
objetoAPI = json.loads(response)

with open("FileToCheck.json","r") as j:
    objetoFile=json.load(j)
    
def BuscarKeySubconjunto (keyFile,valueFile, objetoAPI,nameKey):  
    for keyFile2, valueFile2 in valueFile.items():
            for keyAPI, valueAPI in objetoAPI.items():
                if isinstance(valueAPI, (dict)) and keyAPI==keyFile: 
                    for keyAPI2, valueAPI2 in valueAPI.items():
                        assert keyFile2 in valueAPI, nameKey+"/"+keyFile2+" is not in the json of the API github" 
                        if isinstance(valueFile2, (dict)):
                            nameKey=nameKey+"/"+keyFile2
                            BuscarKeySubconjunto(keyFile2,valueFile2, valueAPI,nameKey)

for keyFile, valueFile in objetoFile.items():
    assert keyFile in objetoAPI, keyFile+" is not in the json of the API github" 
    if isinstance(valueFile, (dict)):
        BuscarKeySubconjunto(keyFile,valueFile, objetoAPI,keyFile)
print("All the keys in the file are in the API")


