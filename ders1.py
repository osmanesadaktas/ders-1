meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LoL": "League of Legends",
            }
    
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("ula uşaum bu kelime nedir lö")
