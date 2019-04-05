import redis

class RedisHelper(object):
    """
    RedisHelper
    """
    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1',port=6379)
        self.chan_sub = 'channel1'
        self.chan_pub = 'channel1'

    def publish(self,msg):
        self.__conn.publish(self.chan_pub,msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_pub)
        pub.parse_response()
        return pub





