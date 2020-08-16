#pragma once

#include "Kernel.h"
#include "KernelList.h"
#include "ModuleList.h"
#include "DeviceList.h"
#include "Job.h"
#include "JobResult.h"
#include "JobStatus.h"
#include <vector>
#include <string>
#include <memory>


namespace csyn {
	/**
	* CSynManager class execute Csyn service commands
	*/
	class CSynManager
	{
	public:
		/**
		* CSynManager destructor
		*/

		~CSynManager();

		/**
		* CSynManager constructor
		* @param ipAddress the Csyn service ip address 
        * @param port the Csyn service port 
		* @param userName the Csyn service admin user name
		* @param password the Csyn service admin password
		* @param isNetworkByteOrder the binary serialization byte order
		* @param timeout the Csyn service connection timeout
 		*/
		CSynManager(const std::string& ipAddress, int port, const std::string& userName = "", const std::string& password = "", int timeout = 1200, bool isNetworkByteOrder = false);

		/**
		* Get available GPU list from Csyn service
		* @return list of Device objects
		*/
		std::shared_ptr<DeviceList> getDeviceList();
		
		/**
		* Get list of Module objects from Csyn service
		* @return list of Module objects
		*/
		std::shared_ptr<ModuleList> getModuleList();

		/**
		* Get list of Kernel objects from Csyn service
		* @param module the name of kernels list module 
		* @param moduleVersion the version of module
		* @param moduleType the type of module
		* @return list of Kernel objects
		*/
		std::shared_ptr<KernelList> getKernelList(const std::string& module, const std::string& moduleVersion, int moduleType);

		/**
		* Get Kernel object from Csyn service
		* @param module the name of kernel module
		* @param moduleVersion the version of module
		* @param moduleType the type of module
		* @param name the kernel name
		* @return Kernel object
		*/
		std::shared_ptr<Kernel> getKernel(const std::string& module, const std::string& moduleVersion, int moduleType, const std::string& name);
		
		/**
		* Submit Csyn service request to execute Job 
		* @param job the Job object
		* @return JobResult object
		*/
		std::shared_ptr<JobResult> runJob(std::shared_ptr<Job>& job);

		/**
		* Submit Csyn service request to execute Job async
		* @param job the Job object
		* @return JobStatus object
		*/
		std::shared_ptr<JobStatus> runJobAsync(std::shared_ptr<Job>& job);

		/**
		* Submit Csyn service request to get Job result
		* @param uuid job UUID
		* @return JobResult object
		*/
		std::shared_ptr<JobResult> getJobResult(const std::string& uuid);

		/**
		* Submit Csyn service request to get Job status
		* @param uuid job UUID
		* @return JobStatus object
		*/
		std::shared_ptr<JobStatus> getJobStatus(const std::string& uuid);
		
		/**
		* Submit Csyn service request to remove Kernel objects
		* @param kernelList the list of Kernel objects
		*/
		void removeKernelList(const std::shared_ptr<KernelList>& kernelList);

		/**
		* Submit Csyn service request to remove Kernel object
		* @param kernel the Kernel object
		*/
		void removeKernel(const std::shared_ptr<Kernel>& kernel);

		/**
		* Submit Csyn service request to create/update Kernel objects
		* @param kernelList the list of Kernel objects
		*/
		void uploadKernelList(const std::shared_ptr<KernelList>& kernelList);
		
		/**
		* Submit Csyn service request to create/update Module object
		* @param module the module object
		* @param path the compiled fat cubin file path
		*/
		void uploadFatCubinModule(const std::shared_ptr<Module>& module, const std::string& path);
		
		/**
		*Submit Csyn service request to create/update Module object
		* @param module the module object
		* @param path the compiled fat cubin file path
		* @param major Device major revision number
		* @param minor Device minor revision number
		*/
		void uploadCubinModule(const std::shared_ptr<Module>& module, const std::string& path, int major, int minor);

		/**
		* Submit Csyn service request to remove Module object
		* @param module the name of module
		* @param moduleVersion the version of module
		* @param moduleType the type of module
		*/
		void removeModule(const std::string& module, const std::string& moduleVersion, int moduleType);

	private:
		std::string _ipAddress;
		int _port;
		int _timeout;
		bool _isNetworkByteOrder;
		std::string _userName;
		std::string _password;
	};

}
