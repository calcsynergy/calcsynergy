#pragma once
#include "Module.h"
#include <string>
#include <vector>
#include <memory>
#include <iostream>

namespace csyn {
	/**
	* ModuleList class contains list of module objects
	*/
	class ModuleList : public Entity
	{
	public:
		/**
		* ModuleList constructor.
 		*/
		ModuleList();
		
		/**
		* ModuleList copy constructor.
		* @param list ModuleList object
		*/	
		ModuleList(const ModuleList& list);
		
		/**
		* ModuleList destructor.
		*/	
		~ModuleList();
		
		/**
		* binary serialize ModuleList object
		* @param stream used to serialize object data 
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize ModuleList object
		* @param stream used to deserialize ModuleList object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to ModuleList object
		*/
		static std::shared_ptr<ModuleList> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

		/**
		* get Module objects list
		* @return Module objects list
		*/
		const std::vector <std::shared_ptr<Module>>& getList()
		{
			return _moduleList;
		}

		/**
		* add Module object
		* @param module Module object
		*/
		void addModule(const std::shared_ptr<Module>& module)
		{
			_moduleList.push_back(module);
		}

	private:
		std::vector<std::shared_ptr<Module>> _moduleList;
	};
}

