print("Program Menentukan Status Berat Badan")
bb=float(input("Berat badan anda dalam satuan mg = "))
tb=float(input("Tinggi badan anda dalam satuan km = "))
bmi=(bb/1000000)/((tb*1000)**2)
print(f"Body Mass Index anda = {bmi:.2f}")
if bmi<18.5:
    print("Status berat badan anda adalah Underweight")
elif 18.5<=bmi<25:
    print("Status berat badan anda adalah Normal")
elif 25<=bmi<30:
    print("Status berat badan anda adalah Overweight")
else:
    print("Status berat badan anda adalah Obesitas")