from django.test import TestCase
from fak_owner.models import OwnerBank


class TestOwnerBankModel(TestCase):
    def setUp(self):
        self.bank_for_test = OwnerBank.objects.create(
            banka_name="Първа",
            kod="1234",
            smetka="123456789",
            last_fak_number="12",
            last_pr_number="0",
        )

    def test_validate_number_for_fak_and_pr(self):
        self.assertEqual(self.bank_for_test.last_fak_number, "0000000012")
        self.assertEqual(self.bank_for_test.last_pr_number, "0000000000")
