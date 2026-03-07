"""Program to get a response from Bob"""
def response(hey_bob):
    "Bob's response function"
    
    if check_question(hey_bob) and check_all_caps(hey_bob):
        return "Calm down, I know what I'm doing!"
        
    if check_all_caps(hey_bob):
        return "Whoa, chill out!"
        
    if check_question(hey_bob):
        return "Sure."

    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    
    return "Whatever."

def check_question(hey_bob):
    return hey_bob.strip().endswith("?")

def check_all_caps(hey_bob):
    return hey_bob.isupper()
