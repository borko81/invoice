from django.test import TestCase, Client
from django.urls import reverse
from fak_owner.models import OwnerBank, Owner


class TestOwnerView(TestCase):
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
        # self.owner = Owner(
        #     full_name="Borko",
        #     town="Велинград",
        #     address="Неизвестен",
        #     email="borko@abv.bg",
        #     bulstat="123456789",
        #     owner_banka=self.owner_bank,
        # )

    def test_view_owner(self):
        response = self.client.get(reverse("fak_owner:owner"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "fak_owner/owner.html")

    def test_create_new_owner(self):
        url = reverse("fak_owner:owner_new")
        response = self.client.post(
            url,
            {
                "full_name": "Borko",
                "town": "Велинград",
                "address": "Неизвестен",
                "email": "borko@abv.bg",
                "bulstat": "123456789",
                "owner_banka": self.owner_bank.id,
            },
        )
        new_owner = Owner.objects.get(id=1)
        self.assertEqual(new_owner.full_name, "Borko")
        self.assertEqual(response.status_code, 302)

    def test_edit_owner(self):
        self.owner_temp = Owner(
            full_name="Borko",
            town="Велинград",
            address="Неизвестен",
            email="borko@abv.bg",
            bulstat="123456789",
            owner_banka=self.owner_bank,
        )
        self.owner_temp.save()

        url = reverse("fak_owner:owner_edit", args=[1])
        response = self.client.post(
            url,
            {
                "full_name": "Борис",
                "town": "Велинград",
                "address": "Неизвестен",
                "email": "borko@abv.bg",
                "bulstat": "123456789",
                "owner_banka": self.owner_bank.id,
            },
        )
        self.owner = Owner.objects.get(id=1)
        self.assertEqual(self.owner.full_name, "Борис")
        self.assertEqual(response.status_code, 302)

    def test_edit_owner_who_not_exists(self):
        url = reverse("fak_owner:owner_edit", args=[2])
        self.assertTrue(self.client.post(url).status_code, 404)

    def test_delete_owner_records_when_exists(self):
        self.owner_temp = Owner(
            full_name="Borko",
            town="Велинград",
            address="Неизвестен",
            email="borko@abv.bg",
            bulstat="123456789",
            owner_banka=self.owner_bank,
        )
        self.owner_temp.save()

        url = reverse("fak_owner:owner_delete", args=[1])
        response = self.client.post(url, follow=True)
        self.assertTemplateUsed(response, "fak_owner/owner.html")
        self.assertEqual(response.status_code, 200)

    def test_delete_record_when_record_does_not_exists_404(self):
        url = reverse("fak_owner:owner_delete", args=[1])
        response = self.client.post(url, follow=True)
        self.assertEqual(response.status_code, 404)
