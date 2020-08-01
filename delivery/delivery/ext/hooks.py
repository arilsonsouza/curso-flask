
def init_app(app):
	@app.before_first_request
	def init_everything():
		print("Run before first request")