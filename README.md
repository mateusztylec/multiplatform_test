# System-info
This project is a container that checks and prints information about the currently running system. The project is implemented using Python and the FastAPI framework.

## Use Case
For example, to run a one-off container in Kubernetes:
``` 
kubectl run --rm system-info -it --image mateusztylec/system-info bash
```
## General Usage
```
docker run -d -p 8000:8000 mateusztylec/system-info
```
And then open a web browser and navigate to http://127.0.0.1:8000/ to view the system information.

## System Information
The following system information is displayed:
```
System name (os.name)  
Platform name (sys.platform)  
System/OS name (platform.system())  
Platform (sysconfig.get_platform())  
Machine type (platform.machine())  
Machine architecture (platform.architecture())
```

## Contributing
Create a pull request