#pragma once
#include "Entity.h"
#include "Module.h"
#include <string>
#include <memory>
#include <vector>
#include <iostream>

namespace csyn {
	class ModuleFilePath : public Entity
	{
	public:
		/**
		* ModuleFilePath constructor.
		* @param path file path
 		*/
		ModuleFilePath(const std::string& path);
		
		/**
		* ModuleFilePath constructor.
		* @param path file path
		* @param major Device major revision number
		* @param minor Device minor revision number
 		*/
		ModuleFilePath(const std::string& path, int major, int minor);
		
		/**
		* ModuleFilePath constructor.
		* @param path file path
		* @param major Device major revision number
		* @param minor Device minor revision number
		* @param data file data
 		*/
		ModuleFilePath(const std::string& path, int major, int minor, const std::vector<char>& data);
		
		/**
		* ModuleFilePath destructor.
		*/	
		~ModuleFilePath();
		
		/**
		* binary serialize ModuleFilePath object
		* @param stream used to serialize object data 
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize ModuleFilePath object
		* @param stream used to deserialize ModuleFilePath object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to ModuleFilePath object
		*/
		static std::shared_ptr<ModuleFilePath> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

		/**
		* get ModuleFilePath path
		* @return file path
		*/
		const std::string& getPath()
		{
			return _path;
		}

		/**
		* get ModuleFilePath major
		* @return Device major revision number
		*/
		int32_t getMajor()
		{
			return _major;
		}

		/**
		* get ModuleFilePath minor
		* @return Device minor revision number
		*/
		int32_t getMinor()
		{
			return _minor;
		}

		/**
		* get ModuleFilePath data
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

