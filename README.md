# Lucians Local Chatroom
This is a project made for a computer networking class. The goal is to have a TCP client/server connection and allow coninuous chat over a local network.

# Version 1.3
Added peer-server encryption using an asymmetric key system then transferring to a symmetric key system.

# Version 1.2
Changed messages over to JSON packages. Allowed for each client to have an identifiable username set by the user. Allows for more functionality to be explored with being able to send more complex messages.
Messages may still be seen by scraping network traffic and will most likely be the goal for v1.3

# Version 1.1
Changed how the 'server' functioned so that it was a distribution node to all connected clients. Fixed a bug with multiple clients not having continuous chat functionality. Set up start to allow for messages to be changed to json packages.

# Version 1.0
Allows for multiple clients to connect to the running app, however the 'Sever' side chat window will only respond to the last client connected.

# Future Plans
- [ ] One file start that allows the user to choose to either start a server or start a client
- [x] Server can connect multiple clients and brodcast one clients message to all other connected clients
- [x] Clients will be prompted for a username for the server to hold temporarily so clients are identifyable other than IP adress
- [ ] Server has option to brodcast to all clients or whisper to an individual
- [x] Adding Security (Peer to server encryption)

# Install Instructions

This app uses Python 3.11. Other versions have not been tested for compatibility.

### Operating System
On Windows
- Install Python 3.11 through the windows appstore.
    
On MacOs
- Install Python 3.11 through the official Python site.
    
This Application has not been tested on any version of Linux

### Install Files

Install files from Git Repository

Make sure these Python libraries are installed

pyqt5, requests, rsa, cryptography

> The easiest way to esure these are installed is to run the program through an IDE.
> 
> In the IDE console enter the command: pip install PACKAGE_NAME
> 
> Where PACKAGE_NAME is put 'PyQt5' or 'Requests'

# Run Instructions

In order to run the app/server, run 'app.py'
> app.py, server.py, port_window.py, and window.py are all neccessary to run the app/server

In order to run a client, run 'client.py'
> client.py, and client_window.py are all neccessary to run the client (They can run independantly and with no dependancy from the app/server files)
