#pragma once
#include <exception>
#include <iostream>
#include <sstream>
#include <string>

namespace csyn {
	/**
	* CSynException class 
	*/
	class CSynException : public std::exception
	{

	public:

		/** CSynException Constructor
		*  @param msg The error message
		*/
		
		CSynException(const std::string& msg) : error_message(msg)
		{
		}

		/** Destructor.
		*  Virtual to allow for subclassing.
		*/
		virtual ~CSynException() throw () {}

		/** Returns a pointer to the error description.
		*  @return A pointer to a const char*
		*/
		virtual const char* what() const throw () {
			return error_message.c_str();
		}

	protected:

		std::string error_message;      ///< Error message

	};
}

