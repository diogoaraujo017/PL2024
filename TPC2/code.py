import os 
import re

htmlcode = """
<!DOCTYPE html>
<html>

 <head>
 <title>TPC2</title>
 </head>

 <body>
"""

# Open the file 
inputfile = open("TPC2/input.md", "r")

# Read the text from the file
textToTransform = inputfile.read()

# Changing # to h1
textToTransform = re.sub(r'^#{1}( .*)$', r'<h1>\1</h1>',textToTransform, flags=re.MULTILINE)
# Changing ## to h
textToTransform = re.sub(r'^#{2}( .*)$', r'<h2>\1</h2>',textToTransform, flags=re.MULTILINE)
# Changing ### to h3
textToTransform = re.sub(r'^#{3}( .*)$', r'<h3>\1</h3>',textToTransform, flags=re.MULTILINE)
# Changing ** to bold
textToTransform = re.sub(r'\*{2}\b(.*?)\*{2}', r'<b>\1</b>',textToTransform)
# Changing * to italic
textToTransform = re.sub(r'\*([^\*]*)\*', r'<i>\1</i>',textToTransform, flags=re.MULTILINE)
# Changing [text](link) to <a href="link">text</a>
textToTransform = re.sub(r' \[([^\]]*)\]\(([^\)]*)\)', r' <a href="\2">\1</a>',textToTransform, flags=re.MULTILINE)
# Changing ![text](link) to <img src="link" alt="text">
textToTransform = re.sub(r'!\[([^\]]*)\]\(([^\)]*)\)', r'<img src="\2" alt="\1"/>',textToTransform, flags=re.MULTILINE)
# Changing lista numera to <ol> <li></li> .... <li></li> </ol>
textToTransform = re.sub(r'^[0-9]+\. *(.+)$', r'<li>\1</li>',textToTransform, flags=re.MULTILINE)
textToTransform = re.sub(r'((<li>.*<\/li>)+)', r'<ol>\1</ol>',textToTransform)

# Addind the modified html code
htmlcode += textToTransform

# Conclude the html code
htmlcode += """
 </body> 
</html>    
"""
            
htmlFile = open("TPC2/output.html", "w")
htmlFile.write(htmlcode)    
htmlFile.close()            


