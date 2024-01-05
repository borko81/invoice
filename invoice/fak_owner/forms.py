from django import forms

from .models import Client, Owner, OwnerBank


class OwnerBankForm(forms.ModelForm):
    class Meta:
        model = OwnerBank
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = "__all__"


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
