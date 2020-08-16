#pragma once
#include "Utils.h"
#include "Entity.h"
#include "Value.h"
#include <string>
#include <vector>
#include <memory>
#include <iostream>


namespace csyn {
	/**
	* Parameter class defines kernel parameter properties and value
	*/
	class Parameter : public Entity
	{
	public:
		/**
		* Parameter constructor
		* @param parameterName Parameter name
		* @param order Parameter order
		* @param dataType Parameter data type
		* @param parameterType Parameter type
 		*/
		Parameter(const std::string& parameterName, int32_t order, DataType dataType, ParameterType parameterType);
		
		/**
		* Parameter constructor
		* @param parameterName Parameter name
		* @param order Parameter order
		* @param dataType Parameter data type
		* @param parameterType Parameter type
		* @param parameterDesciption Parameter desciption
 		*/
		Parameter(const std::string& parameterName, int32_t order, DataType dataType, ParameterType parameterType, const std::string& parameterDesciption);
		
		/**
		* Parameter destructor.
		*/	
		~Parameter();

		/**
		* get Parameter name
		* @return Parameter name
		*/
		const std::string& getParameterName()
		{
			return _parameterName;
		}

		/**
		* get Parameter desciption
		* @return Parameter desciption
		*/
		const std::string& getParameterDesciption()
		{
			return _parameterDesciption;
		}

		/**
		* get Parameter order
		* @return Parameter order
		*/
		int32_t getOrder()
		{
			return _order;
		}

		/**
		* get Parameter data type
		* @return Parameter data type
		*/
		DataType getDataType()
		{
			return _dataType;
		}

		/**
		* get Parameter type
		* @return Parameter type
		*/
		ParameterType getParameterType()
		{
			return _parameterType;
		}

		/**
		* copy Parameter object
		* @return copy of Parameter object 
		*/
		std::shared_ptr<Parameter> getCopy();

		/**
		* get Parameter value
		* @return Parameter value 
		*/
		std::shared_ptr<Value>& getValue()
		{
			return _value;
		}

		/**
		* get Parameter data
		* @return Parameter data 
		*/
		void* getData();
		
		/**
		* set Parameter value
		* @param value Parameter value
		*/
		void setValue(std::shared_ptr<Value>& value);

		/**
		* set global value name
		* @param globalValueName global value name
		*/
		void setGlobalValueName(const std::string& globalValueName);


		/**
		* get global value name
		* @return global value name
		*/
		const std::string& getGlobalValueName()
		{
			return _globalValueName;
		}

		/**
		* validate Parameter object
		* @return true if Parameter object is valid
		*/
		bool validate();

		/**
		* binary serialize Parameter object
		* @param stream used to serialize object data 
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize Parameter object
		* @param stream used to deserialize Parameter object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to Parameter object
		*/
		static std::shared_ptr<Parameter> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

	private:
		std::string _parameterName;
		std::string _parameterDesciption;
		int32_t	_order;
		DataType _dataType;
		ParameterType _parameterType;
		std::shared_ptr<Value> _value;
		std::string _globalValueName;

	};
}

