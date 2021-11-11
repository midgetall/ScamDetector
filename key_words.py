fh=open("/Users/pcasuser/dev/github_others/ScamDetector/info.txt", "r")

word=input("Enter the word to search: ")

count=1
s=fh.readline()
l=s.upper().split()
foundwordcount=0

while(s):
    if word.upper() in l:
        print("line number:", count,":",s)
        foundwordcount+=1
    if "NIGERIA" in l:
        print("line number:", count,":",s)
        foundwordcount+=1  
        print("It appears you have gotten a Nigerian Prince Scam. The best course of action is to ignore this scam email")     
    count+=1
    s=fh.readline()
    l=s.split()

    

if(foundwordcount==0):
    print("The word is not found in info.txt file")     
