# Controller Docker Build

To make it easier to deploy controllers in Docker, here is the dockerfile for the controllers, you need to make sure that docker is available in your environment.

The image of Ryu Controller is built as follows:
```
cd DiffController/build/RyuDocker
sudo docker build -t ryu:latest -f dockerfile .
```

Next, start the Ryu container using the Ryu image as follows:
```
docker run -it --name {CONTAINER NAMES} -privileged=true ryu /bin/bash
```

Other Controllers can be built using similar commands, but require corresponding images. 