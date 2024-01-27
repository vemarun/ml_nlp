import re

pattern1='hello'
input_text='hello did you get pattern'
out=re.match(pattern1,input_text)
if out:
    print('pattern matched')
else:
    print('pattern not matched')
    
input_sentence='roll no 7 is doing better than roll no 8'
pattern2='\d+'
out=re.findall(pattern2,input_sentence)
print(out) 