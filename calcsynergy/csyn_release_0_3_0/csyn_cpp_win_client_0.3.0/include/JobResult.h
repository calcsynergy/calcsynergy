#pragma once

#include "Entity.h"
#include "TaskResult.h"
#include "Utils.h"
#include <string>
#include <vector>
#include <memory>
#include <iostream>

namespace csyn {
	/**
	* JobResult class contains results of job executed by Csyn service
	*/
	class JobResult : public Entity
	{
	public:

		/**
		* JobResult constructor
		* @param jobName Job name
		* @param uuid Job unique id
		*/
		JobResult(const std::string& jobName, const std::string& uuid);
		
		/**
		* JobResult destructor
		*/	
		~JobResult();
		
		/**
		* get Job name
		* @return Job name
		*/
		const std::string& getJobName()
		{
			return _jobName;
		}

		/**
		* get Job unique id
		* @return Job unique id
		*/
		const std::string& getUUID()
		{
			return _uuid;
		}

		/**
		* set Job execution status
		* @param status Job execution status
		*/
		void setExecutionStatus(JobExecutionStatus status)
		{
			_executionStatus = status;
		}

		/**
		* get Job execution status
		* @return Job execution status
		*/
		JobExecutionStatus getExecutionStatus() const
		{
			return _executionStatus;
		}

		/**
		* set Job execution error
		* @param error Job execution error
		*/
		void setExecutionError(const std::string& error)
		{
			_executionError = error;
		}

		/**
		* get Job execution error
		* @return Job execution error
		*/
		const std::string& getExecutionError() const
		{
			return _executionError;
		}

		/**
		* add Task result
		* @param taskResult Task result object
		*/
		void addTaskResult(const std::shared_ptr<TaskResult>& taskResult);

		/**
		* add Task result list
		* @param taskResultList Task result list object
		*/
		void addTaskResultList(const std::vector<std::shared_ptr<TaskResult>>& taskResultList);

		/**
		* get Task result list
		* @return Task result list object
		*/
		std::vector<std::shared_ptr<TaskResult>>& getTaskResultList()
		{
			return _taskResultList;
		}

		/**
		* add Task result
		* @param taskName Task name
		* @return Task result object
		*/
		std::shared_ptr<TaskResult> getTaskResult(const std::string& taskName);

		/**
		* binary serialize JobResult object
		* @param stream used to serialize object data 
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize JobResult object
		* @param stream used to deserialize JobResult object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to JobResult object
		*/
		static std::shared_ptr<JobResult> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

	private:
		std::string _jobName;
		std::string _uuid;
		std::vector<std::shared_ptr<TaskResult>> _taskResultList;
		JobExecutionStatus _executionStatus;
		std::string _executionError;
	};
}