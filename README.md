# Daily-Desktop-Background
Refreshes Windows 10 background image with a new color quantized wallpaper at the start of every day

## Requirements
In order for this project to work, you need to have Python3 installed along with the Pillow and requests modules. You can install Python3 [here](https://www.python.org/downloads/) and install the modules by going to this project's directory and with command line run
```
python -m pip install -r requirements.txt
```

## Getting Started
One way to do a periodic action in Windows 10 is to create a daily task using the Task Scheduler. To create this task just run Create-Scheduled-Task.bat by either double-clicking the file or with the command line run
```
Create-Scheduled-Task.bat
```
Now, if you open Task Scheduler and view the MyTasks folder under Task Scheduler Library, you should see a task called Daily-Desktop-Background.

If you want to get rid of the task or you moved this project's directory to another directory (the project won't work if that happens), just run Delete-Scheduled-Task.bat.

In order for this project to get a new desktop background everyday, it uses the Unplash API. The Unsplash API requires a confidential access key to gain access to its services. To get your own access key, you can create an account [here](https://unsplash.com/developers) and than create a new application. Then create a keys.py file in the project's directory which should contain the following
```
UNSPLASH_ACCESS_KEY = '<your key here>'
```
If a good number of people find this project useful, I can add a bit more to the project so that you can use my secret key while still keeping it confidential. Though, I don't know how to do this yet.

That's it! You now have a daily refresing Windows 10 color quantized background.

## Customization
You can change this project to meet your needs by editing config.py. It allows changes for your desktop dimentions, what kind of backgrounds you want, and more.
