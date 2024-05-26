import pygame
from PIL import Image
import requests
from io import BytesIO
import ctypes
class ImageController:

    @classmethod
    def play_music(cls, music_url):
        song_file = "song.mp3"

        # Скачиваем песню
        response = requests.get(music_url, verify=False)
        with open(song_file, "wb") as f:
            f.write(response.content)

        pygame.mixer.init()
        pygame.mixer.music.load(song_file)
        pygame.mixer.music.play(-1)

    @classmethod
    def show_image(cls, image_url):
        pygame.init()

        screen_info = pygame.display.Info()
        screen_width = screen_info.current_w
        screen_height = screen_info.current_h
        screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Ukrainization")
        response = requests.get(image_url, verify=False)
        image = Image.open(BytesIO(response.content))

        image = image.convert("RGB").resize((screen_width, screen_height))

        pygame_image = pygame.image.fromstring(image.tobytes(), image.size, "RGB")
        screen.blit(pygame_image, (0, 0))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                ...

        pygame.quit()

    @classmethod
    def download_image(cls, url, save_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
        else:
            return False

    @classmethod
    def set_wallpaper(cls, image_path):
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)