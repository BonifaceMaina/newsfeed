import  urllib2

 def get_posts()
url = 'https://jsonplaceholder.typicode.com/posts'
req = urllib2.Request(url)
response = urllib2.urlopen(url)
d = response.read()
print (d)
get_posts()

