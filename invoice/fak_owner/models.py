from django.db import models


class OwnerBank(models.Model):
    banka_name = models.CharField(max_length=52)
    banka_name_lat = models.CharField(max_length=52, null=True, blank=True)
    kod = models.CharField(max_length=12)
    smetka = models.CharField(max_length=52)
    last_fak_number = models.CharField(max_length=10, default="0")
    last_pr_number = models.CharField(max_length=10, default="0")

    def __str__(self):
        return self.banka_name

    def save(self, *args, **kwargs):
        self.last_fak_number = self.last_fak_number.zfill(10)
        self.last_pr_number = self.last_pr_number.zfill(10)
        super().save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
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
