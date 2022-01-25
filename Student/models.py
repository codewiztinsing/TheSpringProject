from django.db import models

class Student(models.Model):
	first_name = models.CharField("First Name",max_length = 20)
	last_name  = models.CharField("Last Name",max_length = 20)
	email  	   = models.EmailField("Enter your Email")
	cid        = models.ForeignKey(
		"Course.Course",
		on_delete=models.CASCADE,
		verbose_name="",
		)

	def __str__(self):
		return self.first_name + " " + self.last_name


