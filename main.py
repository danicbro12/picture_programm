from PIL import Image, ImageFilter, ImageOps

while True:

    in_img = input('Напишіть назву картинки з її розширенням: ')

    print('Блюр - 1\n')
    print('Додати бортики - 2\n')
    print('Перегорнути картинку - 3\n')
    print('Змінити розмір фото - 4\n')
    print('Зробити чб фото - 5\n')

    operation = input('Ніпишить яку операцию виповнити: ')


    def blur(in_img, modified_photo):
        img = Image.open(in_img)
        img = img.convert("RGB")
        blurred_image = img.filter(ImageFilter.BLUR)
        blurred_image.save(modified_photo)
        blurred_image.show()


    def add_border(in_img, modified_photo, border):
        img = Image.open(in_img)
        if isinstance(border, int) or isinstance(border, tuple):
            bimg = ImageOps.expand(img, border=border)
        else:
            raise RuntimeError('Ти вписав не правильне значення!')
        bimg.save(modified_photo)
        bimg.show()


    def rotate(in_img, modified_photo, rotate_img):
        img = Image.open(in_img)
        rotated_img = img.rotate(rotate_img)
        rotated_img.save(modified_photo)
        rotated_img.show()


    def thumbnail(in_img, modified_photo, x_degree, y_degree):
        img = Image.open(in_img)
        img.thumbnail((x_degree, y_degree))
        img.save(modified_photo)
        img.show()


    def bnw(in_img, modified_photo):
        img = Image.open(in_img)
        img = img.convert("L")
        img.save(modified_photo)
        img.show()


    if operation == "1":
        if __name__ == '__main__':
            blur(in_img, modified_photo='mod_photo.png')

    elif operation == "2":

        border_scale = int(input("Розмір бортиків: "))

        if __name__ == '__main__':
            add_border(in_img, modified_photo='mod_photo.png',
                       border=border_scale)

    elif operation == "3":

        rotate_degree = int(input('Наскільки треба перегорнути: '))

        if __name__ == '__main__':
            rotate(in_img, modified_photo='mod_photo.png',
                   rotate_img=rotate_degree)

    elif operation == "4":

        x_scale = int(input('Ширина у пікселях: '))

        y_scale = int(input('Висота у пікселях: '))

        if __name__ == '__main__':
            thumbnail(in_img, modified_photo='mod_photo.png',
                      x_degree=x_scale, y_degree=y_scale)

    elif operation == "5":
        if __name__ == '__main__':
            bnw(in_img, modified_photo='mod_photo.png')
