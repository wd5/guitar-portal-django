# source: http://djangosnippets.org/snippets/2768/

def formview(func):
	"""
	Decorator for separating GET and POST implementations
	Example:
	@formview
	def viewfunction(request):
		#Write code which needs to be called for both 

		def get():
			#return GET view to be rendered

		def post():
			#return view after form POST

		#Make sure to return get, post functions in the same order	
		return get, post
	"""
	def wrapped(request, *args, **kargs):
		get, post = func(request, *args, **kargs)
		if request.method == "POST": 
			return post() 
		else: 
			return get()

	return wrapped


