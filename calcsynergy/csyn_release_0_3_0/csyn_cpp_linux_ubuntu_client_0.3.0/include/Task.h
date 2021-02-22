#pragma once

#include "Entity.h"
#include "Kernel.h"

#include <string>
#include <memory>
#include <iostream>

namespace csyn {
	/**
	* Task class defines task properties and kernel that will be executed during job run
	*/
	class Task : public Entity
	{
	public:
		/**
		* Task constructor
		* @param taskName task name
		* @param kernel task kernel object
		* @param gridDimX task grid dimension X
		* @param gridDimY task grid dimension Y
		* @param gridDimZ task grid dimension Z
		* @param blockDimX task block dimension X
		* @param blockDimY task block dimension Y
		* @param blockDimZ task block dimension Z
		* @param sharedMemory task max shared memory
 		*/
		Task(const std::string& taskName, const std::shared_ptr<Kernel>& kernel, int32_t gridDimX = 1, int32_t gridDimY = 1, int32_t gridDimZ = 1, int32_t blockDimX = 1, int32_t blockDimY = 1, int32_t blockDimZ = 1, int32_t sharedMemory = 0);
		
		/**
		* Task destructor
		*/
		~Task();

		/**
		* get task name
		* @return task name
		*/
		const std::string& getTaskName()
		{
			return _taskName;
		}
		
		/**
		* get task kernel
		* @return task kernel object
		*/
		std::shared_ptr<Kernel>& getKernel()
		{
			return _kernel;
		}
		
		/**
		* get task grid dimension X
		* @return grid dimension X
		*/
		int32_t getGridDimX()
		{
			return _gridDimX;
		}

		/**
		* get task grid dimension Y
		* @return grid dimension Y
		*/
		int32_t getGridDimY()
		{
			return _gridDimY;
		}

		/**
		* get task grid dimension Z
		* @return grid dimension Z
		*/
		int32_t getGridDimZ()
		{
			return _gridDimZ;
		}

		/**
		* get task block dimension X
		* @return block dimension X
		*/
		int32_t getBlockDimX()
		{
			return _blockDimX;
		}

		/**
		* get task block dimension Y
		* @return block dimension Y
		*/
		int32_t getBlockDimY()
		{
			return _blockDimY;
		}

		/**
		* get task block dimension Z
		* @return block dimension Z
		*/
		int32_t getBlockDimZ()
		{
			return _blockDimZ;
		}
		
		/**
		* get task max shared memory
		* @return max shared memory
		*/
		int32_t getSharedMemory()
		{
			return _sharedMemory;
		}

		/**
		* validate task
		* @return validation status
		*/
		bool validate();

		/**
		* binary serialize task object
		* @param stream used to serialize object data 
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize task object
		* @param stream used to deserialize task object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to task object
		*/
		static std::shared_ptr<Task> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

	private:
		std::string _taskName;
		std::shared_ptr<Kernel> _kernel;
		int32_t _gridDimX;
		int32_t _gridDimY;
		int32_t _gridDimZ;
		int32_t _blockDimX;
		int32_t _blockDimY;
		int32_t _blockDimZ;
		int32_t _sharedMemory;
	};
}
