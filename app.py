from baka import Baka
from redis import Redis

app = Baka(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello(request):
    count = redis.incr('hits')
    return 'Hello from Docker! I\'m Baka Framework, It have been seen {} times.\n'.format(count)


@app.route('/events')
def events(request):
   return {'Hello': 'Hello From Baka Dockers'}


app.scan()

if __name__ == "__main__":
    app.run(host="0.0.0.0", use_reloader=True)
