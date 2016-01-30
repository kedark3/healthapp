from django.db import models
from django.contrib import admin
# Create your models here.


class HospitalPerformance(models.Model):
    def __str__(self):              # __unicode__ on Python 2
    	return self.Provider_Id
    Provider_Id = models.CharField(max_length = 10, primary_key=True)
    H_QUIET_HSP_A_P = models.DecimalField(max_digits=10, decimal_places=3)
    HAI1 = models.DecimalField(max_digits=10, decimal_places=3)
    H_CLEAN_HSP_A_P = models.DecimalField(max_digits=10, decimal_places=3)
    H_COMP_1_A_P = models.DecimalField(max_digits=10, decimal_places=3)
    H_COMP_3_A_P = models.DecimalField(max_digits=10, decimal_places=3)
    H_COMP_7_SA = models.DecimalField(max_digits=10, decimal_places=3)
    MORT_30_AMI = models.DecimalField(max_digits=10, decimal_places=3)
    MORT_30_PN = models.DecimalField(max_digits=10, decimal_places=3)
    PN_6 = models.DecimalField(max_digits=10, decimal_places=3)
    HAI4 = models.DecimalField(max_digits=10, decimal_places=3)
    H_COMP_5_A_P = models.DecimalField(max_digits=10, decimal_places=3)
    MORT_30_HF = models.DecimalField(max_digits=10, decimal_places=3)
    SCIP_INF_2 = models.DecimalField(max_digits=10, decimal_places=3)
    H_CLEAN_QUIET = models.DecimalField(max_digits=10, decimal_places=3)
    MSPB_1 = models.DecimalField(max_digits=10, decimal_places=3)
    SCIP_VTE_2 = models.DecimalField(max_digits=10, decimal_places=3)
    AMI_7A = models.DecimalField(max_digits=10, decimal_places=3)
    H_COMP_2_A_P = models.DecimalField(max_digits=10, decimal_places=3)
    H_COMP_4_A_P = models.DecimalField(max_digits=10, decimal_places=3)
    PSI_90_SAFETY = models.DecimalField(max_digits=10, decimal_places=3)
    HAI2 = models.DecimalField(max_digits=10, decimal_places=3)
    HAI3 = models.DecimalField(max_digits=10, decimal_places=3)
    H_COMP_7_A = models.DecimalField(max_digits=10, decimal_places=3)
    SCIP_INF_3 = models.DecimalField(max_digits=10, decimal_places=3)
    H_COMP_7 = models.DecimalField(max_digits=10, decimal_places=3)
    IMM_2 = models.DecimalField(max_digits=10, decimal_places=3)
    SCIP_CARD_2 = models.DecimalField(max_digits=10, decimal_places=3)
    SCIP_INF_9 = models.DecimalField(max_digits=10, decimal_places=3)
    Score = models.DecimalField(max_digits=10, decimal_places=3)


class HospitalGeneralInformation(models.Model):
    def __str__(self):              # __unicode__ on Python 2
    	return self.Provider_Id
    Provider_Id = models.CharField(max_length = 10, primary_key=True)
    Hospital_Name = models.CharField(max_length = 100)
    Address = models.CharField(max_length = 100)
    City = models.CharField(max_length = 100)
    State = models.CharField(max_length = 100)
    ZIP_Code = models.IntegerField()
    County_Name = models.CharField(max_length = 50)
    Phone_Number = models.IntegerField()
    Hospital_Type = models.CharField(max_length = 50)
    Hospital_Ownership = models.CharField(max_length = 100)
    Emergency_Services = models.CharField(max_length = 20)



admin.site.register(HospitalPerformance)
admin.site.register(HospitalGeneralInformation)
