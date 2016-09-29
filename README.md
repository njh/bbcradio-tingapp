BBC Radio Tingbot App
=====================

This Tingbot App allows you to listen to BBC Radio on your [TingBot].

* To change station press the left and right buttons.
* To change the volume, press the middle two buttons.



Installing mpg123
-----------------

The BBC radio streams are played back using [mpg123]. To install it on your [Tingbot] / Raspberry Pi, use the following command: 

    sudo apt-get install mpg123

Or if you want to run the app in the Tingbot Simulator on a Mac, you can install it using:

    brew install mpg123 


Making USB audio default
------------------------

Because the [Tingbot] does not have a built-in speaker, and the 3.5mm audio jack is not easily accessible, I have been using a USB speaker to playback the audio.

To make the USB speaker the default audio output device, I had add some configuration. I created the file `/etc/modprobe.d/alsa.conf`:

```
blacklist snd-bcm2835
alias snd-card-0 snd-usb-audio
options snd-usb-audio index=0
```

This tells the Linux kernel to load the USB audio first and disables the built-in audio.

Finally, `reboot` your Tingbot.


[mpg123]:     http://www.mpg123.org/
[TingBot]:    http://www.tingbot.com/
[Tide]:       http://docs.tingbot.com/tide/
