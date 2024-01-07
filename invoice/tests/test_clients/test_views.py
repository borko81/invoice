from django.test import TestCase, Client
from django.urls import reverse
from fak_owner.models import Client as MClient


class TestClientView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_clients(self):
        response = self.client.get(reverse("fak_owner:clients"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "fak_owner/clients.html")

    def test_add_new_client(self):
        url = reverse("fak_owner:client_new")
        response = self.client.post(
            url,
            {
                "client_name": "Test Client",
                "town": "Some Town",
                "address": "Unknown address",
                "bulstat": "123456789",
                "mol": "Mol Mol Mol",
            },
            follow=True,
        )
        new_client = MClient.objects.get(id=1)
        self.assertEqual(new_client.client_name, "Test Client")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "fak_owner/clients.html")

    def test_edit_client(self):
        self.client_temp = MClient(
            client_name="Borko",
            town="Velingrad",
            bulstat="123456789",
            mol="Botko Borko Borko",
        )
        self.client_temp.save()
        url = reverse("fak_owner:client_edit", args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "fak_owner/clients.html")

        response_post = self.client.post(
            url,
            data={
                "client_name": "Test Client",
                "town": "Some Town",
                "address": "Unknown address",
                "bulstat": "123456789",
                "mol": "Mol Mol Mol",
            },
            follow=True,
        )
        self.edit_client = MClient.objects.get(id=1)
        self.assertEqual(self.edit_client.client_name, "Test Client")
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response, "fak_owner/clients.html")

        invalid_url = reverse("fak_owner:client_edit", args=[5])
        invalid_response = self.client.get(invalid_url)
        self.assertEqual(invalid_response.status_code, 404)

    def test_try_to_delete_client_who_not_exists(self):
        url = reverse("fak_owner:client_delete", args=[1])
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_delete_client_record_when_id_exists(self):
        self.client_temp = MClient(
            client_name="Borko",
            town="Velingrad",
            bulstat="123456789",
            mol="Botko Borko Borko",
        )
        self.client_temp.save()
        url = reverse("fak_owner:client_delete", args=[1])
        self.assertEqual(self.client.get(url).status_code, 200)
        self.assertEqual(self.client.get(url, follow=True).status_code, 200)
