# Atribut karyawan
hari_kerja = 17
hari_kerja_perbulan = 20
gaji_karyawan = 3500000
hari_lembur = 8
gaji_lembur_perjam = 50000

# Menghitung total gaji
gaji_reguler = (hari_kerja / hari_kerja_perbulan) * gaji_karyawan
gaji_lembur = hari_lembur * gaji_lembur_perjam
total_gaji = gaji_reguler + gaji_lembur

# Format total gaji dengan titik sebagai pemisah ribuan
total_gaji_formatted = "{:,.0f}".format(total_gaji).replace(',', '.')

# Menampilkan total gaji karyawan
print("Total gaji karyawan adalah: Rp. ", total_gaji_formatted)