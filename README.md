## CSyn Project Overview
#### Introduction
Calculation Synergy (CSyn) is a distributed general purpose computing system for Graphics Processing Units (GPU).
CSyn is a highly scalable software solution that allows application services to operate in an unattached to specific GPUs.
Multiple client applications can submit multiple requests in parallel and CSyn will handle these requests in parallel on different GPUs.
A scalable architecture will provide linear gains in performance with the addition of more hardware resources.
Current CSyn version supports CUDA as a parallel processing platform.
#### CUDA kernels execution
The ability to easy integrate a new technology into a variety of different environments is a core requirement of any new technology.
CSyn offers support for multiple programming languages with the addition of a easy integration strategy.
The client applications can execute any CUDA kernel hosted on the CSyn using different languages, including C++, Python, Java and CSharp.
CSyn also provides a standards-based, flexible and intuitive programming model to simplify development process.
It provides the ability to create instances of Kernel objects, provide Kernel parameters values, and submit job to CSyn runtime environments
for execution. This job is virtualized and invoked on one of CSyn GPU and job results are returned to the client application.
#### Architecture
CSyn uses Service-Oriented Architecture as an architectural approach.
It includes three different components in its architecture:
- Clients components that create and submit service requests to the CSyn Director
- Director service that manages CSyn resources (modules, executors, engines), execute different client requests, load balance client jobs 
- Executors services that execute client jobs, load balance job tasks to different engines
- Engines services that run job tasks on the CSyn GPUs
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
See CSyn project user [guide](http://www.calcsynergy.com/html_user_guide/index.html) for more details.
#### Prerequisites
To run Engine services CSyn requires to install CUDA 10.2 or higher.
See CUDA installation instructions [guide](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html) for Windows and CUDA installation instructions [guide](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) for Linux for more details.
#### Installing
To install CSyn system on your local machine follow the next steps:
- Downloads Director archive and extract it content to your destination. Update Director configuration file
- Start Director service. To start Director service on Windows use command: CSynService.exe
- Downloads Executor archive and extract it content to your destination. Update Executor configuration file
- Start one or more Executor services. To start Executor service on Windows use command: CSynEngine.exe  /port=8100
- Downloads Engine archive and extract it content to your destination. Update Engine configuration file
- Start one or more Engine services. To start Engine service on Windows use command: CSynEngine.exe  /gpuId=0 /port=8090
See CSyn project user [guide](http://www.calcsynergy.com/html_user_guide/index.html) for more details.
#### Running the tests
To run CSyn system tests on your local machine follow the next steps:
- Downloads Client SDK archive and extract it content to your destination. CSyn provides C++, CShart and Python SDK
- Create test application using SCyn SDK and run it. See CSyn project user [guide](http://www.calcsynergy.com/html_user_guide/index.html) for C++, CSharp and Python code examples
## Versioning
Release 0.1.0 contains next archives:
- Director binary archives for Windows and Linux
- Engine binary archives for Windows and Linux
- C++ SDK binary archives for Windows and Linux
- Python SDK archive

Release 0.2.0. C# SDK has been added. It contains next archives:
- Director binary archives for Windows and Linux
- Engine binary archives for Windows and Linux
- C++ SDK binary archives for Windows and Linux
- Python SDK archive
- CSharp SDK archive

Release 0.3.0. Sort system library has been added. It contains next archives:
- Director binary archives for Windows and Linux
- Engine binary archives for Windows and Linux
- C++ SDK binary archives for Windows and Linux
- Python SDK archive
- CSharp SDK archive

Release 0.3.1. C++ SDK, Director and Engine for linux CentOS has been added. It contains next archives:
- Director binary archives for Windows, Linux Ubuntu and Linux CentOS
- Engine binary archives for Windows, Linux Ubuntu and Linux CentOS
- C++ SDK binary archives for Windows, Linux Ubuntu and Linux CentOS
- Python SDK archive
- CSharp SDK archive

Release 0.3.2. updates list:
- Add CSynEngineLibrary for engine service
- Add CSynServerLibrary for directory service 
- Added engine service get system info json request handler
- Removed cuda stream from cublas context
- Modified job result class and c++/c#/python clients

Release 0.3.3. updates list:
- Added engine service task group result manager pool
- Added director service task group manager pool

Release 0.4.0. updates list:
- Added cusolver system library

Release 0.5.0. updates list:
- Update CSyn architecture. Add Executor service


## License
CSyn system is distributed under terms that allow users to run the system for any purpose and distribute the program at no cost to the user.