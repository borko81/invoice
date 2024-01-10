from django import forms

from .models import Client, Owner, OwnerBank, FakModels, FakElModels


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class FakModelsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["client"].queryset = Client.filtered_objects.only_active()

    class Meta:
        model = FakModels
        fields = (
            "bank",
            "fak_tip",
            "pay_tip",
            "client",
            "due_date",
            "status",
            "poluchena_ot",
            "date_sdelka",
            "comment",
        )

        labels = {
            "date_sdelka": "Дата сделка",
            "bank": "Банка",
            "fak_tip": "Тип",
            "client": "Клиент",
            "due_date": "Падеж",
            "status": "Статус",
            "poluchena_ot": "Получена от",
            "pay_tip": "Плащане",
        }

        widgets = {
            "date_sdelka": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
        }


class FakElModelsForm(forms.ModelForm):
    class Meta:
        model = FakElModels
        fields = ("text", "kol", "dds", "cena_brutna_ed")
