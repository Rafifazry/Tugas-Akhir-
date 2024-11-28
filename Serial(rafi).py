import serial.tools.list_ports

# Menemukan dan menampilkan port serial yang tersedia
ports = serial.tools.list_ports.comports()
portsList = [str(port) for port in ports]

print("Port yang tersedia:")
for onePort in portsList:
    print(onePort)

# Meminta pengguna memilih port, misalnya COM4 (hanya nomor)
val = input("Masukkan nomor port yang ingin digunakan (contoh: 4 untuk COM4): ")

# Menetapkan nama port berdasarkan input pengguna
portVar = "COM" + val

# Mengecek apakah port yang dipilih tersedia
if not any(port.startswith(portVar) for port in portsList):
    print(f"Error: {portVar} tidak tersedia.")
else:
    # Inisialisasi koneksi serial
    serialInst = serial.Serial()
    serialInst.baudrate = 115200
    serialInst.port = portVar
    
    try:
        serialInst.open()
        print(f"Terhubung ke {portVar}. Menunggu data...\n")
        
        # Membaca dan menampilkan data yang diterima
        while True:
            if serialInst.in_waiting:
                data = serialInst.readline()
                print(data.decode('utf-8').rstrip('\n'))  # Menampilkan data di terminal
    except Exception as e:
        print(f"Gagal membuka {portVar}: {e}")
    finally:
        # Menutup koneksi jika terjadi kesalahan atau program dihentikan
        serialInst.close()
