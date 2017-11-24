import urllib2

def get_posts():
    url = urllib2.Request('https://jsonplaceholder.typicode.com/posts')
    response = urllib2.urlopen((url))
    print(response.read())
get_posts()