from django.test import TestCase
from django.urls import resolve, reverse
from fak_owner.views_owner import OwnerView, OwnerEdit, OwnerNew, OwnerDelete


class TestOwnerUrls(TestCase):
    def test_view_owner(self):
        url = reverse("fak_owner:owner")
        self.assertEqual(resolve(url).func.view_class, OwnerView)

    def test_add_new_owner(self):
        url = reverse("fak_owner:owner_new")
        self.assertEqual(resolve(url).func.view_class, OwnerNew)

    def test_edit_owner(self):
        url = reverse("fak_owner:owner_edit", args=[1])
        self.assertEqual(resolve(url).func.view_class, OwnerEdit)

    def test_delete_owner(self):
        url = reverse("fak_owner:owner_delete", args=[1])
        self.assertEqual(resolve(url).func.view_class, OwnerDelete)

    def test_edit_owner_with_uncorect_parameter(self):
        with self.assertRaises(Exception):
            reverse("fak_owner:owner_edit", args=["test"])

    def test_delete_owner_with_uncorect_paramether(self):
        with self.assertRaises(Exception):
            url = reverse("fak_owner:owner_delete", args=["test"])
