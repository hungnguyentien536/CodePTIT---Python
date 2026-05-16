import re
import sys

text = sys.stdin.read()

sentences = re.split(r'[.!?]', text)

result = []

for s in sentences:
    s = ' '.join(s.strip().split()) 
    
    if s and any(c.isalnum() for c in s):
        s = s.lower().capitalize()
        result.append(s)

print('\n'.join(result))
