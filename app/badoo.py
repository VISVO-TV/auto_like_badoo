from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from getpass import getpass
import random
import time


option = Options()
option.add_argument('--headless')
browser = webdriver.Firefox(options=option)
browser.get('https://badoo.com/ru/signin/?f=top')
time.sleep(5)


def reg(login, password):
    try:
        browser.find_element_by_name('email').send_keys(login)
        time.sleep(1)
        browser.find_element_by_name('password').send_keys(password)
        time.sleep(1)
        browser.find_element_by_name('post').click()
    except Exception:
        print('Проверь подключение к интернету')

def paste_like(times):
    try:
        browser.find_element_by_class_name('js-profile-header-vote-yes').click()
    except NoSuchElementException:
        print('Не удалось войти в аккаунт!!! Проверь логин, пароль, подключение к интернету')
    print('Вы успешно вошли в свой аккаунт, начинаю проставлять лайки)\n')
    time.sleep(1)
    page = browser.page_source
    if 'Пока всё!' in page:
        print('Все лайки на сегодня потрачены. Приходи завтра\n')
        return 0

    try:
        browser.find_element_by_class_name('js-chrome-pushes-deny').click()
    except NoSuchElementException:
        print('Все лайки на сегодня потрачены. Приходи завтра\n')
        return 0
    counter = 0

    for i in range(times):
        page = browser.page_source
        if 'Пока всё!' in page:
            print('Все лайки на сегодня потрачены. Приходи завтра\n')
            return counter
        try:
            browser.find_element_by_class_name('ovl__close').click()
            print('Взаимная симпатия, ооо даа!!! У кого-то будет чих-пых)\n')
        except NoSuchElementException:
            pass
        if random.randint(1,5) == 1:
            browser.find_element_by_class_name('js-profile-header-vote-no').click()
        else:
            browser.find_element_by_class_name('js-profile-header-vote-yes').click()
            counter += 1
            print(f'Добавленных лайков  =  {counter} шт.\n')
        time.sleep(2)



def main():
    login = input('Введите логин:  ')
    password = getpass('Введите пароль:  ')
    times = 100
    reg(login, password)
    time.sleep(7)
    a = paste_like(times)
    print(f'Работа скрипта завершена. Проставленно лайков: {a} шт.\n')
    browser.quit()


if __name__ == '__main__':
    main()
