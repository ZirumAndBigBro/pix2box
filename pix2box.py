#Pix2box
#Python 3.6.2
#script BigБро
#idea Zirum

# example result in result.txt
# <spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
#for \AC-Game\data\static_data\spawns\Npcs\New\location.xml

#for npc middle box 701016 / small box 700321

from PIL import Image

im = Image.open('Sample.bmp','r')
width, height = im.size
pix_val = list(im.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]

#insert your bottom left start point
x0=1622
y0=1707
z0=151.5
h0 = 0

# Item size
iw = 0.5 #width  middle box 701016 (0.9) / small box 700321 (0.5)
ih = 0.5 #height  middle box 701016 (0.9) / small box 700321 (0.5)
il = 0.5 #depth  middle box 701016 (0.9) / small box 700321 (0.5)

file = open ('result.txt', 'w')
for h in range (0, height):
  for w in range (0, width):
    color_black = pix_val_flat[(3*w+h*width*3)] < 50 and pix_val_flat[(3*w+h*width*3)+1] < 50 and pix_val_flat[(3*w+h*width*3)+2] < 50
    if color_black:
     x = x0+w*iw 
     y = y0+(height-h-1)*ih
     z = z0
     file.write('<spot h="{:d}" x="{:.1f}" y="{:.1f}" z="{:.1f}"/>\n'.format(h0, x, y, z))
file.close()
