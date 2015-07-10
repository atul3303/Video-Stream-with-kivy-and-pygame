# Video-Stream-with-kivy-and-pygame

The Video Frames is streamed though sockets, and is updated in the kivy(main.py) window in real time.

The Server sets up a TCP server and waits for connection.If connects it captures a image coverts it to a RGB color scheme string and sends to the receiver.

The receiver(main.py) updates the Image "1.jpg" with Image.Reload()


NOTE
  Please keep a image file in the same directory with name '1.jpg'
  
  

