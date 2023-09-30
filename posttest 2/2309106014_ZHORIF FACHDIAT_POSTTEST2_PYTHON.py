nama=str(input("Nama anda = "))
nim=int(input("NIM anda = "))
rnim=range(99999999,9999999999)
while nim not in rnim:
    nim=int(input("Tolong input NIM yang benar = "))
jenisKelamin=str(input("Jenis kelamin anda [pria atau wanita]= "))
while jenisKelamin!="pria" and jenisKelamin!="wanita":
    jenisKelamin=str(input("Tolong input jenis kelamin yang sesuai ketentuan = "))
umur=int(input("Umur anda = "))
while umur<0:
    umur=int(input("Tolong input umur yang benar = "))
tinggiBadan=float(input("Tinggi badan anda dalam satuan centimeter dengan akurasi satu angka dibelakang koma = "))
while tinggiBadan<0:
    tinggiBadan=float(input("Tolong masukkan tinggi badan sesuai ketentuan = "))
beratBadan=float(input("Berat badan anda dalam satuan centimeter dengan akurasi satu angka dibelakang koma = "))
while beratBadan<0:
    beratBadan=float(input("Tolong masukkan berat badan sesuai ketentuan = "))
snim=str(nim)
b3nim=int(snim[-3:])
b3nim%=4
print(f"Nama saya {nama} dengan NIM {nim}, saya berjenis kelamin {jenisKelamin} dan berumur {umur} tahun. Tinggi badan saya dan berat badan saya adalah {tinggiBadan} cm dan {beratBadan} kg. {snim[-3:]} dimodulus 4 = {b3nim}.")
