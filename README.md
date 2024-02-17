# VidScript - MVP

To provide a user-friendly, efficient and accurate video to mp3 conversion platform for content creators, educators, and professionals seeking to convert their video content easily into accessible mp3 format. 

## Table of Contents
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [Contributions](#contributions)
- [Disclaimer](#disclaimer)

## Features
1) Video upload: Upload a video in any common format (e.g MP4, AVI, MOV) through the terminal stream.
2) MP3 availability: Convertion happens from the conversion API. 
3) Notifications: Receive email notifications of the availability of the mp3.
4) Secure storage: Uploaded videos are stored in the secure storage of MongoDB.

## Technology Stack
1) Container Technology: Kubernetes and Docker
2) Backend: Flask, MongoDB, MySQL, RabbitMQ
 
## Installation instructions

### Prerequisites
1) [Docker](https://youtu.be/AAWNQ2wDVAg?si=E9PjHBNwlaktNv0M)
2) [Kubernetes](https://youtu.be/G9MmLUsBd3g?si=4g2fIOjO3Cbg3dd5)
3) [Minikube](https://youtu.be/xNefZ51jHKg?si=4bl-vgTn0jRM0vxf)
4) [k9s](https://youtu.be/pUwlZ0bxkjA?si=loIwEXs-qFIbIOot)
5) [Python](https://youtu.be/H10nfeakm2s?si=4OCEIx-fT61YnuOu)
6) [RabbitMQ](https://youtu.be/TYgrkA5CxdE?si=3IxVstfgukvKJulx)
7) [Mongodb](https://youtu.be/1LiZRYzgM2o?si=RU3ebnt3r1oHultH)
8) [MySQL](https://youtu.be/9cI9UgK3qZA?si=cl3bm6G71cYlhlai)

### Getting Started
1) First you need to clone the directory. You can use the following command

```
git clone --branch video_mp3_converter https://github.com/GArdennes/VidScript.git
```

2) Configure the prerequisite applications on system environment path variables and confirm a successful configuration.

```
<application name> --version

#Docker
docker --version

#Minikube
minikube --version

#Python
python --version
```

3) Install required packages from the requirements file in the subdirectories.

```
pip install -r requirements.txt
```

## Usage instructions
1) Accesss the application in docker container configured with minikube. Ensure docker is installed and running.

2) Run minikube:

```
docker context use default
minikube start --no-vtx-check
```

3) In the subrepository manifests, run the following command:

```
kubectl apply -f ./
```

4) Enable the minikube tunneling feature:

```
minikube tunnel
```

5) Open your terminal and type:

```
#step 1
curl -X POST http://mp3converter.com/login -u {username e.g. thekevin.afachao@gmail.com}:{password e.g. admin}

#step 2
curl -X POST -F 'file=@{path of video file e.g. './test.mp4'}' -H 'Authorization: Bearer {token}' http://mp3converter.com/upload
```

6) An email notification is sent once the mp3 is ready

***
***
NOTE: This is an MVP, and further development is planned to include a frontend feature and other functionality like video to text conversion.
***
***

## Contributions
Contributions and suggestions to this project are welcome. The project was based on this [tutorial](https://youtu.be/hmkF77F9TLw?si=cH6il2gB01gcuXVf)

## Disclaimer
This project is for educational purposes only, to meet the requirements of the ALx Software Engineering certification program. 