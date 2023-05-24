import os
from PIL import Image

def images_to_pdf(input_directory):
    folder_paths = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if os.path.isdir(os.path.join(input_directory, f))]
    for folder_path in folder_paths:
        images = []
        for file_name in sorted(os.listdir(folder_path), key=lambda x: int(x.split('.')[0])):
            if file_name.endswith('.jpg'):
                image_path = os.path.join(folder_path, file_name)
                try:
                    image = Image.open(image_path)
                    image.convert('RGB')
                    images.append(image)
                except (IOError, SyntaxError) as e:
                    print(f"Ошибка открытия файла {image_path}: {e}")
                    continue

        if not images:
            print(f"Папка {folder_path} не содержит изображений в формате .jpg")
            continue

        pdf_path = os.path.join(input_directory, f"{os.path.basename(folder_path)}.pdf")
        images[0].save(pdf_path, save_all=True, append_images=images[1:], format='PDF', quality=100)

        for image in images:
            image.close()
        import shutil
        shutil.rmtree(folder_path)
