# Docker Cheat Sheet: Build, Run, and Basic Commands

This `README.md` provides a simple overview of the essential Docker commands to build, run, and interact with your container, along with basic file navigation and Python commands.

remove "" when running the commands, the content is your preference

---

## **Docker Commands**

### **Building a Docker Image**

To build a Docker image from your `Dockerfile`:

`docker build -t "image_name":"tag" . `

### **Example building then running docker container:**
`docker build -t full-stack-env:latest . `

`docker run -it -v $(pwd):/workspace -p 3000:3000 -p 8000:8000 full-stack-env /bin/bash `

### **Listing files**
`ls`

### **Changing directories**

`cd`

### **running python files**

`python script.py`

### **exiting docker container**
`exit`