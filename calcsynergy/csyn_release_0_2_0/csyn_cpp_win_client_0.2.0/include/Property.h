#pragma once

#include "Entity.h"
#include <string>
#include <vector>
#include <memory>
#include <iostream>

namespace csyn {
	/**
	* Property class defines job property
	*/
	class Property : public Entity
	{
	public:
		/**
		* Property constructor
		* @param key Property key
		* @param value Property value
 		*/
		Property(const std::string& key, const std::string& value);
		
		/**
		* Property destructor
		*/	
		~Property();

		/**
		* Static Property key defines run job tasks sequentially
		*/
		static const std::string KeySequential;
		/**
		* Static Property key defines max job run time
		*/
		static const std::string KeyMaxRunTime;

		/**
		* set Property key.
		* @param key Property key
 		*/
		void setKey(const std::string& key)
		{
			_key = key;
		}

		/**
		* get Property key
		* @return Property key
		*/
		const std::string& getKey()
		{
			return _key;
		}

		/**
		* set Property value.
		* @param value Property value
 		*/
		void setValue(const std::string& value)
		{
			_value = value;
		}

		/**
		* get Property value
		* @return Property value
		*/
		const std::string& getValue()
		{
			return _value;
		}

		/**
		* binary serialize Property object
		* @param stream used to serialize object data 
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize Property object
		* @param stream used to deserialize Property object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to Property object
		*/
		static std::shared_ptr<Property> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

	private:
		std::string _key;
		std::string _value;
	};
}

