import os

def install_requirements():
    try:
        print("Menginstall modul yang diperlukan...")
        os.system("pip install -r requirements.txt")
        print("Instalasi selesai.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menginstall modul: {e}")

if __name__ == "__main__":
    install_requirements()

