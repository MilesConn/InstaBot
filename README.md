## What is this?
Currently the program will scrolldown and save the links to 
Facebooks CDN that fetches thumbnails. These are super low res and 
always square even though the images themselves might not be square

### Why?
Instagram (Facebook) doesn't let you easily access their API. In addition to this,
I've never found a way to access the Saved section for your own posts. This is pretty 
important to me because I save a lot of things I'm interested in there and in addition
to that Instagram posts often get taken down.

To get around this I used Selenium to dynamically load in and save all the post urls...

##How to install
You need the Selenium Chrome Webdriver for your system. Note for macOS the driver 
needs to be verified. The easiest way to do this is to install it using `brew`
```
   > brew cask install chromedriver
   > chromedriver
```
You should get an error messages and then open `System Preferences/Security & Privacy`
and allow it to run. Other systems may vary.

## How to Use
lol

## To Do
1. Get post urls and navigate to them(w/o Selenium)
   + Save higher-res & non-square version of post
  
2. Add support for carosuel galleries
3. Add support for video
4. Make code legible/ not-janky
