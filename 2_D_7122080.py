def hitung_mobil():
    jumlahSol = 0
    jumlahSur = 0
    jumlahJog = 0
    jumlahMag = 0
    
    while True:
        asal_mobil = input("Masukkan asal mobil: ").lower()
        if asal_mobil == 'solo':
            jumlahSol +=1
        elif asal_mobil == 'surabaya':
            jumlahSur +=1
        elif asal_mobil == 'jogja':
            jumlahJog +=1
        elif asal_mobil == 'magelang':
            jumlahMag +=1
        elif asal_mobil == 'done':
            break


    
    print('Jumlah mobil Solo:',jumlahSol)
    print('Jumlah mobil Surabaya:',jumlahSur)
    print('Jumlah mobil Jogja:',jumlahJog)
    print('Jumlah mobil  Magelang:',jumlahMag)
    
hitung_mobil()