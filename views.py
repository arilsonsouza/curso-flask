from flask import Flask

""" Extensão do Flask"""
def init_app(app: Flask):
	""" Factory de inicialização de extensões"""
	@app.route('/')
	def index():
		return '<h1>Hello, CodeShow</h1>'

	@app.route('/about')
	def about():
		return '<h1>This is the best delivery wesbite!</h1>'

	@app.route('/contato')
	def contact():
		return '<form><input type="text"/></form>'