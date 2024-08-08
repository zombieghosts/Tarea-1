meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "cara riendo",
            ":v":"pacman",
            ":3": "cara tierna o de gato"
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Esto no está en el diccionario")
