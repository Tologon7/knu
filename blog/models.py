from django.db import models


class Groups(models.Model):
    group_name = models.CharField(max_length=30, verbose_name='Название группы')
    student_quantity = models.IntegerField(verbose_name='Количество студентов')

    def __str__(self):
        return f"{self.group_name} - {self.student_quantity}"


class Week(models.Model):
    # group = models.ForeignKey(Groups, related_name='weeks', on_delete=models.CASCADE, verbose_name='Группа')
    day_name = models.CharField(max_length=15, verbose_name='День недели')  # Например, Понедельник, Вторник и т.д.z

    def __str__(self):
        return f"{str(self.day_name)}"


class Lesson(models.Model):
    group = models.ForeignKey(Groups, related_name='weeks', on_delete=models.CASCADE, verbose_name='Группа')
    week = models.ForeignKey(Week, related_name='lessons', on_delete=models.CASCADE, verbose_name='День недели')
    lesson_name = models.CharField(max_length=255, verbose_name='Предмет')
    teacher = models.CharField(max_length=255, verbose_name='Преподаватель')
    oclock = models.TimeField(verbose_name='Время')
    audience = models.IntegerField(verbose_name='Аудитория')

    def __str__(self):
        return f"{self.lesson_name} - {self.teacher} ({self.oclock}) {self.audience}"


class ScheduleFile(models.Model):
    c2b11 = models.FileField(upload_to='schedules/')
    c1b11 = models.FileField(upload_to='schedules/')
    c3b9 = models.FileField(upload_to='schedules/')
    c2b9 = models.FileField(upload_to='schedules/')
    c1b9 = models.FileField(upload_to='schedules/')
    it9 = models.FileField(upload_to='schedules/')
    updated_at = models.DateTimeField(auto_now=True)

