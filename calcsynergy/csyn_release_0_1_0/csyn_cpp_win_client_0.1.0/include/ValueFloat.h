#pragma once
#include "Value.h"
#include <string>
#include <memory>
#include <iostream>

namespace csyn {
	/**
	* ValueFloat class defines parameter value type of float
	*/
	class ValueFloat : public Value
	{
	public:
		/**
		* ValueFloat constructor.
		* @param value
		* @param value name
 		*/
		ValueFloat(float value, const std::string& valueName = "");
		
		/**
		* ValueFloat destructor.
		*/
		~ValueFloat();
		
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
		* get value data size
		* @return value data size
 		*/
		uint32_t getSize();
		
		/**
		* get value data
		* @return value data
 		*/
		void* getData();

	private:
		float _value;
	};
}

