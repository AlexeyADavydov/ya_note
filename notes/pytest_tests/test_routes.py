# test_routes.py
from http import HTTPStatus

import pytest

from django.urls import reverse

# [1]
# Указываем в фикстурах встроенный клиент.
def test_home_availability_for_anonymous_user(client):
    # Адрес страницы получаем через reverse():
    url = reverse('notes:home')
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK




# [5]
@pytest.mark.parametrize(
    'name',  # Имя параметра функции.
    # Значения, которые будут передаваться в name.
    ('notes:home', 'users:login', 'users:logout', 'users:signup')
)
# Указываем имя изменяемого параметра в сигнатуре теста.
def test_pages_availability_for_anonymous_user(client, name):
    url = reverse(name)  # Получаем ссылку на нужный адрес.
    response = client.get(url)  # Выполняем запрос.
    assert response.status_code == HTTPStatus.OK




# [2]
@pytest.mark.parametrize(
    'name',
    ('notes:list', 'notes:add', 'notes:success')
)
def test_pages_availability_for_auth_user(admin_client, name):
    url = reverse(name)
    response = admin_client.get(url)
    assert response.status_code == HTTPStatus.OK




# [3]
@pytest.mark.parametrize(
    'parametrized_client, expected_status',
    # Предварительно оборачиваем имена фикстур 
    # в вызов функции pytest.lazy_fixture().
    (
        (pytest.lazy_fixture('admin_client'), HTTPStatus.NOT_FOUND),
        (pytest.lazy_fixture('author_client'), HTTPStatus.OK)
    ),
)
@pytest.mark.parametrize(
    'name',
    ('notes:detail', 'notes:edit', 'notes:delete'),
)
def test_pages_availability_for_different_users(
        parametrized_client, name, note, expected_status
):
    url = reverse(name, args=(note.slug,))
    response = parametrized_client.get(url)
    assert response.status_code == expected_status 


# [4]

from pytest_django.asserts import assertRedirects


@pytest.mark.parametrize(
    'name, args',
    (
        ('notes:detail', pytest.lazy_fixture('slug_for_args')),
        ('notes:edit', pytest.lazy_fixture('slug_for_args')),
        ('notes:delete', pytest.lazy_fixture('slug_for_args')),
        ('notes:add', None),
        ('notes:success', None),
        ('notes:list', None),
    ),
)
# Передаём в тест анонимный клиент, name проверяемых страниц и args:
def test_redirects(client, name, args):
    login_url = reverse('users:login')
    # Теперь не надо писать никаких if и можно обойтись одним выражением.
    url = reverse(name, args=args)
    expected_url = f'{login_url}?next={url}'
    response = client.get(url)
    assertRedirects(response, expected_url)




# Первый этап: тестирование маршрутов; сверим планы:

# 1 Главная страница доступна анонимному пользователю.

# 2 Аутентифицированному пользователю доступна страница со
# списком заметок notes/, страница успешного добавления заметки done/, 
# страница добавления новой заметки add/.

# 3 Страницы отдельной заметки, удаления и редактирования 
# заметки доступны только автору заметки. 
# Если на эти страницы попытается зайти другой пользователь — 
# вернётся ошибка 404.

# 4 При попытке перейти на страницу списка заметок, 
# страницу успешного добавления записи, страницу добавления заметки,
# отдельной заметки, редактирования или удаления заметки 
# анонимный пользователь перенаправляется на страницу логина.

# 5 Страницы регистрации пользователей, входа в учётную запись и 
# выхода из неё доступны всем пользователям.



# Домашнее задание 1
# Напишите тесты маршрутов для проекта YaNews на pytest: «переведите» тесты, написанные на unittest, на синтаксис pytest.



# ТУТ - pytest