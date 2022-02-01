from django.db import models


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_title = models.CharField(max_length=300)

    def __str__(self):
        return self.cat_title


class Product(models.Model):
    pro_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    softwareUsed = models.TextField()
    image = models.ImageField(upload_to='image/')
    imageSS1 = models.ImageField(upload_to='image/', null=True,default="",blank=True)
    imageSS2 = models.ImageField(upload_to='image/', null=True,default="",blank=True)
    imageSS3 = models.ImageField(upload_to='image/', null=True,default="",blank=True)
    imageSS4 = models.ImageField(upload_to='image/', null=True,default="",blank=True)

    def __str__(self):
        return self.name


