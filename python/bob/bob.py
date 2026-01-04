def response(hey_bob):
    stripped = hey_bob.strip()
    
    if stripped == "":
        return "Fine. Be that way!"
    
    if stripped.isupper() and stripped.endswith("?"):
        return "Calm down, I know what I'm doing!"
    
    if stripped.isupper():
        return "Whoa, chill out!"
    
    if stripped.endswith("?"):
        return "Sure."
    
    return "Whatever."
