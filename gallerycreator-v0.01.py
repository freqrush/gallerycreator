import os

folder = 'maps-brussels-perpignan'
files = os.listdir(folder)
quantity = len(files)
pre1 = '  <a href="#img'
pre2 = '''"><img class="thumb" src="./maps-brussels-perpignan/'''
pre3 = '''"></a>
  <div class="lightbox" id="img'''
pre4 = '''">
    <a href="#img'''
pre5 = '''" class="light-btn btn-prev">prev</a>
    <a href="#_" class="btn-close">X</a>
    <img src="./maps-brussels-perpignan/'''
pre6 = '''">
    <a href="#img'''
pre7 = '''" class="light-btn btn-next">next</a>
  </div>
'''
text = 'Sample Text to Save\nNew line!'

# notifies Python that you are opening this file, with the intention to write
saveFile = open('maps-brussels-perpignan.txt','w')

# actually writes the information
for i in range(0,quantity):
    text=(pre1+str(i+66)+pre2+files[i]+pre3+str(i+66)+pre4+str(i+65)+pre5+files[i]+pre6+str(i+67)+pre7)
    saveFile.write(text)

# It is important to remember to actually close the file, otherwise it will
# hang for a while and could cause problems in your script
saveFile.close()

for i in range(0,quantity):
    print(pre1+str(i)+pre2+files[i]+pre3+str(i)+pre4+str(i-1)+pre5+files[i]+pre6+str(i+1)+pre7)
    
