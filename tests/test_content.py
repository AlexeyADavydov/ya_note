


# СКОПИРОВАНО ИЗ YA_NEWS - НАДО ЗАМЕНИТЬ, ЭТО ДЗ

# ТУТ - unittest



from django.conf import settings
from django.test import TestCase

from django.urls import reverse

from news.models import News

from datetime import datetime, timedelta

class TestHomePage(TestCase):
    HOME_URL = reverse('news:home')

    @classmethod
    def setUpTestData(cls):
        today = datetime.today()
        all_news = [
            News(
                title=f'Новость {index}', 
                text='Просто текст.',
                date=today - timedelta(days=index)
            )
            for index in range(settings.NEWS_COUNT_ON_HOME_PAGE + 1)
        ]
        News.objects.bulk_create(all_news)

    def test_news_count(self):
        response = self.client.get(self.HOME_URL)
        object_list = response.context['object_list']
        news_count = len(object_list)
        self.assertEqual(news_count, settings.NEWS_COUNT_ON_HOME_PAGE)

    def test_news_order(self):
        response = self.client.get(self.HOME_URL)
        object_list = response.context['object_list']
        all_dates = [news.date for news in object_list]
        sorted_dates = sorted(all_dates, reverse=True)
        self.assertEqual(all_dates, sorted_dates)

    def test_comments_order(self):
        response = self.client.get(self.detail_url)
        self.assertIn('news', response.context)
        news = response.context['news']
        all_comments = news.comment_set.all()
        self.assertLess(all_comments[0].created, all_comments[1].created) 

    def test_anonymous_client_has_no_form(self):
        response = self.client.get(self.detail_url)
        self.assertNotIn('form', response.context)
        
    def test_authorized_client_has_form(self):
        self.client.force_login(self.author)
        response = self.client.get(self.detail_url)
        self.assertIn('form', response.context)


    # @classmethod
    # def setUpTestData(cls):
    #     all_news = [
    #         News(title=f'Новость {index}', text='Просто текст.')
    #         for index in range(settings.NEWS_COUNT_ON_HOME_PAGE + 1)
    #     ]
    #     News.objects.bulk_create(all_news)



    # @classmethod    
    # def setUpTestData(cls):
    #     all_news = []
    #     for index in range(settings.NEWS_COUNT_ON_HOME_PAGE + 1):
    #         news = News(title=f'Новость {index}', text='Просто текст.')
    #         all_news.append(news)
    #     News.objects.bulk_create(all_news) 

    # @classmethod
    # def setUpTestData(cls):
    #     for index in range(settings.NEWS_COUNT_ON_HOME_PAGE + 1):
    #         news = News(title=f'Новость {index}', 
    #                     text='Просто текст.')
    #         news.save() 

    # @classmethod
    # def setUpTestData(cls):
    #     for index in range(settings.NEWS_COUNT_ON_HOME_PAGE + 1):
    #         News.objects.create(title=f'Новость {index}',
    #                             text='Просто текст.')






# [DONE]
# Количество новостей на главной странице — не более 10.

# Новости отсортированы от самой свежей к самой старой. Свежие новости в начале списка.
# Комментарии на странице отдельной новости отсортированы от старых к новым: старые в начале списка, новые — в конце.

# Анонимному пользователю недоступна форма для отправки комментария на странице отдельной новости, а авторизованному доступна.



# Домашнее задание 1
# Напишите тесты контента в проекте YaNote. План тестирования у вас есть — продолжайте его реализовывать!

