#pragma once

#include "Entity.h"
#include "TaskStatus.h"
#include "Utils.h"
#include <string>
#include <vector>
#include <memory>
#include <iostream>

namespace csyn {
	/**
	* JobStatus class contains status of job executed by Csyn service
	*/
	class JobStatus : public Entity
	{
	public:
		/**
		* JobStatus constructor
		* @param jobName Job name
		* @param uuid Job unique id
		*/
		JobStatus(const std::string& jobName, const std::string& uuid);

		/**
		* JobStatus destructor
		*/
		~JobStatus();

		/**
		* get Job name
		* @return Job name
		*/
		const std::string& getJobName() const
		{
			return _jobName;
		}
		
		/**
		* get Job unique id
		* @return Job unique id
		*/
		const std::string& getUUID() const
		{
			return _uuid;
		}
		
		/**
		* set Job execution start time
		* @param timestamp Job execution start time
		*/
		void setStartTimestamp(const std::string& timestamp)
		{
			_startTimestamp = timestamp;
		}

		/**
		* get Job execution start time
		* @return Job execution start time
		*/
		const std::string& getStartTimestamp() const
		{
			return _startTimestamp;
		}

		/**
		* check is Job execution finished
		* @return true if Job execution is finished
		*/
		bool isJobFinished();

		/**
		* set Job execution end time
		* @param timestamp Job execution end time
		*/
		void setEndTimestamp(const std::string& timestamp)
		{
			_endTimestamp = timestamp;
		}

		/**
		* get Job execution end time
		* @return Job execution end time
		*/
		const std::string& getEndTimestamp() const
		{
			return _endTimestamp;
		}

		/**
		* set Job execution period
		* @param time Job execution period
		*/
		void setExecution(double time)
		{
			_execution = time;
		}
		
		/**
		* get Job execution period
		* @return Job execution period
		*/
		double getExecution()  const
		{
			return _execution;
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
		* add Task status
		* @param taskStatus Task status object
		*/
		void addTaskStatus(const std::shared_ptr<TaskStatus>& taskStatus);

		/**
		* add Task status list
		* @param taskStatusList Task status list object
		*/
		void addTaskStatusList(const std::vector<std::shared_ptr<TaskStatus>>& taskStatusList);


		/**
		* get Task status list
		* @return Task status list 
		*/
		std::vector<std::shared_ptr<TaskStatus>>& getTaskStatusList()
		{
			return _taskStatusList;
		}


		/**
		* binary serialize JobStatus object
		* @param stream used to serialize object data
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);


		/**
		* binary deserialize JobStatus object
		* @param stream used to deserialize JobStatus object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to JobStatus object
		*/
		static std::shared_ptr<JobStatus> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

	private:
		std::string _jobName;
		std::string _uuid;
		std::string _startTimestamp;
		std::string _endTimestamp;
		JobExecutionStatus _executionStatus;
		std::string _executionError;
		double _execution;
		std::vector<std::shared_ptr<TaskStatus>> _taskStatusList;
	};
}