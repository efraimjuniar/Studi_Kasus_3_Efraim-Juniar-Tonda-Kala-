batas_nilai = (65, 100)
nilai_masuk = []
lulus = []
remedi = []

jumlah_nilai = 0
status_lulus = False
status_remedi = False

print("===Program Pengelompokkan Nilai Ujian Mahasiswa===")

while True:
    nilai = input("Masukkan nilai ujian (atau ketik 'selesai'/'hapus'): ")

    if nilai == "selesai":
        if jumlah_nilai < 5 :
            print("data belum cukup, minimal masukkan 5 nilai")
            continue
        elif status_lulus == False:
            print("belum ada nilai yang lulus, masukkan minimal 1 nilai")
            continue
        elif status_remedi == False:
            print("belum ada nilai yang remedi, masukkan minimal 1 nilai")
            continue
        else:
            break

    elif nilai == "hapus":
        print("nilai yang sudah diinput:", nilai_masuk)
        nilai_hapus = int(input("nilai yang mau dihapus: "))
        nilai_masuk.remove(nilai_hapus)
        jumlah_nilai = jumlah_nilai - 1

        if nilai_hapus >= batas_nilai[0]:
            lulus.remove(nilai_hapus)
        else:
            remedi.remove(nilai_hapus)
        print("nilai", nilai_hapus, "sudah dihapus")
        continue
    else:
        nilai = int(nilai)
        nilai_masuk.append(nilai)
        jumlah_nilai = jumlah_nilai + 1

        if nilai >= batas_nilai[0]:
            lulus.append(nilai)
            status_lulus = True
            print("nilai", nilai, "masuk kelompok lulus:", lulus)

        else:
            remedi.append(nilai)
            status_remedi = True
            print("nilai", nilai, "masuk kelompok remedi:", remedi)


print("seluruh nilai yang diinput:", nilai_masuk)
print("nilai yang lulus:", lulus)
print("nilai yang remedi:", remedi)