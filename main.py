import string
text = open('read.txt',encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
tokemized_words = cleaned_text.split()
print(tokemized_words)
