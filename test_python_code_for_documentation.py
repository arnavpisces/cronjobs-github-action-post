"""
Example docstring for generating documentation

1. **First** - Enclose word in double asterisks for bold
2. **Second** - Use numbers for points
"""

# === print ===
def print_text(text="hello world"):
    print(text)
    """
    A method to print text or hello world
    """
    
# === generator ===
def ListGenerator(num):
    """
    A method that returns a list from 0 to num-1
    """
    a = [x for x in range(num)]
    return a
