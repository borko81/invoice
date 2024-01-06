from django.test import TestCase

from fak_owner.forms import OwnerForm
from fak_owner.models import OwnerBank


class TestOWnerForm(TestCase):
    def setUp(self):
        self.bank = OwnerBank.objects.create(
            banka_name="Test Bank", kod="1234", smetka="1234566"
        )

    def test_form_is_valid(self):
        form = OwnerForm(
            data={
                "full_name": "Borko",
                "town": "Велинград",
                "address": "Неизвестен",
                "email": "borko@abv.bg",
                "bulstat": "123456789",
                "owner_banka": self.bank.id,
            }
        )
        # print(form.errors)
        self.assertTrue(form.is_valid())

    def test_form_is_not_valid_when_param_is_missing(self):
        form = OwnerForm(
            data={
                "full_name": "Borko",
                "town": "Велинград",
                "address": "Неизвестен",
                "email": "borko@abv.bg",
                "owner_banka": self.bank.id,
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["bulstat"][0], "This field is required.")
