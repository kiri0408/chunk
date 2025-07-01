import re

def remove_trailing_empty_lines(text):
    lines = text.splitlines()
    while lines and re.match(r'^\s*$', lines[-1]):
        lines.pop()
    return '\n'.join(lines)

# 使用例
original_text = """This is the first line
Second line
Third line

   
"""

result = remove_trailing_empty_lines(original_text)
print(result)
