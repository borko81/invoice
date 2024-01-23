from django.db import models
from colorfield.fields import ColorField


FOOD_CHOICE = (("BB", "BB"), ("HB", "HB"), ("FB", "FB"), ("RO", "RO"))
DDS = (
    ("0", "0"),
    ("9", "9"),
    ("20", "20"),
)


class UslGroupsModel(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self) -> str:
        return self.name


class UslModel(models.Model):
    name = models.CharField(max_length=32, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dds = models.CharField(max_length=2, choices=DDS, default=0)
    group_usl = models.ForeignKey(
        UslGroupsModel, on_delete=models.DO_NOTHING, related_name="usls"
    )

    def __str__(self) -> str:
        return self.name


class FloorsModel(models.Model):
    name = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return str(self.name)


class RoomTypesModel(models.Model):
    name = models.CharField(max_length=32, unique=True)
    max_people = models.PositiveBigIntegerField(default=2)

    def __str__(self) -> str:
        return self.name


class RoomsModel(models.Model):
    name = models.CharField(max_length=32, unique=True)
    floor = models.ForeignKey(
        FloorsModel, on_delete=models.DO_NOTHING, related_name="floors"
    )
    room_type = models.ForeignKey(
        RoomTypesModel, on_delete=models.DO_NOTHING, related_name="types"
    )
    is_active = models.BooleanField(default=True)
    description = models.CharField(max_length=120, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    color = ColorField(default="#FF0000")

    def __str__(self) -> str:
        return self.name


class FoodsModel(models.Model):
    name = models.CharField(max_length=2, choices=FOOD_CHOICE, default="RO")
    usl_group = models.ForeignKey(
        UslGroupsModel,
        on_delete=models.DO_NOTHING,
        related_name="foods",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name


class BedsModel(models.Model):
    name = models.CharField(max_length=32, unique=True)
    age = models.FloatField(default=0)
    dop_bed = models.BooleanField(default=False)
    usl_group = models.ForeignKey(
        UslGroupsModel,
        on_delete=models.DO_NOTHING,
        related_name="beds",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["dop_bed"]

    def __str__(self) -> str:
        return self.name
