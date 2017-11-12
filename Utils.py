class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Unicode:
    digit_subscripts =   '₀₁₂₃₄₅₆₇₈₉'
    digit_superscripts = '⁰¹²³⁴⁵⁶⁷⁸⁹'

def to_subscript(n):
    s = ''
    for digit in str(n):
        s += Unicode.digit_subscripts[int(digit)]
    return s