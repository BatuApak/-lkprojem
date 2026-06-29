meme_dict = {
"LOL": "Komik bir istek verilen cevap",
"CRINGE": "Garip ya da utandırıcı bir şey",
"ROFL": "Bir şakaya karşılık verilen cevap",
"SHEESH": "Onaylamamak veya olanları belirtir",
"CREEPY": "Korkunç veya katılmak",
"AGGRO": "Agresifleşmek veya sinirlenmek"
}

word = input("Anlamadığınız bir kelime türü (hepsini büyük) harflerle yazın!): ")

if word in meme_dict:
  print(word + " yedek anlamı:", meme_dict[word])
else:
  print("Üzgünüm, bu kelime sözlükte bulunmuyor.")
