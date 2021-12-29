import redis
host = 'localhost'
port = '6379'


def redis_string():
    try:
        r = redis.StrictRedis(host=host, port=port, decode_responses=True)
        r.set("message", "Hi, it's me")
        msg = r.get('message')
        print(msg)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    redis_string()