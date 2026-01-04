def translate(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # if is a phrase, modify each word
    if ' ' in text:
        words = text.split()
        translated_words = [translate(word) for word in words]
        return ' '.join(translated_words)
    
    # Case 1: Begins with vowel or 'xr'/'yt'
    if text[0] in vowels or text[:2] in {'xr', 'yt'}:
        return text + 'ay'
    
    # Case 2: Found where ends the group of beginner consonants
    # Take 'qu' like a single letter and 'y' like a vowel if it is not a first letter
    consonant_end = 0
    i = 0
    while i < len(text):
        char = text[i]
        
        # If we found 'qu', move both letters
        if i < len(text) - 1 and text[i:i+2] == 'qu':
            consonant_end = i + 2
            i += 2
        # If it's vowel, break
        elif char in vowels:
            break
        # If is 'y' and not is the first letter, break (y is vowel here)
        elif char == 'y' and i > 0:
            break
        # Is consonant, continue
        else:
            consonant_end = i + 1
            i += 1
    
    return text[consonant_end:] + text[:consonant_end] + 'ay'
