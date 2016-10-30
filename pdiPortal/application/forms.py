from django import forms

def app_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.name, instance.version)

class ApplicationForm(models.Model):
	"""docstring for ApplicationForm"""
	name = forms.CharField(max_length=256)
	operatingSystem = forms.CharField(max_length=40,default='Android')
	version = forms.CharField(max_length=40)
	partNumber = forms.CharField(max_length=15)
	pricePerMonth = forms.FloatField()
	description = forms.TextField(null=True)
	icon = forms.ImageField(upload_to=app_directory_path)
	banner = forms.ImageField(upload_to=app_directory_path)
	screenshot = forms.ImageField(upload_to=app_directory_path)
	applicationFile = forms.FileField(upload_to=app_directory_path)
	created = forms.DateTimeField(auto_now_add=True)


class reviewForm(forms.Form):
    title = forms.CharField(required = False, max_length = 100, help_text = '100 characters max')
    body = forms.TextField(widget = forms.Textarea)
    rating = forms.PositiveIntegerField()
    