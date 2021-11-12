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

print(type(data))

print(data)
#Shows text clearly

print(data.lower())

if "nigeria" in data.lower():
    print("It appears you have gotten a Nigerian Prince Scam. The best course of action is to ignore this scam email.")

if "request" in data.lower():
    print("Potential SCAM:(")
else:
    if "follow up" in data.lower():
        print("Potential SCAM:(")
    else:
        if "urgent" in data.lower():
            print("Potential SCAM:(")
        else:
            if "important" in data.lower():
                print("Potential SCAM:(")
            else:
                if "are you available" in data.lower():
                    print("Potential SCAM:(")
                else:
                    if "are you at your desk" in data.lower():
                        print("Potential SCAM:(")
                    else:
                        if "payment" in data.lower():
                            print("Potential SCAM:(")
                        else:
                            if "status" in data.lower():
                                print("Potential SCAM:(")
                            else:
                                if "purchase" in data.lower():
                                    print("Potential SCAM:(")
                                else:
                                    if "invoice due" in data.lower():
                                        print("Potential SCAM:(")
                                    else:
                                        if "direct deposit" in data.lower():
                                            print("Potential SCAM:(")
                                        else:
                                            if "expenses" in data.lower():
                                                print("Potential SCAM:(")
                                            else:
                                                if "payroll" in data.lower():
                                                    print("Potential SCAM:(")
                                                else:
                                                    if "transfer" in data.lower():
                                                        print("Potential SCAM:(")
                                                    else:
                                                        if "funds" in data.lower():
                                                            print("Potential SCAM:(")












