Redis发布订阅（pub/sub）是一种消息通信模式，发送者（pub）发送消息，订阅者（sub）接收消息。Redis客户端可以订阅任意数量的频道。
当有新消息通过publish命令发送给频道channel1时，这个消息就会被发送给订阅它的三个客户端。