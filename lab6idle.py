
def word_count(text):
    text_count = text.split(' ')
    count = 0
    for word in text_count:
        count += 1
    return count #adds to the count for each word

def find_longest_word(text):
  text_length = text.split(' ')
  for word in text_length:
    if len(word) > len(text_length):
      text_length = word
      return text_length #returns the longest word so reads the word with the most characters and returns it


def count_substring(text):
    substring = input('Enter a substring to count:')
    if substring in text:
        num_occurences = text.count(substring)
        return num_occurences #asks for substring then runs the function to find the amount of occurences

def extract_unique_words(text):
    unique_words = text.split(' ')
    unique_words1 = []
    for word in unique_words:
       if word not in unique_words1:
           unique_words1.append(word)
    return unique_words1 #makes a new list with all words that only appear once so any other repetitive word is not added

def main():#runs all the functions under while loop with the options printed out
    print('Welcome to the Test Processingf Test')
    text = input('Enter a text:')
    print('Original Text:')
    print(text)
    print()
    while True:
        print('Text Analysis Options:')
        print('1. Word Count')
        print('2. Longest Word')
        print('3. Count of Substring')
        print('4. Unique Words')
        print('5. Exit')
        user_input = int(input('Enter the number of the analysis option (1-5):'))
        if user_input == 1:
            print(word_count(text))
        elif user_input == 2:
            print(find_longest_word(text))
        elif user_input == 3:
            print(count_substring(text))
        elif user_input == 4:
            print(extract_unique_words(text))
        elif user_input == 5:
            quit()







if __name__ == "__main__":
    main()#the main that you call the function

    


