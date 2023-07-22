from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from news.models import Comment, News

User = get_user_model()

class TestRoutes(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.news = News.objects.create(
            title='Заголовок',
            text='Текст',
        )
        cls.author = User.objects.create(
            username="Лев Толстой",
        )
        cls.reader = User.objects.create(
            username="Читатель простой",
        )
        cls.comment = Comment.objects.create(
            news=cls.news,
            author=cls.author,
            text='Текст комментария',
        )


    def test_availability_for_comments_edit_and_delete(self):
        users_statuses = (
            (self.author, HTTPStatus.OK),
            (self.reader, HTTPStatus.NOT_FOUND),
        )

        for user, status in users_statuses:
            self.client.force_login(user)
            for name in ('news:edit', 'news:delete'):
                with self.subTest(user=user, name=name):
                    url = reverse(name, args=(self.comment.id,))
                    response = self.client.get(url)
                    self.assertEqual(response.status_code, status)


    def test_pages_availability(self):
        urls = (
            ('news:home', None),
            ('news:detail', (self.news.id,)),
            ('users:logout', None),
            ('users:signup', None),
        )

        for name, args in urls:
            with self.subTest(name=name):
                url = reverse(name, args=args)
                response = self.client.get(url)
                self.assertEqual(response.status_code,
                                 HTTPStatus.OK)

    def test_redirect_for_anonymous_client(self):
        login_url = reverse('users:login')
        for name in ('news:edit', 'news:delete'):
            with self.subTest(name=name):
                url = reverse(name, args=(self.comment.id,))
                redirect_url = f'{login_url}?next={url}'
                response = self.client.get(url)
                self.assertRedirects(response, redirect_url)




    # def test_home_page(self):
    #     url = reverse('news:home')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, HTTPStatus.OK)

    # def test_detail_page(self):
    #     url = reverse('news:detail', args=(self.news.id,))
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, HTTPStatus.OK)






# url = reverse('news:detail', args=(self.news.pk,))
# # Или
# url = reverse('news:detail', kwargs={'pk': self.news.pk}) 

# url = reverse('news:detail', args=(self.news.id,))
# # Или
# url = reverse('news:detail', kwargs={'pk': self.news.id})







# [DONE-#] Главная страница доступна анонимному пользователю.
# [DONE] Страница отдельной новости доступна анонимному пользователю.

# [DONE] Страницы удаления и редактирования комментария доступны автору комментария.
# [DONE] При попытке перейти на страницу редактирования или удаления комментария анонимный пользователь перенаправляется на страницу авторизации.
# [DONE] Авторизованный пользователь не может зайти на страницы редактирования или удаления чужих комментариев (возвращается ошибка 404).

# [DONE] Страницы регистрации пользователей, входа в учётную запись и выхода из неё доступны анонимным пользователям.



# Домашнее задание 2
# Напишите тесты для маршрутов проекта YaNote; в работе ориентируйтесь на ваш план тестирования этого проекта. 
# Если в уроке какие-то моменты показались сложными или непонятными — сделайте перерыв на несколько часов, а потом прочтите его снова. Попробуйте, должно сработать!














