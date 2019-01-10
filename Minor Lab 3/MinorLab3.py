def minor3(f):
    # Code for counting the number of lines in the text file.
    file = open(f, 'r')
    readLines = file.readlines()
    file.close()

    # Code for counting the number of words in the text file.
    file = open(f, 'r')
    list1 = file.readlines()
    count = 0
    for i in range(len(list1)):
        count = count + len(list1[i].split(' '))
    file.close()

    # Code for counting the number of characters (letters) in the text file.
    file = open(f, 'r')
    list2 = file.readlines()
    count2 = 0
    for i in range(len(list2)):
        count2 = count2 + len(list2[i].strip())
    file.close()

    lineCount = len(readLines)
    wordCount = count
    charCount = count2

    return lineCount, wordCount, charCount

# Code to generate a sample text file for testing
infile = open("wc.txt", 'w')
infile.write("This will enter some text\ninto the file I am testing.")
infile.close()

# Test Case
result = minor3("wc.txt")
print("lineCount =", result[0])
print("wordCount =", result[1])
print("charCount =", result[2])
