meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "RIZZ": "Karizma",
    "CAP": "Yalan",
    "FLEX": "Böbürlenmek"
}

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print("Bu kelimenin anlamı: {meme_dict[word]}")
else:
    print("Bu kelime sözlükte bulunmamaktadır.")
