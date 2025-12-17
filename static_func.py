

def form_key_note(note):
    if len(note) > 20:
        return note[:16]
    else:
        return note

def check_len_note(note):
    if len(note) > 4000:
        return note[:4000]
    return note

def form_capture(capture):
    if len(capture) > 800:
        return capture[:800]
    return capture