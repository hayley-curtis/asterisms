from django.db import models




class Culture(models.Model): 
    culture_name = models.CharField(max_length=200)
    geographic_region = models.CharField(max_length=200, null=True, blank=True) 
    culture_desc = models.CharField(max_length=1000, blank=True, null=True)
    culture_img = models.CharField(max_length=30, blank=True, null=True)
    culture_img_2 = models.CharField(max_length=30, blank=True, null=True)
    

    def __str__(self): 
        return self.culture_name
    
    
class Asterism(models.Model): 
    asterism_name = models.CharField(max_length=200)
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    asterism_desc = models.CharField(max_length=1000, blank=True, null=True)
    asterism_img = models.CharField(max_length=30, blank=True, null=True)
    asterism_img_2 = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self): 
        return self.asterism_name


class Stars(models.Model):
    star_hip = models.IntegerField()
    star_ra = models.FloatField()
    star_dec = models.FloatField()
    asterisms = models.ForeignKey(Asterism, on_delete=models.CASCADE)

def __str__(self): 
        return str(self.star_id)



    




#here are some past potential models -- to keep just in case 

#class Constellation(models.Model):
    #constellation_name = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')

    #def __str__(self): 
        #return self.constellation_name


#class Star(models.Model):
    #constellation = models.ForeignKey(Constellation, on_delete=models.CASCADE)
    #star_name = models.CharField(max_length=200, default= 'none')
    #star_hd = models.IntegerField(default=0)

    #def __str__(self):
        #return self.star_name
    
#class StarSample(models.Model): 
    #star_hd = models.IntegerField()
    #star_proper_name = models.CharField(max_length=200)
    #asterism = models.ForeignKey(Asterism, on_delete=models.CASCADE)
    #asterism = models.ManyToManyField(Asterism)??

    #def __str__(self): 
        #return str(star_hd)