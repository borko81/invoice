from django.test import TestCase
from django.urls import resolve, reverse
from fak_owner.views_clients import ViewAllClients, ClientNew, ClientEdit, ClientDelete


class TestClientsUrls(TestCase):
    def test_view_all_clients_url(self):
        url = reverse("fak_owner:clients")
        self.assertEqual(resolve(url).func.view_class, ViewAllClients)

    def test_add_new_client_url(self):
        url = reverse("fak_owner:client_new")
        self.assertEqual(resolve(url).func.view_class, ClientNew)

    def test_edit_client_url(self):
        url = reverse("fak_owner:client_edit", args=[1])
        self.assertEqual(resolve(url).func.view_class, ClientEdit)

    def test_edit_client_url_with_uncorect_paramether(self):
        with self.assertRaises(Exception):
            reverse("fak_owner:client_edit", args=["Borko"])

    def test_delete_client_url(self):
        url = reverse("fak_owner:client_delete", args=[1])
        self.assertEqual(resolve(url).func.view_class, ClientDelete)

    def test_delete_client_url_with_uncorect_paramether(self):
        with self.assertRaises(Exception):
            reverse("fak_owner:client_delete", args=["Borko"])
