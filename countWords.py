import collections

def wordFrequency(paragraph):
    paragraphWords = paragraph.split()
    frequency = collections.Counter((paragraphWords)).values()
    words = collections.Counter((paragraphWords))
    for word, freq in words.items():
        if freq == max(frequency):
            return(word)

def reverseString(string):
    return string[::-1]

def largestWord(string):
    paragraphWords = paragraph.split()
    largestWord = paragraphWords[0]
    largestWordSize = len(largestWord)
    largestWordIndex = 0
    for i in range(1, len(paragraphWords)):
        if(len(paragraphWords[i]) > largestWordSize):
            largestWord = paragraphWords[i]
            largestWordSize = len(largestWord)
            largestWordIndex = i

    for i in range(1, largestWordIndex):
        if(len(paragraphWords[i]) > largestWordSize):
            largestWord = paragraphWords[i]
            largestWordSize = len(largestWord)
    
    return largestWord


paragraph = "I think one of the hardest things in the world for people to do is to love themselves. If you loved yourself you would take better care of yourself, and respect the things around you because you respect yourself. Even the condition of your home whether clean or dirty can reveal how much you love yourself. Just don't expect someone else to give what you neglect to give yourself which is love. That's why relationships don't work out so well most times. I find it is accommodating to me."
print(wordFrequency(paragraph))

word = "orange"
print(reverseString(word))

print(largestWord(paragraph))
