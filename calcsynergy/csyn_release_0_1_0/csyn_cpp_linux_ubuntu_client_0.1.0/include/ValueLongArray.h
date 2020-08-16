#pragma once
#include "Value.h"
#include <string>
#include <vector>
#include <memory>
#include <iostream>

namespace csyn {
	/**
	* ValueLongArray class defines parameter value type of long array
	*/
	class ValueLongArray : public Value
	{
	public:
		/**
		* ValueLongArray constructor.
		* @param data array data
		* @param length array length
		* @param value name
 		*/
		ValueLongArray(const int64_t* data, int32_t length, const std::string& valueName = "");
		
		/**
		* ValueLongArray constructor.
		* @param length array length
		* @param value name
 		*/
		ValueLongArray(int32_t length, const std::string& valueName = "");
		
		/**
		* ValueLongArray destructor.
		*/
		~ValueLongArray();
		
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
		* get array length
		* @return array length
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


