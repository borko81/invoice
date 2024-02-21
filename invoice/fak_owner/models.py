from django.db import models

from django.db.models.signals import post_delete
from django.dispatch import receiver

from decimal import Decimal
from datetime import datetime


FAK_TYPE = (
    ("Фактура", "Фактура"),
    ("Проформа фактура", "Проформа фактура"),
    ("Кредитно известие", "Кредитно известие"),
)

DUEDATE = (
    ("now", "now"),
    ("14 days", "14 days"),
    ("30 days", "30 days"),
    ("60 days", "60 days"),
)

STATUS = (
    ("CURRENT", "CURRENT"),
    ("EMAIL_SENT", "EMAIL_SENT"),
    ("OVERDUE", "OVERDUE"),
    ("PAID", "PAID"),
    ("DELETED", "DELETED"),
)

PAY_TIP = (
    ("Брой", "Брой"),
    ("Карта", "Карта"),
    ("Банка", "Банка"),
)

DDS = ((0, 0), (9, 9), (20, 20))


class OwnerBank(models.Model):
    DEFAULT_PK = 1
    banka_name = models.CharField(max_length=52)
    banka_name_lat = models.CharField(max_length=52, null=True, blank=True)
    kod = models.CharField(max_length=12)
    smetka = models.CharField(max_length=52)
    # last_fak_number = models.CharField(max_length=10, default="0")
    # last_pr_number = models.CharField(max_length=10, default="0")

    def __str__(self):
        return self.banka_name

    # def save(self, *args, **kwargs):
    #     self.last_fak_number = self.last_fak_number.zfill(10)
    #     self.last_pr_number = self.last_pr_number.zfill(10)
    #     super().save(*args, **kwargs)


class Owner(models.Model):
    full_name = models.CharField(max_length=52)
    full_name_lat = models.CharField(max_length=52, null=True, blank=True)
    town = models.CharField(max_length=32, null=True, blank=True)
    town_lat = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=32)
    address_lat = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    owner_banka = models.ForeignKey(OwnerBank, on_delete=models.DO_NOTHING)
    bulstat = models.CharField(max_length=9, blank=False, null=False)
    id_nomer = models.CharField(max_length=11, blank=True, null=True)
    url = models.EmailField(blank=True, null=True)
    image = models.ImageField(default="default.jpg", upload_to="owner_picture")
    mol = models.CharField(max_length=120)

    last_fak_number = models.CharField(max_length=10, default="0")
    last_pr_number = models.CharField(max_length=10, default="0")

    def save(self, *args, **kwargs):
        self.last_fak_number = self.last_fak_number.zfill(10)
        self.last_pr_number = self.last_pr_number.zfill(10)
        if not self.pk and Owner.objects.exists():
            raise ValueError("This model has already its record.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class ClientManager(models.Manager):
    def only_active(self):
        return self.get_queryset().filter(is_deleted=False)

    def only_unactive(self):
        return self.get_queryset().filter(is_deleted=True)


class Client(models.Model):
    client_name = models.CharField(max_length=52)
    town = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=32)
    bulstat = models.CharField(max_length=9, unique=True)
    id_nomer = models.CharField(max_length=11, blank=True, null=True)
    mol = models.CharField(max_length=72)
    is_deleted = models.BooleanField(default=False)
    email = models.EmailField(blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    comment = models.CharField(max_length=120, blank=True, null=True)

    objects = models.Manager()
    filtered_objects = ClientManager()

    def __str__(self):
        return self.client_name

    class Meta:
        ordering = ["client_name"]

    # def only_not_deleted(self):
    #     return


class FakModels(models.Model):
    bank = models.ForeignKey(
        OwnerBank, on_delete=models.CASCADE, default=OwnerBank.DEFAULT_PK
    )
    owner = models.ForeignKey(Owner, default=1, on_delete=models.PROTECT)
    fak_number = models.CharField(max_length=10, blank=True, null=True)
    fak_tip = models.CharField(max_length=32, choices=FAK_TYPE, default="Фактура")
    pay_tip = models.CharField(max_length=32, choices=PAY_TIP, default="Брой")
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    suma = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    dds = models.IntegerField(choices=DDS, default=20)
    cena_netna_total = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    dds_suma = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    due_date = models.CharField(max_length=10, choices=DUEDATE, default="now")
    status = models.CharField(max_length=32, choices=STATUS, default="CURRENT")
    poluchena_ot = models.CharField(max_length=52)
    date_sdelka = models.DateField(auto_now_add=False)
    date_created = models.DateField(blank=True, null=True)
    comment = models.CharField(max_length=120, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.fak_number)

    def save(self, *args, **kwargs):
        self.bank_name = self.bank
        if not self.pk:
            if self.fak_tip == "Фактура" or self.fak_tip == "Кредитно известие":
                self.fak_number = str(int(self.owner.last_fak_number) + 1).zfill(10)
                self.owner.last_fak_number = self.fak_number
                self.owner.save()
            elif self.fak_tip == "Проформа":
                self.fak_number = str(int(self.owner.last_pr_number) + 1).zfill(10)
                self.owner.last_pr_number = self.fak_number
                self.owner.save()
        self.date_created = datetime.now()
        super().save(*args, **kwargs)


class FakElModels(models.Model):
    # me = [("бр.", "бр"), ("кг.", "кг."), ("л.", "л."), ("пакет", "пакет"), ("т.", "т.")]
    fak_id = models.ForeignKey(
        FakModels, on_delete=models.CASCADE, blank=True, null=True
    )
    text = models.CharField(max_length=52)
    kol = models.PositiveIntegerField(default=1)
    dds = models.IntegerField(choices=DDS, default=20)
    cena_brutna_ed = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    cena_netna_ed = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True
    )
    cena_netna_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True
    )
    dds_suma = models.DecimalField(max_digits=8, decimal_places=2, null=2, blank=2)
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total = self.kol * self.cena_brutna_ed
        self.cena_netna_ed = self.cena_brutna_ed / Decimal(1 + self.dds / 100)
        self.cena_netna_total = self.cena_netna_ed * self.kol
        self.dds_suma = self.total - self.cena_netna_total
        if not self.pk:
            current_fak = FakModels.objects.get(fak_number=self.fak_id.fak_number)
            current_fak.suma += self.total
            current_fak.dds = self.dds
            current_fak.cena_netna_total += self.cena_netna_total
            current_fak.dds_suma += self.dds_suma
            current_fak.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fak_id.fak_number};{self.text};{self.cena_netna_ed};{self.dds};{self.dds_suma};{self.total}"


@receiver(post_delete, sender=FakElModels)
def model_delete(sender, instance, **kwargs):
    current_fak = FakModels.objects.get(fak_number=instance.fak_id.fak_number)
    current_fak.suma -= instance.total
    current_fak.cena_netna_total -= instance.cena_netna_total
    current_fak.dds_suma -= instance.dds_suma
    current_fak.save()
