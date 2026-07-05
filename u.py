import yaml
import subprocess
import os

# 1. Membaca file .yml custom Anda
with open("tugas.yml", "r") as file:
    config = yaml.safe_load(file)

print(f"=== Memulai Workflow: {config['nama_alur_kerja']} ===\n")

# 2. Melakukan perulangan untuk setiap perintah (seperti GitHub Run)
for langkah in config['tahapan']:
    print(f"-> Menjalankan Langkah: {langkah['nama']}")
    
    # 3. Mengeksekusi perintah langsung di terminal Debian
    hasil = subprocess.run(langkah['perintah'], shell=True, capture_output=True, text=True)
    
    # 4. Menampilkan output log (seperti log di GitHub Actions)
    if hasil.returncode == 0:
        print(hasil.stdout)
    else:
        print(f"Gagal! Error: {hasil.stderr}")
        break  # Berhenti jika ada error (perilaku default CI/CD)

print("=== Semua Proses Selesai ===")
  
