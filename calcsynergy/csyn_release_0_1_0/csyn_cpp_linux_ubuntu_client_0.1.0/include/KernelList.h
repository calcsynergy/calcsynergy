#pragma once
#include "Kernel.h"
#include <string>
#include <vector>
#include <memory>
#include <iostream>

namespace csyn {
	/**
	* KernelList class contains list of kernel objects
	*/
	class KernelList : public Entity
	{
	public:
		/**
		* KernelList constructor.
 		*/
		KernelList();
		
		/**
		* KernelList copy constructor.
		* @param list KernelList object
 		*/
		KernelList(const KernelList& list);
		
		/**
		* KernelList destructor.
		*/	
		~KernelList();

		/**
		* binary serialize KernelList object
		* @param stream used to serialize object data 
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize KernelList object
		* @param stream used to deserialize KernelList object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to KernelList object
		*/
		static std::shared_ptr<KernelList> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

		/**
		* get Kernel list
		* @return list of Kernel objects
		*/
		const std::vector <std::shared_ptr<Kernel>>& getList()
		{
			return _kernelList;
		}

		/**
		* add Kernel
		* @param Kernel object
		*/
		void addKernel(const std::shared_ptr<Kernel>& kernel)
		{
			_kernelList.push_back(kernel);
		}

	private:
		std::vector<std::shared_ptr<Kernel>> _kernelList;
	};
}

