#pragma once
#include "Poco/Net/HTTPRequest.h"
#include <string>

namespace csyn {

	/**
	* SecurityManager class defines user credentials
	*/

	class SecurityManager
	{
	public:
		/**
		* SecurityManager destructor
		*/	
		~SecurityManager();

		/**
		* get SecurityManager 
		* @return SecurityManager
		*/
		static SecurityManager* getManager();

		/**
		* set credentials
		* @param request HTTPRequest object
		* @param userName user name
		* @param password
 		*/
		void setCredentials(Poco::Net::HTTPRequest& request, const std::string& userName, const std::string& password);

	private:
		static SecurityManager* _manager;

		SecurityManager();
		SecurityManager(const SecurityManager&);
		SecurityManager& operator=(const SecurityManager&);
	};

}


