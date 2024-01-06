from django.test import TestCase
from fak_owner.forms import OwnerBankForm


class TestOwnerBankForm(TestCase):
    def test_form_is_valid(self):
        form = OwnerBankForm(
            data={
                "banka_name": "Банка Име 2",
                "banka_name_lat": "Bank Name 2",
                "kod": "12345",
                "smetka": "UA12345678",
                "last_fak_number": "0",
                "last_pr_number": "123",
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_when_missing_somerequired_field(self):
        form = OwnerBankForm(data={})
        self.assertFalse(form.is_valid())
