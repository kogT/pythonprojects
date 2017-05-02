#import argv from sys module
from sys import argv

#write the first argv argument into script, the second into filename
script, filename = argv

#try to open the file "filename" and save the file object into txt
txt = open(filename)

print "Here's your file %r: " %(filename)

#use the read() command on that file object
print txt.read()
txt.close()


print "Type the Filename again:"
file_again = raw_input("> ")

txt_again=open(file_again)

print txt_again.read()
txt.close()

#   close -- Closes the file. Like File->Save.. in your editor.
#    read -- Reads the contents of the file. You can assign the result to a variable.
#    readline -- Reads just one line of a text file.
#    truncate -- Empties the file. Watch out if you care about the file.
#    write('stuff') -- Writes "stuff" to the file.
