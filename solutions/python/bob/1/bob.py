def response(hey_bob):
    bob = hey_bob.strip()
    
    if not bob:
        return "Fine. Be that way!"
    
    yell = bob.isupper()
    ques = bob.endswith('?')

    if yell and ques:
        return "Calm down, I know what I'm doing!" 
    elif yell:
        return "Whoa, chill out!"
    elif ques:
        return "Sure."
    else:
        return "Whatever."