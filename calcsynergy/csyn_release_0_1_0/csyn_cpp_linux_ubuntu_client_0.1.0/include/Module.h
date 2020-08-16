#pragma once
#include "Entity.h"
#include <string>
#include <memory>

namespace csyn {
	/**
	* Module class defines module properties
	*/

	class Module : public Entity
	{
	public:
		/**
		* Module constructor
		* @param moduleName Module name
		* @param version Module version
		* @param moduleDescription Module description
		* @param moduleType Module type
 		*/
		Module(const std::string& moduleName, const std::string& moduleVersion, int moduleType, const std::string& moduleDescription="");
		
		/**
		* Module destructor
		*/	
		~Module();

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
		const std::string& getModuleVersion()
		{
			return _moduleVersion;
		}

		/**
		* get Module description
		* @return Module description
		*/
		const std::string& getModuleDescription()
		{
			return _moduleDescription;
		}

		/**
		* get Module type
		* @return Module type
		*/
		const int32_t getModuleType()
		{
			return _moduleType;
		}

		/**
		* binary serialize Module object
		* @param stream used to serialize object data 
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize Module object
		* @param stream used to deserialize Module object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to Module object
		*/
		static std::shared_ptr<Module> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

	private:
		std::string _moduleName;
		std::string _moduleDescription;
		int32_t _moduleType;
		std::string _moduleVersion;
	};
}
