#pragma once
#include <string>

#if defined(WIN32)
	#if defined(CSYN_EXPORTS)
		#define CSYN_API __declspec(dllexport)
	#else
		#define CSYN_API __declspec(dllimport)
	#endif
#else
	#define CSYN_API
#endif

const std::string _csyn_version = "0.2.0";


