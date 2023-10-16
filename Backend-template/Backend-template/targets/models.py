from django.db import models

class Target(models.Model):
    name = models.CharField(max_length= 100)
    attack_priority =models.IntegerField()
    longitude = models.DecimalField(decimal_places=5 , max_digits= 1000)       #רוחב 
    latitude = models.DecimalField(decimal_places=5 , max_digits= 1000)   # אורך 
    enemy_organization = models.CharField(max_length= 100)
    target_goal = models.CharField(max_length= 100)
    was_target_destroyed = models.BooleanField()
    target_id = models.IntegerField(primary_key= True)
    
    def __str__(self) -> str:
        return f"{self.name}, {self.attack_priority }, {self.longitude} , {self.latitude},{self.enemy_organization},{self.target_goal}, {self.was_target_destroyed}, {self.target_id}"
    # Implement here a target model with a __str__ function
