import os
print("-------------------------------MORSE CODE TRANSLATOR----------------------------------")
print("1 - English to Morse code")
print("2 - Morse code to English")
n = int(input("Enter your choice[1-2]"))
if(n==1):
    print("Enter text content(in English,one sentence per line)")
    print("For reference (English - Morse code)")
    choice = input("Enter yes[y] or No[n]")
    if(choice=='y'):
        os.startfile(r"C:\Users\mohoith\PycharmProjects\Project\Morse Code - English.txt")
    elif(choice=='n'):
        print("continue")
    my_file=open("INPUT_FILE.txt","w")
    ans='y'
    while ans=='y':
        sentence=input("Enter a sentence")
        my_file.write(sentence)
        my_file.write("\n")
        ans = input("Do you want to enter one more sentence?(y/n)")
        if(ans=='n'):
            break
    my_file.close()
    with open("INPUT_FILE.txt","r") as myfile:
        contents = myfile.readlines()
    print(contents)
    myfile.close()
    file=open("OUTPUT_FILE.txt","w")
    for i in contents:
        new_str=""
        for j in i:
            if j=='a':
                morse_code=".-"
                new_str=new_str+morse_code
            if j=='b':
                morse_code="-..."
                new_str=new_str+morse_code
            if j=='c':
                morse_code="-.-."
                new_str=new_str+morse_code
            if j=='d':
                morse_code="-.."
                new_str=new_str+morse_code
            if j=='e':
                morse_code="-...-"
                new_str=new_str+morse_code
            if j=='f':
                morse_code="..-."
                new_str=new_str+morse_code
            if j=='g':
                morse_code="--."
                new_str=new_str+morse_code
            if j=='h':
                morse_code="...."
                new_str=new_str+morse_code
            if j=='i':
                morse_code=".."
                new_str=new_str+morse_code
            if j=='j':
                morse_code=".---"
                new_str=new_str+morse_code
            if j=='k':
                morse_code="-.-"
                new_str=new_str+morse_code
            if j=='l':
                morse_code=".-.."
                new_str=new_str+morse_code
            if j=='m':
                morse_code="--"
                new_str=new_str+morse_code
            if j=='n':
                morse_code="-."
                new_str=new_str+morse_code
            if j=='o':
                morse_code="---"
                new_str=new_str+morse_code
            if j=='p':
                morse_code=".--."
                new_str=new_str+morse_code
            if j=='q':
                morse_code="--.-"
                new_str=new_str+morse_code
            if j=='r':
                morse_code=".-."
                new_str=new_str+morse_code
            if j=='s':
                morse_code="..."
                new_str=new_str+morse_code
            if j=='t':
                morse_code="-"
                new_str=new_str+morse_code
            if j=='u':
                morse_code="..-"
                new_str=new_str+morse_code
            if j=='v':
                morse_code="...-"
                new_str=new_str+morse_code
            if j=='w':
                morse_code=".--"
                new_str=new_str+morse_code
            if j=='x':
                morse_code="-..-"
                new_str=new_str+morse_code
            if j=='y':
                morse_code="-.--"
                new_str=new_str+morse_code
            if j=='z':
                morse_code="--.."
                new_str=new_str+morse_code
            if j=='1':
                morse_code=".----"
                new_str=new_str+morse_code
            if j=='2':
                morse_code="..---"
                new_str=new_str+morse_code
            if j=='3':
                morse_code="...--"
                new_str=new_str+morse_code
            if j=='4':
                morse_code="....-"
                new_str=new_str+morse_code
            if j=='5':
                morse_code="....."
                new_str=new_str+morse_code
            if j=='6':
                morse_code="-...."
                new_str=new_str+morse_code
            if j=='7':
                morse_code="--..."
                new_str=new_str+morse_code
            if j=='8':
                morse_code="---.."
                new_str=new_str+morse_code
            if j=='9':
                morse_code="----."
                new_str=new_str+morse_code
            if j=='0':
                morse_code="-----"
                new_str=new_str+morse_code
            if j=='.':
                morse_code=".-.-.-"
                new_str=new_str+morse_code
            if j==',':
                morse_code="--..--"
                new_str=new_str+morse_code
            if j=='?':
                morse_code="..--.."
                new_str=new_str+morse_code
            if j=='(':
                morse_code="-.--."
                new_str=new_str+morse_code
            if j==')':
                morse_code="-.--.-"
                new_str=new_str+morse_code
            if j=='-':
                morse_code="-....-"
                new_str=new_str+morse_code
            if j=='"':
                morse_code=".-..-."
                new_str=new_str+morse_code
            if j=='_':
                morse_code="..--.-"
                new_str=new_str+morse_code
            if j=="'":
                morse_code=".----."
                new_str=new_str+morse_code
            if j==' ':
                morse_code="......"
                new_str=new_str+morse_code
        file.write(new_str)
        file.write("\n")
    file.close()
elif (n==2):
    print("Enter message in Morse code(one encoded character per line, with end of word indicated by a blank line"
          " and end of sentence indicated by two blank lines ")
    print("For reference (Morse code - English)")
    choice = input("Enter yes[y] or No[n]")
    if(choice=='y'):
        os.startfile(r"C:\Users\mohoith\PycharmProjects\Project\Morse Code - English.txt")
    elif(choice=='n'):
        print("continue")
    file = open("INPUT_FILE.txt","w")
    ans = 'y'
    while ans=='y':
        code = input("Enter an encoded character")
        if code is not '.' :
            file.write(code)
            file.write("\n")
        if(code=='.'):
            file.write("\n\n")
        ans = input("Do you wish to enter one more character?[y/n]")
        if(ans=='n'):
            break
    file.close()
    with open("INPUT_FILE.txt","r") as FILE:
        content = FILE.readlines()
    print(content)
    files = open("OUTPUT_FILE.txt","w")
    for i in range(len(content)-1):
        chr=""
        str=""
        for j in range(len(content[i])):
            chr=chr+content[i][j]
        if(chr=="\n"):
            str=str+'.'
        if(chr==" \n"):
            str=str+' '
        if(chr==".-\n"):
            str=str+'a'
        if(chr=="-...\n"):
            str=str+'b'
        if(chr=="-.-.\n"):
            str=str+'c'
        if(chr=="-..\n"):
            str=str+'d'
        if(chr=="-...-\n"):
            str=str+'e'
        if(chr=="..-.\n"):
            str=str+'f'
        if(chr=="--.\n"):
            str=str+'g'
        if(chr=="....\n"):
            str=str+'h'
        if(chr=="..\n"):
            str=str+'i'
        if(chr==".---\n"):
            str=str+'j'
        if(chr=="-.-\n"):
            str=str+'k'
        if(chr==".-..\n"):
            str=str+'l'
        if(chr=="--\n"):
            str=str+'m'
        if(chr=="-.\n"):
            str=str+'n'
        if(chr=="---\n"):
            str=str+'o'
        if(chr==".--.\n"):
            str=str+'p'
        if(chr=="--.-\n"):
            str=str+'q'
        if(chr==".-.\n"):
            str=str+'r'
        if(chr=="...\n"):
            str=str+'s'
        if(chr=="-\n"):
            str=str+'t'
        if(chr=="..-\n"):
            str=str+'u'
        if(chr=="...-\n"):
            str=str+'v'
        if(chr==".--\n"):
            str=str+'w'
        if(chr=="-..-\n"):
            str=str+'x'
        if(chr=="-.--\n"):
            str=str+'y'
        if(chr=="--..\n"):
            str=str+'z'
        if(chr==".----\n"):
            str=str+'1'
        if(chr=="..---\n"):
            str=str+'2'
        if(chr=="...--\n"):
            str=str+'3'
        if(chr=="....-\n"):
            str=str+'4'
        if(chr==".....\n"):
            str=str+'5'
        if(chr=="-....\n"):
            str=str+'6'
        if(chr=="--...\n"):
            str=str+'7'
        if(chr=="---..\n"):
            str=str+'8'
        if(chr=="----.\n"):
            str=str+'9'
        if(chr=="-----\n"):
            str=str+'0'
        if(chr==".-.-.-\n"):
            str=str+'.'
        if(chr=="--..--\n"):
            str=str+','
        if(chr=="..--..\n"):
            str=str+'?'
        if(chr=="-.--.\n"):
            str=str+'('
        if(chr=="-.--.-\n"):
            str=str+')'
        if(chr=="-....-\n"):
            str=str+'-'
        if(chr==".-..-.\n"):
            str=str+'"'
        if(chr=="..--.-\n"):
            str=str+'_'
        if(chr==".----.\n"):
            str=str+"'"
        files.write(str)
    files.close()
else:
    print("Invalid choice")





















