# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
	return HttpResponse("hello")

def all(request):
	products = Product.objects.all()
	context = {'products': products}
	template = 'home/all.html'
	return render (request, template, context)

def single(request):
	try:
		x = request.GET.get("q",None)
		print x
		product = Product.objects.get(productId = x)
		print product

		#images = product.productimage_set.all()
		images = ProductImage.objects.filter(product=product)
		context = {'product': product, "images": images}
		template = 'home/single.html'
		return render (request, template, context)
	except:
		raise Http404 


def buyAnotherProduct(request):
	#you have to write view for adding product into the user
	#return render(request, 'home/thanks.html', {'home':'/','about':'/about_us','products':'/products','contact':'/contact_us'})

	'''if request.method == "POST":
		parentId=request.POST.get('sponserId')
		isSponserIdValid=validateSponserId(parentId)
		errorSponserId=""
		if not isSponserIdValid:
			errorSponserId="Invalid Sponser Id"


	if isSponserIdValid:
			h_password=make_pw_hash(username,password)
			User.objects.create(sponserId=sponserId,username=username,password=h_password, plan=product,amount=0.00)
			UserDetails.objects.create(username=username,firstName=firstName,lastName=lastName, phoneNo=phoneNo,email=email,address=address)
			UserAccount.objects.create(username=username,holderName=holderName,IFSCCode=IFSCCode,bankName=bankName,branchName=branchName,
				accountType=accountType,accountNo=accountNo,panCard=panCard,panNo=panNo,aadhaarCard=aadhaarCard,aadhaarNo=aadhaarNo)
			UserRelation.objects.create(sponserId=sponserId,parentId=parentId)
			# Payment
			insertUser(parentId,sponserId)
			#set Cookie
			# redirect to homepage
			id_to_send=make_secure_val(str(sponserId))
			# print "ID TO SEND"+id_to_send
			# print "SPONSERID"+sponserId
			response = redirect('/')
			response.set_cookie('user_id', id_to_send)
			return response
		else:
			# Render The page with errors
			return render(request, 'home/sign_up.html', {'home':'/','about':'/about_us','products':'/products','contact':'/contact_us','signup':'/sign_up','errorSponserId':errorSponserId,'errorUsername':errorUsername,'errorPassword':errorPassword, 'errorPhoneNumber':errorPhoneNumber, 'errorPanNumber':errorPanNumber,'errorAdharNumber':errorAdharNumber})
	'''
	return render(request,'home/buyAnotherProduct.html', {'home':'/','about':'/about_us','products':'/products','contact':'/contact_us'})


def products(request):
	return render(request, 'home/products.html', {'home':'/','about':'/about_us','products':'/products','contact':'/contact_us','buyAnotherProduct':'/buyAnotherProduct'})
	"""if isLoggedIn(request):
		# usr=User.objects.get(sponserId=sponserId)
		greet='<a class="page-scroll" href="/dashboard">Dashboard</a>'
		logout='<a class="page-scroll" href="/logout">Logout</a>'
		# Logout link
		return render(request, 'home/products.html', {'home':'/','about':'/about_us','products':'/products','contact':'/contact_us','buyAnotherProduct':'/buyAnotherProduct','greet':greet,'logout':logout})
	else:
		greet='<a class="page-scroll" href="/sign_up">Sign Up</a>'
		return render(request, 'home/products.html', {'home':'/','about':'/about_us','products':'/products','contact':'/contact_us','buyAnotherProduct':'/buyAnotherProduct','greet':greet})

"""
