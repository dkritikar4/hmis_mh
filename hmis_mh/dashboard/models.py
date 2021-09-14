from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class MhAreaDetails(models.Model):
    area_parent_id = models.IntegerField(blank=True, null=True)
    area_name = models.CharField(max_length=100, blank=True, null=True)
    area_level = models.IntegerField(blank=True, null=True)
    area_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'mh_area_details'

class MhDSdPw(models.Model):
    financial_year = models.CharField(max_length=20, blank=True, null=True)
    month = models.TextField(blank=True, null=True)  # This field type is a guess.
    tot_no_pw_reg_anc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_early_anc_register = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_anc_4_or_more = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_pw_given_tt1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_pw_given_tt2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_pw_given_tt_booster = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_pw_given_calcium = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_pw_given_ifa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_pw_given_albendazole = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_pw_moderate_anaemia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_pw_severe_anaemia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_pw_severe_anaemia_treated = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_preterm_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_institutional_delivery = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_home_delivery = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_c_section_deliveries = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_chld_born = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_still_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_spontaneous_abortion = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_mtp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    early_anc_register = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    anc_4_or_more = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    pw_tt1_given = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    pw_tt2_given = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    pw_tt_booster_given = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    pw_calcium = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    pw_ifa = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    pw_albendazole = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    per_pw_given_tt1_or_tt_booster = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    per_severe_anaemia_tested_treated = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    per_pw_outcome = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    preterm_birth_rate = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    c_section_deliveries = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    per_still_birth = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    area_parent_id = models.IntegerField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mh_d_sd_pw'

class MhDSdCi(models.Model):
    financial_year = models.CharField(max_length=20, blank=True, null=True)
    month = models.TextField(blank=True, null=True)  # This field type is a guess.
    tot_chld_born = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    chld_immunzt_vit_k1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    chld_immunzt_bcg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    chld_immunzt_9to11m_mr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    chld_immunzt_vit_a_dose_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_12to59m_albendazole = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    chld_immunzt_dpt1_penta1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    chld_immunzt_dpt2_penta2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    chld_immunzt_dpt3_penta3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    per_chld_immunzt_vit_k1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_chld_immunzt_bcg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_chld_immunzt_9to11m_mr = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_chld_immunzt_vit_a_dose_1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_no_chld_12to59m_albendazole = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_chld_immunzt_dpt1_penta1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_chld_immunzt_dpt2_penta2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_chld_immunzt_dpt3_penta3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    area_parent_id = models.IntegerField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mh_d_sd_ci'

class MhDSdCd(models.Model):
    financial_year = models.CharField(max_length=20, blank=True, null=True)
    month = models.TextField(blank=True, null=True)  # This field type is a guess.
    tot_chld_born = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    chld_disease_pneumonia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    chld_disease_sepsis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    chld_disease_tb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    chld_disease_malaria = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    chld_disease_diarrhoea = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    chld_disease_diarrhoea_trtd_inpatnt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    chld_admtd_upper_resp_infec = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    chld_disease_sam = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    per_chld_disease_pneumonia = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_chld_disease_sepsis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_chld_disease_tb = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_chld_disease_malaria = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_chld_disease_diarrhoea = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_chld_disease_diarrhoea_trtd_inpatnt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_chld_admtd_upper_resp_infec = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_chld_disease_sam = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    area_parent_id = models.IntegerField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mh_d_sd_cd'
        