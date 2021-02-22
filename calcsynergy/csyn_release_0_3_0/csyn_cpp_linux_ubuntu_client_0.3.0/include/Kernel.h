#pragma once

#include "Entity.h"
#include "Module.h"
#include "Parameter.h"
#include <string>
#include <vector>
#include <memory>
#include <iostream>

namespace csyn {
	/**
	* Kernel class defines kernel parameters and properties
	*/
	class Kernel : public Entity
	{
	public:
		/**
		* Kernel constructor
		* @param kernelName Kernel name
		* @param moduleName Kernel module name
		* @param moduleVersion Kernel module version
		* @param moduleType Kernel module type
		* @param kernelDescription Kernel description
 		*/
		Kernel(const std::string& kernelName, const std::string& moduleName, const std::string& moduleVersion, int moduleType,  const std::string& kernelDescription = "");
		
		/**
		* Kernel destructor
		*/	
		~Kernel();

		/**
		* get Kernel name
		* @return Kernel name
		*/
		const std::string& getKernelName()
		{
			return _kernelName;
		}

		/**
		* get Kernel description
		* @return Kernel description
		*/
		const std::string& getKernelDescription()
		{
			return _kernelDescription;
		}

		/**
		* get Module name
		* @return Module name
		*/
		const std::string& getModuleName()
		{
			return _moduleName;
		}

		/**
		* set Module version
		* @param moduleVersion
		*/
		void setModuleVersion(const std::string& moduleVersion)
		{
			_moduleVersion = moduleVersion;
		}

		/**
		* get Module version
		* @return Module version
		*/
		const std::string& getModuleVersion()
		{
			return _moduleVersion;
		}

		/**
		* set Module type
		* @param moduleType
		*/
		void setModuleType(int32_t moduleType)
		{
			_moduleType = moduleType;
		}
		
		/**
		* get Module type
		* @return Module type
		*/
		int32_t getModuleType()
		{
			return _moduleType;
		}
		
		/**
		* get Kernel parameter list
		* @return Kernel parameter list
		*/
		std::vector<std::shared_ptr<Parameter>>& getParameterList()
		{
			return _parameterList;
		}

		/**
		* copy Kernel object
		* @return copy of Kernel object 
		*/
		std::shared_ptr<Kernel> getCopy();

		/**
		* validate Kernel object
		* @param isRuntime is run time validation
		* @return true if Kernel object is valid
		*/
		bool validate(bool isRuntime = false);

		/**
		* get Kernel parameter by parameter name
		* @param name Kernel parameter name
		* @return Kernel parameter
		*/
		std::shared_ptr<Parameter> getParameterByName(const std::string& name);

		/**
		* get Kernel parameter by parameter order
		* @param order Kernel parameter order
		* @return Kernel parameter
		*/
		std::shared_ptr<Parameter> getParameterByOrder(int order);

		/**
		* set Kernel parameter value by parameter name
		* @param name Kernel parameter name
		* @param value Kernel parameter value
		*/
		void setParameterValueByName(const std::string& name, std::shared_ptr<Value>& value);

		/**
		* set Kernel parameter value by parameter order
		* @param order Kernel parameter order
		* @param value Kernel parameter value
		*/
		void setParameterValueByOrder(int order, std::shared_ptr<Value>& value);

		/**
		* set Kernel parameter value as global value by parameter name
		* @param name Kernel parameter name
		* @param globalValueName global value name
		*/
		void setParameterGlobalValueByName(const std::string& name, const std::string& globalValueName);

		/**
		* set Kernel parameter value as global value by parameter order
		* @param order Kernel parameter order
		* @param globalValueName global value name
		*/
		void setParameterGlobalValueByOrder(int order, const std::string& globalValueName);

		/**
		* add Kernel parameter
		* @param Kernel parameter
		*/
		void addParameter(const std::shared_ptr<Parameter>& parameter);

		/**
		* binary serialize Kernel object
		* @param stream used to serialize object data 
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize Kernel object
		* @param stream used to deserialize Kernel object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to Kernel object
		*/
		static std::shared_ptr<Kernel> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

	private:
		std::string _kernelName;
		std::string _kernelDescription;
		std::string _moduleName;
		std::string _moduleVersion;
		int32_t _moduleType;
		std::vector<std::shared_ptr<Parameter>> _parameterList;
	};
}
