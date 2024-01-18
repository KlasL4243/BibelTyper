from json import load, dump

with open('schlachter.json') as file:
    data = load(file)

with open('schlachter2.json', 'w', encoding="utf-8") as file:
    dump(data, file, ensure_ascii=False, indent=4)