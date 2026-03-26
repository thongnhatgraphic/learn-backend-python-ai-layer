with  open("file_example.txt", "r") as f:
    contentRead = f.read()


print(contentRead)



with open("file_example.txt", "w") as f:
    f.write("Hello world Only write")