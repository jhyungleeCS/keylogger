## About
##### [Read Full Report Here (My Blog)](https://www.mangoxsecurity.com)

### What is a keylogger?

Picture this scenario. You are at your desk at work. While you are productively working away, you get a thought about the product you saw on the Internet last night. You spontaneously decide to purchase the product on Amazon during your lunch break. You look around and see no one near you as you whip out your credit card to type away the numbers and pin. However, even with no one around you, you feel like someone is still watching you. Do you feel safe? 

Well those erie feelings might be right. You may not be as safe as you think, your device may be susceptible to eavesdropping. 

Keyloggers are a type of technology, hardware or software, that is designed to record user input that is typed by a user on the computer keyboard. User input can include letters, numbers, symbols, and even mouse clicks. The keylogger’s general purpose is to gather as much information as possible from what the user is typing into their keyboard. 

### Is a keylogger dangerous? How can you protect against one?

Keylogging can be used for both malicious and legitimate purposes. A company may use it as part of their policy to monitor user activtity on their network. However, an attacker might use a keylogger maliciously for data exfiltration on a network or simply collect sensitive information about a target including  their SSN, credit card numbers, and other PII information. 

There are a variety of methods and steps that you or an organization can take to prevent keyloggers (both software and hardware). A company can have multiple DLP (data loss prevention) methods set in play to prevent user’s workstations from having any unauthorized hardware devices accessing company owned equipment. Some examples include, 

- USB data blocker
- Hardening default installations
- Signature-based/Heuristic-based IPS
- Whitelisting/Backlisting Applications

### Creating the Project

To understand attacks on users vulnerable to these eavesdropping/sniffing attacks, I wanted to create my own version of a hardware keylogger that can be transmitted through a USB port. 

To start, I worked on the scripts that will be responsible for logging the keystrokes and saving these inputs into your local machine. I first created a keylogger function. Using the pynput  ibrary, I pulled two different functions from it “Key” and “Listener”. These classes helped me with creating functions and variables that would listen for and handle these events. The script will stop executing if the user had pressed the escape key. 

Next, I created a script that would be responsible for the user’s workstation to save the keylog file into a text file that is legible for the user. Using the os library, I was able to interact with my operating system’s in a platform-independent way. With the module os.path.join and os.path.expanduser, I was able to create a file called keylog.txt and save the file underneath the ~/Desktop path. This module was helpful in making sure that the path is resolved to the correct home directory on the user’s local machine. 

Lastly, I imported both these scripts into my [main.py](http://main.py) file which ran both functions keylogger() and savefile().

### Takeaways and future ideas

Throughout this project, my main focus was to understand the different modules and libraries that python has to offer. As an avid programmer, I wanted to expand my understandings of scripting in a language like python to help broaden my capabilities of having it in my arsenal. 

Additionally, I wanted to showcase my understandings of how sniffing tools leave users vulnerable to attacks and how a malcious actor may create one to do such that. Attackers are often looking to steal personal information. Recording key strokes can expose a lot about a user including websites they visit, accounts they access, and personal information. 

Some next steps I want to take in order to expand upon my project and work on improving the capabilities of the keylogger include: 

- Stealh Feature: With operating systems having strong antivirus software, such as Microsoft’s Defender, they can easily detect files that are suspicious. I believe this is done through machine learning and signature-based IPS that vendors create in order to block certain files if they fall under a particular category. I wonder if I some how obfuscate my code and rename my python file to a system file that is used by the operating system, this can bypass some security walls.
- Hardware Access Feature: Currently, with Raspberry Pi’s that are out of stock, I didn’t have the opportunity to deploy my script into a hardware component. With more research on Raspberry Pi’s firmware and once they come out (Q3 of 2023), I want to be able to implement my current files and store them to execute once the Raspberry Pi is plugged into the machine.

### Disclaimer

The purpose of this project is to conduct ethical hacking to identify vulnerabilities in my local system and to help understand security.

 The project will be conducted under my own home lab that I have setup under my network, on my local machine. All information obtained during the project will be kept confidential and will only be shared with authorized parties.



