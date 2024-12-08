from django.db import models


class UserProfile(models.Model):
	ROLE_CHOICES = (
		('клиент', 'клиент'),
		('преподаватель', 'преподаватель'),
		('администратор', 'администратор'),
	)
	profile_picture = models.CharField()


class Category(models.Model):
	category_name = models.CharField(max_length=32)#например, программирование, маркетинг


class Lesson(models.Model):
	title = models.CharField(max_length=32, verbose_name='название урока')
	video_url = models.URLField(max_length=200, null=True, blank=True)
	content = models.TextField()
	course_url = models.URLField(max_length=200)


class Course(models.Model):
	course_name = models.CharField(max_length=32)
	description = models.TextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	LEVEL_CHOICES = (
		('начальный', 'начальный'),
		('средний', 'средний'),
		('продвинутый', 'продвинутый')
	)
	course_price = models.PositiveIntegerField()#(для платных курсов)
	created_by = models.URLField(max_length=200)#ссылка на преподавателя
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class Assignment(models.Model):
	title = models.CharField(max_length=32)
	description = models.TextField()
	due_date = models.DateTimeField()
	course_assignment = models.URLField(max_length=200)
	students = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='students')


class Exam(models.Model):
	title = models.CharField(max_length=32)
	course_exam = models.URLField(max_length=200)
	questions = models.TextField()
	passing_score = models.PositiveSmallIntegerField(verbose_name='проходной балл', default=0)
	duration = models.DateTimeField()#(время на сдачу экзамена).


class Certificate(models.Model):
	student_certificate = models.URLField(max_length=200)
	course_certificate = models.URLField(max_length=200)
	issued_at = models.DateTimeField()#(дата выдачи).
	certificate_url = models.URLField(max_length=200)


class Review(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)#(ссылка на студента).
	course_review = models.URLField(max_length=200)
	stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Рейтинг", null=True,
								blank=True)
	comment = models.TextField()
