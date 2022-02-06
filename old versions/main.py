import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import token
from config import id
import time

print(" ")
print(" ")
print("               Бот запускается...")
print(" ")
time.sleep(0.5)
print("           Выберите метод использования...")
print("              Возможные варианты ↓")
print("             ")
print(" ")
time.sleep(0.5)
print("              1.Установить статус")
print("             2.Отправить сообщение")
print("             3.Заблокировать пользователя")
print("              4.Опубликовать пост.  ")

session = vk_api.VkApi(token = token)

def send(domain, text):
    session.method("messages.send", {
        "domain": domain,
        "message": text,
        "random_id": 0
    })

def send_id(user_id, text):
    session.method("messages.send", {
        "user_id": user_id,
        "message": text,
        "random_id": 0
    })

def set_status(id):
    session.method("status.set", {
        "user_id": id,
        "text": text,
    })

def ban(owner_id):
    session.method("account.ban", {
        "owner_id": owner_id,
    })

def wall_post(id, post):
    session.method("wall.post", {
        "owner_id": id,
        "message": post
    })



var = int(input())

# Установить статус
if (var == 1):
    print("Вы выбрали метод 1 (Установить статус)")
    print("Напишите статус который вы хотите установить.")
    text = str(input())
    set_status(text)
    time.sleep(0.5)
    print("Статус установлен.")
    print("Программа выключается.")
    time.sleep(5)
# Отправить сообщение
if (var == 2):
    print("Вы выбрали метод 2 (написать сообщение)")
    print("Выберите способ ввода страницы человека.")
    print("Доступные варианты: ")
    time.sleep(0.5)
    print("1.ID")
    print("2.Короткий адрес пользователя")
    var2 = int(input())
    # Указать ID
    if (var2 == 1):
        print("Отлично! Теперь напишите ID, которому хотите отправить сообщение.")
        user_id = int(input())
        print("Отлично! Теперь напишите сообщение, которое хотите отправить.")
        text = str(input())
        send_id(user_id, text)
        print("Сообщение отправлено! Если хотите выключить программу, нажмите CTRL + C")
        print("Если хотите продолжить писать сообщения, то пишите.")
        while True:
                text = str(input())
                send_id(user_id, text)
    # Указать домен
    elif (var2 == 2):
        print("Отлично! Теперь напишите короткий адрес пользователя, которому хотите отправить сообщение.")
        print("Пример: \n Страница:  \n  это краткий адресс.")
        domain = str(input())
        print("Отлично! Теперь напишите сообщение, которое хотите отправить.")
        text = str(input())
        send(domain, text)
        print("Сообщение отправлено! Если хотите выключить программу, нажмите CTRL + C")
        print("Если хотите продолжить писать сообщения, то пишите.")
        while True:
                text = str(input())
                send(domain, text)
# Бросить в чс.
if (var == 3):
    print("Вы выбрали метод 3 (добавить человека в чс)")
    print("Напишите ID человека которого вы хотите отправить в чс.")
    owner_id = int(input())
    print("Отлично! Вы уверены что хотите заблокировать его/ее ? \n 1 - Да \n 0 - Нет")
    confirm = int(input())
    if (confirm == 1):
        print("Вы заблокировали пользователя")
        ban(owner_id)
    else:
        print("Операция отменена.")
# Опубликовать пост
if (var == 4):
    print("Вы выбрали метод 4 (опубликовать пост)")
    print("Напишите сообщение которое хотите опубликовать ↓")
    post = str(input())
    wall_post(id, post)
    print("Классно! Пост опубликован!")

