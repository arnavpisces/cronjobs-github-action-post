"""
Example docstring for generating documentation

1. **First** - Enclose word in double asterisks for bold
2. **Second** - For numbered points
"""

# === print ===
def print_text(text="hello world"):
    print(text)

# === generator ===
def ListGenerator(num):
    """
    A method that returns a list from 0 to num-1
    """
    a = [x for x in range(num)]
    return a
