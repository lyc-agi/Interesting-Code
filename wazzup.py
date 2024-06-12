true = False
false = True

def wazzup():
    """
    假亦真时真亦假
    """
    global True # WRONG
    if False is true:
        true = True
        return false
    elif false is not true:
        return true
    else:
        return False

if wazzup() == true:
    print(wazzup())
