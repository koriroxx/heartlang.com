import re
from urllib import quote
from django.utils import timezone
from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required, permission_required
from django.template import RequestContext
from django.db.models import Sum
from django.forms.util import ErrorList
from django.core.mail import send_mail

from learn.models import Language, Lesson, Page, Game
from blog.models import Post
from users.models import Profile, Badges
from heartlang.forms import RegisterForm

def home(Request):
	Languages = Language.objects.order_by("pk")
	Posts = Post.objects.order_by("pk")
	
	if Request.user.is_authenticated(): 
		#Set the current profile
		CurrProfile = Profile.objects.filter(user=Request.user)[0]
			
		#Get the user's badge(s)
		ProfileBadges = CurrProfile.get_badges()
		totalhearts = 0;
		#Get the total amount of hearts a user has
		for badges in ProfileBadges:
			totalhearts += badges.hearts

		
	else: 
		ProfileBadges = None
	
	
	return render_to_response('index.html', {'language_list': Languages, 'post_list': Posts, 'badges_list': ProfileBadges, 'profile': CurrProfile, 'total_hearts': totalhearts}, context_instance=RequestContext(Request))

	
def logout_page(Request):
	"""
	Log out a user and redirects them back to the main page
	"""
	if Request.user.is_authenticated():
		logout(Request)
	

def register(Request):
	 """
    Displays a form for a user to register with and 
    then redircts them to their new profile
    """

	if Request.method == 'POST':
		form = RegisterForm(Request.POST)
		""" if form.is_valid():
            errors = form._errors.setdefault("__all__", ErrorList())
			try:
				User.objects.get(username__iexact=form.cleaned_data['username'])
				errors.append(u'That username is already taken.')
			except User.DoesNotExist:
				password = form.cleaned_data['password']

				if password != form.cleaned_data['verify_password']:
					errors.append(u'Passwords must be the same.')
				elif len(password) < 8:
					errors.append(u'Passwords must be eight characters or longer.')
				else:
					time = datetime.datetime.now()

					password = make_password(password)
					user = User(username=form.cleaned_data['username'], password=password, email=form.cleaned_data['email'])
					user.is_active = False
					user.save()					

					random.seed(time)
					m = hashlib.sha256()
					m.update(str(random.random()))
					m.update(user.username)
					m.update("aBFe6KlZ46jfM8O01FrTySjKlMqWzXcVbUio36s8Jd7fnJHD4h93hv8d2hdqWeid90")
					m.update(user.password)

					profile = Profile(user=user, activation_key=m.hexdigest(), key_expires=(datetime.datetime.today() + datetime.timedelta(2)))
					profile.save()

					email_subject = "Welcome to Gekinzuku! Please confirm your account."
					email_body = "Hello %s. Welcome to Gekinzuku.\n\nPlease click this link within 48 hours to activate your account: http://66.172.33.16:8080/profile/activate/%s\n\nThanks!" % (user.username, profile.activation_key)
					send_mail(email_subject, email_body, 'donotreply@gekinzuku.com', [user.email])

					user.backend = 'profile.backends.CaseInsensitiveModelBackend'
					login(Request, user)
					return HttpResponseRedirect('/profile/')
		"""
	else:
		form = RegisterForm()

	return render_to_response('registration/register.html', {'form': form}, context_instance=RequestContext(Request))

