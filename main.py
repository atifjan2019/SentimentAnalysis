#removing punctuation from data and make it lower case
import string
text = open('read.txt',encoding='utf-8').read()
lower_case = text.lower()
# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
# splitting text into words
tokemized_words = cleaned_text.split()

