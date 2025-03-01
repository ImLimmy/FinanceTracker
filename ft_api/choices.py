from django.db import models

class Suffix(models.TextChoices):
    NONE = '', ''
    JR = 'Jr.', 'Jr.'
    SR = 'Sr.', 'Sr.'
    I = 'I', 'I'
    II = 'II', 'II'
    III = 'III', 'III'
    IV = 'IV', 'IV'
    V = 'V', 'V'
    VI = 'VI', 'VI'
    VII = 'VII', 'VII'
    VIII = 'VIII', 'VIII'
    IX = 'IX', 'IX'
    X = 'X', 'X'
    OTHER = 'Other', 'Other'

class Gender(models.TextChoices):
    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'
    OTHER = 'Other', 'Other'

class CivilStatus(models.TextChoices):
    SINGLE = 'Single', 'Single'
    MARRIED = 'Married', 'Married'
    DIVORCED = 'Divorced', 'Divorced'
    SEPARATED = 'Separated', 'Separated'
    WIDOW = 'Widow', 'Widow'
    OTHER = 'Other', 'Other'