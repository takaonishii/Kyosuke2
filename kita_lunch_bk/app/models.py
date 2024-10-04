from django.db import models
class UserInfo(models.Model):
    user_id = models.AutoField(primary_key=True, verbose_name="ユーザID")  # 主キー				
    last_name = models.CharField(max_length=50, verbose_name="名字")				
    first_name = models.CharField(max_length=50, verbose_name="名前")				
    age_group = models.CharField(max_length=2, verbose_name="年代")				
    gender = models.CharField(max_length=1, verbose_name="性別")				
    department_cd = models.CharField(max_length=10, verbose_name="所属部署CD")				
				
def __str__(self):				
    return f"{self.user_id} - {self.last_name} {self.first_name}"				

from django.db import models

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name
    

