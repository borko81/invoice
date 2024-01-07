from django.test import TestCase

from fak_owner.forms import ClientForm
from fak_owner.models import Client


class TestClientForm(TestCase):
    def test_client_form_is_valid(self):
        form = ClientForm(
            data={
                "client_name": "Test Client",
                "town": "Some Town",
                "address": "Unknown address",
                "bulstat": "123456789",
                "mol": "Mol Mol Mol",
            }
        )
        self.assertTrue(form.is_valid())
        form.save()
        self.c = Client.objects.get(id=1)
        self.assertEqual(self.c.client_name, "Test Client")
        self.assertEqual(self.c.town, "Some Town")
        self.assertEqual(self.c.address, "Unknown address")
        self.assertEqual(self.c.bulstat, "123456789")
        self.assertEqual(self.c.mol, "Mol Mol Mol")

    def test_client_form_is_not_valid_when_missing_parameter(self):
        form = ClientForm(data={})
        required_fields = "client_name bulstat mol".split()
        for field in required_fields:
            self.assertIn(field, form.errors)
