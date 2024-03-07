# topic-3:buffer read and write 
# different from other files is that it is going to write and read in chunks

import io
with open("test10.txt", "wb") as f:
    file=io.BufferedWriter(f)
    file.write(b"hello world\n")
    file.write(b"explain\n")
    file.flush()

with open("test10.txt", "rb") as f:
    file=io.BufferedReader(f)
    data=file.read(10)
    print(data) 