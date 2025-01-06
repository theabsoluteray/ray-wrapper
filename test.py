from ray import Ray

token = "your_token_here"  # your token must be string tho
guild = 123456789  # guild id must be int

# added the proxy support u can use any proxies u want put them in a txt file format should be ip:port
# specify the path of proxy file
proxy = "proxies.txt"

# proxy parameter is optional u can remove it if u dont want to use proxies
ray = Ray(token,guild,proxy_file=proxy)

#number of messages u want to send must be int
spam_count = 10
#message u want to send must be string
message = "Hello, world!"
ray.spam_channels(spam_count,message)

#number of channels u want to create
count = 400 
#message u want to send
spam_message="idk lol"
ray.create_channels(count,spam_message)

#ban all members
ray.massban(reason="rayuwu")

#kick all members
ray.masskick(reason="rayuwu")

#prune server
day =7 
ray.prune(day,reason="rayuwu")
