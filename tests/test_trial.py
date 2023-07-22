
'''

Анонимы

from django.test import TestCase, Client
from django.contrib.auth import get_user_model

User = get_user_model()

class TestNews(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Создаём пользователя.
        cls.user = User.objects.create(username='testUser')
        # Создаём объект клиента.
        cls.user_client = Client()
        # "Логинимся" в клиенте при помощи метода force_login().        
        cls.user_client.force_login(cls.user)
        # Теперь через этот клиент можно отправлять запросы
        # от имени пользователя с логином "testUser". 

'''








# from django.test import TestCase
# from news.models import News

# class TestNews(TestCase):

#     TITLE = 'Заголовок новости'
#     TEXT = 'Тестовый текст'

#     @classmethod
#     def setUpTestData(cls):
#         cls.news = News.objects.create(
#             title=cls.TITLE,
#             text=cls.TEXT,
#         )

#     def test_successful_creation(self):
#         news_count = News.objects.count()
#         self.assertEqual(news_count, 1)


#     def test_title(self):
#         # Чтобы проверить равенство с константой -
#         # обращаемся к ней через self, а не через cls:
#         self.assertEqual(self.news.title, self.TITLE)







# class Test(TestCase):

#     def test_example_success(self):
#         self.assertTrue(True)


# class YetAnotherTest(TestCase):

#     def test_example_fails(self):
#         self.assertTrue(False)














# class DemonstrationExample(TestCase):

#     @classmethod
#     def setUpClass(cls):        
#         super().setUpClass()  # Вызов метода setUpClass() из родительского класса.
#         # А здесь код, который подготавливает данные
#         # перед выполнением тестов этого класса. 

# class MyTestCase(TestCase):

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         ...

#     @classmethod
#     def tearDownClass(cls):
#         ...  # Выполнение необходимых операций.
#         super().tearDownClass()  # Вызов родительского метода