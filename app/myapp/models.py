from django.db import models
from myapp.managers.base import BaseModelManager
from django.utils import timezone


class BaseModel(models.Model):

    class Meta:
        abstract = True

    objects = BaseModelManager()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    deleted_on = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id or not self.created_on:
            self.created_on = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)

class Drug(BaseModel):

    class Meta:
        db_table = 'drug'
    
    # DRUG_FORM_CHOICES = (
    #     ('TABLET', 'Tablet'),
    #     ('CAPSUL', 'Capsule'),
    #     ('INJION', 'Injection'),
    #     ('SUSPNS', 'Suspension'),
    #     ('SYRUPP', 'Syrup'),
    #     ('POWDER', 'Powder'),
    #     ('ORALQD', 'Oral Liquid')
    #     ('ONTMNT', 'Ointment')
    # )

    sku_id = models.CharField(max_length=256, null=True, blank=True)
    product_id = models.CharField(max_length=256, null=True, blank=True)
    sku_name = models.CharField(max_length=512)
    price = models.DecimalField(
        max_digits=20,
        decimal_places=10,
        default=0)
    manufacturer = models.CharField(max_length=512)
    salt_name = models.CharField(max_length=512)
    drug_form = models.CharField(max_length=256)
    # drug_form = models.CharField(
    #     choices=DRUG_FORM_CHOICES, null=True, blank=True, max_length=5)
    pack_size = models.CharField(max_length=256)
    strength = models.CharField(max_length=256)
    is_banned = models.BooleanField(default=False)
    unit = models.CharField(max_length=256, null=True, blank=True)
    price_per_unit = models.DecimalField(
        max_digits=20,
        decimal_places=10,
        default=0)

# d = Drug.objects.create(
#     sku_id=270721,
#     product_id=47046,
#     sku_name='Olworm 400mg Tablet',
#     price=2.5,
#     manufacturer='Biochem Pharmaceutical Industries',
#     salt_name='Albendazole',
#     drug_form='Tablet',
#     strength='400mg'
# )