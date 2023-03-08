import math
while True:
  jarak_awal = float(input("Masukkan jarak awal : "))
  sudut_elevasi_1 = float(input("Masukkan sudut elevasi pada menit ke-5 (dalam derajat) : "))
  sudut_elevasi_2 = float(input("Masukkan sudut elevasi pada menit ke-6 (dalam derajat) : "))

  tinggi_helikopter_awal = jarak_awal * math.tan(sudut_elevasi_1)
  jarak_helikopter_akhir = jarak_awal * math.tan(sudut_elevasi_2) - math.tan(sudut_elevasi_1)
  selisih_ketinggian_helikopter = jarak_helikopter_akhir * math.tan(sudut_elevasi_2) 

  print("Ketinggian drone pada menit ke-5 adalah :", tinggi_helikopter_awal)
  print("Selisih ketinggian helikopter :", selisih_ketinggian_helikopter)

  program_lanjut = input("Masukkan jarak awal : ")
  sudut_elevasi_1 = float(input("Masukkan sudut elevasi pada menit ke-5 (dalam derajat) : "))
  sudut_elevasi_2 = float(input("Masukkan sudut elevasi pada menit ke-6 (dalam derajat) : "))

  tinggi_helikopter_awal = jarak_awal * math.tan(sudut_elevasi_1)
  jarak_helikopter_akhir = jarak_awal * math.tan(sudut_elevasi_2) - math.tan(sudut_elevasi_1)
  selisih_ketinggian_helikopter = jarak_helikopter_akhir * math.tan(sudut_elevasi_2) 
  if program_lanjut.lower() == "y":
    continue
  elif program_lanjut.lower() == "n" or program_lanjut.lower() == "stop" or program_lanjut.lower() == "berhenti":
    print ('Program dihentikan')
    break
  else:
    print("Input yang anda masukkan salah. Silahkan coba lagi.")
    break