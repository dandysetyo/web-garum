from pathlib import Path
root=Path('/mnt/data/website-garum')
header='''<!DOCTYPE html>\n<html lang="id">\n<head>\n  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <link rel="stylesheet" href="css/style.css">\n'''
nav='''</head>\n<body>\n<header class="topbar"><div class="container nav"><a class="brand" href="index.html"><span class="brand-badge"><img src="image/logo-garum.png" alt="Logo Garum"></span><span class="brand-title">Kecamatan Garum <span class="brand-sub">Kabupaten Blitar</span></span></a><nav class="menu"><a href="index.html">Beranda</a><a href="index.html#layanan">Layanan</a><a href="index.html#informasi">Informasi Publik</a><a href="berita.html">Berita</a><a href="kontak.html">Kontak</a></nav></div></header>\n<main class="container">'''
footer='''</main><footer class="footer"><div class="container footer-grid"><div><h4>Kecamatan Garum</h4><p>Portal lokal untuk akses informasi dan layanan masyarakat Kecamatan Garum, Kabupaten Blitar.</p></div><div><h4>Menu</h4><ul><li><a href="layanan-publik.html">Layanan Publik</a></li><li><a href="pengumuman.html">Pengumuman</a></li><li><a href="ppid.html">PPID</a></li></ul></div><div><h4>Kontak</h4><p>Kecamatan Garum, Kabupaten Blitar<br>Email: kecamatan.garum@example.go.id</p></div></div><div class="container copyright">© 2026 Kecamatan Garum. Seluruh halaman sudah memakai tautan lokal.</div></footer></body></html>'''
def page(file,title,desc,cards):
    html=header+f'  <title>{title} - Kecamatan Garum</title>\n'+nav+f'<section class="hero-page"><h1>{title}</h1><p>{desc}</p></section><section><div class="content-grid">'
    for h,p in cards:
        html+=f'<div class="content-card"><h3>{h}</h3><p>{p}</p></div>'
    html+='</div><a class="btn" href="index.html#layanan">Kembali ke Layanan</a></section>'+footer
    (root/file).write_text(html,encoding='utf-8')

pages={
'berita.html':('Berita','Kumpulan berita dan kegiatan terbaru Kecamatan Garum.', [('Kegiatan Kecamatan','Informasi kegiatan pemerintahan dan pelayanan masyarakat.'),('Program Desa','Berita program pembangunan dan pemberdayaan masyarakat.'),('Agenda Terbaru','Ringkasan agenda yang dapat diikuti masyarakat.')]),
'galeri.html':('Galeri','Dokumentasi foto kegiatan, fasilitas, dan lingkungan Kecamatan Garum.', [('Foto Kegiatan','Dokumentasi kegiatan pelayanan dan acara masyarakat.'),('Lingkungan Garum','Potret wilayah dan fasilitas umum.'),('Album Publik','Album dokumentasi yang dapat diperbarui sesuai kebutuhan.')]),
'kontak.html':('Kontak Kami','Informasi kontak dan kanal komunikasi Kecamatan Garum.', [('Alamat Kantor','Kantor Kecamatan Garum, Kabupaten Blitar.'),('Jam Layanan','Senin-Jumat pukul 08.00-15.00 WIB.'),('Kanal Bantuan','Gunakan kanal layanan publik untuk pertanyaan administrasi.')]),
'layanan-publik.html':('Layanan Publik','Daftar informasi layanan administrasi dan pengaduan untuk masyarakat.', [('Administrasi Kependudukan','Informasi persyaratan surat pengantar, KTP, KK, dan dokumen warga.'),('Pengaduan Masyarakat','Sampaikan aspirasi, keluhan, atau laporan pelayanan.'),('Pelayanan Umum','Panduan pelayanan umum di kantor kecamatan.')]),
'dokumen-pelaporan.html':('Dokumen Pelaporan','Dokumen publik dan laporan yang dapat diakses masyarakat.', [('Laporan Kinerja','Ringkasan pelaksanaan program dan kegiatan.'),('Dokumen Perencanaan','Dokumen rencana kerja dan prioritas kegiatan.'),('Arsip Publik','Daftar arsip dokumen untuk informasi masyarakat.')]),
'pengumuman.html':('Pengumuman','Informasi pengumuman resmi Kecamatan Garum.', [('Pengumuman Pelayanan','Perubahan jadwal layanan dan pemberitahuan penting.'),('Agenda Warga','Informasi kegiatan yang melibatkan masyarakat.'),('Informasi Mendesak','Pemberitahuan penting yang perlu segera diketahui warga.')]),
'ppid.html':('PPID','Informasi Pejabat Pengelola Informasi dan Dokumentasi.', [('Profil PPID','Informasi tugas dan fungsi pengelolaan informasi publik.'),('Permohonan Informasi','Panduan pengajuan permohonan informasi publik.'),('Daftar Informasi Publik','Daftar informasi yang tersedia untuk masyarakat.')]),
'ringkasan-apbd.html':('Ringkasan APBD','Informasi ringkas anggaran dan belanja daerah.', [('Pendapatan','Ringkasan sumber pendapatan daerah.'),('Belanja','Ringkasan alokasi belanja dan program.'),('Transparansi','Informasi untuk mendukung keterbukaan anggaran.')]),
'media-sosial.html':('Media Sosial','Halaman lokal daftar kanal media sosial, tidak lagi langsung keluar ke web asli.', [('Facebook','Tempat menampilkan tautan kanal Facebook resmi.'),('Instagram','Tempat menampilkan tautan kanal Instagram resmi.'),('YouTube dan TikTok','Tempat menampilkan tautan video dan konten singkat.')])
}
for f,args in pages.items(): page(f,*args)
