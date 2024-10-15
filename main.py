def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file


file1_name = "TF2_1.txt"
file2_name = "TF2_2.txt"

file_1_w = Open(file1_name, "w")

if file_1_w is not None:
    file_1_w.write(
        "A file is a container for storing data. When we want to read from or write to a file, "
        "we need to open it first. After we're done reading/writing, we need to close the file to "
        "release the resources associated with it. The file is opened in one of two modes: read or write. "
        "The default mode is read, but we can also specify."
    )
    print("Information was successfully added to TF2_1.txt!")
    file_1_w.close()  
    print("File TF2_1.txt was closed!")


file_1_r = Open("TF2_1.txt", "r")
file_2_w = Open("TF2_2.txt", "w")

if file_1_r is not None and file_2_w is not None:
    content = file_1_r.read().replace("\n", "")   
    index = 0
    line_length = 1  

    while index < len(content):
        file_2_w.write(content[index:index + line_length] + "\n")  
        index += line_length
        line_length = line_length + 1 if line_length < 10 else 1   

    file_1_r.close()
    file_2_w.close()

    print("File TF2_1.txt was read and TF2_2.txt was written!")
file_2_r = Open("TF2_2.txt", "r")
if file_2_r is not None:
  for line in file_2_r:
      print(line.strip())
  file_2_r.close()
  print ("File TF2_2.txt was closed!")