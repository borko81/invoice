from django.test import TestCase, Client
from django.urls import reverse
from fak_owner.models import OwnerBank


class TestOwnerBank(TestCase):
    def setUp(self):
        self.client = Client()
        self.owner_bank = OwnerBank.objects.create(
            banka_name="Банка Име",
            banka_name_lat="Bank Name",
            kod="1234",
            smetka="UA12345678",
            last_fak_number="0",
            last_pr_number="123",
        )

    def test_view_bank_account(self):
        response = self.client.get(reverse("fak_owner:bank_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "fak_owner/ownerbank_list.html")

    def test_create_new_bank_accout(self):
        url = reverse("fak_owner:bank_new")
        response = self.client.post(
            url,
            {
                "banka_name": "Банка Име 2",
                "banka_name_lat": "Bank Name 2",
                "kod": "12345",
                "smetka": "UA12345678",
                "last_fak_number": "0",
                "last_pr_number": "123",
            },
        )
        new_bank_account_records = OwnerBank.objects.get(id=2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(new_bank_account_records.banka_name, "Банка Име 2")
        self.assertEqual(new_bank_account_records.kod, "12345")
        self.assertEqual(new_bank_account_records.smetka, "UA12345678")
        self.assertEqual(new_bank_account_records.last_fak_number, "0000000000")
        self.assertEqual(new_bank_account_records.last_pr_number, "0000000123")

    def test_bank_account_edit(self):
        url = reverse("fak_owner:bank_edit", args=[1])
        response = self.client.post(
            url,
            {
                "banka_name": "Банка Име 2",
                "banka_name_lat": "Bank Name 2",
                "kod": "12345",
                "smetka": "UA12345678",
                "last_fak_number": "0",
                "last_pr_number": "123",
            },
        )
        edit_owner_bank_acc = OwnerBank.objects.get(id=1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(edit_owner_bank_acc.banka_name, "Банка Име 2")
        self.assertEqual(edit_owner_bank_acc.kod, "12345")
        self.assertEqual(edit_owner_bank_acc.smetka, "UA12345678")
        self.assertEqual(edit_owner_bank_acc.last_fak_number, "0000000000")
        self.assertEqual(edit_owner_bank_acc.last_pr_number, "0000000123")

    def test_bank_account_edit_not_valid_model_record_shoudl_raise_error(self):
        response = self.client.post(reverse("fak_owner:bank_edit", args=[2]))
        self.assertEqual(response.status_code, 404)

    def test_bank_account_deleted(self):
        response = self.client.post(reverse("fak_owner:bank_delete", args=[1]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(OwnerBank.objects.all()), 0)

    def test_bank_account_deleted_when_not_valid_id_should_raise_error(self):
        response = self.client.post(reverse("fak_owner:bank_delete", args=[2]))
        self.assertEqual(response.status_code, 404)
