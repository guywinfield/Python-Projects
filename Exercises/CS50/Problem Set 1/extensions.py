def main():
    file_type = input("File name: ")
    print(file_check(file_type))

def file_check(x):
    x = x.strip().lower()

    # Check to see if file is image type
    if x.endswith((".jpg",".jpeg")):
        y = "image/jpeg"

    elif x.endswith((".gif",".png")):
        # Logically if it's an image type it will be split by a ".". We take the last entry in the list as the final format type
        y = "image/" + x.split('.',maxsplit = 2)[-1]

    elif x.endswith((".pdf",".zip")):
        y = "application/" + x.split('.',maxsplit = 2)[-1]

    elif x.endswith((".txt")):
        y = "text/" + x.split('.',maxsplit = 2)[0]

    else:
        y = "application/octet-stream"

    return y

main()
