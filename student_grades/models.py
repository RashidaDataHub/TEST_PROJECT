from django.db import models
import uuid

# Create your models here.


class MST_Subject(models.Model):
    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject_key = models.CharField(max_length=10, unique=True,blank=True, null=True,)
    subject_name = models.CharField(max_length=50, blank=True, null=True, unique=True)

    def __str__(self):
        return self.subject_name


class MST_Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_key = models.CharField(max_length=10, unique=True,blank=True, null=True,)
    student_name = models.CharField(max_length=50, blank=True, null=True, unique=True)
    subject_name = models.ForeignKey(MST_Subject, on_delete=models.CASCADE)
    grade = models.IntegerField()
    remarks = models.CharField(max_length=10, editable=False)

    def save(self, *args, **kwargs):
        self.remarks = 'PASS' if self.grade >= 75 else 'FAIL'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.student_name