#pragma once
#include "Entity.h"
#include <string>
#include <memory>
#include <iostream>

namespace csyn {
	/**
	* Device class defines GPU properties
	*/
	class Device : public Entity
	{
	public:
		/**
		* Device constructor
		* @param id GPU id
 		*/
		Device(int32_t id);
		
		/**
		* Device destructor
		*/
		~Device();
		
		/**
		* binary serialize Device object
		* @param stream used to serialize object data 
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize Device object
		* @param stream used to deserialize Device object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to Device object
		*/
		static std::shared_ptr<Device> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);
		
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
		* get Device id
		* @return Device id 
		*/
		int32_t getId()
		{
			return _id;
		}

		/**
		* set Device id
		* @param id 
		*/
		void setId(int32_t id)
		{
			_id = id;
		}
		
		/**
		* get Device name
		* @return Device name
		*/
		const std::string& getName()
		{
			return _name;
		}

		/**
		* set Device name
		* @param name 
		*/
		void setName(const std::string& name)
		{
			_name = name;
		}

		/**
		* get Device major revision number
		* @return Device major
		*/
		int32_t getMajor()
		{
			return _major;
		}

		/**
		* set Device major revision number
		* @param major
		*/
		void setMajor(int32_t major)
		{
			_major = major;
		}

		/**
		* get Device minor revision number
		* @return Device minor
		*/
		int32_t getMinor()
		{
			return _minor;
		}

		/**
		* set Device minor revision number
		* @param minor
		*/
		void setMinor(int32_t minor)
		{
			_minor = minor;
		}

		/**
		* get Device total global memory
		* @return Device total global memory
		*/
		int64_t getTotalGlobalMem()
		{
			return _totalGlobalMem;
		}


		/**
		* set Device total global memory
		* @param totalGlobalMem
		*/
		void setTotalGlobalMem(int64_t totalGlobalMem)
		{
			_totalGlobalMem = totalGlobalMem;
		}

		/**
		* get number of Device multiprocessors
		* @return number of Device multiprocessors
		*/
		int32_t getMultiProcessorCount()
		{
			return _multiProcessorCount;
		}

		/**
		* set number of Device multiprocessors
		* @param multiProcessorCount
		*/
		void setMultiProcessorCount(int32_t multiProcessorCount)
		{
			_multiProcessorCount = multiProcessorCount;
		}

		/**
		* get Device clock rate
		* @return Device clock rate
		*/
		int32_t getClockRate()
		{
			return _clockRate;
		}

		/**
		* set Device clock rate
		* @param clockRate
		*/
		void setClockRate(int32_t clockRate)
		{
			_clockRate = clockRate;
		}

		/**
		* get Device total constant memory
		* @return Device total constant memory
		*/
		int64_t getTotalConstMem()
		{
			return _totalConstMem;
		}

		/**
		* set Device total constant memory
		* @param totalConstMem
		*/
		void setTotalConstMem(int64_t totalConstMem)
		{
			_totalConstMem = totalConstMem;
		}

		/**
		* get Device shared memory per block
		* @return Device shared memory per block
		*/
		int64_t getSharedMemPerBlock()
		{
			return _sharedMemPerBlock;
		}

		/**
		* set Device shared memory per block
		* @param sharedMemPerBlock
		*/
		void setSharedMemPerBlock(int64_t sharedMemPerBlock)
		{
			_sharedMemPerBlock = sharedMemPerBlock;
		}

		/**
		* get Device warp size
		* @return Device warp size
		*/
		int32_t getWarpSize()
		{
			return _warpSize;
		}

		/**
		* set Device warp size
		* @param warpSize
		*/
		void setWarpSize(int32_t warpSize)
		{
			_warpSize = warpSize;
		}

		/**
		* get Device max threads per multiprocessor
		* @return Device max threads per multiprocessor
		*/
		int32_t getMaxThreadsPerMultiProcessor()
		{
			return _maxThreadsPerMultiProcessor;
		}

		/**
		* set Device max threads per multiprocessor
		* @param maxThreadsPerMultiProcessor
		*/
		void setMaxThreadsPerMultiProcessor(int32_t maxThreadsPerMultiProcessor)
		{
			_maxThreadsPerMultiProcessor = maxThreadsPerMultiProcessor;
		}

		/**
		* get Device max threads per block
		* @return Device max threads per block
		*/
		int32_t getMaxThreadsPerBlock()
		{
			return _maxThreadsPerBlock;
		}

		/**
		* set Device max threads per block
		* @param maxThreadsPerBlock
		*/
		void setMaxThreadsPerBlock(int32_t maxThreadsPerBlock)
		{
			_maxThreadsPerBlock = maxThreadsPerBlock;
		}

		/**
		* get Device max threads dimension X
		* @return Device max threads dimension X
		*/
		int32_t getMaxThreadsDimX()
		{
			return _maxThreadsDimX;
		}

		/**
		* set Device max threads dimension X
		* @param maxThreadsDimX
		*/
		void setMaxThreadsDimX(int32_t maxThreadsDimX)
		{
			_maxThreadsDimX = maxThreadsDimX;
		}

		/**
		* get Device max threads dimension Y
		* @return Device max threads dimension Y
		*/
		int32_t getMaxThreadsDimY()
		{
			return _maxThreadsDimY;
		}

		/**
		* set Device max threads dimension Y
		* @param maxThreadsDimY
		*/
		void setMaxThreadsDimY(int32_t maxThreadsDimY)
		{
			_maxThreadsDimY = maxThreadsDimY;
		}

		/**
		* get Device max threads dimension Z
		* @return Device max threads dimension Z
		*/
		int32_t getMaxThreadsDimZ()
		{
			return _maxThreadsDimZ;
		}

		/**
		* set Device max threads dimension Z
		* @param maxThreadsDimZ
		*/
		void setMaxThreadsDimZ(int32_t maxThreadsDimZ)
		{
			_maxThreadsDimZ = maxThreadsDimZ;
		}

		/**
		* get Device max grid size X
		* @return Device max grid size X
		*/
		int32_t getMaxGridSizeX()
		{
			return _maxGridSizeX;
		}

		/**
		* set Device max grid size X
		* @param maxGridSizeX
		*/
		void setMaxGridSizeX(int32_t maxGridSizeX)
		{
			_maxGridSizeX = maxGridSizeX;
		}

		/**
		* get Device max grid size Y
		* @return Device max grid size Y
		*/
		int32_t getMaxGridSizeY()
		{
			return _maxGridSizeY;
		}

		/**
		* set Device max grid size Y
		* @param maxGridSizeY
		*/
		void setMaxGridSizeY(int32_t maxGridSizeY)
		{
			_maxGridSizeY = maxGridSizeY;
		}

		/**
		* get Device max grid size Z
		* @return Device max grid size Z
		*/
		int32_t getMaxGridSizeZ()
		{
			return _maxGridSizeZ;
		}

		/**
		* set Device max grid size Z
		* @param maxGridSizeZ
		*/
		void setMaxGridSizeZ(int32_t maxGridSizeZ)
		{
			_maxGridSizeZ = maxGridSizeZ;
		}

		/**
		* get Device overlap. If is 1 the device can concurrently copy memory between host and device while executing a kernel
		* @return Device overlap
		*/
		int32_t getDeviceOverlap()
		{
			return _deviceOverlap;
		}

		/**
		* set Device overlap. If is 1 the device can concurrently copy memory between host and device while executing a kernel
		* @param deviceOverlap
		*/
		void setDeviceOverlap(int32_t deviceOverlap)
		{
			_deviceOverlap = deviceOverlap;
		}

		int32_t getAsyncEngineCount()
		{
			return _asyncEngineCount;
		}

		void setAsyncEngineCount(int32_t asyncEngineCount)
		{
			_asyncEngineCount = asyncEngineCount;
		}

		/**
		* get Device kernel execution timeout enabled. If is 1 there is a run time limit for kernels executed on the device
		* @return Device kernel execution timeout enabled
		*/
		int32_t getKernelExecTimeoutEnabled()
		{
			return _kernelExecTimeoutEnabled;
		}

		/**
		* set Device kernel execution timeout enabled. If is 1 there is a run time limit for kernels executed on the device
		* @param kernelExecTimeoutEnabled
		*/
		void setKernelExecTimeoutEnabled(int32_t kernelExecTimeoutEnabled)
		{
			_kernelExecTimeoutEnabled = kernelExecTimeoutEnabled;
		}

		/**
		* get Device integrated
		* @return Device integrated
		*/
		int32_t getIntegrated()
		{
			return _integrated;
		}

		/**
		* set Device integrated
		* @param integrated
		*/
		void setIntegrated(int32_t integrated)
		{
			_integrated = integrated;
		}

		/**
		* get Device can map host memory. If is 1 the device can map host memory into the CUDA address space
		* @return Device can map host memory
		*/
		int32_t getCanMapHostMemory()
		{
			return _canMapHostMemory;
		}

		/**
		* set Device can map host memory. If is 1 the device can map host memory into the CUDA address space
		* @param canMapHostMemory
		*/
		void setCanMapHostMemory(int32_t canMapHostMemory)
		{
			_canMapHostMemory = canMapHostMemory;
		}

		/**
		* get Device max registers per block
		* @return Device max registers per block
		*/
		int32_t getRegsPerBlock()
		{
			return _regsPerBlock;
		}

		/**
		* set Device max registers per block
		* @param regsPerBlock
		*/
		void setRegsPerBlock(int32_t regsPerBlock)
		{
			_regsPerBlock = regsPerBlock;
		}

		/**
		* get Device concurrent kernels. If 1 the device supports executing multiple kernels within the same context simultaneously
		* @return Device concurrent kernels
		*/
		int32_t getConcurrentKernels()
		{
			return _concurrentKernels;
		}

		/**
		* set Device concurrent kernels. If 1 the device supports executing multiple kernels within the same context simultaneously
		* @param concurrentKernels
		*/
		void setConcurrentKernels(int32_t concurrentKernels)
		{
			_concurrentKernels = concurrentKernels;
		}


	private:
		std::string _ipAddress;
		int32_t _port;
		std::string _name;
		int32_t _major;
		int32_t _minor;
		int64_t _totalGlobalMem;
		int32_t _multiProcessorCount;
		int32_t _clockRate;
		int64_t _totalConstMem;
		int64_t _sharedMemPerBlock;
		int32_t _warpSize;
		int32_t _maxThreadsPerMultiProcessor;
		int32_t _maxThreadsPerBlock;
		int32_t _regsPerBlock;
		int32_t _maxThreadsDimX;
		int32_t _maxThreadsDimY;
		int32_t _maxThreadsDimZ;
		int32_t _maxGridSizeX;
		int32_t _maxGridSizeY;
		int32_t _maxGridSizeZ;
		int32_t _deviceOverlap;
		int32_t _asyncEngineCount;
		int32_t _kernelExecTimeoutEnabled;
		int32_t _integrated;
		int32_t _canMapHostMemory;
		int32_t _concurrentKernels;
		int32_t _id;
	};
}

