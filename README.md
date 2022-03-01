# Lixur

![Screenshot 2021-11-18 192213ccc](https://user-images.githubusercontent.com/87288707/155904619-8dca0af8-4e9f-433f-8c2e-60e7b0e97a64.jpg)

![image](https://user-images.githubusercontent.com/87288707/155904797-03df3651-ea9d-40e9-9998-14726876519b.png) ![image](https://img.shields.io/badge/State-Testnet%20Beta%20Under%20Construction-informational) ![image](https://img.shields.io/badge/Python-3.7.0-blueviolet)

### What is Lixur ?
Welcome, we're glad to have you! Lixur is an open-sourced project building a distributed ledger platform. Lixur plans on implementing things such as DAGs and A.I smart contracts which enables fast, privacy-preserving, feeless, infinitely scalable, quantum resistant and an interconnected ecosystem, which users can make use of for any application requiring decentralized, automated intelligence and more. To learn more, please read the whitepaper [ 📖 Here 📖](https://drive.google.com/file/d/1mfqufIxTuvegdc8VjfgJahROHA6CBJHM/view?usp=sharing) 

This project is by no means complete and may feature plenty of bugs, security holes, etc. Please be aware of this. We haven't even launched the Testnet Beta yet so this is a work-in-progress.

You may have struggles to install the required module PQCrypto, it's likely you'll need to downgrade or upgrade your Python interpreter to 3.7.0 and manually install the package. 

Installation Instructions for PQCrypto: 

If you have previously installed the PQCrypto: Delete it completely off of your hard drive completely, restart your laptop and continue with the instructions
1. Make sure you have Python 3.7.0 and uninstall all other versions of Python! Link: https://www.python.org/downloads/release/python-370/
2. Grab the two folders, and move them to the following directory for Windows (or Mac/Linux Equivalent): 
C:\Users\(Your Windows Name)\AppData\Local\Programs\Python\Python37\Lib\site-packages
3. Once copied and pasted there, restart your laptop and head to your text editor and it should hopefully work.
Any questions, email me at naisukhy@gmail.com or submit the issue on the GitHub Repository

### How to Contribute

Lixur is open-sourced and powered by the community, so feel free to contribute in any way you can to help us!

### How you can help

So you want to contribute? Please, please join our Discord Server and our JetBrains Space Collaboration Platform if you want to contribute to this project. It's a must. Our project management and our project checklist is avaiable on JetBrains and our primary source of communication is Discord, it only takes a minute at most to signup! Open issues or contact us on Discord/JetBrains for things you want to see added, modified, discuss ideas or help out with existing issues. If you have any questions, please contact me on Jetbrains, Discord or if those aren't possible, my email which is `naisukhy@gmail.com`
    
<br> [Click here to join our Official Discord Server Link](https://discord.gg/HCRAQHKGeG)
<br> [Click here to join our Official Jetbrains Space Group Link](https://lixur.jetbrains.space/oauth/auth/invite/4bf814e7091de971b3c9fde59b99eb63)

### How to Run
* To run a node, install the required packages ***(download requirements.txt)***, and run Flask ***(not in terminal!)***, and it should pop up with three genesis trasactions.
* To add new transactions, head to: `127.0.0.1:5000/transactions/new`
* To access wallet or make a new wallet, head to: `127.0.0.1:5000/wallet`
* To check network stats, head to: `127.0.0.1:5000/stats`
* To check node status, head to: `127.0.0.1:5000/node`

You can replace `127.0.0.1:5000` with a new IP:Port pair

***If you find any bugs, or anything that should be added, initiate a pull request, add the issue to the repository page or email me personally at:*** `naisukhy@gmail.com`

---

``Addressing a potential concern: For those examining the code and are concerned with the speed of Python, This code will soon feature a JIT Complier that will accelerate the code either with Numba, accelerating execution speed on par or even better than Go, C++ or Julia. Solving the speed dilemma. Here are some examples to illustrate this...``

<br> ![image](https://user-images.githubusercontent.com/87288707/155394541-28719860-ac4e-4db8-97d4-c7c2980cb273.png)
<br> ![image](https://user-images.githubusercontent.com/87288707/155394794-6cd735c6-93ea-41fc-abb3-844f90c60162.png)
<br> ![image](https://user-images.githubusercontent.com/87288707/155395059-717c2782-cd2c-4974-bcc5-7c718c9a4561.png)
<br> ![image](https://user-images.githubusercontent.com/87288707/155395258-632c6132-cb67-43b9-9d6c-c7021bdd2b17.png)

#### Other Links
* https://users.rust-lang.org/t/why-my-rust-code-is-10-times-slower-than-python-with-numba/57738
