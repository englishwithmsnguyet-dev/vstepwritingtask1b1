import re

def preProcess(t):
    # Normalize ellipsis
    t = re.sub(r'…', '...', t)
    t = re.sub(r'\.\s*\.\s*\.', '...', t)
    # Normalize quotes
    t = re.sub(r"[’‘]", "'", t)
    t = re.sub(r'[“”]', '"', t)
    # Normalize dashes and hyphens with surrounding spaces
    t = re.sub(r'\s*[-\u2010\u2011\u2013\u2014\u2212]+\s*', ' - ', t)
    return t

def diffWords(userText, targetText):
    uWords = [w for w in preProcess(userText).strip().split() if w]
    tWords = [w for w in preProcess(targetText).strip().split() if w]
    print("User words:", uWords)
    print("Target words:", tWords)
    print("Match:", uWords == tWords)
    print("-" * 40)

# Test cases
diffWords(
    "I hope you will consider [hành động - Ving].",
    "I hope you will consider [hành động – Ving]."
)

diffWords(
    "I hope you will consider [hành động-Ving].",
    "I hope you will consider [hành động – Ving]."
)

diffWords(
    "well-known",
    "well – known"
)
