#pragma once
#include "Entity.h"
#include "Utils.h"
#include <string>
#include <vector>
#include <memory>
#include <iostream>


namespace csyn {
	/**
	* TaskStatus class contains status of task executed by Csyn service
	*/
	class TaskStatus : public Entity
	{
	public:

		/**
		* TaskStatus constructor.
		* @param taskName Task name
		* @param uuid Task unique id
		*/
		TaskStatus(const std::string& taskName, const std::string& uuid);

		/**
		* TaskStatus destructor.
		*/
		~TaskStatus();

		/**
		* get Engine ip address
		* @return Device ip address
		*/
		const std::string& getIpAddress()
		{
			return _ipAddress;
		}

		/**
		* set Engine ip address
		* @param ipAddress
		*/
		void setIpAddress(const std::string& ipAddress)
		{
			_ipAddress = ipAddress;
		}

		/**
		* get Engine port
		* @return Device engine port
		*/
		int32_t getPort()
		{
			return _port;
		}

		/**
		* set Engine port
		* @param port
		*/
		void setPort(int32_t port)
		{
			_port = port;
		}

		/**
		* get Task name
		* @return Task name
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
		* set Task execution start time
		* @param timestamp Task execution start time
		*/
		void setStartTimestamp(const std::string& timestamp)
		{
			_startTimestamp = timestamp;
		}
		
		/**
		* get Task execution start time
		* @return Task execution start time
		*/
		const std::string& getStartTimestamp()
		{
			return _startTimestamp;
		}

		/**
		* set Task execution period
		* @param time Task execution period
		*/
		void setExecution(double time)
		{
			_execution = time;
		}
		
		/**
		* get Task execution period
		* @return Task execution period
		*/
		double getExecution()
		{
			return _execution;
		}

		/**
		* set Task execution status
		* @param status Task execution status
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
		* @param error Task execution error
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
		* binary serialize TaskStatus object
		* @param stream used to serialize object data
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize TaskStatus object
		* @param stream used to deserialize TaskStatus object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to TaskStatus object
		*/
		static std::shared_ptr<TaskStatus> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

	private:
		std::string _taskName;
		std::string _uuid;
		TaskExecutionStatus _executionStatus;
		std::string _executionError;
		std::string _startTimestamp;
		double _execution;
		std::string _ipAddress;
		int32_t _port;
	};
}


