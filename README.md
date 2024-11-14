Django Plagiarism Checker

Deskripsi

Aplikasi Django Plagiarism Checker adalah sebuah proyek berbasis web yang digunakan untuk memeriksa tingkat kemiripan antar dokumen teks menggunakan metode TF-IDF dan Cosine Similarity. Proyek ini dikembangkan dengan Django sebagai framework backend dan dirancang untuk membantu pengguna dalam mendeteksi kemiripan konten secara efisien.

Fitur

Pengunggahan Dokumen: Pengguna dapat mengunggah dokumen teks untuk diperiksa.

Analisis Kemiripan: Menghitung tingkat kemiripan antar dokumen menggunakan metode TF-IDF dan Cosine Similarity.

Tampilan Hasil: Menampilkan hasil analisis kemiripan dalam bentuk persentase yang mudah dipahami.


Teknologi yang Digunakan

Backend: Django

Algoritma: TF-IDF, Cosine Similarity

Database: MySQL


Instalasi
Clone repository ini:

bash
Salin kode
git clone https://github.com/DedeRamdan-G/django-plagiarism-checker-.git
Masuk ke direktori proyek:

bash
Salin kode
cd django-plagiarism-checker-
Buat dan aktifkan virtual environment (opsional tapi direkomendasikan):

bash
Salin kode
python -m venv env
source env/bin/activate  # Untuk MacOS/Linux
env\Scripts\activate     # Untuk Windows
Install dependensi proyek:

bash
Salin kode
pip install -r requirements.txt
Jalankan migrasi database:

bash
Salin kode
python manage.py migrate
Jalankan server lokal:

bash
Salin kode
python manage.py runserver
Buka browser dan akses http://127.0.0.1:8000 untuk menggunakan aplikasi.



Cara Menggunakan

Unggah dokumen yang ingin diperiksa kemiripannya.

Aplikasi akan menghitung skor kemiripan antara dokumen menggunakan TF-IDF dan Cosine Similarity.

Hasil kemiripan ditampilkan dalam bentuk persentase, memudahkan pengguna untuk mengevaluasi hasilnya.

Kontribusi
Kontribusi terbuka untuk siapa saja yang ingin membantu meningkatkan proyek ini. Silakan buat pull request atau ajukan issue untuk diskusi lebih lanjut.
