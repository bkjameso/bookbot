#this function is to return charcter count for sorting
def get_count(item):
   return item["num"]


def character_count(text):
  letter_count = {}
  for c in text:
    lower_case = c.lower()
    if lower_case in letter_count:
        letter_count[lower_case] += 1
    else :
        letter_count[lower_case] = 1 
  return letter_count

def word_count(text):
  words = text.split()
  return len(words)
# splits up words and counts them

def main():
 with open("books/frankenstien.txt") as f:
    file_contents = f.read()
    print(file_contents)

    num_words = word_count(file_contents)
    letter_counts = character_count(file_contents)
    #covert dic to list of dics
    char_list = [{"char": char, "num": count} for char, count in letter_counts.items()] 
   # this is so they print in a deceding order. 
    char_list.sort(key=get_count, reverse=True)

    #prnting the report
    print(f"--- Begin report of books/frankenstien.txt ---")
    print(f"{num_words} words found in the document\n")

    for item in char_list:
        char, count = item["char"], item["num"]
        if char.isalpha():
            print(f"The'{char}'character was found {count} times")

    print(f"--- End report ---")
if __name__ == "__main__":
  main()
# prints frankenstien



 


  
  
  

