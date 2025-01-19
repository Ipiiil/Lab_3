from multiprocessing import Pool, cpu_count
#Pool- для создания пула потоков
from PIL import Image
import os
import time

def invert_colors(pixel_data):
    """Инвертирует цвет пикселей."""
    #Возвращаем кортеж с инвертированными значениями цвет.комп. пикселя
    return tuple(255 - value for value in pixel_data)
    #Альтернативный вариант:
    #r, g, b = pixel_data
    #return (255 - r, 255 - g, 255 - b)

def process_image(image_path, output_path):
    """Параллельная обработка для инверсии цветов."""
    try:
        with Image.open(image_path) as img:
            img = img.convert("RGB")
            pixels = list(img.getdata())

            # Создаём пул процессов
            with Pool(cpu_count()) as pool:
                new_pixels = pool.map(invert_colors, pixels)

            # Обновляем изображение и сохраняем
            img.putdata(new_pixels)
            img.save(output_path)
            print(f"Изображение изменено и сохранено в {output_path}")
    except Exception as e:
        print(f"Ошибка при обработке изображения: {e}")

def main():
    input_image = "input.jpg"  # Входное изображение
    output_image = "output.jpg"  # Обработанное изображение

    if os.path.exists(input_image):
        start_time = time.time()

        process_image(input_image, output_image)

        end_time = time.time()
        print(f"Время выполнения: {end_time - start_time:.2f} секунд")
    else:
        print("Файл входного изображения не найден.")

if __name__ == "__main__":
    main()

