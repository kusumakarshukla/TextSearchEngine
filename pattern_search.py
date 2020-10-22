import re
pattern1=re.compile("[a-z]*\skusumakar" )
print(pattern1.findall("hello kusumakar how are you kusumakar"))

# Finding every word in the string

pattern2= re.compile(r"\w+")
print("Words-->",pattern2.findall("Hey man how are you?"))

#finding all a's in the list

pattern3=re.compile(r"a*")
print(pattern3.findall("abey kya hai yaar"))

#getting the details of the matches using finditer

iterator=pattern2.finditer("Hey man how are you")
print(iterator)

for i in iterator:
    print(i.groups(),i.span())


#splitting a sentene based on a pattern.

#splitting based on a new line

pattern4=re.compile("\n")
print(pattern4.split("Hey man you are split due to a space\n bye"))

#Replacing a pattern with some other character
pattern5 = re.compile("[0-9]*-[0-9]*-[0-9]*|\s[0-9]*")
print(pattern5.sub("","voldis_log.20-10-2020"))


#Changing all words beginning with a - with A and others not beginning with a - with B

pattern6=re.compile("-")
print(pattern6.sub("A","-1234"))

pattern7 = re.compile("[A-Z]+")
print(pattern7.sub("B","AZ193"))

#changing words surrounded with ** with bold
text="*Hello* how  are  *you*?"
pattern8=re.compile("\*(.*?)\*")
match=pattern8.search(text)
print(match.end(1))
print(match.span(1))
print(match.group(0,1))
print(pattern8.sub("<b>\g<1></b>",text))
print(re.findall(re.escape("$"),("^like$")))


pattern2= re.compile(r"\w+")
print("Words-->",pattern2.findall("Hey man how are you?"))