import os

folder = input('dir: ')
nr = int(input("first photo's number: "), base=10)
files = os.listdir(folder)
quantity = len(files)
pre1 = '  <a href="#img'
pre2 = '''"><img class="thumb" src="''' + str(folder)
pre3 = '''"></a>
  <div class="lightbox" id="img'''
pre4 = '''">
    <a href="#img'''
pre5 = '''" class="light-btn btn-prev">prev</a>
    <a href="#_" class="btn-close">X</a>
    <img src="''' + str(folder)
pre6 = '''">
    <a href="#img'''
pre7 = '''" class="light-btn btn-next">next</a>
  </div>
'''
text = 'Sample Text to Save\nNew line!'
output = str(folder) + '.txt'
# notifies Python that you are opening this file, with the intention to write
saveFile = open(output,'w')

# actually writes the information
for i in range(0,quantity):
    text=(pre1+str(i+nr)+pre2+files[i]+pre3+str(i+nr)+pre4+str(i+nr-1)+pre5+files[i]+pre6+str(i+nr+1)+pre7)
    saveFile.write(text)

# It is important to remember to actually close the file, otherwise it will
# hang for a while and could cause problems in your script
saveFile.close()
message = 'The file "' + str(output) + '" has been created'
finish = input(message)
