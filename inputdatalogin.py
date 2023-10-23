# Meminta pengguna untuk menentukan tempat penyimpanan
file_path = input("Masukkan alamat tempat penyimpanan (contoh: D:\\data\\login.txt): ")

# Memeriksa apakah nama file adalah "login.txt"
if not file_path.endswith("\\login.txt"):
    print("Nama file harus 'login.txt'.")
else:
    existing_data = set()  # Membuat set untuk melacak data yang sudah dimasukkan

    while True:
        # Mencari nomor Login Data terkecil yang tersedia dalam file
        smallest_available_number = 1
        with open(file_path, "r") as data_file:
            for line in data_file:
                if line.startswith("Login Data #"):
                    try:
                        data_number = int(line.split("#")[1])
                        if data_number >= smallest_available_number:
                            smallest_available_number = data_number + 1
                    except ValueError:
                        pass

        # Meminta input username/email dan password dari pengguna
        username_email = input("Username/Email: ")
        password = input("Password: ")

        # Mencetak keluaran dalam format yang diinginkan
        login_data = f"Login Data #{smallest_available_number}\nUsername/Email: {username_email}\nPassword: {password}\n"

        # Memeriksa apakah data sudah ada dalam set
        if login_data in existing_data:
            print("Data ini sudah dimasukkan sebelumnya. Silakan coba lagi.")
        else:
            # Menggabungkan username/email dan password menjadi satu string
            login_data_key = f"Username/Email: {username_email}\nPassword: {password}\n"

            # Memeriksa apakah login_data_key sudah ada dalam set
            if login_data_key in existing_data:
                print("Username/Email dan Password ini sudah dimasukkan sebelumnya. Silakan coba lagi.")
            else:
                existing_data.add(login_data_key)  # Menambahkan data baru ke set
                # Menyimpan data ke lokasi yang ditentukan
                with open(file_path, "a") as data_file:
                    position = data_file.tell()
                    if position != 0:
                        data_file.write("\n" + login_data)
                    else:
                        data_file.write(login_data)

                continue_input = input("Ingin mengisi data login lainnya? (y/n): ")
                if continue_input.lower() != 'y':
                    break
