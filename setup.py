import gdown

destination = 'https://drive.google.com/drive/folders/10Yw5jYIWY1l8pn3yTnkbAD5OlTiNqc34?usp=drive_link'

print(f"Downloading to '{destination}'...")
gdown.download_folder(destination)
print("Download completed successfully.")
