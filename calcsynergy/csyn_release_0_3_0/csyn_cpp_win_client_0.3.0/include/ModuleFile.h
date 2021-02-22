#pragma once
#include "Entity.h"
#include "Module.h"
#include <string>
#include <memory>
#include <vector>
#include <iostream>

namespace csyn {
	/**
	* ModuleFile class defines module file path and content
	*/

	class ModuleFile : public Entity
	{
	public:
		/**
		* ModuleFile constructor.
		* @param path file path
 		*/
		ModuleFile(const std::string& path);
		
		/**
		* ModuleFile constructor.
		* @param path file path
		* @param major Device major revision number
		* @param minor Device minor revision number
 		*/
		ModuleFile(const std::string& path, int major, int minor);
		
		/**
		* ModuleFile constructor.
		* @param path file path
		* @param major Device major revision number
		* @param minor Device minor revision number
		* @param data file data
 		*/
		ModuleFile(const std::string& path, int major, int minor, const std::vector<char>& data);
		
		/**
		* ModuleFile destructor.
		*/	
		~ModuleFile();
		
		/**
		* binary serialize ModuleFile object
		* @param stream used to serialize object data 
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize ModuleFile object
		* @param stream used to deserialize ModuleFile object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to ModuleFile object
		*/
		static std::shared_ptr<ModuleFile> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

		/**
		* get ModuleFile path
		* @return file path
		*/
		const std::string& getPath()
		{
			return _path;
		}

		/**
		* get ModuleFile major
		* @return Device major revision number
		*/
		int32_t getMajor()
		{
			return _major;
		}

		/**
		* get ModuleFile minor
		* @return Device minor revision number
		*/
		int32_t getMinor()
		{
			return _minor;
		}

		/**
		* get ModuleFile data
		* @return file data
		*/
		std::vector<char>& getContent()
		{
			return _content;
		}

		/**
		* load file data
		*/
		void loadData();

	private:
		std::string _path;
		int32_t _major;
		int32_t _minor;
		std::vector<char> _content;
	};
}

