from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from education.models import EdModule, EdVideo
from users.models import User, UserRoles


class EdVideoTestCase(APITestCase):
    """ Тесты на CRUD видео """

    def setUp(self):
        self.user = User.objects.create(email="test@admin.pro", password="admin", role=UserRoles.MODERATOR)
        self.user2 = User.objects.create(email="test2@admin.pro", password="admin", role=UserRoles.MODERATOR)
        self.user3 = User.objects.create(email="test3@admin.pro", password="admin")
        self.edvideo = EdVideo.objects.create(
            title='Test',
            description='Test',
            owner=self.user
        )
        self.data = {
            'title': 'Test1',
            'description': 'Test1'
        }

    def test_create_edvideo(self):
        """ Тесты на создание видео """
        self.client.force_authenticate(user=self.user)
        data = self.data
        response = self.client.post(
            reverse('education:edvideo-create'),
            data=data
        )
        video_owner = response.data["owner"]

        # Проверка на статус ответа
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # Проверка на верность создаваемых полей
        self.assertEqual(
            response.json(),
            {
                'id': 2,
                'title': 'Test1',
                'description': 'Test1',
                'edmodule': None,
                'image': None,
                'owner': video_owner,
                'video_link': None
            }
        )

        # Проверка на то, что запись создалась в базе
        self.assertTrue(
            EdVideo.objects.all().exists()
        )

    def test_list_edvideo(self):
        """ Тесты на список видео """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('education:edvideo-list'))

        # Проверка на статус ответа
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Проверка на верность структуры и полей в списке
        self.assertEqual(
            response.json(),
            [
                {
                    "title": "Test",
                    "edmodule": None
                }
            ]
        )

    def test_detail_edvideo(self):
        """ Тест на отображение деталей конкретного видео """
        self.client.force_authenticate(user=self.user)
        data = self.data
        response = self.client.post(reverse('education:edvideo-create'), data=data)
        edvideo_id = response.data['id']

        response = self.client.get(
            reverse("education:edvideo-detail", args=[edvideo_id])
        )

        # Проверка на код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверка на содержимое поля title
        self.assertEqual(response.data["title"], "Test1")

    def test_update_edvideo(self):
        """ Тесты на обновление данных видео """
        self.client.force_authenticate(user=self.user)
        data = self.data
        response = self.client.post(reverse('education:edvideo-create'), data=data)
        edvideo_id = response.data['id']

        # Проверка, что владелец может вносить изменения
        self.client.force_authenticate(user=self.user)
        update_edvideo = self.client.patch(
            reverse("education:edvideo-update", args=[edvideo_id]),
            data={"title": "Updated title"}
        )
        # Проверка на статус ответа
        self.assertEqual(update_edvideo.status_code, status.HTTP_200_OK)
        # Проверка на верность изменямых полей
        self.assertEqual(
            update_edvideo.data["title"],
            "Updated title"
        )

        # Проверка на невозможность внесения изменений в видео, созданное другим пользователем
        self.client.force_authenticate(user=self.user2)
        update_edvideo = self.client.patch(
            reverse("education:edvideo-update", args=[edvideo_id]),
            data={"title": "Updated title"},
        )
        self.assertEqual(
            update_edvideo.status_code, status.HTTP_403_FORBIDDEN
        )

    def test_create_validator_edvideo(self):
        """ Тест на отработку валидатора, что видео может быть только с youtube """
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Test1',
            'description': 'Test1',
            'video_link': 'https:test.com/sofiwer'
        }
        response = self.client.post(
            reverse('education:edvideo-create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_create_edvideo_wrong_user(self):
        """ Тест на невозможность создания видео не модератором """
        self.client.force_authenticate(user=self.user3)
        data = self.data
        response = self.client.post(
            reverse('education:edvideo-create'),
            data=data
        )

        # Проверка на статус ответа
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_delete_edvideo(self):
        """ Тесты на удаление видео """
        # Создание нового видео
        self.client.force_authenticate(user=self.user)
        data = self.data
        response = self.client.post(reverse('education:edvideo-create'), data=data)
        edvideo_id = response.data['id']

        # Проверка на невозможность удаления видео сторонним пользователем
        self.client.force_authenticate(user=self.user2)
        delete_edvideo = self.client.delete(reverse('education:edvideo-delete', args=[edvideo_id]))
        self.assertEqual(delete_edvideo.status_code, status.HTTP_403_FORBIDDEN)

        # Проверка на удаление видео владельцем
        self.client.force_authenticate(user=self.user)
        delete_edvideo = self.client.delete(reverse('education:edvideo-delete', args=[edvideo_id]))
        # Проверка статуса ответа
        self.assertEquals(
            delete_edvideo.status_code,
            status.HTTP_204_NO_CONTENT
        )

        # Проверка отсутствия удаленного видео в базе
        get_deleted_edvideo = self.client.get(reverse("education:edvideo-detail", args=[edvideo_id]))
        self.assertEqual(
            get_deleted_edvideo.status_code, status.HTTP_404_NOT_FOUND
        )


class EdModuleTestCase(APITestCase):
    """ Тесты на CRUD модулей """

    def setUp(self):
        self.user = User.objects.create(email="test@admin.pro", password="admin", role=UserRoles.MODERATOR)
        self.user2 = User.objects.create(email="test2@admin.pro", password="admin", role=UserRoles.MODERATOR)
        self.user3 = User.objects.create(email="test3@admin.pro", password="admin")
        self.edmodule = EdModule.objects.create(
            module_number=1,
            title='Test',
            description='Test',
            owner=self.user
        )
        self.data = {
            'module_number': 2,
            'title': 'Test1',
            'description': 'Test1'
        }

    def test_create_edmodule(self):
        """ Тесты на создание модуля """
        self.client.force_authenticate(user=self.user)
        data = self.data
        response = self.client.post(
            reverse('education:edmodule-list'),
            data=data
        )

        # Проверка на статус ответа
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # Проверка на верность создаваемых полей
        self.assertEqual(
            response.json(),
            {
                'id': 2,
                'module_number': 2,
                'title': 'Test1',
                'description': 'Test1',
                'image': None,
                'owner': 1
            }
        )

        # Проверка на то, что запись создалась в базе
        self.assertTrue(
            EdModule.objects.all().exists()
        )

    def test_list_edmodule(self):
        """ Тесты на список модулей """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('education:edmodule-list'))

        # Проверка на статус ответа
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Проверка на верность структуры и полей в списке
        self.assertEqual(
            response.json(),
            [
                {
                    'id': 8,
                    'module_number': 1,
                    'title': 'Test',
                    'description': 'Test',
                    'image': None,
                    'owner': 13
                }
            ]
        )

    def test_detail_edmodule(self):
        """ Тест на отображение деталей конкретного модуля """
        self.client.force_authenticate(user=self.user)
        data = self.data
        response = self.client.post(reverse('education:edmodule-list'), data=data)
        edmodule_id = response.data['id']

        response = self.client.get(
            reverse("education:edmodule-detail", args=[edmodule_id])
        )

        # Проверка на код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверка на содержимое поля title
        self.assertEqual(response.data["title"], "Test1")

    def test_update_edmodule(self):
        """ Тесты на обновление данных видео """
        self.client.force_authenticate(user=self.user)
        data = self.data
        response = self.client.post(reverse('education:edmodule-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        edmodule_id = response.data['id']

        # Проверка, что владелец может вносить изменения
        self.client.force_authenticate(user=self.user)
        update_data = {"title": "Updated title"}
        update_edmodule = self.client.patch(
            reverse("education:edmodule-detail", args=[edmodule_id]),
            data=update_data
        )
        # Проверка на статус ответа
        self.assertEqual(update_edmodule.status_code, status.HTTP_200_OK)

        # Проверка на верность изменямых полей
        self.assertEqual(
            update_edmodule.data["title"],
            "Updated title"
        )

        # Проверка на невозможность внесения изменений в модуль, созданный другим пользователем
        self.client.force_authenticate(user=self.user3)
        update_data = self.client.patch(
            reverse("education:edmodule-detail", args=[edmodule_id]),
            data={"title": "Updated title"},
        )
        self.assertEqual(
            update_data.status_code, status.HTTP_403_FORBIDDEN
        )

    def test_create_edmodule_wrong_user(self):
        """ Тест на невозможность создания модуля не модератором """
        self.client.force_authenticate(user=self.user3)
        data = self.data
        response = self.client.post(
            reverse('education:edmodule-list'),
            data=data
        )

        # Проверка на статус ответа
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_delete_edmodule(self):
        """ Тесты на удаление модуля """
        # Создание нового модуля
        self.client.force_authenticate(user=self.user)
        data = self.data
        response = self.client.post(reverse('education:edmodule-list'), data=data)
        edmodule_id = response.data['id']

        # Проверка на невозможность удаления модуля сторонним пользователем
        self.client.force_authenticate(user=self.user2)
        delete_edmodule = self.client.delete(reverse('education:edmodule-detail', args=[edmodule_id]))
        self.assertEqual(delete_edmodule.status_code, status.HTTP_403_FORBIDDEN)

        # Проверка на удаление модуля владельцем
        self.client.force_authenticate(user=self.user)
        delete_edmodule = self.client.delete(reverse('education:edmodule-detail', args=[edmodule_id]))
        # Проверка статуса ответа
        self.assertEquals(
            delete_edmodule.status_code,
            status.HTTP_204_NO_CONTENT
        )

        # Проверка отсутствия удаленного модуля в базе
        get_deleted_edmodule = self.client.get(reverse("education:edmodule-detail", args=[edmodule_id]))
        self.assertEqual(
            get_deleted_edmodule.status_code, status.HTTP_404_NOT_FOUND
        )
