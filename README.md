pinyMessage
========

A Basic Python CLI Messenger
--------

This is meant to be as **basic** and **simple** of an example as possible to demonstrate Python's *socket*, *select*, and *threading*.

Dependencies

 - Python 3

Backstory

 - After searching, I could not find any simple [functional] projects that integrated the *socket*, *select*, and *threading* module.  Therefore this script was created using the trial and error method, without full understanding of all the elements.  I hope this helps my fellow Python and networking amateurs, and saves you from the frustration and hair-pulling I encountered.


How to Use

 - Open a Terminal window and run the script without any arguments ('python3 messenger.py')  This will initialize the server.
 - Open a second Terminal window and run the script adding any argument you'd like ('python3 messenger.py clientmode')  This will initialize the client.
 - You will be prompted to enter an IP or hostname.  If you are using a second computer, you must find this information and enter it.  Otherwise press ENTER to use localhost.
 - Now you will be able to send messages back and forth between Terminal windows until one user sends 'quit.' This will stop the loop on both ends.


I hope this was a helpful example for beginners.  If you'd like more practice projects, there are many ways this script could be expanded/improved (I plan on trying most of these myself).

 - Allow for multiple Clients
 - Create a GUI with tkinter (or module of choice)
 - Use server as a relay, so clients can come and go without forcing the server to close.
 - Usernames for Clients
