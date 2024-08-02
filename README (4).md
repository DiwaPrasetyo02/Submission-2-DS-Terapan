# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Jaya jaya institut perlu mengatasi tingginya angka dropout. Angka dropout yang tinggi akan berdampak negatif pada jaya jaya institut. 
Permasalahan yang akan dihadapi oleh Jaya Jaya Insitut mencakup:
1. Hilangnya rasa kepercayaan siswa dan orang tua untuk menimba ilmu di jaya jaya institut
2. Dikarenakan angka dropout yang besar akan berdampak pada penurunan akreditasi institut
3. Institut Jaya Jaya akan berisiko mengalami bangkrut karena tidak sedikit siswa yang keluar sehingga pendapatan institut berkurang.
   
### Cakupan Proyek
1. Mengumpulkan dan memproses data mahasiswa.
2. Menganalisis data untuk menemukan pola dan faktor-faktor yang mempengaruhi dropoutnya mahasiswa.
3. Membangun model klasifikasi untuk mengetahui mahasiswa yang diprediksi lulus dan dropout.
4. Membuat dashboard bisnis untuk menganalisis faktor permasalahan.
5. Memberikan rekomendasi tindakan berdasarkan hasil analisis.

### Persiapan
Tahapan Persiapan
[Sumber Data]('https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv')
Setup environment:
    ```
     !pip install pycaret
     !pip install pycaret[analysis]
     !pip install numpy==1.24.4 pandas==2.1.4 matplotlib==3.7.5 seaborn==0.13.2
    ```

## Business Dashboard
Dashboard yang telah dibuat memberikan visualisasi faktor apa yang menjadi penyebab seseorang dropout di Jaya Jaya Institut. Faktor penyebab ini ditemukan dengan menggunakan machine learning. 
Pada halaman pertama secara umum, ditampilkan 6 faktor penyebab seorang mahasiswa dropout dan tidak dropout. Pada halaman kedua secara lebih spesifik ditampilkan mengenai faktor penyebab mengapa seorang mahasiswa dropout.
Pada halaman kedua filter control yang digunakan adalah Pemegang Beasiswa dimana mahasiswa yang bukan menjadi pemegang beasiswa memiliki resiko dropout yang tinggi.

## Conclusion
Dropout mahasiswa di institusi ini dipengaruhi oleh berbagai faktor, termasuk jumlah mata kuliah yang diselesaikan, status beasiswa, usia saat pendaftaran, mode aplikasi, dan waktu kehadiran kelas. Dukungan finansial seperti beasiswa dan stabilitas tempat tinggal juga berperan penting dalam keberhasilan akademik mahasiswa. Untuk mengurangi tingkat dropout, institusi dapat fokus pada pemberian dukungan finansial, memastikan stabilitas tempat tinggal, dan memberikan bimbingan akademik khususnya untuk mahasiswa yang lebih tua dan yang menghadiri kelas di malam hari.

### Rekomendasi Action Items

1. Peningkatan Dukungan Finansial
* Penambahan Beasiswa: Perluasan program beasiswa untuk menjangkau lebih banyak mahasiswa yang membutuhkan.
* Subsidi Biaya Pendidikan: Memberikan subsidi atau bantuan finansial untuk mahasiswa yang kesulitan membayar biaya pendidikan tepat waktu.
2. Pendekatan Personal dan Dukungan Akademik
* Program Mentoring: Menerapkan program mentoring bagi mahasiswa baru untuk membantu mereka beradaptasi dengan lingkungan akademik.
* Konseling Akademik: Menyediakan layanan konseling akademik yang proaktif untuk membantu mahasiswa merencanakan jalur pendidikan mereka.
3. Stabilitas Tempat Tinggal
* Dukungan Pemindahan: Memberikan bantuan logistik dan finansial bagi mahasiswa yang perlu berpindah tempat tinggal.
* Akomodasi Kampus: Menyediakan atau meningkatkan fasilitas akomodasi di kampus untuk mengurangi kebutuhan pemindahan tempat tinggal.
4. Penyesuaian Waktu Kelas
* Kelas Siang Hari: Meningkatkan jumlah kelas yang tersedia di siang hari, mengingat mahasiswa yang menghadiri kelas di siang hari cenderung memiliki tingkat kelulusan lebih tinggi.
* Jadwal Fleksibel: Menyediakan opsi jadwal fleksibel untuk mahasiswa yang memiliki komitmen lain di luar akademik.
5. Peningkatan Kualitas Pengajaran dan Kurikulum
* Evaluasi Kurikulum: Mengkaji ulang kurikulum untuk memastikan relevansi dan kemudahan penyelesaian mata kuliah.
* Pelatihan Pengajar: Memberikan pelatihan tambahan bagi pengajar untuk meningkatkan kualitas pengajaran dan interaksi dengan mahasiswa.
6. Pemantauan dan Intervensi Dini
* Sistem Peringatan Dini: Mengimplementasikan sistem machine learning yang telah dibuat untuk peringatan dini yang bisa mendeteksi mahasiswa yang berisiko dropout berdasarkan kinerja akademik dan kehadiran.
* Intervensi Proaktif: Melakukan intervensi proaktif bagi mahasiswa yang menunjukkan tanda-tanda kesulitan akademik atau finansial.
7. Kolaborasi dengan Industri dan Alumni
* Magang dan Kerjasama Industri: Meningkatkan program magang dan kerjasama dengan industri untuk memberikan pengalaman praktis yang dapat meningkatkan motivasi belajar.
* Jaringan Alumni: Mengaktifkan jaringan alumni untuk memberikan bimbingan dan kesempatan karir bagi mahasiswa saat dan setelah mereka lulus.
8. Pengembangan Komunitas dan Kegiatan Ekstrakurikuler
* Kegiatan Ekstrakurikuler: Meningkatkan kegiatan ekstrakurikuler yang dapat mendukung pengembangan soft skills dan membangun komunitas yang kuat di antara mahasiswa.
* Komunitas Belajar: Membentuk komunitas belajar untuk mata kuliah tertentu agar mahasiswa dapat saling mendukung dan berbagi pengetahuan.
