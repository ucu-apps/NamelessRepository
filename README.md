# Robert

Robert mobile robot 

[![License](https://img.shields.io/github/license/ucuapps/robert.svg)](https://github.com/ucuapps/robert/blob/kinetic-devel/LICENSE)


## Docker
For convenience it is recommended to use Docker containers.
Please follow these steps to run Docker container on your machine.

 1. Install Desktop OS Ubuntu Trusty or Xenial on your machine or in virtual machine
 2. Install Docker-CE using these [instructions](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/)
 3. In order to executed Docker without sudo please execute
```bash
sudo usermod -aG docker $USER
```
 4. Logout and login to your machine again :)
 5. For development [the following](http://hub.docker.com/r/ucuapps/robert/) docker container was used.
 6. To pull it please run
```bash
docker pull ucuapps/robert:latest
```
 7. Use the following command to start Docker container
```bash
docker run -it --name robert_dev -e DISPLAY -e LOCAL_USER_ID=$(id -u) -v /tmp/.X11-unix:/tmp/.X11-unix:rw ucuapps/robert:latest
```
 8. Black window of [Terminator](https://gnometerminator.blogspot.com/p/introduction.html) UI console will appear after some time.
 9. You can use it's features to [split terminal window](https://linux.die.net/man/1/terminator) into smaller terminals and run few commands in parallel (Ctrl+Shift+E).
 10. If you want to run real robot add user to dialout group and restart Docker container
```bash
sudo usermod -a -G dialout user
```

In order to relaunch docker container after you closed Terminator window or rebooted machine please run
```bash
docker start robert_dev
```
After some time Terminator window will reappear.

## IDEs

In case if you want to run PyCharm in Docker container please run

```bash
pycharm
```

To launch QtCreator please run

```bash
qtcreator
```

For VSCode type
```bash
vscode
```

# URDF and RViz

In order to debug URDF please launch

```bash
roslaunch robert_launch view_urdf.launch
```

To have a look on the state of the robot in RViz run

```bash
roslaunch robert_launch rviz.launch
```

## Navigating on known map

Start office simulation

```bash
roslaunch robert_launch simulation.launch
```

Start UCU simulation
```bash
roslaunch robert_launch simulation.launch world_file:=ucu
```

Launch navigation stack (in order to launch second command split Terminator window by two using Ctrl-Shift-E. More information on Terminator shortcuts can be found [here](https://dmaricic.wordpress.com/2011/01/28/terminator-keyboard-shortcuts/))
```bash
roslaunch robert_launch navigation.launch
```

In RViz which appear after some time select "2D Nav Goal" and robot will travel to it.
Like it is shown in [this video](https://www.youtube.com/watch?v=xSdHlC2ISq8).

## Building the map

Start simulation

```bash
roslaunch robert_launch simulation.launch
```

Launch gmapping node

```bash
roslaunch robert_launch gmapping.launch
```

Drive arround environment to build map using [the following keys](http://wiki.ros.org/stdr_simulator/Tutorials/Teleop%20with%20teleop_twist_keyboard#Teleoperate_your_robot.21).
*Please note that console window with gmapping launch file should be active in order to teleoperate robot using keys*

Save map to file
```bash
rosrun map_server map_saver -f <map_file_name>
```
