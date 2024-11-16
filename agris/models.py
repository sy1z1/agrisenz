from django.db import models

class NPKSensor(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()

    def __str__(self):
        return f"{self.timestamp}: N-{self.nitrogen}, P-{self.phosphorus}, K-{self.potassium}"
    
class AmbientSensor(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    A_Temp = models.FloatField()
    A_Humid = models.FloatField()

    def __str__(self):
        return f"{self.timestamp}: N-{self.A_Temp}, P-{self.A_Humid}"
    
class SoilSensor(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    S_Temp = models.FloatField()
    S_Humid = models.FloatField()

    def __str__(self):
        return f"{self.timestamp}: N-{self.S_Temp}, P-{self.S_Humid}"

class Settings(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.BooleanField(default=True)  # True for enabled, False for disabled

    def __str__(self):
        return self.name