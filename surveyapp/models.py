from django.db import models


# Create your models here.
class main_category(models.Model):
    main_cat_name=models.CharField(max_length=80)
    def __str__(self):
        return self.main_cat_name
class sub_category(models.Model):
    main_cat_name=models.ForeignKey(main_category,on_delete="CASCADE")
    sub_cat_name=models.CharField(max_length=80)

class question_type(models.Model):
    question_type=models.CharField(max_length=100)
class question(models.Model):
    question = models.CharField(max_length=200)
    sub_cat_name = models.ForeignKey(sub_category, on_delete='CASCADE')
    question_type=models.ForeignKey(question_type,on_delete='CASCADE')
    option1 = models.CharField(max_length=150)
    option2 = models.CharField(max_length=150,null=True)
    option3 = models.CharField(max_length=150, null=True)
    option4 = models.CharField(max_length=150, null=True)

