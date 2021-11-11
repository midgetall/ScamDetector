"""
Nishants First program 
"""
print("Nishants First Program")

"""
This program will detect scam emails:)
An email is a scam if it has a suspicous keyword. 
The email is there, so the keywords will be run through and checked for detection.
The email is in a file. 
Step 1: Open the file 
Step 2: Read the file
Step 3: Check file for keywords
Step 4:Show that the keyword/s has/have been detected
"""
#Step 1:
with open("/Users/pcasuser/dev/github_others/ScamDetector/info.txt", "r") as file:
    data = file.read().replace('\n', '')

print(data)
#Shows text clearly

if "solicit" in data:
    print("true")








