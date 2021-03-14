import zipfile, glob

verF = 'db.ver'

# read current database
with open(verF) as f:
    line = f.read()
    ver = int(line) if len(line) else 0
    
ver +=1
print "> Updating layout database:", ver

# write new database   
with open(verF,'w') as f:
    f.write( str(ver) )
    
# zip layouts
with zipfile.ZipFile('xml.pkg', 'w') as zf:
    zf.write(verF)
    for f in glob.iglob('./*/*.xml'):
        zf.write(f, f)   