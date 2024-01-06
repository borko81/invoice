from django.test import TestCase, Client, SimpleTestCase
from django.urls import resolve, reverse
from fak_owner.views import (
    OwnerBankListView,
    OwnerBanNew,
    OwnerBankEdit,
    OwnerBankDelete,
)


class TestOwnerBankUrls(TestCase):
    def test_bank_url_resolve(self):
        url = reverse("fak_owner:bank_list")
        self.assertEqual(resolve(url).func.view_class, OwnerBankListView)

    def test_bank_new_url_resolve(self):
        url = reverse("fak_owner:bank_new")
        self.assertEqual(resolve(url).func.view_class, OwnerBanNew)

    def test_bank_edit_url_resolve(self):
        url = reverse("fak_owner:bank_edit", args=[1])
        self.assertEqual(resolve(url).func.view_class, OwnerBankEdit)

    def test_bank_delete_url_resolve(self):
        url = reverse("fak_owner:bank_delete", args=[1])
        self.assertEqual(resolve(url).func.view_class, OwnerBankDelete)

    def test_bank_edit_with_uncorect_paramether(self):
        with self.assertRaises(Exception):
            url = reverse("fak_owner:bank_edit", args=["test"])

    def test_bank_delete_with_uncorect_paramether(self):
        with self.assertRaises(Exception):
            url = reverse("fak_owner:bank_delete", args=["something"])
