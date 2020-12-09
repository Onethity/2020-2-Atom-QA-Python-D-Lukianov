""" Нагрузочные тесты на фреймворке Locust """

from locust import HttpUser, task, between, TaskSet


class PositiveTasks(TaskSet):
    AUTH_DATA = {
        'login': 'Dima',
        'password': '123'
    }

    def on_start(self):
        """ Авторизация пользователя на старте """
        response = self.client.get('/', auth=(self.AUTH_DATA['login'], self.AUTH_DATA['password']))
        self.client.headers.update({'Authorization': response.request.headers['Authorization']})

        assert response.status_code == 200

    def on_stop(self):
        """ Логаут при завершении """
        response = self.client.get('/logout', catch_response=True)
        if response.status_code == 401:
            response.success()

    @task
    def profile(self):
        """ Пользователь открывает свой профиль """
        response = self.client.get('/profile')
        assert self.AUTH_DATA['login'] in response.text

    @task
    def album_and_photo(self):
        """ Пользователь открывает альбом, а затем фото"""
        response = self.client.get('/album')
        assert 'album' in response.text

        response = self.client.get('/photo')
        assert 'photo' in response.text

    @task
    def profile_and_album(self):
        """ Пользователь открывает свой профиль, а затем альбом"""
        self.client.get('/profile')

        response = self.client.get('/album')
        assert 'album' in response.text

    @task
    def profile_and_shareware(self):
        """ Пользователь открывает свой профиль, а потом идет на открытый url"""
        self.client.get('/profile')

        response = self.client.get('/shareware')
        assert 'Free for all!' in response.text


class NegativeTasks(TaskSet):
    @task
    def not_authorized(self):
        """ Незалогиненный пользователь идет на закрытый роут """
        response = self.client.get('/photo', catch_response=True)
        if response.status_code == 401:
            response.success()


class WebSiteUser(HttpUser):
    tasks = [PositiveTasks, NegativeTasks]
    wait_time = between(1, 2)
