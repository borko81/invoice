from django.test import TestCase

from fak_owner.models import Owner, OwnerBank


class TestOwnerMethod(TestCase):
    def setUp(self):
        self.bank = OwnerBank.objects.create(
            banka_name="Test Bank", kod="1234", smetka="1234566"
        )

    def test_successfully_created_new_owner(self):
        self.owner_create = Owner(
            full_name="Borko",
            town="Велинград",
            address="Неизвестен",
            email="borko@abv.bg",
            owner_banka=self.bank,
        )
        self.owner_create.save()
        self.assertEqual(len(Owner.objects.all()), 1)
        self.owner = Owner.objects.get(id=1)
        self.assertEqual(self.owner.full_name, "Borko")
        self.assertEqual(self.owner.bulstat, "")

    def test_raise_error_when_try_to_save_another_owner(self):
        self.owner_create = Owner(
            full_name="Borko",
            town="Велинград",
            address="Неизвестен",
            email="borko@abv.bg",
            owner_banka=self.bank,
        )
        self.owner_create.save()
        with self.assertRaises(Exception):
            Owner.objects.create(
                full_name="Borko1",
                town="Велинград",
                address="Неизвестен",
                email="borko@abv.bg",
                owner_banka=self.bank,
            )
        self.assertEqual(len(Owner.objects.all()), 1)

    def test_update_owner_model(self):
        self.owner_create = Owner(
            full_name="Borko",
            town="Велинград",
            address="Неизвестен",
            email="borko@abv.bg",
            owner_banka=self.bank,
        )
        self.owner_create.save()
        self.check_owner = Owner.objects.get(id=1)
        self.check_owner.full_name = "Борис"
        self.check_owner.save()
        self.assertEqual(self.check_owner.full_name, "Борис")
        self.assertEqual(len(Owner.objects.all()), 1)
