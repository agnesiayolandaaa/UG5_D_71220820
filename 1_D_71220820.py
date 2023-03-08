kalimat = input("Masukkan Kalimat: ")
carikata = input("Kata yang dicari: ")
ganti = input("Diganti menjadi: ")

def ganti_kata(kalimat, carikata, ganti):
  kata = kalimat.split(" ")
  for i in range(len(kata)):
    if kata[i] == carikata:
      kata[i] = ganti
  hasil = " ".join(kata)
  return hasil

print("Kalimat baru:", ganti_kata(kalimat, carikata, ganti))