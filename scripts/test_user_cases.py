import re

def preProcess(t):
    # Normalize ellipsis
    t = re.sub(r'…', '...', t)
    t = re.sub(r'\.\s*\.\s*\./g', '...', t)
    # Normalize quotes
    t = re.sub(r"[’‘]", "'", t)
    t = re.sub(r'[“”]', '"', t)
    # Normalize dashes and hyphens with surrounding spaces
    t = re.sub(r'\s*[-\u2010\u2011\u2013\u2014\u2212]+\s*', ' - ', t)
    return t

def diffWords(userText, targetText):
    uWords = [w for w in preProcess(userText).strip().split() if w]
    tWords = [w for w in preProcess(targetText).strip().split() if w]
    print(f"Comparing:")
    print(f"  User:   '{userText}'")
    print(f"  Target: '{targetText}'")
    print(f"  Match:  {uWords == tWords}")
    print("-" * 50)

# The user's specific examples
target = "I hope you will consider [hành động – Ving]."

# Case 1: [hành động-Ving]
diffWords("I hope you will consider [hành động-Ving].", target)

# Case 2: [hành động  –  Ving]
diffWords("I hope you will consider [hành động  –  Ving].", target)

# Case 3: [hành động - Ving]
diffWords("I hope you will consider [hành động - Ving].", target)
