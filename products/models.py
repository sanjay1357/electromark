from django.db import models

    
MOCAT_CHOICES = ( 
    ("MOBILES", "MOBILES"), 
    ("TABLETS", "TABLETS"),

     
) 

MORAM_CHOICES = ( 
    ("512", "512MB"), 
    ("1", "1GB"),
    ("2", "2GB"),
    ("3", "3GB"),
    ("4", "4GB"),
    ("6", "6GB"),
    ("8", "8GB"),
    ("12", "12GB"),
    ("16", "16GB"),   
) 

MOROM_CHOICES = ( 
    ("512", "512MB"), 
    ("1", "1GB"),
    ("4", "4GB"),
    ("6", "6GB"),
    ("8", "8GB"),
    ("16", "16GB"),
    ("32", "32GB"),
    ("64", "64GB"),
    ("128", "128GB"), 
    ("256", "256GB"),   
) 



class Mobiles(models.Model):
    
    category = models.CharField(max_length=10,choices = MOCAT_CHOICES,default = 'MOBILES')
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    oriprice = models.IntegerField()
    curprice = models.IntegerField()
    
    stock = models.IntegerField()
    img1 = models.ImageField(upload_to='mobiles')
    img2 = models.ImageField(upload_to='mobiles')
   
    rating = models.IntegerField()
    description = models.CharField(max_length = 800)
    processor = models.CharField(max_length=50)
    pricamera = models.FloatField()
    seccamera = models.FloatField()
    ram= models.IntegerField(choices = MORAM_CHOICES,default = '512')
    internal = models.IntegerField(choices = MOROM_CHOICES,default = '512')
    color = models.CharField(max_length=30)
    battery =  models.IntegerField()
    discount =  models.IntegerField(null=True)
    


PCCAT_CHOICES = ( 
    ("COMPUTERS", "COMPUTERS"), 
    ("LAPTOPS", "LAPTOPS"),

     
) 


PCRAM_CHOICES = ( 
   
    ("2", "2GB"),
    ("4", "4GB"),
    ("6", "6GB"),
    ("8", "8GB"),
    ("16", "16GB"),   
) 

PCHDD_CHOICES = ( 
    ("0", "NIL"), 
    ("32", "32GB"),
    ("250", "250GB"),
    ("320", "320GB"),
    ("500", "500GB"),
    ("1", "1TB"),
    ("2", "2TB"),
    ("3", "3TB"),
    ("4", "4TB"), 
       
) 

PCSSD_CHOICES = ( 
    ("0", "NIL"), 
    ("8", "8GB"),
    ("128", "128GB"),
    ("256", "256GB"),
    ("512", "512GB"),
    ("500", "500GB"),
    ("1", "1TB"),
    ("2", "2TB"), 
       
) 

class Pc(models.Model):
    
    category = models.CharField(max_length=10,choices = PCCAT_CHOICES,default = 'COMPUTERS')
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=70)
    oriprice = models.IntegerField()
    curprice = models.IntegerField()
    stock = models.IntegerField()
    img1 = models.ImageField(upload_to='pc')
    img2 = models.ImageField(upload_to='pc')
    
    rating = models.IntegerField()
    description = models.CharField(max_length = 800)
    pcram = models.IntegerField(choices = PCRAM_CHOICES,default = '2')
    pcharddisk = models.IntegerField(choices = PCHDD_CHOICES,default = '0')
    pcprocessor =  models.CharField(max_length=50)
    pcssd =  models.IntegerField(choices = PCSSD_CHOICES,default = '0')
    discount =  models.IntegerField(null=True)


TVRES_CHOICES = ( 
    ("NORMAL", "NORMAL"), 
    ("FULL HD", "FULL HD"),
    ("HD READY", "HD READY"),
    ("4K", "4K"),
    ("8K", "8K"),
) 


TVSCREEN_CHOICES = ( 
    ("LED", "LED"), 
    ("OLED", "OLED"),
    ("QLED", "QLED"),
    
) 


TVSMART_CHOICES = ( 
    ("YES", "YES"), 
    ("NO", "NO"),
    
    
) 

class Tv(models.Model):
    
    category = models.CharField(max_length=10)
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=70)
    oriprice = models.IntegerField()
    curprice = models.IntegerField()
    stock = models.IntegerField()
    img1 = models.ImageField(upload_to='tv')
    img2 = models.ImageField(upload_to='tv')
   
    rating = models.IntegerField()
    description = models.CharField(max_length = 800)
    screensize=models.IntegerField()
    resolution=models.CharField(max_length=20,choices = TVRES_CHOICES,default = 'NORMAL')
    screentype=models.CharField(max_length=10,choices = TVSCREEN_CHOICES,default = 'LED')
    smarttv=models.CharField(max_length=10,choices = TVSMART_CHOICES,default = 'YES')
    discount =  models.IntegerField(null=True)


ACCCAT_CHOICES = ( 
    ("HEADSETS", "HEADSETS"), 
    ("MOBILE CASES", "MOBILE CASES"),
    ("TEMPERED GLASS", "TEMPERED GLASS"),
    ("MOBILE CHARGERS", "MOBILE CHARGERS"),
    ("MOUSE", "MOUSE"),
    ("POWER BANKS", "POWER BANKS"),
    ("EXTERNAL HARD DISKS", "EXTERNAL HARD DISKS"),
    ("KEYBOARDS", "KEYBOARDS"),
) 



class Accessories(models.Model):
    
    subcategory1 = models.CharField(max_length=25,choices = ACCCAT_CHOICES,default = 'HEADSETS')
    accbrand = models.CharField(max_length=20)
    name = models.CharField(max_length=70)
    oriprice = models.IntegerField()
    curprice = models.IntegerField()
    stock = models.IntegerField()
    img1 = models.ImageField(upload_to='accessories')
    img2 = models.ImageField(upload_to='accessories')
    
    rating = models.IntegerField()
    description = models.CharField(max_length = 800)
    acctype = models.CharField(max_length=80,null=True)
    accfeatures = models.CharField(max_length=80,null=True)
    accinterfaces = models.CharField(max_length=80,null=True)
    acccapacity = models.IntegerField(null=True)
    accconnectivity = models.CharField(max_length=80,null=True)
    discount =  models.IntegerField(null=True)


APPCAT_CHOICES = ( 
    ("WASHING MACHINE", "WASHING MACHINE"), 
    ("REFRIGERATORS", "REFRIGERATORS"),
    ("AIR CONDITIONERS", "AIR CONDITIONERS"),
    ("FANS", "FANS"),   
) 

class Appliances(models.Model):
    
    subcategory2 = models.CharField(max_length=25,choices = APPCAT_CHOICES,default = 'FANS')
    appbrand = models.CharField(max_length=20)
    name = models.CharField(max_length=70)
    oriprice = models.IntegerField()
    curprice = models.IntegerField()
    stock = models.IntegerField()
    img1 = models.ImageField(upload_to='appliances')
    img2 = models.ImageField(upload_to='appliances')
    
    rating = models.IntegerField()
    description = models.CharField(max_length = 800)
    apptype = models.CharField(max_length=70)
    appcapacity = models.FloatField()
    appsize = models.IntegerField(null=True)
    appfeatures = models.CharField(max_length=70,null=True)
    discount =  models.IntegerField(null=True)






