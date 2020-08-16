#pragma once
#include <string>
#include "CSYN.h"

namespace csyn {

	/**
	* EntityType enum define supported entity types
	*/
	typedef enum{
		ENTITY_TYPE_NONE = 0,
		ENTITY_TYPE_DEVICE = 1,
		ENTITY_TYPE_DEVICE_LIST = 2,
		ENTITY_TYPE_JOB_RESULT = 3,
		ENTITY_TYPE_JOB_STATUS = 4,
		ENTITY_TYPE_JOB_STATUS_LIST = 5,
		ENTITY_TYPE_KERNEL = 6,
		ENTITY_TYPE_KERNEL_LIST = 7,
		ENTITY_TYPE_MODULE = 8,
		ENTITY_TYPE_MODULE_LIST = 9,
		ENTITY_TYPE_TASK_GROUP_RESULT_LIST = 10
	} EntityType;

	/**
	* JobExecutionStatus enum define supported job execution status
	*/
	typedef enum
	{
		JOB_QUEUE = 0,
		JOB_IN_PROGRESS,
		JOB_SUCCEED,
		JOB_FAILED
	} JobExecutionStatus;

	/**
	* TaskExecutionStatus enum define supported task execution status
	*/
	typedef enum
	{
		TASK_QUEUE = 0,
		TASK_IN_PROGRESS,
		TASK_SUCCEED,
		TASK_FAILED
	} TaskExecutionStatus;

	/**
	* DataType enum define supported kernel parameter data types
	*/
	typedef enum{
		TYPE_CHAR = 1,
		TYPE_INT32 = 2,
		TYPE_INT64 = 3,
		TYPE_FLOAT = 4,
		TYPE_DOUBLE = 5,
		TYPE_CHAR_ARRAY = 6,
		TYPE_INT32_ARRAY = 7,
		TYPE_INT64_ARRAY = 8,
		TYPE_FLOAT_ARRAY = 9,
		TYPE_DOUBLE_ARRAY = 10,
		TYPE_STRING = 11
	} DataType;

	/**
	* ParameterType enum define supported kernel parameter types
	*/
	typedef enum{
		PARAMETER_INPUT = 1,
		PARAMETER_INPUT_OUTPUT = 2,
		PARAMETER_OUTPUT = 3
	} ParameterType;

	typedef enum {
		BLAS_OP_N = 0,
		BLAS_OP_T = 1,
		BLAS_OP_C = 2
	} CublasOperation;

	typedef enum {
		BLAS_FILL_MODE_LOWER = 0,
		BLAS_FILL_MODE_UPPER = 1
	} CublasFillMode;

	typedef enum {
		BLAS_DIAG_NON_UNIT = 0,
		BLAS_DIAG_UNIT = 1
	} CublasDiagType;

	typedef enum {
		BLAS_SIDE_LEFT = 0,
		BLAS_SIDE_RIGHT = 1
	} CublasSideMode;

	class Utils
	{
	public:
		/**
		* convert DataType to string
		* @param dataType
		* @return string
		*/
		static std::string dataTypeToString(DataType dataType);

		/**
		* convert string to DataType
		* @param dataType
		* @return DataType
		*/
		static DataType stringToDataType(const std::string& dataType);

		/**
		* convert ParameterType to string
		* @param parameterType
		* @return string
		*/
		static std::string parameterTypeToString(ParameterType parameterType);

		/**
		* convert string to ParameterType
		* @param parameterType
		* @return ParameterType
		*/
		static ParameterType stringToParameterType(const std::string& parameterType);

		/**
		* check DataType is array 
		* @param type
		* @return false if type is array
		*/
		static bool IsDataTypeBase(DataType type);

	};
}

