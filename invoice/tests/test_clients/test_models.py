from django.test import TestCase

from fak_owner.models import Client


class TestClientModel(TestCase):
    def test_successfully_added_new_client_and_return(self):
        self.client = Client(
            client_name="Borko",
            town="Velingrad",
            bulstat="123456789",
            mol="Botko Borko Borko",
        )
        self.client.save()
        self.client_check = Client.objects.get(id=1)
        self.assertEqual(self.client_check.client_name, "Borko")
        self.assertEqual(self.client_check.town, "Velingrad")
        self.assertEqual(self.client_check.bulstat, "123456789")
        self.assertEqual(self.client_check.mol, "Botko Borko Borko")

    def test_added_client_with_duplicate_unique_param_should_raise_error(self):
        self.client_temp = Client(
            client_name="Borko",
            town="Velingrad",
            bulstat="123456789",
            mol="Botko Borko Borko",
        )
        self.client_temp.save()

        with self.assertRaises(Exception):
            Client.objects.create(
                client_name="Borko",
                town="Velingrad",
                bulstat="123456789",
                mol="Botko Borko Borko",
            )

    def test_update_client_when_exists(self):
        self.client_temp = Client(
            client_name="Borko",
            town="Velingrad",
            bulstat="123456789",
            mol="Botko Borko Borko",
        )
        self.client_temp.save()

        self.edit_client = Client.objects.get(id=1)
        self.edit_client.client_name = "Boris"
        self.edit_client.save()

        self.assertEqual(Client.objects.get(id=1).client_name, "Boris")
