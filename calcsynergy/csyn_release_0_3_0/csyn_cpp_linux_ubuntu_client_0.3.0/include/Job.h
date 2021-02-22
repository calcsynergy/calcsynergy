#pragma once

#include "Entity.h"
#include "Task.h"
#include "Value.h"
#include "Device.h"
#include <string>
#include <vector>
#include <memory>
#include <iostream>


namespace csyn {
	/**
	* Job class contains list of task objects, global parameters and properties. Csyn service will be used these data to execute job 
	*/
	class Job : public Entity
	{
	public:
		/**
		* Job constructor
		* @param jobName Job name
		* @param gridDimX Job grid dimension X
		* @param gridDimY Job grid dimension Y
		* @param gridDimZ Job grid dimension Z
		* @param blockDimX Job block dimension X
		* @param blockDimY Job block dimension Y
		* @param blockDimZ Job block dimension Z
		* @param sharedMemory Job max shared memory
 		*/
		Job(const std::string& jobName, int32_t gridDimX = 1, int32_t gridDimY = 1, int32_t gridDimZ = 1, int32_t blockDimX = 1, int32_t blockDimY = 1, int32_t blockDimZ = 1, int32_t sharedMemory = 0);
		
		/**
		* Job destructor
		*/	
		~Job();

		/**
		* get Job name
		* @return Job name
		*/
		const std::string& getJobName()
		{
			return _jobName;
		}
		
		/**
		* get Job grid dimension X
		* @return grid dimension X
		*/
		int32_t getGridDimX()
		{
			return _gridDimX;
		}
		
		/**
		* get Job grid dimension Y
		* @return grid dimension Y
		*/
		int32_t getGridDimY()
		{
			return _gridDimY;
		}
		
		/**
		* get Job grid dimension Z
		* @return grid dimension Z
		*/
		int32_t getGridDimZ()
		{
			return _gridDimZ;
		}
		
		/**
		* get Job block dimension X
		* @return block dimension X
		*/
		int32_t getBlockDimX()
		{
			return _blockDimX;
		}
		
		/**
		* get Job block dimension Y
		* @return block dimension Y
		*/
		int32_t getBlockDimY()
		{
			return _blockDimY;
		}
		
		/**
		* get Job block dimension Z
		* @return block dimension Z
		*/
		int32_t getBlockDimZ()
		{
			return _blockDimZ;
		}
		
		/**
		* get Job max shared memory
		* @return max shared memory
		*/
		int32_t getSharedMemory()
		{
			return _sharedMemory;
		}

		/**
		* validate job
		* @return validation status
		*/
		bool validate();

		/**
		* add global value task
		* @param value
		*/
		void addGlobalValue(const std::shared_ptr<Value>& value);

		/**
		* add global value by name
		* @param value
		* @return global value
		*/
		std::shared_ptr<Value> getGlobalValueByName(const std::string& valueName);

		/**
		* get global value list
		* @return global value list
		*/
		std::vector<std::shared_ptr<Value>>& getGlobalValueList()
		{
			return _globalValueList;
		}
	
		/**
		* add Job task
		* @param task
		*/
		void addTask(const std::shared_ptr<Task>& task);

		/**
		* get Job task list
		* @return task list
		*/
		std::vector<std::shared_ptr<Task>>& getTaskList()
		{
			return _taskList;
		}

		/**
		* set Job run concurrently flag
		* @param concurrentRun
		*/
		void setConcurrentRun(char concurrentRun)
		{
			_concurrentRun = concurrentRun;
		}
		
		/**
		* check Job run concurrently flag
		* @return true is Job run concurrently flag is set
		*/
		bool concurrentRun()
		{
			return (_concurrentRun != 0);
		}

		/**
		* set Job max run time in seconds
		* @param maxRunTime
		*/
		void setMaxRunTime(int32_t maxRunTime)
		{
			_maxRunTime = maxRunTime;
		}

		/**
		* get Job  max run time in seconds
		* @return Job  max run time
		*/
		int32_t getMaxRunTime()
		{
			return _maxRunTime;
		}
		
		/**
		* binary serialize Job object
		* @param stream used to serialize object data 
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize Job object
		* @param stream used to deserialize Job object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to Job object
		*/
		static std::shared_ptr<Job> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

	private:
		std::string _jobName;
		std::vector<std::shared_ptr<Task>> _taskList;
		std::vector<std::shared_ptr<Value>> _globalValueList;
	 	int32_t _gridDimX;
		int32_t _gridDimY;
		int32_t _gridDimZ;
		int32_t _blockDimX;
		int32_t _blockDimY;
		int32_t _blockDimZ;
		int32_t _sharedMemory;
		int32_t _maxRunTime;
		char _concurrentRun;
	};
}


