import fitz 
import os
import matplotlib.pyplot as plt

if not os.path.exists('modified_documents'): 
    os.makedirs('modified_documents')

if not os.path.exists('images'): 
    os.makedirs('images')

content = [file.name for file in os.scandir('unmodified_documents') if file.is_file() and file.name.endswith('.pdf')]

x = [1, 2, 3]
y = [3, 6, 9]

plt.ioff()
fig, ax = plt.subplots(nrows = 1, ncols = 1) 
ax.set_title('Figure_1')
ax.plot(x, y)
fig.savefig('images/Image1.png')
#plt.show()

image = fitz.Pixmap('images/Image1.png')

height_image = 200
width_image = image.width * height_image/image.height
x_coord = 345
y_coord = 350

canva_image = fitz.Rect(x_coord, y_coord, x_coord + width_image, y_coord + height_image)

for file in content:
    pdf = fitz.open(f'unmodified_documents/{file}')
    page = pdf[0]
    page.insert_image(canva_image, pixmap = image)
    pdf.save(f'modified_documents/{file}_modified.pdf')
    pdf.close()