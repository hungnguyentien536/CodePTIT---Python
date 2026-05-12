import re
import sys

# Đọc toàn bộ input
text = sys.stdin.read()

# Tách câu
sentences = re.split(r'[.!?]', text)

result = []

for s in sentences:
    s = ' '.join(s.strip().split())  # chuẩn hóa khoảng trắng
    
    if s and any(c.isalnum() for c in s):
        s = s.lower().capitalize()
        result.append(s)

# In kết quả
print('\n'.join(result))