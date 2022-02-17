import json

dicionario = {
  "GUI": ["Guilherme de Freitas", "15/02/2022" , "TERM1"],
  "MARI:": ["Mariana Alice","14/02/2022","TERM2"],
  "BATMAN": ["Batman ","13/02/2022","TERM3"]
}

with open("bd1.json", "w") as json_file:
    json.dump(dicionario, json_file)