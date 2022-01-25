from django.db import models

class Lecture(models.Model):
	first_name = models.CharField(max_length = 20)
	last_name  = models.CharField(max_length = 20)
	email  	   = models.EmailField("Enter your Email",default = "aleludago@gmail.com")
	sid        = models.ForeignKey(
		"Student.Student",
		on_delete=models.CASCADE,
		verbose_name="Student Id",
		)

	def __str__(self):
		return self.first_name + " " + self.last_name