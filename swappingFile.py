def swappingFileDta(): 
     
    file1 = open("sample1.txt")
    file2 = open("sample2.txt")

    with open (file1, 'r') as a:
        data_a = a.read()
    with open (file1, 'w') as a:
        a.write(data_b)
    
    with open (file2, 'r') as a:
        data_b = a.read()
    with open (file2, 'w') as a:
        a.write(data_a)
     
file = input("Enter the file name:- ")   
swappingFileDta()
