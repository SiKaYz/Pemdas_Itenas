import pandas as pd

# Pertanyaan 1
data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Menghitung gaji setiap karyawan setelah diberikan peningkatan 5%
df['Gaji'] = df['Gaji'].apply(lambda x: x * 1.05)

# Pertanyaan 2
# Menampilkan DataFrame yang sudah diperbarui
print("DataFrame setelah peningkatan 5% gaji:")
print(df)
# Ringkasan Perubahan:
# - Gaji setiap karyawan telah ditingkatkan sebesar 5%.

# Pertanyaan 3
# Mengevaluasi karyawan yang usianya di atas 30 tahun dan memberikan peningkatan tambahan 2%
df['Gaji'] = df.apply(lambda row: row['Gaji'] * 1.02 if row['Usia'] > 30 else row['Gaji'], axis=1)

# Pertanyaan 4
# Menampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan
print("DataFrame setelah peningkatan 5% gaji dan peningkatan tambahan untuk usia di atas 30 tahun:")
print(df)
# Ringkasan Perubahan:
# - Gaji setiap karyawan telah ditingkatkan sebesar 5%.
# - Karyawan yang berusia di atas 30 tahun menerima peningkatan tambahan sebesar 2%.
