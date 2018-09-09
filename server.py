from flask import Flask
import redis
app = Flask(__name__)


r = redis.Redis(host="localhost", port=6379)
r.set("venusaur", 0)
r.set("charizard", 0)
r.set("blastoise", 0)
r.set("articuno", 0)
r.set("zapdos", 0)
r.set("moltres", 0)
r.set("mewtwo", 0)

# @app.errorhandler(500)
# def exception_handler(e):
#     return render_template('500.html'), 500

@app.route('/clearall')
def clearall():
	r.set("venusaur", 0)
	r.set("charizard", 0)
	r.set("blastoise", 0)
	r.set("articuno", 0)
	r.set("zapdos", 0)
	r.set("moltres", 0)
	r.set("mewtwo", 0)
	return 'cleared'

@app.route('/increment/<pokemon>')
def increment(pokemon):
	tmp = pokemon
	r.incr(tmp)    
	#return 'Incremented %s' % pokemon
	return ''

@app.route('/count/<pokemon>')
def count(pokemon):
	retval = int(r.get(pokemon))
	retstr = "{" + pokemon + " : " + str(retval) +  "}\n"
	return '%s' % retstr
