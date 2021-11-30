#######################################
# Targil-2   09-09-2020   Uri Inbar   #
#######################################
def clean_text(text_to_clean):
    cleaned_text = ''
    for t in text_to_clean:
      if t in string.ascii_letters:
        cleaned_text += t
      else:
        cleaned_text += ' '
    return cleaned_text
#######################################
def count_letters_in_each_word(text_after_clean):
#    words_len = []
#    for word in text_after_clean:
#      words_len.append(len(word))
    words_len = [ len(word) for word in text_after_clean ]
    return words_len
#######################################
def count_words_of_length(lengths_list, desired_length):
    return lengths_list.count(desired_length)
#######################################
def word_most_appears(text_after_clean):
  dic_word_appears = {}
  word_most_name   = ''
  word_most_times  = 0
# compute word most appears
  for word in text_after_clean:
    if word in dic_word_appears:
      dic_word_appears[word] +=1
      if dic_word_appears[word] > word_most_times:
        word_most_name  = word
        word_most_times = dic_word_appears[word]
    else:
      dic_word_appears[word] = 1
#
  print('***********************************')
  print('dic_word_appears=\n',dic_word_appears)
  return word_most_name, word_most_times
#######################################
#               main                  #
#######################################
import string
#
initial_text = '''Down, down, down. Would the fall _never_ come to an end? "I wonder how
many miles I've fallen by this time?" she said aloud. "I must be
getting somewhere near the centre of the earth. Let me see: that would
be four thousand miles down, I think�" (for, you see, Alice had learnt
several things of this sort in her lessons in the schoolroom, and
though this was not a _very_ good opportunity for showing off her
knowledge, as there was no one to listen to her, still it was good
practice to say it over) "�yes, that's about the right distance�but
then I wonder what Latitude or Longitude I've got to?" (Alice had no
idea what Latitude was, or Longitude either, but thought they were nice
grand words to say.)'''
#=======================================
# clean text
print('text_before_clean=\n',initial_text,'\n')
text_after_clean = clean_text(initial_text).split()
print('text_after_clean=\n',text_after_clean,'\n')
#=======================================
# count letters
length_lists = count_letters_in_each_word(text_after_clean)
print('length_lists=\n',length_lists,'\n')
#=======================================
# user input
while 1:
  desired_len = int(input("Enter desired len - 0 to finish: "))
  if desired_len == 0:
    break
  count = count_words_of_length(length_lists, desired_len)
  print('There are: ' + str(count) +' such words.\n')
#
print('***********************************')
#=======================================
# convert text_after_clean to UPPERcase
#for i in range (len(text_after_clean)):
#  text_after_clean[i]= text_after_clean[i].upper()
text_after_clean = [ i.upper() for i in text_after_clean ]
print('text_after_clean AFTER UPPERcase=\n',text_after_clean)
#=======================================
# find the most word appears in the text
most_name   = ''
most_times  = 0
most_name, most_times = word_most_appears(text_after_clean)
print('***********************************')
print('word_most_name  = ',most_name)
print('word_most_times = ',most_times)
#=======================================
# end of program
#=======================================


