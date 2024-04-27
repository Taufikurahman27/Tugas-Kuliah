import os
os.system("cls")

print("======================================================")
print("   Welcome to the student score calculation program   ")
print("          Taufikurahman(41823010025)                  ")
print("             Advanced programming                     ")
print("======================================================")
nilai_tugas = input("Please input your asssignment value:    ")
nilai_uts = input("Please input your UTS value:              ")
nilai_uas = input("Please input your UAS value:              ")
nilai_akhir = (0.25 * float(nilai_tugas)) + (0.35 * float(nilai_uts)) + (0.4 * float(nilai_uas))
print("Your final score is: ", nilai_akhir)

if nilai_akhir >= 85:
    print("Congrats, You Got Grade A")
elif nilai_akhir >= 80 and nilai_akhir < 85:
    print("Congrats, You Got Grade A-")
elif nilai_akhir >= 75 and nilai_akhir < 80:
    print("Congrats, You Got Grade B+")
elif nilai_akhir >= 70 and nilai_akhir < 75:
    print("You Got Grade B")
elif nilai_akhir >= 65 and nilai_akhir < 70:
    print("You Got Grade B-")
elif nilai_akhir >= 60 and nilai_akhir < 65:
    print("You Got Grade C+")
elif nilai_akhir >= 55 and nilai_akhir < 60:
    print("Regret it, You Got Grade C")
elif nilai_akhir >= 50 and nilai_akhir < 55:
    print("Regret it, You Got Grade C-")
elif nilai_akhir >= 30 and nilai_akhir < 50:
    print("Regret it, You Got Grade D")
elif nilai_akhir < 30:
    print("You Got Grade E, You didn't pass the course")
else:
    print("Your Score is Invalid")
