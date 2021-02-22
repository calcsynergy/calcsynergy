#pragma once
#include "Utils.h"
#include "Entity.h"
#include <string>
#include <memory>

namespace csyn {
	/**
	* Value class kernel parameter value base class
	*/
	class Value : public Entity
	{
	public:
		Value(DataType dataType, const std::string& valueName = "");
		virtual ~Value();

		const std::string& getValueName()
		{
			return _valueName;
		}

		virtual void* getData();

		virtual void** getDataAsPointerArray();
		
		DataType getDataType()
		{
			return _dataType;
		}

		virtual uint32_t getSize() = 0;
		
		virtual std::shared_ptr<Value> getCopy() = 0;
		
		virtual int32_t getLength();

	protected:
		
		std::string _valueName;
		DataType _dataType;
		void* _data;
	};
}



