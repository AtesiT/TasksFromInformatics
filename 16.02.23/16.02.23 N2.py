#2        Отредактировать заданное предложение, удаляя из него те слова, которые встречаются в предложении заданное число раз.

# anySentence = 'privet kak dela privet privet'
# space = ' '
# anySentenceInArray = (anySentence.split())

# i = 0
# amountWords = 0


def remove_words(sentence, count):
    words = sentence.split()
    
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    filtered_words = [word for word in words if word_count[word] != count]
    
    filtered_sentence = " ".join(filtered_words)
    
    return filtered_sentence

sentence = "this is a sample sentence with some words repeated words"
count = 2
filtered_sentence = remove_words(sentence, count)
print(filtered_sentence)


# while i < len(anySentenceInArray):
#     j = 0
#     while j < len(anySentenceInArray):
#         if anySentenceInArray[i] == anySentenceInArray[j]:
#             amountWords += 1
#             del anySentenceInArray[j]
#         j+=1
#     i+=1
# print(anySentenceInArray)


# print(amountWords)

# for symbol in anySentence:
#     if 