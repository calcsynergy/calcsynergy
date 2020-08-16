#pragma once
#include "Entity.h"
#include "Utils.h"
#include <string>
#include <vector> 
#include <memory> 
#include <iostream>


namespace csyn {
	class Response
	{
	public:

		/**
		* Response contructor.
		*/
		Response();

		/**
		* Response destructor.
		*/
		virtual ~Response();
		
		/**
		* binary serialize Response object
		* @param stream used to serialize object data
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize Response object
		* @param stream used to deserialize Response object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to Response object
		*/
		static std::shared_ptr<Response> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

		/**
		* get Response status
		* @return Response status
		*/
		char getStatus()
		{
			return _status;
		}


		/**
		* set Response status
		* @param status Response status
		*/
		void setStatus(char status)
		{
			_status = status;
		}

		/**
		* get Response error message
		* @return Response error message
		*/
		const std::string& getError()
		{
			return _error;
		}

		/**
		* set Response error message
		* @param error Response error message
		*/
		void setError(const std::string& error)
		{
			_error = error;
		}

		/**
		* get Response entity type
		* @return Response entity type
		*/
		EntityType getEntityType()
		{
			return _entityType;
		}

		/**
		* set Response entity type
		* @param entityType Response entity type
		*/
		void setEntityType(EntityType entityType)
		{
			_entityType = entityType;
		}

		/**
		* get Response entity object
		* @return Response entity object
		*/
		std::shared_ptr<Entity> getEntity()
		{
			return _entity;
		}

		/**
		* set Response entity object
		* @param entity Response entity object
		*/
		void setEntity(std::shared_ptr<Entity> entity)
		{
			_entity = entity;
		}

	protected:
		char _status;
		std::string _error;
		EntityType _entityType;
		std::shared_ptr<Entity> _entity;
	};

}