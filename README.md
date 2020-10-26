# DurstexpressTelegramBot
This is a recent Python project I did to search for reduced items on durstexpress.de

### Disclamer
This was just a fun project to refresh my python skills and learn a bit about webscraping.
If you want the list of currently reduced items on [Durstexpress](http://www.durstexpress.de) you can easily subscribe to the existing telegram bot called *DurstExpress_bot* (the one without the logo). You will get notified every monday between 10am and 11am UTC+2.
However if you just want to look how you can scrape a website with bs4 or creating a telegram bot in a simple way check out my source code.
I compiled both python files using pyinstaller to a .sh which is running on my Raspberry Pi 3B+. To make sure the script is running all the time even if you close your ssh connection use the following command:
```bash
nohup yourScript.sh &
```
check if it's running with
```bash
htop
```
