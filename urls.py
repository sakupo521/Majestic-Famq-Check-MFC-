import webbrowser
import subprocess
import sys
import os

# Добавляеете ссылки на нужные сайты для проверки пользователя

urls = ['https://forum.majestic-rp.ru/', 
        'https://vanish-cheat.com/', 
        'https://leet-cheats.ru/', 
        'https://nixware.cc/purchase-cheats/unicore-gta-v/',
        'https://www.youtube.com/feed/history',
        'https://github.com/',
        'https://drive.google.com/drive/',
        'https://www.voidtools.com/ru-ru/',
        'https://www.nirsoft.net/utils/computer_activity_view.html',
        'https://giphy.com/gifs/reaction-mood-2x0VePimPaFJDpGZ7H'
]


def open_url(): #открытие ссылок
    for i in range(len(urls)):
        webbrowser.open_new_tab(urls[i])

def open_explorer(): #открытие проводника
    if sys.platform == "win32":
        try:
            subprocess.run(['explorer.exe'], check=True)
        except subprocess.CalledProcessError:
            pass
            
if __name__ == "__main__":
    #выполнение функций (если вы удалили фунцию то тут нужно ее тоже удалить!!!)
    open_url()

    open_explorer()
