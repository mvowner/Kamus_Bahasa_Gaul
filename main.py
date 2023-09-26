meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "gabut": "gak ada kerjaan",
            "GG": "good game",
            "YTTA": "Yang tau tau aja",
            "tbh":"to be honest",
            "ngl": "Not gonna lie",
            "TTYL": "Talk to you later",
            "aka": 'alias',
            "salfok": "salah fokus",
            "AYGDK": 'Anak y gaul dan keren',
            'idk': "i don't know",
            "BRB": "Be right back",
            "WIBU": "pecinta manga dan anime",
            "nn": "naon"
            }
            
word = input("Ketik kata yang tidak Kamu mengerti: ")
if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print(meme_dict[word])
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("Kata yang kamu cari tidak ada!")
