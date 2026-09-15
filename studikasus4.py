produk = {
    "nama": "indomie",
    "harga": "3000",
    "stok": 20
}

while True:
    print("\n=== MENU DATA PRODUK ===")
    print("1. Tampilkan data")
    print("2. Tambah kategori")
    print("3. Ubah harga")
    print("4. Hapus kategori")
    print("5. Keluar")

    pilihan = input("pilih menu: ")

    if pilihan == "1":
        print("\nData produk:")
        print("Nama  :", produk["nama"])
        print("Harga :", produk["harga"])
        print("Stok  :", produk["stok"])

        if "kategori" in produk:
            print("Kategori:", produk["kategori"])

    elif pilihan == "2":
        kategori = input("Masukan kategori produk: ")
        produk["kategori"] = kategori
        print("Kategori berhasil ditambahkan.")

    elif pilihan == "3":
        harga_baru = int(input("Masukkan harga baru: "))
        produk["harga"] = harga_baru
        print("Harga berhasil di ubah.")

    elif pilihan == "4":
        if "kategori" in produk:
            del produk ["kategori"]
            print("Kategoti berhasil dihapus,")
        else:
            print("Data ketegori belum ada.")

    elif pilihan == "5":
        print("\nProgram selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")

print("\n=== DATA PRODUK SETELAH DIUBAH ===")
print(produk)
