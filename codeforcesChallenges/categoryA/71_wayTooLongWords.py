def abbreviation(wordToCheck):
    if len(wordToCheck) < 11:
        return wordToCheck
    else:
        lengthString = len(wordToCheck) - 2
        firstCharacter = wordToCheck[0]
        lastCharacter = wordToCheck[-1]
        return firstCharacter + str(lengthString) + lastCharacter


testCases = int(input())

for i in range(testCases):
    word = input()
    print(abbreviation(word))
