def game_utama():
    print("--- MEMULAI PETUALANGAN DIGITAL ---")
    nama = input("Siapa namamu? ")
    
    print(f"\n🏝️  Selamat datang, {nama}!")
    print("=" * 50)
    print("\nAnda terbangun di sebuah pulau misterius yang penuh dengan hutan lebat.")
    print("Suara-suara aneh terdengar dari kejauhan... itu adalah orang-orang kanibal!")
    print("Anda harus menemukan cara untuk melarikan diri dari pulau yang menakutkan ini.")
    print("\n" + "=" * 50)
    print("\n⚠️  PILIHAN JALUR ESCAPE ⚠️")
    print("1. Membuat Perahu Coding - Kumpulkan kayu dan buat perahu dengan teknik coding")
    print("2. Berenang Bug - Cepat-cepat berenang meninggalkan pulau sebelum ketahuan")
    print("3. Menjelajahi Pulau - Cari harta karun dan sumber daya tersembunyi")
    
    pilihan = input("\nPilihan Anda (1, 2, atau 3): ")
    
    if pilihan == "1":
        print("\n" + "=" * 50)
        print("🛠️  JALUR: MEMBUAT PERAHU CODING")
        print("=" * 50)
        print(f"\n{nama} memutuskan untuk membuat perahu menggunakan kekuatan coding...")
        print("✔️  Mengumpulkan kayu dari hutan...")
        print("✔️  Menulis algoritma konstruksi...")
        print("✔️  Menggunakan Python untuk menghitung struktur yang kuat...")
        print(f"\n🎉 Berhasil! Perahu {nama} selesai dibuat dengan sempurna!")
        print("⛵ Anda berlayar menjauh dari pulau berbahaya ini.")
        print("\n✅ SELAMAT! Anda berhasil melarikan diri dengan perahu yang kokoh!")
        print(f"   {nama} telah menyelamatkan diri dari pulau kanibal! 🎊")
        
    elif pilihan == "2":
        print("\n" + "=" * 50)
        print("🏊 JALUR: BERENANG BUG")
        print("=" * 50)
        print(f"\n{nama} memutuskan untuk segera berenang meninggalkan pulau...")
        print("⚡ Berlari cepat ke tepi pantai...")
        print("🌊 Melompat ke laut dan mulai berenang dengan kencang...")
        print("👀 Mendengar suara kaki orang kanibal di belakang...")
        print("💨 Berenang semakin cepat meninggalkan pulau...")
        print("\n🎉 Berhasil! Anda lolos!!")
        print("🏊 Anda terapung di laut dan ditemukan oleh kapal penyelamat!")
        print("\n✅ SELAMAT! Anda berhasil melarikan diri dengan cepat!")
        print(f"   {nama} telah selamat dari pulau kanibal! 🎊")
        
    elif pilihan == "3":
        print("\n" + "=" * 50)
        print("🗺️  JALUR: MENJELAJAHI PULAU")
        print("=" * 50)
        print(f"\n{nama} memutuskan untuk menjelajahi pulau dan mencari sumber daya berharga...")
        print("\n🔦 Berjalan menembus hutan yang lebat dengan hati-hati...")
        print("📍 Menemukan sebuah gua misterius!")
        print("\n⭐ PILIHAN EKSPLORASI:")
        print("a. Masuk ke dalam gua - Mungkin ada harta karun!")
        print("b. Mendengarkan suara dari gua - Terdengar seperti air terjun!")
        
        sub_pilihan = input("\nPilihan eksplorasi Anda (a atau b): ")
        
        if sub_pilihan == "a":
            print(f"\n{nama} berani masuk ke dalam gua yang gelap...")
            print("✔️  Menyalakan api untuk menerangi gua...")
            print("💎 Menemukan harta karun: emas, permata, dan peta harta!")
            print("📜 Peta menunjukkan lokasi perahu pelarian yang sudah siap!")
            print("\n🎉 Jackpot! Semua yang " + nama + " butuhkan ada di gua!")
            print("⛵ Mengikuti peta dan menemukan perahu yang sudah dilengkapi makanan!")
            print("\n✅ SELAMAT! Anda berhasil melarikan diri dengan harta karun!")
            print(f"   {nama} kaya raya dan selamat dari pulau kanibal! 💰🎊")
        elif sub_pilihan == "b":
            print(f"\n{nama} mengikuti suara air terjun ke dalam gua...")
            print("💧 Menemukan air tawar yang jernih!")
            print("🐠 Kolam ikan besar penuh dengan makanan lezat!")
            print("✔️  Mengumpulkan makanan dan air tawar untuk perjalanan...")
            print("🎒 Bersiap dengan perbekalan yang cukup...")
            print("🌳 Kembali keluar dan menemukan pohon kelapa yang penuh buah!")
            print("🛠️  Menggunakan kelapa untuk membuat tali dan kayu untuk perahu buatan!")
            print("\n🎉 Berhasil! Perahu sederhana tapi kuat berhasil dibuat!")
            print("⛵ Berlayar dengan penuh semangat meninggalkan pulau berbahaya!")
            print("\n✅ SELAMAT! Anda berhasil survive dan melarikan diri!")
            print(f"   {nama} keluar dari pulau dengan strategi jitu! 🎊")
        else:
            print("\n❌ Pilihan eksplorasi tidak valid! Orang kanibal mendengar suara Anda!")
            print(f"   {nama} tidak berhasil melarikan diri. GAME OVER! 💀")
        
    else:
        print("\n❌ Pilihan tidak valid! Anda terlalu lama mempertimbangkan dan orang kanibal menemukan Anda!")
        print(f"   {nama} tidak berhasil melarikan diri. GAME OVER! 💀")
    
if __name__ == "__main__":
    game_utama()