from PIL import Image
import pytesseract as p
img=Image.open("input_image.jpg")
text=p.image_to_string(img)
print(text)

file1 = open("output_file.txt","w")
# to append more lines
L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
  
# \n is placed to indicate EOL (End of Line)
file1.write(text)
file1.writelines(L)
file1.close() #to change file access modes
  
file1 = open("output_file.txt","r+") 
  
print("Output of Read function is ")
print(file1.read())
print()
file1.close()