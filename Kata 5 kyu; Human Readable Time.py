#Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

#HH = hours, padded to 2 digits, range: 00 - 99
#MM = minutes, padded to 2 digits, range: 00 - 59
#SS = seconds, padded to 2 digits, range: 00 - 59
#The maximum time never exceeds 359999 (99:59:59)

#You can find some examples in the test fixtures.

def make_readable(seconds):
    s = str(seconds % 60).zfill(2)
    m = str((seconds // 60)%60).zfill(2)
    h = str((seconds // 3600)%100).zfill(2)
    return f"{h}:{m}:{s}"
