import json

izlaznaLista = []

with open('data.json', 'r') as f:
    data = json.load(f)


for i, (attCoi, entries) in enumerate(data.items()):

    NAME = 'data' + str(i) + '.json'
    with open(NAME, 'w') as w:
        w.write(json.dumps({attCoi: entries}))


