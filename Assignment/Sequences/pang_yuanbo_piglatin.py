# pang_yuanbo_piglatin.py This program translates a sentence into Pig Latin. The user is prompted to enter a
# sentence, and the program displays the Pig Latin translation of the sentence. The program continues to prompt the
# user for sentences until the user presses ENTER without entering any text.


def pig_latin(word):
    vowels = 'aeiouy'
    word = word.lower()
    # For this program, we ignore punctuation and assume words have no punctuation

    if word[0] in vowels:
        return word + 'way'
    else:
        # Move consonants from the beginning to the end until a vowel is encountered
        index = 0
        while index < len(word) and word[index] not in vowels:
            index += 1
        if index == len(word):
            # Word has no vowels
            return word + 'ay'
        else:
            return word[index:] + word[:index] + 'ay'


def pig_latin_sentence(sentence):
    words = sentence.strip().split()
    pig_latin_words = [pig_latin(word) for word in words]
    return ' '.join(pig_latin_words)


def main():
    while True:
        sentence = input("Enter a sentence (or press ENTER to quit): ")
        if sentence == '':
            break
        else:
            pig_latin_translation = pig_latin_sentence(sentence)
            print(pig_latin_translation)


if __name__ == '__main__':
    main()
