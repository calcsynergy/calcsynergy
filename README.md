## CSyn Project Overview
  
### Introduction

	Calculation Synergy (CSyn) is a distributed general purpose computing system for Graphics Processing Units (GPU). CSyn is a highly scalable software solution that allows application services to operate in an unattached to specific GPUs. Multiple client applications can submit multiple requests in parallel and CSyn will handle these requests in parallel on different GPUs. A scalable architecture will provide linear gains in performance with the addition of more hardware resources. Current CSyn version supports CUDA as a parallel processing platform.

### CUDA kernels execution

	The ability to easy integrate a new technology into a variety of different environments is a core requirement of any new technology. CSyn offers support for multiple programming languages with the addition of a easy integration strategy. The client applications can execute any CUDA kernel hosted on the CSyn using different languages, including C++, Python, Java and C#. CSyn also provides a standards-based, flexible and intuitive programming model to simplify development process. It provides the ability to create instances of Kernel objects, provide Kernel parameters values, and submit job to CSyn runtime environments for execution. This job is virtualized and invoked on one of CSyn GPU and job results are returned to the client application. 
 
### Architecture

	CSyn uses Service-Oriented Architecture as an architectural approach. It includes three different components in its architecture:

		1 Clients - The components that create and submit service requests to the CSyn Director
		2 Engines - The services that host and run CUDA kernels on the CSyn GPUs
		3 Director - The service that assigns Clients job to Engines, load balance Engines and manages CSyn resources
		
## Getting Started

	These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See CSyn project [user guide](http://calcsynergy.com/html_user_guide/index.html) for more details.
	
#### Prerequisites

	To run Director and Engine services CSyn requires to install CUDA 10.2 or higher. See [CUDA installation instructions guide for Windows](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html) and [CUDA installation instructions guide for Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) for more details.
	
#### Installing

	To install CSyn system on your local machine follow the next steps:
	
		1 Downloads Director archive and extract it content to your destination. Update Director configuration file
		2 Start Director service. To start Director service on Windows use command: CSynService.exe
		3 Downloads Engine archive and extract it content to your destination. Update Engine configuration file
		4 Start one or more Engine services. To start Engine service on Windows use command: CSynEngine.exe  /gpuId=0 /port=8090
		
	See CSyn project [user guide](http://calcsynergy.com/html_user_guide/index.html) for more details.
	
#### Running the tests

	To run CSyn system tests on your local machine follow the next steps:
	
	1 Downloads Client SDK archive and extract it content to your destination. CSyn provides C++, C# and Python SDK
	2 Create test application using SCyn SDK and run it. See CSyn project [user guide](http://calcsynergy.com/html_user_guide/index.html) for C++, C# and Python code examples.
	
## Versioning
	1 Release 0.1.0 contains next archives:
		1 Director binary archives for Windows and Linux
		2 Engine binary archives for Windows and Linux
		3 C++ SDK binary archives for Windows and Linux
		4 Python SDK archive
	2 Release 0.2.0. C# SDK has been added. It contains next archives:
		1 Director binary archives for Windows and Linux
		2 Engine binary archives for Windows and Linux
		3 C++ SDK binary archives for Windows and Linux
		4 Python SDK archive
		5 C# SDK archive
	

## License
	
	CSyn system is distributed under terms that allow users to run the system for any purpose and distribute the program at no cost to the user.
	

	
