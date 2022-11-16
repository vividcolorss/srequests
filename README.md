# srequests

## A package for taking requests from a Scratch project

![PyPI Version](https://img.shields.io/pypi/v/srequests?style=for-the-badge) ![Forks](https://img.shields.io/github/forks/heyimocto/srequests?style=for-the-badge)  ![License](https://img.shields.io/github/license/heyimocto/srequests?style=for-the-badge)

## Documentation

For making a project, open [this project](https://scratch.mit.edu/projects/759181792/) and backpack the main sprite

## Connect to a project

To connect to a project, import the library and connect to a project with your credentials.

```py
from srequests import srequests

sr = srequests.SRequests("Username","Pass","ProjectID")
```

## Check if request is unanswered

To check if there is an unanswered request, use `Request.IsPending()`.

```py
if sr.Request.IsPending():
    print("Request unanswered!")
```

## Respond to a request

To reply, use the function `Request.Respond()`.

```py
if sr.Request.IsPending():
    sr.Request.Respond("Response")
```

## Get request data

To get the request info & content, use `Request.GetName()` and `Request.GetContent()`.

```py
name = sr.Request.GetName()
content = sr.Request.GetContent()
```

## Get user info (new in 0.0.3)

You can also get info of the user that sent the request.

To get the user's name you can use the `Request.User.GetName()` function, which returns the name of the user.

To get more user info , you can also use the `Request.User.GetData()` function.

### Attributes of GetData

```py
user.join_date
user.about_me
user.wiwo
user.country
user.icon_url
```
