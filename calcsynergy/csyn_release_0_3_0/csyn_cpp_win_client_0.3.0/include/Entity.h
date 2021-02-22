#pragma once
#include <string>
#include <vector> 
#include <memory> 
#include <iostream>

namespace csyn {
	class Entity
	{
	public:
		/**
		* Entity constructor.
 		*/
		Entity();
		
		/**
		* Entity destructor.
		*/	
		virtual ~Entity();

		/**
		* binary serialize Entity object
		* @param stream used to serialize object data 
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		virtual void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

	};

}