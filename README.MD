Welcome, my name is Hyun Woo!
This is a simple python script that allows anyone to change their MAC address to your desired new address! 
This only works on linux machine, however if you know how to play around with your windows or mac settings,
I am sure that you can modify them to your liking! Feel free to share, modify!

Libraries Used:
  subprocess # used to call cmd system call
  optparse   # used to parse the arguments into the program
  re         # used to grab the mac address using real expressions.

Description:
  python ./macChanger.py -i <INTERFACE> -m <NEW_MAC_ADDRESS>
  python ./macChanger.py -h # This will bring a helper menu!
