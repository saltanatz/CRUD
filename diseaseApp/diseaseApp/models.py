from django.db import models


class Country(models.Model):
    cname = models.CharField(max_length=50, primary_key=True)
    population = models.BigIntegerField()

    def __str__(self):
        return self.cname


class Users(models.Model):
    email = models.EmailField(max_length=60, primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.IntegerField()
    phone = models.CharField(max_length=20)
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Patients(models.Model):
    email = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Patient: {self.email}"


class DiseaseType(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=140)

    def __str__(self):
        return self.description


class Disease(models.Model):
    disease_code = models.CharField(max_length=50, primary_key=True)
    pathogen = models.CharField(max_length=20)
    description = models.CharField(max_length=140)
    id = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)

    def __str__(self):
        return self.disease_code


class Discover(models.Model):
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)
    disease_code = models.ForeignKey(Disease, on_delete=models.CASCADE)
    first_enc_date = models.DateField()

    class Meta:
        unique_together = (('cname', 'disease_code'),)

    def __str__(self):
        return f"{self.disease_code} in {self.cname}"


class PatientDisease(models.Model):
    email = models.ForeignKey(Users, on_delete=models.CASCADE)
    disease_code = models.ForeignKey(Disease, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('email', 'disease_code'),)

    def __str__(self):
        return f"{self.email} - {self.disease_code}"


class PublicServant(models.Model):
    email = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=50)

    def __str__(self):
        return f"Public Servant: {self.email}"


class Doctor(models.Model):
    email = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    degree = models.CharField(max_length=20)

    def __str__(self):
        return f"Doctor: {self.email}"


class Specialize(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Specialization {self.id} - {self.email}"


class Record(models.Model):
    email = models.ForeignKey(PublicServant, on_delete=models.CASCADE)
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)
    disease_code = models.ForeignKey(Disease, on_delete=models.CASCADE)
    total_deaths = models.IntegerField()
    total_patients = models.IntegerField()

    class Meta:
        unique_together = (('email', 'cname', 'disease_code'),)

    def __str__(self):
        return f"Record: {self.email}, {self.cname}, {self.disease_code}"
