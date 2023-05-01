from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from album_api.models import Album, Photo


class AlbumTestCase(APITestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.user = User.objects.create_user(username='testalbum_user', password='testalbum_password')
        self.client.force_authenticate(user=self.user)

    def test_create_album(self):
        data = {
            'name': 'test album (new)',
            'description': 'test description (new)',
            'category': 1
        }

        response = self.client.post('/api/albums/', data)
        new_album_id = response.data.get('id', None)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # test if request was successfull
        self.assertEqual(new_album_id, 3)  # test if auto_incremented id is correct
        self.assertEqual(Album.objects.count(), 3)  # test if new album was created
        self.assertEqual(Album.objects.get(pk=3).name, 'test album (new)')  # test if new album has correct name

    def test_list_albums(self):
        response = self.client.get('/api/albums/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # test if request was successfull
        self.assertEqual(len(response.data), 2)  # test if correct number of albums returned

    def test_get_album(self):
        response = self.client.get('/api/albums/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # test if request was successfull
        self.assertEqual(response.data['id'], 1)  # test if correct album id returned
        self.assertEqual(response.data['name'], 'test album')  # test if correct album name returned

    def test_update_album(self):
        data = {
            'name': 'test album (updated)',
            'category': 2
        }

        response = self.client.put('/api/albums/1/', data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # test if request was successfull
        self.assertEqual(Album.objects.get(pk=1).category, 2)  # test if album category was updated
        self.assertEqual(Album.objects.get(pk=1).name, 'test album (updated)')  # test if album name was updated

    def test_delete_album(self):
        response = self.client.delete('/api/albums/2/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)   # test if request was successfull
        self.assertEqual(Album.objects.count(), 1)  # test if album was deleted
        self.assertEqual(Album.objects.all().first().id, 1)

    def tearDown(self):
        self.user.delete()


class PhotoTestCase(APITestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.user = User.objects.create_user(username='testphoto_user', password='testphoto_password')
        self.client.force_authenticate(user=self.user)

    def test_create_photo(self):
        data = {
            'name': 'test photo (new)',
            'description': 'test photo description (new)',
            'albums': [2]
        }

        response = self.client.post('/api/photos/', data)
        new_photo_id = response.data.get('id', None)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # test if request was successfull
        self.assertEqual(new_photo_id, 3)  # test if auto_incremented id is correct
        self.assertEqual(Photo.objects.count(), 3)   # test if new photo was created
        self.assertEqual(Photo.objects.get(pk=new_photo_id).name, 'test photo (new)')   # test if new photo has correct name
        self.assertEqual(Photo.objects.get(pk=new_photo_id).albums.count(), 1)  # test if new photo has correct album count
        self.assertEqual(Photo.objects.get(pk=new_photo_id).albums.all().first().id, 2)  # test if new photo has correct album

    def test_list_photos(self):
        response = self.client.get('/api/photos/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # test if request was successfull
        self.assertEqual(len(response.data), 2)  # test if correct number of photos returned

    def test_get_photo(self):
        response = self.client.get('/api/photos/2/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # test if request was successfull
        self.assertEqual(response.data['id'], 2)   # test if correct photo returned
        self.assertEqual(response.data['name'], 'test photo (2)')  # test if returned photo has expected name
        self.assertEqual(response.data['albums'], [1, 2])  # test if returned photo has expected albums

    def test_update_photo(self):
        data = {
            'name': 'test photo (updated)',
            'albums': [2]
        }

        response = self.client.put('/api/photos/1/', data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # test if request was successfull
        self.assertEqual(Photo.objects.get(pk=1).albums.count(), 1)   # test if updated photo has correct album count
        self.assertEqual(Photo.objects.get(pk=1).albums.first().id, 2)  # test if updated photo has correct album

    def test_delete_photo(self):
        response = self.client.delete('/api/photos/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # test if request was successfull
        self.assertEqual(Photo.objects.count(), 1)  # test if photo was deleted
        self.assertEqual(Photo.objects.all().first().id, 2)  # test if photo was deleted

    def tearDown(self):
        self.user.delete()
