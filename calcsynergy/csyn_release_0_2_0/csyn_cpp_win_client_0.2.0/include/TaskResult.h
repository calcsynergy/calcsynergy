#pragma once
#include "Entity.h"
#include "Parameter.h"
#include <string>
#include <vector>
#include <memory>
#include <iostream>

namespace csyn {
	/**
	* TaskResult class contains results of task executed by Csyn service
	*/
	class TaskResult : public Entity
	{
	public:
		/**
		* TaskResult constructor.
		* @param taskName task name
		* @param uuid Task unique id
		* @param parameterList calculated task kernel parameter list object
 		*/
		TaskResult(const std::string& taskName, const std::string& uuid, std::vector<std::shared_ptr<Parameter>>& parameterList);
		
		/**
		* TaskResult constructor.
		* @param taskName task name
		* @param uuid Task unique id
 		*/
		TaskResult(const std::string& taskName, const std::string& uuid);
		
		/**
		* TaskResult destructor.
		*/	
		~TaskResult();

		/**
		* get task name
		* @return task name
		*/
		const std::string& getTaskName()
		{
			return _taskName;
		}

		/**
		* get Task unique id
		* @return Task unique id
		*/
		const std::string& getUUID()
		{
			return _uuid;
		}

		/**
		* set Task unique id
		* @param uuid
		*/
		void setUUID(const std::string& uuid)
		{
			_uuid = uuid;
		}

		/**
		* set Task execution status
		* @param status
		*/
		void setExecutionStatus(TaskExecutionStatus status)
		{
			_executionStatus = status;
		}

		/**
		* get Task execution status
		* @return Task execution status
		*/
		const TaskExecutionStatus getExecutionStatus()
		{
			return _executionStatus;
		}

		/**
		* set Task execution error
		* @param error
		*/
		void setExecutionError(const std::string& error)
		{
			_executionError = error;
		}

		/**
		* get Task execution error
		* @return Task execution error
		*/
		const std::string& getExecutionError()
		{
			return _executionError;
		}

		/**
		* set calculated task kernel parameter list object
		* @param parameterList calculated task kernel parameter list object
 		*/
		void setParameterList(std::vector<std::shared_ptr<Parameter>>& parameterList)
		{
			_parameterList = parameterList;
		}

		/**
		* get calculated task kernel parameter object by name
		* @return calculated task kernel parameter object
 		*/
		std::shared_ptr<Parameter> getParameterByName(std::string& name);

		/**
		* get calculated task kernel parameter list object
		* @return calculated task kernel parameter list object
 		*/
		std::vector<std::shared_ptr<Parameter>>& getParameterList()
		{
			return _parameterList;
		}
		
		/**
		* binary serialize TaskResult object
		* @param stream used to serialize object data 
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize TaskResult object
		* @param stream used to deserialize TaskResult object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to TaskResult object
		*/
		static std::shared_ptr<TaskResult> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

	private:
		std::string _taskName;
		std::string _uuid;
		TaskExecutionStatus _executionStatus;
		std::string _executionError;
		std::vector<std::shared_ptr<Parameter>> _parameterList;
	};
}


