from django.db import models
class UserInfo(models.Model):
    user_id = models.AutoField(primary_key=True, verbose_name="ユーザID")  # 主キー				
    first_name = models.CharField(max_length=50, verbose_name="名字")				
    last_name = models.CharField(max_length=50, verbose_name="名前")				
    age_group = models.CharField(max_length=2, verbose_name="年代")				
    gender = models.CharField(max_length=1, verbose_name="性別")				
    department_cd = models.CharField(max_length=10, verbose_name="所属部署CD")				
				
    def __str__(self):				
        return f"{self.user_id} - {self.last_name} {self.first_name}"				
    class Meta:
        db_table = 'user_info'

from django.db import models

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'genre_info'

from django.db import models

class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True) 
    tag_name = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.tag_name  
    
    class Meta:
        verbose_name = 'タグ'
        verbose_name_plural = 'タグ'
        db_table = 'Tag_info'

from django.db import models

class Area(models.Model):
    area_id = models.AutoField(primary_key=True)  # エリアID（自動でインクリメントされる）
    area_name = models.CharField(max_length=100, unique=True)  # エリア名（重複を防ぐためにユニークに設定）

    def __str__(self):
        return self.area_name  # 管理画面などでエリア名を表示

    class Meta:
        verbose_name = 'エリア'
        verbose_name_plural = 'エリア'
        db_table = 'Area_info'

from django.db import models

class Store(models.Model):
    store_id = models.AutoField(primary_key=True)  # 店舗ID（自動でインクリメント）
    store_name = models.CharField(max_length=200)  # 店名
    address = models.CharField(max_length=300)  # 住所
    phone_number = models.CharField(max_length=15)  # 電話番号
    menu = models.TextField()  # メニュー（複数行テキスト）
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 金額（少数点付きで保存）
    photo = models.ImageField(upload_to='store_photos/', blank=True, null=True)  # 写真（画像ファイルのアップロード）
    business_hours = models.CharField(max_length=100)  # 営業時間
    map_link = models.URLField(max_length=300, blank=True, null=True)  # 地図リンク（Google MapsなどのURL）
    payment_methods = models.CharField(max_length=200)  # 支払い方法（例: 現金、クレジットカードなど）

    def __str__(self):
        return self.store_name  # 管理画面で店舗名を表示

    class Meta:
        verbose_name = '店舗'
        verbose_name_plural = '店舗'
        db_table = 'Store_info'


    

    

