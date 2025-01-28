[Русский Язык](https://github.com/ma1de/rt-rce/blob/main/README_RU.md)

# RT RCE
Rostelecom Remote Code Execution bug found in the Web Panel

# Warning
This is just proof of concept and isn't meant for anything evil. Use at your own risk. <br>
By attempting to cause harm you might be subject to "УК РФ Статья 272. Неправомерный доступ к компьютерной информации" or any other applicable law in your juristiction <br>
You've been warned! <br>
P.S: the code itself might be incredibely jank cause I am not a python developer. If you'd like to change that, please consider submitting a pull request and I might merge it into this repository. <br>
P.S.S: if someone else have already found this bug, then please notify me with appropriate proof. I will take down this repository or I will give you credit for finding this bug.

# How this works
In the web panel you can find some diagnostic tools like ping and traceroute. <br>
In the Ping6 section the panel takes your input and executes this command with root permissions:
```
ip -6 <input>
```
Because of this major oversight we are able to pass in whatever we want and it will execute that command without hesitation.
For example:
```
ip -6 :: | echo "Hello, world!"
```
So much for [allocating 60 bilion rubles to block websites](https://www.svoboda.org/a/roskomnadzor-potratit-pochti-60-mlrd-rubley-na-sistemy-po-blokirovke/33114493.html), huh? <br>
Anyway, before that you should log into the web panel and grab the sessionid, otherwise this isn't going to work. <br>

# What do I do if I own a vulnerable RT router?
Use the command sample to stop some of the spyware they have. Or you can get another router and use the RT router as a bridge. The most ideal way to set this up is to buy a OpenWrt compatible router and connect it to the vulnerable router using an ethernet cable. In the vulnerable router change the protocol from PPPoE to Bridged (make sure you have the credentials for your internet connection, you can ask support for it and they will give it to you). In the OpenWrt compatible router install OpenWrt and set up a PPPoE connection. Make sure to switch DNS to something like Cloudflare and make sure to block their DNS servers in the firewall (preferably use iptables for this, but you can do it in the LuCI as well).<br>
I wanna clarify that I do not take any responsibility for you bricking your router or modifying it without permission (if you rented it).

# License
You can find a copy of the MIT license in this GitHub repository