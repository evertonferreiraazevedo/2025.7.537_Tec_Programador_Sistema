from PIL import ImageFont, ImageDraw, Image

img = Image.open("exemplo.png")
desenho = ImageDraw.Draw(img)

# Fonte padrão do sistema (ou forneça um caminho para um .ttf)
fonte = ImageFont.load_default()
desenho.text((50, 50), "Olá Mundo!", fill="white", font=fonte)

img.save("com_texto.jpg")
