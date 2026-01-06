import requests
import os


file_urls = [f"https://dummyimage.com/{i}.png" for i in range(300, 306)]


def download_file(file_url, cookies, headers):
    file_name = os.path.basename(file_url)
    file_path = os.path.join("downloads", file_name)
    print(f"Downloading {file_name} ... ")

    response = requests.get(file_url, cookies=cookies, headers=headers)
    with open(file_path,"wb") as f:
        f.write(response.content)
    print(f"{file_name} download successfully")


if not os.path.exists("downloads"):
    os.makedirs("downloads")


for file_url in file_urls:
    download_file(file_url, {}, {})

print("all files downloaded successfully")
