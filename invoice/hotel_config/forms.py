from django import forms

from . import models


class FloorForm(forms.ModelForm):
    class Meta:
        model = models.FloorsModel
        fields = ("name",)


class BedsForm(forms.ModelForm):
    class Meta:
        model = models.BedsModel
        fields = "__all__"
        labels = {
            "name": "Име",
            "age": "Години",
            "dop_bed": "Допълнително легло",
            "usl_group": "Група",
        }

    def __init__(self, *args, **kwargs):
        super(BedsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
