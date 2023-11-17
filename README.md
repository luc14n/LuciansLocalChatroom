# Lucians Local Chatroom
This is a project made for a computer networking class. The goal is to have a UTP client/server connection and allow coninuous chat over a local network.

# Version 1.0
Allows for multiple clients to connect to the running app, however the 'Sever' side chat window will only respond to the last client connected.

# Future Plans
  - One file start that allows the user to choose to either start a server or start a client
  - Server can connect multiple clients and brodcast one clients message to all other connected clients
  - Clients will be prompted for a username for the server to hold temporarily so clients are identifyable other than IP adress
  - Server has option to brodcast to all clients or whisper to an individual
  - Adding Security

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

Ensure 'PyQt5' is installed and is usable by Python.

Ensure 'Requests' is installed and is usable by Python.

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
