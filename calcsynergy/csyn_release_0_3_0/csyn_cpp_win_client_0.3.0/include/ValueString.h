#pragma once
#include "Value.h"
#include <string>
#include <vector>
#include <memory>
#include <iostream>

namespace csyn {
	/**
	* ValueString class defines parameter value type of string
	*/
	class ValueString : public Value
	{
	public:
		/**
		* ValueString constructor.
		* @param data
		* @param value name
 		*/
		ValueString(const char* data, const std::string& valueName = "");
		
		/**
		* ValueString constructor.
		* @param data
		* @param value name
 		*/
		ValueString(const std::string& data, const std::string& valueName = "");
		
		/**
		* ValueString destructor.
		*/
		~ValueString();
		
		/**
		* get copy of value object
		* @return copy of value object
 		*/
		std::shared_ptr<Value> getCopy();

		/**
		* binary serialize value object
		* @param stream used to serialize object data 
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize value object
		* @param stream used to deserialize value object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to value object
		*/
		static std::shared_ptr<Value> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

		/**
		* get value length
		* @return value length
 		*/
		int32_t getLength()
		{
			return _length;
		}
		
		/**
		* get value data size
		* @return value data size
 		*/
		uint32_t getSize();

	private:
		int32_t _length;

	};
}


