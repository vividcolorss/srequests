# srequests
## A package for taking requests from a Scratch project.

# Documentation
## For making a project, open this project and backpack the main sprite: https://scratch.mit.edu/projects/759181792/

## Connect to a project
To connect to a project, import the library and connect to a project with your credentials.

```
from srequests import srequests

sr = srequests.SRequests("Username","Pass","ProjectID")
```

## Check if request is unanswered.
To check if there is an unanswered request, use Request.IsPending().

```
if sr.Request.IsPending():
    print("Request unanswered!")
```

## Respond to a request
To reply, use the function Request.Respond().

```
if sr.Request.IsPending():
    sr.Request.Respond("Response")
```

## Get request data
To get the request info & content, use Request.GetName() and Request.GetContent().

```
name = sr.Request.GetName()
content = sr.Request.GetContent()
```
