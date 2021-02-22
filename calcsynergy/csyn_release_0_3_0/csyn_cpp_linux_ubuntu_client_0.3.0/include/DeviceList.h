#pragma once
#include "Device.h"
#include <string>
#include <vector>
#include <memory>
#include <iostream>


namespace csyn {
	/**
	* DeviceList class contains list of device objects
	*/
	class DeviceList : public Entity
	{
	public:
		/**
		* DeviceList constructor.
 		*/
		DeviceList();
		
				
		/**
		* DeviceList destructor.
		*/
		~DeviceList();
		
		/**
		* binary serialize DeviceList object
		* @param stream used to serialize object data 
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		*/
		void serializeBinary(std::ostream& stream, bool isNetworkByteOrder = false);

		/**
		* binary deserialize DeviceList object
		* @param stream used to deserialize DeviceList object
		* @param isNetworkByteOrder define byte order. If parameter value is true network byte order will be used, otherwise native byte order
		* @return shared pointer to DeviceList object
		*/
		static std::shared_ptr<DeviceList> deserializeBinary(std::istream& stream, bool isNetworkByteOrder = false);

		/**
		* get list of Device objects
		* @return list of Device objects
		*/
		std::vector<std::shared_ptr<Device>>& getList() 
		{
			return _deviceList;
		}

		/**
		* add Device
		* @param device
		*/
		void addDevice(const std::shared_ptr<Device>& device)
		{
			_deviceList.push_back(device);
		}

	private:
		std::vector<std::shared_ptr<Device>> _deviceList;
	};
}

