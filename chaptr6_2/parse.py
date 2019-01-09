from pyperclip import copy,paste
with open("cnotes.txt","r") as f:
    copy("".join(f.readlines()))
g = paste()
g.rstrip('')
text = g.split('\n') #separates the lines.
print(g)
for i in range(len(text)):
   if text[i].startswith(" "):
       
       text[i] = " --> " + text[i].lstrip(" ")
   else:
       text[i] = '\n' + "* " + text[i] 
text.pop(len(text) - 1)
print(text)
copy("\n".join(text)) #converts back to string
with open("cnoteparsed.txt", "w") as f:
     f.write(paste())

  
