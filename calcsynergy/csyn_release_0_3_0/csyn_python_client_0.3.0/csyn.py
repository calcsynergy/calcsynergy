##
# @package csyn
# CSyn service Python SDK 
#

import struct
import urllib.request
import base64
import sys
#import time

##
# DataType enum define supported kernel parameter data types
#
class DataType:
    type_byte = 1
    type_int = 2
    type_long = 3
    type_float = 4
    type_double = 5
    type_byte_array = 6
    type_int_array = 7
    type_long_array = 8
    type_float_array = 9
    type_double_array = 10
    type_string = 11

##
# ParameterType enum define supported kernel parameter types
#
class ParameterType:
    parameter_input = 1
    parameter_input_output = 2
    parameter_output = 3

##
# EntityType define supported entity types
#
class EntityType:
    entity_none = 0
    entity_device = 1
    entity_device_list = 2
    entity_job_result = 3
    entity_job_status = 4
    entity_job_status_list = 5
    entity_kernel = 6
    entity_kernel_list = 7
    entity_module = 8
    entity_module_list = 9
 
##
# JobExecutionStatus define job execution status
#
class JobExecutionStatus:
    job_queue = 0
    job_in_progress = 1
    job_succeed = 2
    job_failed = 3

##
# TaskExecutionStatus define task execution status
#
class TaskExecutionStatus:
    task_queue = 0
    task_in_progress = 1
    task_succeed = 2
    task_failed = 3

##
# CublasOperation define cublas library operation
#
class CublasOperation:
    BLAS_OP_N = 0
    BLAS_OP_T = 1
    BLAS_OP_C = 2

##
# CublasFillMode define cublas library fill mode
#	
class CublasFillMode:
	BLAS_FILL_MODE_LOWER = 0
	BLAS_FILL_MODE_UPPER = 1

##
# CublasDiagType define cublas library diagonal type
#	
class CublasDiagType:
	BLAS_DIAG_NON_UNIT = 0
	BLAS_DIAG_UNIT = 1

##
# CublasSideMode define cublas library side mode
#
class CublasSideMode:
	BLAS_SIDE_LEFT = 0
	BLAS_SIDE_RIGHT = 1

class SecurityManager:
	##
	# SecurityManager constructor
	# @param user the Csyn service admin user name
	# @param password the Csyn service admin password
	#
	def __init__(self, user, password):
		self.user = user
		self.password = password
		self.scheme = 'Basic'
		self.authorization = 'Authorization'
         
    ##
	# Set headers credentials
    # @param headers 
	#
	def set_credentials(self, headers):
		cred = self.user + ':' + self.password
		encode = base64.b64encode(bytes(cred, 'utf-8'))
		auth = self.scheme + ' ' + encode.decode(encoding="utf-8")
		headers[self.authorization] = auth
 
class CSynException(Exception):
    pass


class Parser:
    network=False
 
    def get_byte_size(self):
        frm = '=B'
        if Parser.network: 
            frm = '!B'
        sz = struct.calcsize(frm) * 2
        return sz
    
    def serialize_byte(self, value, buffer, offset):
        frm = '=B'
        if Parser.network: 
            frm = '!B'
        t = DataType.type_byte
        struct.pack_into(frm, buffer, offset, t)
        offset = offset + struct.calcsize(frm)
        struct.pack_into(frm, buffer, offset, value)
        offset = offset + struct.calcsize(frm)
        return offset

    def deserialize_byte(self, buffer, offset, no_type_byte = False):
        frm = '=B'
        if Parser.network: 
            frm = '!B'
        if not no_type_byte:
            t, = struct.unpack_from(frm, buffer, offset)
            offset = offset + struct.calcsize(frm)
            if t != DataType.type_byte:
                raise CSynException('Failed deserialize value. Incorrect data type')
        value, = struct.unpack_from(frm, buffer, offset)
        offset = offset + struct.calcsize(frm)
        return (offset, value)
 
    def get_int_size(self):
        frm = '=B'
        if Parser.network: 
            frm = '!B'
        sz = struct.calcsize(frm)
        frm = '=i'
        if Parser.network: 
            frm = '!i'
        sz = sz + struct.calcsize(frm)
        return sz

    def serialize_int(self, value, buffer, offset):
        frm = '=B'
        if Parser.network: 
            frm = '!B'
        t = DataType.type_int
        struct.pack_into(frm, buffer, offset, t)
        offset = offset + struct.calcsize(frm)
        frm = '=i'
        if Parser.network: 
            frm = '!i'
        struct.pack_into(frm, buffer, offset, int(value))
        offset = offset + struct.calcsize(frm)
        return offset
    
    def deserialize_int(self, buffer, offset, no_type_byte = False):
        if not no_type_byte:
            frm = '=B'
            if Parser.network: 
                frm = '!B'
            t, = struct.unpack_from(frm, buffer, offset)
            offset = offset + struct.calcsize(frm)
            if t != DataType.type_int:
                raise CSynException('Failed deserialize value. Incorrect data type')
        frm = '=i'
        if Parser.network: 
            frm = '!i'
        value, = struct.unpack_from(frm, buffer, offset)
        offset = offset + struct.calcsize(frm)
        return (offset, value)
    
    def get_long_size(self):
        frm = '=B'
        if Parser.network: 
            frm = '!B'
        sz = struct.calcsize(frm)
        frm = '=q'
        if Parser.network: 
            frm = '!q'
        sz = sz + struct.calcsize(frm)
        return sz
    
    def serialize_long(self, value, buffer, offset):
        frm = '=B'
        if Parser.network: 
            frm = '!B'
        t = DataType.type_long
        struct.pack_into(frm, buffer, offset, t)
        offset = offset + struct.calcsize(frm)
        frm = '=q'
        if Parser.network: 
            frm = '!q'
        struct.pack_into(frm, buffer, offset, int(value))
        offset = offset + struct.calcsize(frm)
        return offset
    
    def deserialize_long(self, buffer, offset, no_type_byte = False):
        if not no_type_byte:
            frm = '=B'
            if Parser.network: 
                frm = '!B'
            t, = struct.unpack_from(frm, buffer, offset)
            offset = offset + struct.calcsize(frm)
            if t != DataType.type_long:
                raise CSynException('Failed deserialize value. Incorrect data type')
        frm = '=q'
        if Parser.network: 
            frm = '!q'
        value, = struct.unpack_from(frm, buffer, offset)
        offset = offset + struct.calcsize(frm)
        return (offset, value)
    
    def get_float_size(self):
        frm = '=B'
        if Parser.network: 
            frm = '!B'
        sz = struct.calcsize(frm)
        frm = '=f'
        if Parser.network: 
            frm = '!f'
        sz = sz + struct.calcsize(frm)
        return sz
    
    def serialize_float(self, value, buffer, offset):
        frm = '=B'
        if Parser.network: 
            frm = '!B'
        t = DataType.type_float
        struct.pack_into(frm, buffer, offset, t)
        offset = offset + struct.calcsize(frm)
        frm = '=f'
        if Parser.network: 
            frm = '!f'
        struct.pack_into(frm, buffer, offset, float(value))
        offset = offset + struct.calcsize(frm)
        return offset
    
    def deserialize_float(self, buffer, offset, no_type_byte = False):
        if not no_type_byte:
            frm = '=B'
            if Parser.network: 
                frm = '!B'
            t, = struct.unpack_from(frm, buffer, offset)
            offset = offset + struct.calcsize(frm)
            if t != DataType.type_float:
                raise CSynException('Failed deserialize value. Incorrect data type')
        frm = '=f'
        if Parser.network: 
            frm = '!f'
        value, = struct.unpack_from(frm, buffer, offset)
        offset = offset + struct.calcsize(frm)
        return (offset, value)
    
    def get_double_size(self):
        frm = '=B'
        if Parser.network: 
            frm = '!B'
        sz = struct.calcsize(frm)
        frm = '=d'
        if Parser.network: 
            frm = '!d'
        sz = sz + struct.calcsize(frm)
        return sz
    
    def serialize_double(self, value, buffer, offset):
        frm = '=B'
        if Parser.network: 
            frm = '!B'
        t = DataType.type_double
        struct.pack_into(frm, buffer, offset, t)
        offset = offset + struct.calcsize(frm)
        frm = '=d'
        if Parser.network: 
            frm = '!d'
        struct.pack_into(frm, buffer, offset, value)
        offset = offset + struct.calcsize(frm)
        return offset
    
    def deserialize_double(self, buffer, offset, no_type_byte = False):
        if not no_type_byte:
            frm = '=B'
            if Parser.network: 
                frm = '!B'
            t, = struct.unpack_from(frm, buffer, offset)
            offset = offset + struct.calcsize(frm)
            if t != DataType.type_double:
                raise CSynException('Failed deserialize value. Incorrect data type')
        frm = '=d'
        if Parser.network: 
            frm = '!d'
        value, = struct.unpack_from(frm, buffer, offset)
        offset = offset + struct.calcsize(frm)
        return (offset, value)
    
    def get_array_size(self, value, aFormat):
        frm = '=B'
        if Parser.network: 
            frm = '!B'
        sz = struct.calcsize(frm) * 2
        frm = '=i'
        if Parser.network: 
            frm = '!i'
        sz = sz + struct.calcsize(frm)
        if value is not None:
            length = len(value)
            if length > 0:
                sz = sz + struct.calcsize(aFormat.format(length))
        return sz
    
    def serialize_array(self, value, length, dataType, aFormat, buffer, offset):
        frmByte = '=B'
        if Parser.network: 
            frmByte = '!B'
        struct.pack_into(frmByte, buffer, offset, dataType)
        offset = offset + struct.calcsize(frmByte)
        
        frmInt = '=i'
        if Parser.network: 
            frmInt = '!i'
        struct.pack_into(frmInt, buffer, offset, length)
        offset = offset + struct.calcsize(frmInt)
            
        if value is None:
            isEmpty = 0
            struct.pack_into(frmByte, buffer, offset, isEmpty)
            offset = offset + struct.calcsize(frmByte)
        else:
            if length > 0:
                isEmpty = 1
                frm = aFormat.format(length)
                struct.pack_into(frmByte, buffer, offset, isEmpty)
                offset = offset + struct.calcsize(frmByte)
                struct.pack_into(frm, buffer, offset, *value)
                offset = offset + struct.calcsize(frm)
            else:
                isEmpty = 0
                struct.pack_into(frmByte, buffer, offset, isEmpty)
                offset = offset + struct.calcsize(frmByte)
        return offset
    
    def deserialize_array(self, dataType, aFormat, buffer, offset):
        frmByte = '=B'
        if Parser.network: 
            frmByte = '!B'
        t, = struct.unpack_from(frmByte, buffer, offset)
        offset = offset + struct.calcsize(frmByte)
        if t != dataType:
            raise CSynException('Failed deserialize array. Incorrect data type')
                
        frmInt = '=i'
        if Parser.network: 
            frmInt = '!i'
        length, = struct.unpack_from(frmInt, buffer, offset)
        offset = offset + struct.calcsize(frmInt)
        if length < 0:
            raise CSynException('Failed deserialize array. Incorrect array length')
        
        array = []
        isEmpty, = struct.unpack_from(frmByte, buffer, offset)
        offset = offset + struct.calcsize(frmByte)
        if length > 0 and isEmpty != 0 :
            frm = aFormat.format(length)
            array = list(struct.unpack_from(frm, buffer, offset))
            offset = offset + struct.calcsize(frm)

        return (offset, length, array)
    
    def get_byte_array_size(self, value):
        frm = '={0}B'
        if Parser.network: 
            frm = '!{0}B'
        return self.get_array_size(value, frm)
     
    def serialize_byte_array(self, value, length, buffer, offset):
        frm = '={0}B'
        if Parser.network: 
            frm = '!{0}B'
        return self.serialize_array(value, length, DataType.type_byte_array, frm, buffer, offset)
    
    def deserialize_byte_array(self, buffer, offset):
        frm = '={0}B'
        if Parser.network: 
            frm = '!{0}B'
        return self.deserialize_array(DataType.type_byte_array, frm, buffer, offset)
    
    def get_int_array_size(self, value):
        frm = '={0}i'
        if Parser.network: 
            frm = '!{0}i'
        return self.get_array_size(value, frm)
      
    def serialize_int_array(self, value, length, buffer, offset):
        frm = '={0}i'
        if Parser.network: 
            frm = '!{0}i'
        return self.serialize_array(value, length, DataType.type_int_array, frm, buffer, offset)
    
    def deserialize_int_array(self, buffer, offset):
        frm = '={0}i'
        if Parser.network: 
            frm = '!{0}i'
        return self.deserialize_array(DataType.type_int_array, frm, buffer, offset)
    
    def get_long_array_size(self, value):
        frm = '={0}q'
        if Parser.network: 
            frm = '!{0}q'
        return self.get_array_size(value, frm)
    
    def serialize_long_array(self, value, length, buffer, offset):
        frm = '={0}q'
        if Parser.network: 
            frm = '!{0}q'
        return self.serialize_array(value, length, DataType.type_long_array, frm, buffer, offset)
     
    def deserialize_long_array(self, buffer, offset):
        frm = '={0}q'
        if Parser.network: 
            frm = '!{0}q'
        return self.deserialize_array(DataType.type_long_array, frm, buffer, offset)
     
    def get_float_array_size(self, value):
        frm = '={0}f'
        if Parser.network: 
            frm = '!{0}f'
        return self.get_array_size(value, frm)
    
    def serialize_float_array(self, value, length, buffer, offset):
        frm = '={0}f'
        if Parser.network: 
            frm = '!{0}f'
        return self.serialize_array(value, length, DataType.type_float_array, frm, buffer, offset)
    
    def deserialize_float_array(self, buffer, offset):
        frm = '={0}f'
        if Parser.network: 
            frm = '!{0}f'
        return self.deserialize_array(DataType.type_float_array, frm, buffer, offset)
    
    def get_double_array_size(self, value):
        frm = '={0}d'
        if Parser.network: 
            frm = '!{0}d'
        return self.get_array_size(value, frm)
    
    def serialize_double_array(self, value, length, buffer, offset):
        frm = '={0}d'
        if Parser.network: 
            frm = '!{0}d'
        return self.serialize_array(value, length, DataType.type_double_array, frm, buffer, offset)
    
    def deserialize_double_array(self, buffer, offset):
        frm = '={0}d'
        if Parser.network: 
            frm = '!{0}d'
        return self.deserialize_array(DataType.type_double_array, frm, buffer, offset)
    
    def get_string_size(self, value):
        frm = '=B'
        if Parser.network: 
            frm = '!B'
        sz = struct.calcsize(frm)
        frm = '=i'
        if Parser.network: 
            frm = '!i'
        sz = sz + struct.calcsize(frm)
        length = len(value)
        if length > 0:
            frm = '={0}B'
            if Parser.network:
                frm = '!{0}B'
            sz = sz + struct.calcsize(frm.format(length))
        return sz
     
    def serialize_string(self, value, buffer, offset):
        frmByte = '=B'
        if Parser.network: 
            frmByte = '!B'
        struct.pack_into(frmByte, buffer, offset, DataType.type_string)
        offset = offset + struct.calcsize(frmByte)
        length = len(value)
        frmInt = '=i'
        if Parser.network: 
            frmInt = '!i'
        struct.pack_into(frmInt, buffer, offset, length)
        offset = offset + struct.calcsize(frmInt)
            
        if length > 0:
            aFormat = '={0}B'
            if Parser.network: 
                aFormat = '!{0}B'
            frm = aFormat.format(length)
            bvalue = bytes(value, "utf-8")
            struct.pack_into(frm, buffer, offset, *bvalue)
            offset = offset + struct.calcsize(frm)
        return offset
        
    def deserialize_string(self, buffer, offset, no_type_byte = False):
        frmByte = '=B'
        if Parser.network: 
            frmByte = '!B'
        if not no_type_byte:
            t, = struct.unpack_from(frmByte, buffer, offset)
            offset = offset + struct.calcsize(frmByte)
            if t != DataType.type_string:
                raise CSynException('Failed deserialize array. Incorrect data type')
        frmInt = '=i'
        if Parser.network: 
            frmInt = '!i'
        length, = struct.unpack_from(frmInt, buffer, offset)
        offset = offset + struct.calcsize(frmInt)
        if length < 0:
            raise CSynException('Failed deserialize string. Incorrect string length')
        string = ''
        if length > 0:
            barray = bytearray(length)
            for i in range(length):
                v, = struct.unpack_from(frmByte, buffer, offset)
                offset = offset + struct.calcsize(frmByte)
                barray[i] = v
            string = barray.decode('utf-8')
        return (offset, string)

##
# class JobManager execute Csyn service commands
#      
class JobManager:
    
    ##
    # JobManager constructor.
    # @param url the Csyn service url
    # @param user the Csyn service admin user name
    # @param password the Csyn service admin password
    # @param request_timeout the Csyn service timeout
    #
    
    def __init__(self, url, user=None, password=None, request_timeout=60):
        if url is None:
            raise CSynException('Job manager url is None')
        self.url = url
        self.user = user
        self.password = password
        self.request_timeout = request_timeout

    ##
	# Get list of available GPU
	# @return list of Device objects
	#
     
    def get_device_list(self):
        buffer = None
        try:
            list_url = self.url + '/binary/device_list'
            if self.url.endswith('/'):
                list_url = self.url + 'binary/device_list'
            request = urllib.request.Request(list_url,  method='GET')
            buffer = urllib.request.urlopen(request, timeout = self.request_timeout).read()
        except urllib.request.HTTPError as e:
            raise CSynException('Get device list request failed. Error: {0}'.format(str(e)))
        except urllib.request.URLError as e:
            raise CSynException('Get device list request failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Get device list request unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Get device list request unexpected exception')
        
        response = Response()
        try:
            offset = 0
            response.deserialize(buffer, offset)
        except struct.error as e:
            raise CSynException('Get device list request failed. Response deserialize error: {0}'.format(e))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Get device list request failed. Response deserialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Get device list request failed. Response deserialize unexpected exception')
            
        if response.status != 0:
            raise CSynException('Get device list request failed. Error: {0}'.format(response.error))

        return response.entity

	##
	# Get list of Module objects
	# @return list of Module objects
	#

    def get_module_list(self):
        buffer = None
        try:
            list_url = self.url + '/binary/module_list'
            if self.url.endswith('/'):
                list_url = self.url + 'binary/module_list'
            request = urllib.request.Request(list_url, method='GET')
            buffer = urllib.request.urlopen(request, timeout = self.request_timeout).read()
        except urllib.request.HTTPError as e:
            raise CSynException('Get module list request failed. Error: {0}'.format(str(e)))
        except urllib.request.URLError as e:
            raise CSynException('Get module list request failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Get module list request unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Get module list request unexpected exception')
        
        response = Response()
        try:
            offset = 0
            response.deserialize(buffer, offset)
        except struct.error as e:
            raise CSynException('Get module list request failed. Response deserialize error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Get module list request failed. Response deserialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Get module list request failed. Response deserialize unexpected exception')
            
        if response.status != 0:
            raise CSynException('Get module list request failed. Error: {0}'.format(response.error))
        return response.entity

    ##
	# Get list of Kernel objects
	# @param moduleName the name of module 
	# @param moduleVersion the version of  module 
    # @param moduleType the type of module 
	# @return list of Kernel objects
	#

    def get_kernel_list(self, moduleName, moduleVersion, moduleType):
        buffer = None
        if moduleName is None:
            raise CSynException('Get kernel list request failed. Module name is None')
        if moduleVersion is None:
            raise CSynException('Get kernel list request failed. Module version is None')
        if moduleType is None:
            raise CSynException('Get kernel list request failed. Module type is None')

        try:
            list_url = self.url + '/binary/kernel_list' 
            if self.url.endswith('/'):
                list_url = self.url + 'binary/kernel_list'
            urllib.parse.quote(moduleName)
            urllib.parse.quote(moduleVersion)
            
            list_url = list_url + '?module=' + moduleName +'&moduleVersion=' + moduleVersion +'&moduleType=' + str(moduleType)
            request = urllib.request.Request(list_url, method='GET')
            buffer = urllib.request.urlopen(request, timeout = self.request_timeout).read()
        except urllib.request.HTTPError as e:
            raise CSynException('Get kernel list request failed. Error: {0}'.format(str(e)))
        except urllib.request.URLError as e:
            raise CSynException('Get kernel list request failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Get kernel list request unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Get kernel list request unexpected exception')
        
        response = Response()
        try:
            offset = 0
            response.deserialize(buffer, offset)
        except struct.error as e:
            raise CSynException('Get kernel list request failed. Response deserialize error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Get kernel list request failed. Response deserialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Get kernel list request failed. Response deserialize unexpected exception')
            
        if response.status != 0:
            raise CSynException('Get kernel list request failed. Error: {0}'.format(response.error))
        return response.entity
 
	##
	# Get Kernel object
	# @param moduleName the name of module
	# @param moduleVersion the version of module 
    # @param moduleType the type of module 
	# @param kernelName the kernel name
	# @return Kernel object
	#
                
    def get_kernel(self, moduleName, moduleVersion, moduleType, kernelName):
        buffer = None
        if moduleName is None:
            raise CSynException('Get kernel request failed. Module name is None')
        if moduleVersion is None:
            raise CSynException('Get kernel request failed. Module version is None')
        if moduleType is None:
            raise CSynException('Get kernel request failed. Module type is None')
        if kernelName is None:
            raise CSynException('Get kernel request failed. Kernel name is None')
        try:
            kernel_url = self.url + '/binary/kernel'
            if self.url.endswith('/'):
                kernel_url = self.url + 'binary/kernel'
            urllib.parse.quote(moduleName)
            urllib.parse.quote(moduleVersion)
            urllib.parse.quote(kernelName)
            
            kernel_url = kernel_url + '?module=' + moduleName +'&moduleVersion=' + moduleVersion +'&moduleType=' + str(moduleType) + '&kernel=' + kernelName
            request = urllib.request.Request(kernel_url, method='GET')
            buffer = urllib.request.urlopen(request, timeout = self.request_timeout).read()
        except urllib.request.HTTPError as e:
            raise CSynException('Get kernel request failed. Error: {0}'.format(str(e)))
        except urllib.request.URLError as e:
            raise CSynException('Get kernel request failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Get kernel request unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Get kernel request unexpected exception')

        response = Response()
        try:
            offset = 0
            response.deserialize(buffer, offset)
        except struct.error as e:
            raise CSynException('Get kernel request failed. Response deserialize error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Get kernel request failed. Response deserialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Get kernel request failed. Response deserialize unexpected exception')
            
        if response.status != 0:
            raise CSynException('Get kernel request failed. Error: {0}'.format(response.error))
        return response.entity
 
 

	##
	# Execute Job
	# @param job the Job object
	#
           
    def run_job(self, job):
        buffer = None
        if job is None:
            raise CSynException('Run job request failed.  Job is None')

        try:
            job.validate()
            jobLength = job.get_size()
            buffer = bytearray(jobLength)
            offset = 0
            job.serialize(buffer, offset)   
        except struct.error as e:
            raise CSynException('Job serialize failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Job serialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Job serialize unexpected exception')
                
        try:
            list_url = self.url + '/binary/run_job'
            if self.url.endswith('/'):
                list_url = self.url + 'binary/run_job'
            request = urllib.request.Request(list_url, data=buffer, headers={'Content-Type': 'application/octet-stream'},  method='POST')
            buffer = urllib.request.urlopen(request, timeout = self.request_timeout).read()
        except urllib.request.HTTPError as e:
            raise CSynException('Run job request failed. Error: {0}'.format(str(e)))
        except urllib.request.URLError as e:
            raise CSynException('Run job request failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Run job request unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Run job request unexpected exception')
        
        response = Response()
        try:
            offset = 0
            response.deserialize(buffer, offset)
        except struct.error as e:
            raise CSynException('Run job request failed. Response deserialize error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Run job request failed. Response deserialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Run job request failed. Response deserialize unexpected exception')
        
        if response.status != 0:
            raise CSynException('Run job request failed. Error: {0}'.format(response.error))
        return response.entity

    
    ##
	# Execute Job Async
	# @param job the Job object
	#
           
    def run_job_async(self, job):
        buffer = None
        if job is None:
            raise CSynException('Run job async request failed.  Job is None')

        try:
            job.validate()
            jobLength = job.get_size()
            buffer = bytearray(jobLength)
            offset = 0
            job.serialize(buffer, offset)   
        except struct.error as e:
            raise CSynException('Job serialize failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Job serialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Job serialize unexpected exception')
                
        try:
            list_url = self.url + '/binary/run_job_async'
            if self.url.endswith('/'):
                list_url = self.url + 'binary/run_job_async'
            request = urllib.request.Request(list_url, data=buffer, headers={'Content-Type': 'application/octet-stream'},  method='POST')
            buffer = urllib.request.urlopen(request, timeout = self.request_timeout).read()
        except urllib.request.HTTPError as e:
            raise CSynException('Run job async request failed. Error: {0}'.format(str(e)))
        except urllib.request.URLError as e:
            raise CSynException('Run job async request failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Run job async request unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Run job async request unexpected exception')
        
        response = Response()
        try:
            offset = 0
            response.deserialize(buffer, offset)
        except struct.error as e:
            raise CSynException('Run job async request failed. Response deserialize error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Run job async request failed. Response deserialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Run job async request failed. Response deserialize unexpected exception')
        
        if response.status != 0:
            raise CSynException('Run job async request failed. Error: {0}'.format(response.error))
        return response.entity

    
    ##
	# Get Job Result
	# @param uuid the Job UUID
	#
           
    def get_job_result(self, uuid):
        buffer = None
        if uuid is None:
            raise CSynException('Get job result request failed. UUID is None')
        try:
            result_url = self.url + '/binary/job_result'
            if self.url.endswith('/'):
                result_url = self.url + 'binary/job_result'
            urllib.parse.quote(uuid)
             
            result_url = result_url + '?uuid=' + uuid
            request = urllib.request.Request(result_url, method='GET')
            buffer = urllib.request.urlopen(request, timeout = self.request_timeout).read()
        except urllib.request.HTTPError as e:
            raise CSynException('Get job result request failed. Error: {0}'.format(str(e)))
        except urllib.request.URLError as e:
            raise CSynException('Get job result request failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Get job result request unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Get job result request unexpected exception')
        
        response = Response()
        try:
            offset = 0
            response.deserialize(buffer, offset)
        except struct.error as e:
            raise CSynException('Get job result request failed. Response deserialize error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Get job result request failed. Response deserialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Get job result request failed. Response deserialize unexpected exception')
        
        if response.status != 0:
            raise CSynException('Get job result request failed. Error: {0}'.format(response.error))
        return response.entity
   
    ##
	# Get Job Status
	# @param uuid the Job UUID
	#
           
    def get_job_status(self, uuid):
        buffer = None
        if uuid is None:
            raise CSynException('Get job status request failed. UUID is None')
        try:
            status_url = self.url + '/binary/job_status'
            if self.url.endswith('/'):
                status_url = self.url + 'binary/job_status'
            urllib.parse.quote(uuid)
             
            status_url = status_url + '?uuid=' + uuid
            request = urllib.request.Request(status_url, method='GET')
            buffer = urllib.request.urlopen(request, timeout = self.request_timeout).read()
        except urllib.request.HTTPError as e:
            raise CSynException('Get job status request failed. Error: {0}'.format(str(e)))
        except urllib.request.URLError as e:
            raise CSynException('Get job status request failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Get job status request unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Get job status request unexpected exception')
        
        response = Response()
        try:
            offset = 0
            response.deserialize(buffer, offset)
        except struct.error as e:
            raise CSynException('Get job status request failed. Response deserialize error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Get job status request failed. Response deserialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Get job status request failed. Response deserialize unexpected exception')
        
        if response.status != 0:
            raise CSynException('Get job status request failed. Error: {0}'.format(response.error))
        return response.entity


    ##
	# Create/update kernel list
	# @param kernelList the list of Kernel objects
	#
            
    def create_kernel_list(self, kernel_list):
        buffer = None
        if self.user is None:
            raise CSynException('Create kernel list request failed. Job manager user name is None')
        if self.password is None:
            raise CSynException('Create kernel list request failed. Job manager password is None')
        if kernel_list is None:
            raise CSynException('Create kernel list request failed. Kernel list is None')
            
        kernel_list.validate()
        try:
            requestLength = kernel_list.get_size()
            buffer = bytearray(requestLength)
            offset = 0
            kernel_list.serialize(buffer, offset)   
        except struct.error as e:
            raise CSynException('Kernel list serialize failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Kernel list serialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Kernel list serialize unexpected exception')
                    
        try:
            list_url = self.url + '/binary/upload_kernel_list'
            if self.url.endswith('/'):
                list_url = self.url + 'binary/upload_kernel_list'
                
            headers={'Content-Type': 'application/octet-stream'}
            security = SecurityManager(self.user, self.password)
            security.set_credentials(headers)
            
            request = urllib.request.Request(list_url, data=buffer, headers=headers,  method='POST')
            buffer = urllib.request.urlopen(request, timeout = self.request_timeout).read()
        except urllib.request.HTTPError as e:
            raise CSynException('Create kernel list request failed. Error: {0}'.format(str(e)))
        except urllib.request.URLError as e:
            raise CSynException('Create kernel list request failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Create kernel list request failed. Unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Create kernel list request failed. Unexpected exception')
        
        response = Response()
        try:
            offset = 0
            response.deserialize(buffer, offset)
        except struct.error as e:
            raise CSynException('Create kernel list request failed. Response deserialize error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Create kernel list request failed. Response deserialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Create kernel list request failed. Response deserialize unexpected exception')
        
        if response.status != 0:
            raise CSynException('Create kernel list request failed. Error: {0}'.format(response.error))
         
              
	##
	# Remove kernel list
	# @param kernelList the list of Kernel objects
	#
                
    def remove_kernel_list(self, kernel_list):
        buffer = None
        if self.user is None:
            raise CSynException('Remove kernel list request failed. Job manager user name is None')
        if self.password is None:
            raise CSynException('Remove kernel list request failed. Job manager password is None')
        if kernel_list is None:
            raise CSynException('Remove kernel list request failed. Kernel list is None')
            
        kernel_list.validate()
        try:
            requestLength = kernel_list.get_size()
            buffer = bytearray(requestLength)
            offset = 0
            kernel_list.serialize(buffer, offset)   
        except struct.error as e:
            raise CSynException('Kernel list serialize failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Kernel list serialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Kernel list serialize unexpected exception')
                    
        try:
            list_url = self.url + '/binary/remove_kernel_list'
            if self.url.endswith('/'):
                list_url = self.url + 'binary/remove_kernel_list'
                
            headers={'Content-Type': 'application/octet-stream'}
            security = SecurityManager(self.user, self.password)
            security.set_credentials(headers)
            
            request = urllib.request.Request(list_url, data=buffer, headers=headers,  method='POST')
            buffer = urllib.request.urlopen(request, timeout = self.request_timeout).read()
        except urllib.request.HTTPError as e:
            raise CSynException('Remove kernel list request failed. Error: {0}'.format(str(e)))
        except urllib.request.URLError as e:
            raise CSynException('Remove kernel list request failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Remove kernel list request failed. Unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Remove kernel list request failed. Unexpected exception')
            
        response = Response()
        try:
            offset = 0
            response.deserialize(buffer, offset)
        except struct.error as e:
            raise CSynException('Remove kernel list request failed. Response deserialize error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Remove kernel list request failed. Response deserialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Remove kernel list request failed. Response deserialize unexpected exception')
        
        if response.status != 0:
            raise CSynException('Remove kernel list request failed. Error: {0}'.format(response.error))

    ##
	# Remove kernel
	# @param kernel the kernel objects
	#
                
    def remove_kernel(self, kernel):
        buffer = None
        if self.user is None:
            raise CSynException('Remove kernel request failed. Job manager user name is None')
        if self.password is None:
            raise CSynException('Remove kernel request failed. Job manager password is None')
        if kernel is None:
            raise CSynException('Remove kernel request failed. Kernel is None')
            
        kernel.validate()
        try:
            requestLength = kernel.get_size()
            buffer = bytearray(requestLength)
            offset = 0
            kernel.serialize(buffer, offset)   
        except struct.error as e:
            raise CSynException('Kernel serialize failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Kernel serialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Kernel serialize unexpected exception')
                    
        try:
            kernel_url = self.url + '/binary/remove_kernel'
            if self.url.endswith('/'):
                kernel_url = self.url + 'binary/remove_kernel'
                
            headers={'Content-Type': 'application/octet-stream'}
            security = SecurityManager(self.user, self.password)
            security.set_credentials(headers)
            
            request = urllib.request.Request(kernel_url, data=buffer, headers=headers,  method='POST')
            buffer = urllib.request.urlopen(request, timeout = self.request_timeout).read()
        except urllib.request.HTTPError as e:
            raise CSynException('Remove kernel request failed. Error: {0}'.format(str(e)))
        except urllib.request.URLError as e:
            raise CSynException('Remove kernel request failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Remove kernel request failed. Unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Remove kernel request failed. Unexpected exception')
            
        response = Response()
        try:
            offset = 0
            response.deserialize(buffer, offset)
        except struct.error as e:
            raise CSynException('Remove kernel request failed. Response deserialize error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Remove kernel request failed. Response deserialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Remove kernel li request failed. Response deserialize unexpected exception')
        
        if response.status != 0:
            raise CSynException('Remove kernel request failed. Error: {0}'.format(response.error))
        
    ##
	# Remove Module object
	# @param moduleName the name of module
	# @param moduleVersion the version of module
    # @param moduleType the type of module
	#
                
    def remove_module(self, moduleName, moduleVersion, moduleType):
        buffer = None
        if self.user is None:
            raise CSynException('Remove module request failed. Job manager user name is None')
        if self.password is None:
            raise CSynException('Remove module request failed. Job manager password is None')
        if moduleName is None:
            raise CSynException('Remove module request failed. Module name is None')
        if moduleVersion is None:
            raise CSynException('Remove module request failed. Module version is None')
            
        try:
            module_url = self.url + '/binary/remove_module'
            if self.url.endswith('/'):
                module_url = self.url + 'binary/remove_module'
            urllib.parse.quote(moduleName)
            urllib.parse.quote(moduleVersion)
            module_url = module_url + '?module=' + moduleName +'&moduleVersion=' + moduleVersion + '&moduleType=' + str(moduleType)
            
            headers={}
            security = SecurityManager(self.user, self.password)
            security.set_credentials(headers)
            
            request = urllib.request.Request(module_url, headers=headers, method='GET')
            buffer = urllib.request.urlopen(request, timeout = self.request_timeout).read()
        except urllib.request.HTTPError as e:
            raise CSynException('Remove module request failed. Error: {0}'.format(str(e)))
        except urllib.request.URLError as e:
            raise CSynException('Remove module request failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Remove module request failed. Unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Remove module request failed. Unexpected exception')
        
        response = Response()
        try:
            offset = 0
            response.deserialize(buffer, offset)
        except struct.error as e:
            raise CSynException('Remove module request failed. Response deserialize error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Remove module request failed. Response deserialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Remove module request failed. Response deserialize unexpected exception')
        
        if response.status != 0:
            raise CSynException('Remove module request failed. Error: {0}'.format(response.error))
        
	##
	# Create/update Module object
	# @param module the module object
	# @param path the compiled module file path
    # @param major Device major revision number
    # @param minor Device minor revision number
	#
            
    def create_module(self, module, path, major = 0, minor = 0):
        buffer = None
        if self.user is None:
            raise CSynException('Create module request failed. Job manager user name is None')
        if self.password is None:
            raise CSynException('Create module request failed. Job manager password is None')
        if module is None:
            raise CSynException('Create module request failed. Module is None')
        if path is None:
            raise CSynException('Create module request failed. Module path is None')
            
        module.validate()
        module_file = ModuleFile(path, major, minor)
        module_file.load_data()

        buffer = None
        offset = 0

        try:
            requestLength = module.get_size() + module_file.get_size()
            buffer = bytearray(requestLength)
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Failed allocate serialize buffer. Unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Failed allocate serialize buffer. Unexpected exception')
        
        try:
            offset = module.serialize(buffer, offset)       
        except struct.error as e:
            raise CSynException('Module serialize failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Module serialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Module serialize unexpected exception')
            
        try:
            offset = module_file.serialize(buffer, offset)       
        except struct.error as e:
            raise CSynException('ModuleFile object serialize failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('ModuleFile object serialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('ModuleFile object serialize unexpected exception')
                    
        try:
            module_url = self.url + '/binary/upload_module'
            if self.url.endswith('/'):
                module_url = self.url + 'binary/upload_module'
            
            headers={'Content-Type': 'application/octet-stream'}
            security = SecurityManager(self.user, self.password)
            security.set_credentials(headers)
            
            request = urllib.request.Request(module_url, data=buffer, headers=headers,  method='POST')
            buffer = urllib.request.urlopen(request, timeout = self.request_timeout).read()
        except urllib.request.HTTPError as e:
            raise CSynException('Create module request failed. Error: {0}'.format(str(e)))
        except urllib.request.URLError as e:
            raise CSynException('Create module request failed. Error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Create module request failed. Unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Create module request failed. Unexpected exception')
            
        response = Response()
        try:
            offset = 0
            response.deserialize(buffer, offset)
        except struct.error as e:
            raise CSynException('Create module request failed. Response deserialize error: {0}'.format(str(e)))
        except:
            se = sys.exc_info()
            if len(se) > 0:
                raise CSynException('Create module request failed. Response deserialize unexpected exception. Error: {0}'.format(str(se[1])))
            else:
                raise CSynException('Create module request failed. Response deserialize unexpected exception')
        
        if response.status != 0:
            raise CSynException('Create cubin module request failed. Error: {0}'.format(response.error))

##
# class Response Csyn service response
#         
class Response:
    ##
	# Response constructor
	#
    def __init__(self):
        self.status = 0
        self.error = ''
        self.entity_type = EntityType.entity_none
        self.entity = None

    ##
	# Validate Response object    
    def validate(self):
        if self.entity_type != EntityType.entity_none and self.entity is None:
            raise CSynException("Failed Response validation. Incorrect entity type")
    ##
	# Get Response object size
    # @return size of Response object
	#     
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_byte_size()
        sz = sz + parser.get_string_size(self.error)
        sz = sz + parser.get_byte_size()
        if self.entity_type != EntityType.entity_none and self.entity is not None:
            sz = sz + self.entity.get_size()
        return sz

    ##
	# Serialize Response object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#      
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_byte(self.status, buffer, offset)
        offset = parser.serialize_string(self.error, buffer, offset)
        offset = parser.serialize_byte(self.entity_type, buffer, offset)
        if self.entity_type != EntityType.entity_none and self.entity is not None:
            offset = self.entity.serialize(buffer, offset)
        return offset

    ##
	# Deserialize Response object
    # @param buffer deserialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#      
    def deserialize(self, buffer, offset):
        parser = Parser()
        offset, self.status = parser.deserialize_byte(buffer, offset)
        offset, self.error = parser.deserialize_string(buffer, offset)
        offset, self.entity_type = parser.deserialize_byte(buffer, offset)
        if self.entity_type == EntityType.entity_device:
            self.entity = Device()
            offset = self.entity.deserialize(buffer, offset)
        elif self.entity_type == EntityType.entity_device_list:
            self.entity = DeviceList()
            offset = self.entity.deserialize(buffer, offset)
        elif self.entity_type == EntityType.entity_job_result:
            self.entity = JobResult()
            offset = self.entity.deserialize(buffer, offset)
        elif self.entity_type == EntityType.entity_job_status:
            self.entity = JobStatus()
            offset = self.entity.deserialize(buffer, offset)
        elif self.entity_type == EntityType.entity_kernel:
            self.entity = Kernel('','','',0)
            offset = self.entity.deserialize(buffer, offset)
        elif self.entity_type == EntityType.entity_kernel_list:
            self.entity = KernelList()
            offset = self.entity.deserialize(buffer, offset)
        elif self.entity_type == EntityType.entity_module:
            self.entity = Module('','',0)
            offset = self.entity.deserialize(buffer, offset)
        elif self.entity_type == EntityType.entity_module_list:
            self.entity = ModuleList()
            offset = self.entity.deserialize(buffer, offset)
            
    ## @var status

    ## @var error 

    ## @var enentity_type

    ## @var entity 
    # CSyn server response 

##
# class Device defines GPU properties
# 
class Device:
    ##
	# Device constructor
	# @param id device id
	#
    def __init__(self, id = 0):
        self.ip_address = ''
        self.port = 0
        self.id = id
        self.name = ''
        self.major = 0
        self.minor = 0
        self.total_global_mem = 0
        self.multi_processor_count = 0
        self.clock_rate = 0
        self.total_const_mem = 0
        self.shared_mem_per_block = 0
        self.warp_size = 0
        self.max_threads_per_multi_processor = 0
        self.max_threads_per_block = 0
        self.regs_per_block = 0
        self.max_threads_dim_x = 0
        self.max_threads_dim_y = 0
        self.max_threads_dim_z = 0
        self.max_grid_size_x = 0
        self.max_grid_size_y = 0
        self.max_grid_size_z = 0
        self.device_overlap = 0
        self.async_engine_count = 0
        self.kernel_exec_timeout_enabled = 0
        self.integrated = 0
        self.can_map_host_memory = 0
        self.concurrent_kernels = 0

    ##
	# Get Device object size
    # @return size of Device object
	#          
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_string_size(self.ip_address)
        sz = sz + parser.get_string_size(self.name)
        sz = sz + parser.get_int_size() * 22
        sz = sz + parser.get_long_size() * 3
        return sz
    
    ##
	# Validate Device object
	#  
    def validate(self):
        if self.ip_address is None:
            raise CSynException("Failed device validation. Device host name is none")
        if self.name is None:
            raise CSynException("Failed device validation. Device name is none")
 
    ##
	# Serialize Device object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#   
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.ip_address, buffer, offset)
        offset = parser.serialize_int(self.port, buffer, offset)
        offset = parser.serialize_int(self.id, buffer, offset)
        offset = parser.serialize_string(self.name, buffer, offset)
        offset = parser.serialize_int(self.major, buffer, offset)
        offset = parser.serialize_int(self.minor, buffer, offset)
        offset = parser.serialize_long(self.total_global_mem, buffer, offset)
        offset = parser.serialize_long(self.multi_processor_count, buffer, offset)
        offset = parser.serialize_int(self.clock_rate, buffer, offset)
        offset = parser.serialize_long(self.total_const_mem, buffer, offset)
        offset = parser.serialize_long(self.shared_mem_per_block, buffer, offset)
        offset = parser.serialize_int(self.warp_size, buffer, offset)
        offset = parser.serialize_int(self.max_threads_per_multi_processor, buffer, offset)
        offset = parser.serialize_int(self.max_threads_per_block, buffer, offset)
        offset = parser.serialize_int(self.regs_per_block, buffer, offset)
        offset = parser.serialize_int(self.max_threads_dim_x, buffer, offset)
        offset = parser.serialize_int(self.max_threads_dim_y, buffer, offset)
        offset = parser.serialize_int(self.max_threads_dim_z, buffer, offset)
        offset = parser.serialize_int(self.max_grid_size_x, buffer, offset)
        offset = parser.serialize_int(self.max_grid_size_y, buffer, offset)
        offset = parser.serialize_int(self.max_grid_size_z, buffer, offset)
        offset = parser.serialize_int(self.device_overlap, buffer, offset)
        offset = parser.serialize_int(self.async_engine_count, buffer, offset)
        offset = parser.serialize_int(self.kernel_exec_timeout_enabled, buffer, offset)
        offset = parser.serialize_int(self.integrated, buffer, offset)
        offset = parser.serialize_int(self.can_map_host_memory, buffer, offset)
        offset = parser.serialize_int(self.concurrent_kernels, buffer, offset)
        return offset 

    ##
	# Deserialize Device object
    # @param buffer deserialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#        
    def deserialize(self, buffer, offset):
        parser = Parser()
        offset, self.ip_address = parser.deserialize_string(buffer, offset)
        offset, self.port = parser.deserialize_int(buffer, offset)
        offset, self.id = parser.deserialize_int(buffer, offset)
        offset, self.name = parser.deserialize_string(buffer, offset)
        offset, self.major = parser.deserialize_int(buffer, offset)
        offset, self.minor = parser.deserialize_int(buffer, offset)
        offset, self.total_global_mem = parser.deserialize_long(buffer, offset)
        offset, self.multi_processor_count = parser.deserialize_long(buffer, offset)
        offset, self.clock_rate = parser.deserialize_int(buffer, offset)
        offset, self.total_const_mem = parser.deserialize_long(buffer, offset)
        offset, self.shared_mem_per_block = parser.deserialize_long(buffer, offset)
        offset, self.warp_size = parser.deserialize_int(buffer, offset)
        offset, self.max_threads_per_multi_processor = parser.deserialize_int(buffer, offset)
        offset, self.max_threads_per_block = parser.deserialize_int(buffer, offset)
        offset, self.regs_per_block = parser.deserialize_int(buffer, offset)
        offset, self.max_threads_dim_x = parser.deserialize_int(buffer, offset)
        offset, self.max_threads_dim_y = parser.deserialize_int(buffer, offset)
        offset, self.max_threads_dim_z = parser.deserialize_int(buffer, offset)
        offset, self.max_grid_size_x = parser.deserialize_int(buffer, offset)
        offset, self.max_grid_size_y = parser.deserialize_int(buffer, offset)
        offset, self.max_grid_size_z = parser.deserialize_int(buffer, offset)
        offset, self.device_overlap = parser.deserialize_int(buffer, offset)
        offset, self.async_engine_count = parser.deserialize_int(buffer, offset)
        offset, self.kernel_exec_timeout_enabled = parser.deserialize_int(buffer, offset)
        offset, self.integrated = parser.deserialize_int(buffer, offset)
        offset, self.can_map_host_memory = parser.deserialize_int(buffer, offset)
        offset, self.concurrent_kernels = parser.deserialize_int(buffer, offset)
        return offset
        
    def print_device(self):
        print('Id: {0}'.format(self.id))
        print('Host Name: {0}'.format(self.ip_address))
        print('Port: {0}'.format(self.port))
        print('Name: {0}'.format(self.name))
        print('Major: {0}'.format(self.major))
        print('Minor: {0}'.format(self.minor))

 
    ## @var ip_address 
    # Device engine ip address
	
	## @var port 
    # Device engine port

    ## @var id 
    # Device id

    ## @var name 
    # Device name

    ## @var major 
    # Device major revision number

    ## @var minor 
    # Device minor revision number

    ## @var total_global_mem 
    # Device total global memory

    ## @var multi_processor_count 
    # number of Device multiprocessors

    ## @var clock_rate 
    # Device clock rate

    ## @var total_const_mem 
    # Device total const memory

    ## @var shared_mem_per_block 
    # Device shared memory per block

    ## @var warp_size 
    # Device warp size

    ## @var max_threads_per_multi_processor 
    # Device max threads per multiprocessor

    ## @var max_threads_per_block 
    # Device max threads per block

    ## @var regs_per_block 
    # Device registers per block 

    ## @var max_threads_dim_x 
    # Device max threads dimension X

    ## @var max_threads_dim_y 
    # Device max threads dimension Y

    ## @var max_threads_dim_z 
    # Device max threads dimension Z

    ## @var max_grid_size_x 
    # Device max threads grid X

    ## @var max_grid_size_y 
    # Device max threads grid Y

    ## @var max_grid_size_z 
    # Device max threads grid Z

    ## @var device_overlap 
    # Device device overlap

    ## @var kernel_exec_timeout_enabled 
    # Device kernel execution timeout enabled

    ## @var integrated

    ## @var can_map_host_memory 
    # Device can map host memory

    ## @var concurrent_kernels 
    # Device concurrent kernels

    
    
##
# class DeviceList contains list of device objects
# 
class DeviceList:
    ##
	# DeviceList constructor
	#
    def __init__(self):
         self.device_list = []

    ##
	# Validate DeviceList object    
    def validate(self):
        if self.device_list is None:
            raise CSynException("Failed device list validation. Device list is empty")
        if not isinstance(self.device_list, list):
            raise CSynException("Failed device list validation. Device list is not list type")
        for device in self.device_list:
            device.validate()
 
    ##
	# Get DeviceList object size
    # @return size of DeviceList object
	#     
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_int_size()
        if self.device_list is not None:
            for device in self.device_list:
                sz = sz + device.get_size()
        return sz

    ##
	# Serialize DeviceList object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#      
    def serialize(self, buffer, offset):
        parser = Parser()
        device_list_sz = 0
        if self.device_list is not None:
            device_list_sz = len(self.device_list)
        offset = parser.serialize_int(device_list_sz, buffer, offset)
        if device_list_sz != 0:
            for device in self.device_list:
                offset = device.serialize(buffer, offset)
        return offset

    ##
	# Deserialize DeviceList object
    # @param buffer deserialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#      
    def deserialize(self, buffer, offset):
        parser = Parser()
        offset, device_list_sz = parser.deserialize_int(buffer, offset)
        if device_list_sz > 0:
            for i in range(device_list_sz):
                device = Device(i)
                offset = device.deserialize(buffer, offset)
                self.device_list.append(device)
        return offset
            
    def print_device_list(self):
        if self.device_list is not None:
            for device in self.device_list:
                device.print_device()

    ## @var device_list 
    # List of Device objects

##
# class Module defines module properties
#             
class Module:
    ##
	# Module constructor
    # @param module_name module name
    # @param module_version module version
    # @param module_type module type
    # @param module_description module description
	#
    def __init__(self, module_name, module_version, module_type, module_description = ''):
        self.module_name = module_name
        self.module_version = module_version
        self.module_type = module_type
        self.module_description = module_description

    ##
	# Validate Module object        
    def validate(self):
        if self.module_name is None:
            raise CSynException("Failed module validation. Module name is none")
        if self.module_version is None:
            raise CSynException("Failed module validation. Module version is none")
        if self.module_type is None:
            raise CSynException("Failed module validation. Module type is none")
        if self.module_type < 0 or self.module_type > 4:
            raise CSynException("Failed module validation. Incorrect module type")
                
    ##
	# Get Module object size
    # @return size of Module object
	#               
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_string_size(self.module_name)
        sz = sz + parser.get_string_size(self.module_version)
        sz = sz + parser.get_string_size(self.module_description)
        sz = sz + parser.get_int_size()
        return sz

    ##
	# Serialize Module object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#       
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.module_name, buffer, offset)
        offset = parser.serialize_string(self.module_version, buffer, offset)
        offset = parser.serialize_string(self.module_description, buffer, offset)
        offset = parser.serialize_int(self.module_type, buffer, offset)
        return offset 

    ##
	# Deserialize Module object
    # @param buffer deserialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#       
    def deserialize(self, buffer, offset):
        parser = Parser()
        offset, self.module_name = parser.deserialize_string(buffer, offset)
        offset, self.module_version = parser.deserialize_string(buffer, offset)
        offset, self.module_description = parser.deserialize_string(buffer, offset)
        offset, self.module_type = parser.deserialize_int(buffer, offset)
        return offset
        
    def print_module(self):
        print('Module Name: {0}'.format(self.module_name))
        print('Module Version: {0}'.format(self.module_version))
        print('Module Description: {0}'.format(self.module_description))
        print('Module Type: {0}'.format(self.module_type))
    
    ## @var module_name 
    # Module name

    ## @var module_version 
    # Module version 

    ## @var module_type 
    # Module type

    ## @var module_description 
    # Module description 

##
# class Module contains list of module objects
# 
class ModuleList:
    ##
	# ModuleList constructor
    def __init__(self):
        self.module_list = []

    ##
	# Validate ModuleList object        
    def validate(self):
        if self.module_list is None:
            raise CSynException("Failed module list validation. Module list is empty")
        if not isinstance(self.module_list, list):
            raise CSynException("Failed module list validation. Module list is not list type")
        for module in self.module_list:
            module.validate()
 
    ##
	# Get ModuleList object size
    # @return size of ModuleList object
	#  
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_int_size()
        if self.module_list is not None:
            for module in self.module_list:
                sz = sz + module.get_size()
        return sz

    ##
	# Serialize ModuleList object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#     
    def serialize(self, buffer, offset):
        parser = Parser()
        module_list_sz = 0
        if self.module_list is not None:
            module_list_sz = len(self.module_list)
        offset = parser.serialize_int(module_list_sz, buffer, offset)
        if module_list_sz != 0:
            for module in self.module_list:
                offset = module.serialize(buffer, offset)
        return offset

    ##
	# Deserialize ModuleList object
    # @param buffer deserialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#     
    def deserialize(self, buffer, offset):
        parser = Parser()
        offset, module_list_sz = parser.deserialize_int(buffer, offset)
        for i in range(module_list_sz):
            module = Module('', '', 0, '')
            offset = module.deserialize(buffer, offset)
            self.module_list.append(module)
        return offset
            
    def print_module_list(self):
        if self.module_list is not None:
            for module in self.module_list:
                module.print_module()

    ## @var module_list 
    # List of Module objects

##
# class ModuleFile defines module file
#                 
class ModuleFile:
    ##
	# ModuleFile constructor
    # @param path path to compiled module file
    # @param major Device major revision number
    # @param minor Device minor revision number
    def __init__(self, path, major, minor):
        self.path = path
        self.major = major
        self.minor = minor
        self.data = []

    ##
	# Validate ModuleFile object 
    #      
    def validate(self):
        if self.path is None:
           raise CSynException("Failed module file validation. Path is none")
        if not isinstance(self.data, list):
            raise CSynException("Failed module file validation. Module file path data is not list type")

    ##
	# Get ModuleFile object size
    # @return size of ModuleFile object
	#             
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_string_size(self.path)
        sz = sz + parser.get_int_size() * 2
        sz = sz + parser.get_byte_size()
        sz = sz + parser.get_byte_array_size(self.data)
        return sz

    ##
	# Serialize ModuleFile object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#      
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.path, buffer, offset)
        offset = parser.serialize_int(self.major, buffer, offset)
        offset = parser.serialize_int(self.minor, buffer, offset)
        isEmpty = 0
        if len(self.data) > 0:
            isEmpty = 1
        offset = parser.serialize_byte(isEmpty, buffer, offset)
        offset = parser.serialize_byte_array(self.data, len(self.data), buffer, offset)
        return offset 

    ##
	# Deserialize ModuleFile object
    # @param buffer deserialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#       
    def deserialize(self, buffer, offset):
        parser = Parser()
        offset, self.path = parser.deserialize_string(buffer, offset)
        offset, self.major = parser.deserialize_int(buffer, offset)
        offset, self.minor = parser.deserialize_int(buffer, offset)
        offset, isEmpty = parser.deserialize_byte(buffer, offset)
        if isEmpty != 0:
            offset, length, self.data = parser.deserialize_byte_array(buffer, offset)
        return offset
    
    ##
	# Load data from file
	# 
    def load_data(self):
        df = None
        try:
            df = open(self.path, 'rb')
        except:
            raise CSynException('Failed to opean file: {0}'.format(self.path))
            
        try:
            self.data = list(df.read())
        except:
            raise CSynException('Failed to read data from file: {0}'.format(self.path))
        
    def print_module_file_path(self):
        print('Path: {0}'.format(self.path))
        print('Major: {0}'.format(self.major))
        print('Minor: {0}'.format(self.minor))

    ## @var path 
    # Path to compiled module file

    ## @var major 
    # Device major revision number

    ## @var minor 
    # Device minor revision number

    ## @var data 
    # Module file data
 
     
##
# class Value base class for different value types
#       
class Value:
    ##
	# Value constructor
    #
    def __init__(self):
        pass

    ##
	# Validate Value object 
    #     
    def validate(self):
        pass

    ##
	# Get Value object size
    # @return size of Value object
	#      
    def get_size(self):
        return 0

    ##
	# Serialize Value object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#      
    def serialize(self, buffer, offset):
        return offset

    ##
	# Deserialize Value object
    # @param data_type value data type
    # @param buffer deserialize buffer
    # @param offset buffer offset
    # @return buffer offset and value object
	#  
    @staticmethod     
    def deserialize(data_type, buffer, offset):
        parser = Parser()
        value = None
        if data_type == DataType.type_byte:
            offset, value_name = parser.deserialize_string(buffer, offset)
            offset, data = parser.deserialize_byte(buffer, offset)
            value = ValueByte(data, value_name)
        elif data_type == DataType.type_int:
            offset, value_name = parser.deserialize_string(buffer, offset)
            offset, data = parser.deserialize_int(buffer, offset)
            value = ValueInt(data, value_name)
        elif data_type == DataType.type_long:
            offset, value_name = parser.deserialize_string(buffer, offset)
            offset, data = parser.deserialize_long(buffer, offset)
            value = ValueLong(data, value_name)
        elif data_type == DataType.type_float:
            offset, value_name = parser.deserialize_string(buffer, offset)
            offset, data = parser.deserialize_float(buffer, offset)
            value = ValueFloat(data, value_name)
        elif data_type == DataType.type_double:
            offset, value_name = parser.deserialize_string(buffer, offset)
            offset, data = parser.deserialize_double(buffer, offset)
            value = ValueDouble(data, value_name)
        elif data_type == DataType.type_string:
            offset, value_name = parser.deserialize_string(buffer, offset)
            offset, data = parser.deserialize_string(buffer, offset)
            value = ValueString(data, value_name)
        elif data_type == DataType.type_byte_array:
            offset, value_name = parser.deserialize_string(buffer, offset)
            offset, data_length, data = parser.deserialize_byte_array(buffer, offset)
            value = ValueByteArray(data_length, data, value_name)
        elif data_type == DataType.type_int_array:
            offset, value_name = parser.deserialize_string(buffer, offset)
            offset, data_length, data = parser.deserialize_int_array(buffer, offset)
            value = ValueIntArray(data_length, data, value_name)
        elif data_type == DataType.type_long_array:
            offset, value_name = parser.deserialize_string(buffer, offset)
            offset, data_length, data = parser.deserialize_long_array(buffer, offset)
            value = ValueLongArray(data_length, data, value_name)
        elif data_type == DataType.type_float_array:
            offset, value_name = parser.deserialize_string(buffer, offset)
            offset, data_length, data = parser.deserialize_float_array(buffer, offset)
            value = ValueFloatArray(data_length, data, value_name)
        elif data_type == DataType.type_double_array:
            offset, value_name = parser.deserialize_string(buffer, offset)
            offset, data_length, data = parser.deserialize_double_array(buffer, offset)
            value = ValueDoubleArray(data_length, data, value_name)
        else:
            raise CSynException("Failed deserialize parameter value. Incorrect data type")
        return offset, value
        
    def print_value(self):
        pass

##
# class ValueByte defines parameter value type of byte
#     
class ValueByte(Value):
    ##
	# ValueByte constructor
    # @param data ValueByte data
    # @param value_name value object name
    #
    def __init__(self, data, value_name = ''):
        self.data_type = DataType.type_byte
        self.data = data
        self.value_name = value_name

    ##
	# Validate ValueByte object 
    #     
    def validate(self):
       if self.data_type != DataType.type_byte:
           raise CSynException("Failed parameter value validation. Incorrect data type")

    ##
	# Get ValueByte object size
    # @return size of ValueByte object
	#     
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_byte_size() 
        sz = sz + parser.get_string_size(self.value_name)
        return sz

    ##
	# Serialize ValueByte object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#     
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.value_name, buffer, offset)
        offset = parser.serialize_byte(self.data, buffer, offset)
        return offset

    def print_value(self):
        print('Data: {0}'.format(self.data))

    ## @var data 
    # ValueByte data

    ## @var value_name 
    # Value name

##
# class ValueInt defines parameter value type of int
#         
class ValueInt(Value):
    ##
	# ValueInt constructor
    # @param data ValueInt data
    # @param value_name value object name
    #
    def __init__(self, data, value_name = ''):
        self.data_type = DataType.type_int
        self.data = data
        self.value_name = value_name

    ##
	# Validate ValueInt object 
    #   
    def validate(self):
        if self.data_type != DataType.type_int:
           raise CSynException("Failed parameter value validation. Incorrect data type")

    ##
	# Get ValueInt object size
    # @return size of ValueInt object
	#     
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_int_size() 
        sz = sz + parser.get_string_size(self.value_name)
        return sz

    ##
	# Serialize ValueInt object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#     
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.value_name, buffer, offset)
        offset = parser.serialize_int(self.data, buffer, offset)
        return offset
        
    def print_value(self):
         print('Data: {0}'.format(self.data))
    
    ## @var data 
    # ValueInt data

    ## @var value_name 
    # Value name

##
# class ValueLong defines parameter value type of long
#          
class ValueLong(Value):
    ##
	# ValueLong constructor
    # @param data ValueInt data
    # @param value_name value object name
    #
    def __init__(self, data, value_name = ''):
        self.data_type = DataType.type_long
        self.data = data
        self.value_name = value_name

    ##
	# Validate ValueLong object 
    #    
    def validate(self):
        if self.data_type != DataType.type_long:
           raise CSynException("Failed parameter value validation. Incorrect data type")
    
    ##
	# Get ValueLong object size
    # @return size of ValueLong object
	#
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_long_size() 
        sz = sz + parser.get_string_size(self.value_name)
        return sz

    ##
	# Serialize ValueLong object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#    
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.value_name, buffer, offset)
        offset = parser.serialize_long(self.data, buffer, offset)
        return offset
        
    def print_value(self):
         print('Data: {0}'.format(self.data))

    ## @var data 
    # ValueLong data

    ## @var value_name 
    # Value name

##
# class ValueFloat defines parameter value type of float
# 
class ValueFloat(Value):
    ##
	# ValueFloat constructor
    # @param data ValueInt data
    # @param value_name value object name
    #
    def __init__(self, data, value_name = ''):
        self.data_type = DataType.type_float
        self.data = data
        self.value_name = value_name

    ##
	# Validate ValueFloat object 
    #   
    def validate(self):
        if self.data_type != DataType.type_float:
           raise CSynException("Failed parameter value validation. Incorrect data type")

    ##
	# Get ValueFloat object size
    # @return size of ValueFloat object
	#    
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_float_size() 
        sz = sz + parser.get_string_size(self.value_name)
        return sz

    ##
	# Serialize ValueFloat object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#     
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.value_name, buffer, offset)
        offset = parser.serialize_float(self.data, buffer, offset)
        return offset
          
    def print_value(self):
        print('Data: {0}'.format(self.data))
    
    ## @var data 
    # ValueFloat data

    ## @var value_name 
    # Value name

##
# class ValueDouble defines parameter value type of double
#          
class ValueDouble(Value):
    ##
	# ValueDouble constructor
    # @param data ValueInt data
    # @param value_name value object name
    #
    def __init__(self, data, value_name = ''):
        self.data_type = DataType.type_double
        self.data = data
        self.value_name = value_name

    ##
	# Validate ValueDouble object 
    #   
    def validate(self):
        if self.data_type != DataType.type_double:
           raise CSynException("Failed parameter value validation. Incorrect data type")

    ##
	# Get ValueDouble object size
    # @return size of ValueDouble object
	#     
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_double_size() 
        sz = sz + parser.get_string_size(self.value_name)
        return sz

    ##
	# Serialize ValueDouble object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#      
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.value_name, buffer, offset)
        offset = parser.serialize_double(self.data, buffer, offset)
        return offset
          
    def print_value(self):
         print('Data: {0}'.format(self.data))
    
    ## @var data 
    # ValueDouble data

    ## @var value_name 
    # Value name

##
# class ValueString defines parameter value type of string
#   
class ValueString(Value):
    ##
	# ValueString constructor
    # @param data ValueInt data
    # @param value_name value object name
    #
    def __init__(self, data, value_name = ''):
        self.data_type = DataType.type_string
        self.data = data
        self.value_name = value_name

    ##
	# Validate ValueString object 
    #    
    def validate(self):
        if self.data_type != DataType.type_string:
           raise CSynException("Failed parameter value validation. Incorrect data type")
        if self.data is None:
           raise CSynException("Failed validate parameter value. String parameter value data is none")

    ##
	# Get ValueString object size
    # @return size of ValueString object
	#    
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_string_size(self.data) 
        sz = sz + parser.get_string_size(self.value_name)
        return sz

    ##
	# Serialize ValueString object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#     
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.value_name, buffer, offset)
        offset = parser.serialize_string(self.data, buffer, offset)
        return offset
          
    def print_value(self):
         print('Data: {0}'.format(self.data))

    ## @var data 
    # ValueString data

    ## @var value_name 
    # Value name
         
##
# class ValueByteArray defines parameter value type of byte array
#     
class ValueByteArray(Value):
    ##
	# ValueByteArray constructor
    # @param array_length data length
    # @param data ValueByteArray data
    # @param value_name value object name
    #
    def __init__(self, array_length, data = None, value_name = ''):
        self.data_type = DataType.type_byte_array
        self.data = data
        self.array_length = array_length
        self.value_name = value_name

    ##
	# Validate ValueByteArray object 
    #     
    def validate(self):
        if self.data_type != DataType.type_byte_array:
           raise CSynException("Failed parameter value validation. Incorrect data type")
        if self.array_length <= 0:
                raise CSynException("Failed parameter value validation. Incorrect array length")
        if self.data is not None:    
            if type(self.data) is not list:
                raise CSynException("Failed parameter value validation. Data type is not list")

    ##
	# Get ValueByteArray object size
    # @return size of ValueByteArray object
	#     
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_byte_array_size(self.data) 
        sz = sz + parser.get_string_size(self.value_name)
        return sz

    ##
	# Serialize ValueByteArray object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#     
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.value_name, buffer, offset)
        offset = parser.serialize_byte_array(self.data, self.array_length, buffer, offset)
        return offset
        
 
    ## @var data 
    # ValueByteArray data

    ## @var array_length 
    # ValueByteArray data length

    ## @var value_name 
    # Value name

##
# class ValueIntArray defines parameter value type of int array
#           
class ValueIntArray(Value):
    ##
	# ValueIntArray constructor
    # @param array_length data length
    # @param data ValueIntArray data
    # @param value_name value object name
    #
    def __init__(self, array_length, data = None, value_name = ''):
        self.data_type = DataType.type_int_array
        self.data = data
        self.array_length = array_length
        self.value_name = value_name

    ##
	# Validate ValueIntArray object 
    #      
    def validate(self):
        if self.data_type != DataType.type_int_array:
           raise CSynException("Failed parameter value validation. Incorrect data type")
        if self.array_length <= 0:
                raise CSynException("Failed parameter value validation. Incorrect array length")
        if self.data is not None:    
            if type(self.data) is not list:
                raise CSynException("Failed parameter value validation. Data type is not list")

    ##
	# Get ValueIntArray object size
    # @return size of ValueIntArray object
	#        
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_int_array_size(self.data) 
        sz = sz + parser.get_string_size(self.value_name)
        return sz

    ##
	# Serialize ValueIntArray object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#      
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.value_name, buffer, offset)
        offset = parser.serialize_int_array(self.data, self.array_length, buffer, offset)
        return offset

    ## @var data 
    # ValueIntArray data

    ## @var array_length 
    # ValueIntArray data length

    ## @var value_name 
    # Value name

##
# class ValueLongArray defines parameter value type of long array
#     
class ValueLongArray(Value):
    ##
	# ValueLongArray constructor
    # @param array_length data length
    # @param data ValueLongArray data
    # @param value_name value object name
    #
    def __init__(self, array_length, data = None, value_name = ''):
        self.data_type = DataType.type_long_array
        self.data = data
        self.array_length = array_length
        self.value_name = value_name
        
    ##
	# Validate ValueLongArray object 
    #     
    def validate(self):
        if self.data_type != DataType.type_long_array:
           raise CSynException("Failed parameter value validation. Incorrect data type")
        if self.array_length <= 0:
                raise CSynException("Failed parameter value validation. Incorrect array length")
        if self.data is not None:    
            if type(self.data) is not list:
                raise CSynException("Failed parameter value validation. Data type is not list")

    ##
	# Get ValueLongArray object size
    # @return size of ValueLongArray object
	#       
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_long_array_size(self.data) 
        sz = sz + parser.get_string_size(self.value_name)
        return sz

    ##
	# Serialize ValueLongArray object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#      
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.value_name, buffer, offset)
        offset = parser.serialize_long_array(self.data, self.array_length, buffer, offset)
        return offset
     
    ## @var data 
    # ValueLongArray data

    ## @var array_length 
    # ValueLongArray data length

    ## @var value_name 
    # Value name

##
# class ValueFloatArray defines parameter value type of float array
#             
class ValueFloatArray(Value):
    ##
	# ValueFloatArray constructor
    # @param array_length data length
    # @param data ValueFloatArray data
    # @param value_name value object name
    #
    def __init__(self, array_length, data = None, value_name = ''):
        self.data_type = DataType.type_float_array
        self.data = data
        self.array_length = array_length
        self.value_name = value_name
        
    ##
	# Validate ValueFloatArray object 
    #    
    def validate(self):
        if self.data_type != DataType.type_float_array:
           raise CSynException("Failed parameter value validation. Incorrect data type")
        if self.array_length <= 0:
                raise CSynException("Failed parameter value validation. Incorrect array length")
        if self.data is not None:    
            if type(self.data) is not list:
                raise CSynException("Failed parameter value validation. Data type is not list")

    ##
	# Get ValueFloatArray object size
    # @return size of ValueFloatArray object
	#     
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_float_array_size(self.data) 
        sz = sz + parser.get_string_size(self.value_name)
        return sz

    ##
	# Serialize ValueFloatArray object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#     
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.value_name, buffer, offset)
        offset = parser.serialize_float_array(self.data, self.array_length, buffer, offset)
        return offset

    ## @var data 
    # ValueFloatArray data

    ## @var array_length 
    # ValueFloatArray data length

    ## @var value_name 
    # Value name

##
# class ValueDoubleArray defines parameter value type of double array
# 
class ValueDoubleArray(Value):
    ##
	# ValueDoubleArray constructor
    # @param array_length data length
    # @param data ValueDoubleArray data
    # @param value_name value object name
    #
    def __init__(self, array_length, data = None, value_name = ''):
        self.data_type = DataType.type_double_array
        self.data = data
        self.array_length = array_length
        self.value_name = value_name
        
    ##
	# Validate ValueDoubleArray object 
    #      
    def validate(self):
        if self.data_type != DataType.type_double_array:
           raise CSynException("Failed parameter value validation. Incorrect data type")
        if self.array_length <= 0:
                raise CSynException("Failed parameter value validation. Incorrect array length")
        if self.data is not None:    
            if type(self.data) is not list:
                raise CSynException("Failed parameter value validation. Data type is not list")

    ##
	# Get ValueDoubleArray object size
    # @return size of ValueDoubleArray object
	#     
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_double_array_size(self.data) 
        sz = sz + parser.get_string_size(self.value_name)
        return sz

    ##
	# Serialize ValueDoubleArray object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#      
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.value_name, buffer, offset)
        offset = parser.serialize_double_array(self.data, self.array_length, buffer, offset)
        return offset
     
    ## @var data 
    # ValueDoubleArray data

    ## @var array_length 
    # ValueDoubleArray data length

    ## @var value_name 
    # Value name
        
##
# class Parameter defines kernel parameter properties and value
#
class Parameter:
    ##
	# Parameter constructor
    # @param parameter_name Parameter name
    # @param data_type Parameter data type
    # @param parameter_type Parameter type
    # @param order Parameter order
    # @param parameter_description Parameter description
    #
    def __init__(self, parameter_name, data_type, parameter_type, order, parameter_description = ''):
        self.parameter_name = parameter_name
        self.parameter_description = parameter_description
        self.data_type = data_type
        self.parameter_type = parameter_type
        self.order = order
        self.__value = None
        self.global_value = ''

    ##
	# Set Parameter value
    # @param value 
    #     
    def set_value(self, value):
        if(value is not None):
            if(value.data_type != self.data_type):
                raise CSynException("Failed set parameter value. Incorrect value data type")
            self.__value = value
        else:
            self.__value = value
    
    ##
	# Get Parameter value
    # @return Parameter value
	#  
    def get_value(self):
        return self.__value

    ##
	# Validate Parameter object 
    #     
    def validate(self, is_runtime = False):
        if self.data_type != DataType.type_byte and \
           self.data_type != DataType.type_int and \
           self.data_type != DataType.type_long and \
           self.data_type != DataType.type_float and \
           self.data_type != DataType.type_double and \
           self.data_type != DataType.type_string and \
           self.data_type != DataType.type_byte_array and \
           self.data_type != DataType.type_int_array and \
           self.data_type != DataType.type_long_array and \
           self.data_type != DataType.type_float_array and \
           self.data_type != DataType.type_double_array and \
           self.data_type != DataType.type_double_array:
            raise CSynException("Failed parameter validation. Incorrect data type")
        if self.parameter_type != ParameterType.parameter_input and \
           self.parameter_type != ParameterType.parameter_output and \
           self.parameter_type != ParameterType.parameter_input_output:
            raise CSynException("Failed parameter validation. Incorrect parameter type")
            
        if self.parameter_name is None:
            raise CSynException("Failed parameter validation. Parameter name is none")
        if is_runtime:
            if self.__value is not None:
                if self.data_type != self.__value.data_type:
                    raise CSynException("Failed parameter validation. Kernel parameter data type does not match value data type")
                self.__value.validate()

            if self.global_value is not None and len(self.global_value) > 0:
                if self.parameter_type != ParameterType.parameter_input:
                    raise CSynException("Failed parameter validation. Kernel parameter for global value must be type input")

    ##
	# Get Parameter object size
    # @return size of Parameter object
	#          
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_string_size(self.parameter_name)
        sz = sz + parser.get_string_size(self.parameter_description)
        sz = sz + parser.get_int_size()
        sz = sz + parser.get_byte_size()
        sz = sz + parser.get_byte_size()
        sz = sz + parser.get_byte_size()
        sz = sz + parser.get_string_size(self.global_value)
        if self.__value is not None:
             sz = sz + self.__value.get_size()
        return sz

    ##
	# Serialize Parameter object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#     
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.parameter_name, buffer, offset)
        offset = parser.serialize_string(self.parameter_description, buffer, offset)
        offset = parser.serialize_int(self.order, buffer, offset)
        offset = parser.serialize_byte(self.data_type, buffer, offset)
        offset = parser.serialize_byte(self.parameter_type, buffer, offset)
        offset = parser.serialize_string(self.global_value, buffer, offset)
        if self.__value is None:
            isValue = 0
            offset = parser.serialize_byte(isValue, buffer, offset)
        else:
            isValue = 1
            offset = parser.serialize_byte(isValue, buffer, offset)
            offset = self.__value.serialize(buffer, offset)
        return offset

    ##
	# Deserialize Parameter object
    # @param buffer deserialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#     
    def deserialize(self, buffer, offset):
        parser = Parser()
        offset, self.parameter_name = parser.deserialize_string(buffer, offset)
        offset, self.parameter_description = parser.deserialize_string(buffer, offset)
        offset, self.order = parser.deserialize_int(buffer, offset)
        offset, self.data_type = parser.deserialize_byte(buffer, offset)
        offset, self.parameter_type = parser.deserialize_byte(buffer, offset)
        offset, self.global_value = parser.deserialize_string(buffer, offset)
        offset, isValue = parser.deserialize_byte(buffer, offset)
        if isValue > 0:
            offset, value = Value.deserialize(self.data_type, buffer, offset)
            self.__value = value
        return offset
        
    def print_parameter(self):
        print('Parameter Name: {0}'.format(self.parameter_name))
        print('Parameter Description: {0}'.format(self.parameter_description))
        print('Order: {0}'.format(self.order))
        print('Data Type: {0}'.format(self.data_type))
        print('Parameter Type: {0}'.format(self.parameter_type))
        print('Global Value: {0}'.format(self.global_value))
        if self.__value is not None:
            self.__value.print_value()

    ## @var parameter_name 
    # Parameter name

    ## @var parameter_description 
    # Parameter description 

    ## @var data_type 
    # Parameter data type 

    ## @var parameter_type 
    # Parameter type

    ## @var order 
    # Parameter order

    ## @var global_value
    # Name of parameter global value 
        

##
# class Kernel defines kernel parameters and properties
#        
class Kernel:
    ##
	# Kernel constructor
    # @param kernel_name Kernel name
    # @param module Module name
    # @param module_version Module version
    # @param module_type Module type
    # @param kernel_description Kernel description
    #
    def __init__(self, kernel_name, module, module_version, module_type, kernel_description = ''):
        self.kernel_name = kernel_name
        self.kernel_description = kernel_description
        self.module = module
        self.module_version = module_version
        self.module_type = module_type
        self.parameter_list = []

    ##
	# Get Kernel parameter object by name
    # @param name Parameter name
    # @return Parameter object
	#        
    def get_parameter_by_name(self, name):
        if self.parameter_list is not None:
            for parameter in self.parameter_list:
                if parameter.name == name:
                    return parameter
        raise CSynException("Failed to get kernel parameter by name. Can not find parameter with name {0}".format(name))
    
    ##
	# Get Kernel parameter object by order
    # @param order Parameter order
    # @return Parameter object
	#  
    def get_parameter_by_order(self, order):
        if self.parameter_list is not None:
            for parameter in self.parameter_list:
                if parameter.order == order:
                    return parameter
        raise CSynException("Failed to get kernel parameter by order. Can not find parameter with order {0}".format(order))
    
    ##
	# Set Kernel parameter value by parameter name
    # @param name Parameter name
    # @param value Parameter value
	#      
    def set_parameter_value_by_name(self, name, value):
        parameter = self.get_parameter_by_name(name)
        parameter.set_value(value)
 
    
    ##
	# Set Kernel parameter value by parameter order
    # @param order Parameter order
    # @param value Parameter value
	#    
    def set_parameter_value_by_order(self, order, value):
        parameter = self.get_parameter_by_order(order)
        parameter.set_value(value)
  
    ##
	# Set Kernel parameter global value by parameter name
    # @param name Parameter name
    # @param global_value Parameter global value
	#      
    def set_parameter_global_value_by_name(self, name, global_value):
        parameter = self.get_parameter_by_name(name)
        parameter.global_value = global_value
    
    ##
	# Set Kernel parameter global value by parameter order
    # @param order Parameter order
    # @param global_value Parameter global value
	#    
    def set_parameter_global_value_by_order(self, order, global_value):
        parameter = self.get_parameter_by_order(order)
        parameter.global_value = global_value
     
    ##
	# Get Kernel object copy
    # @return Kernel object
	#    
    def get_copy(self):
        kernel = Kernel(kernel_name=self.kernel_name, module=self.module, module_version=self.module_version, module_type=self.module_type, kernel_description=self.kernel_description)
        if self.parameter_list is not None:
            kernel.parameter_list = list(self.parameter_list)
        return kernel
            
    ##
	# Validate Kernel object 
    #      
    def validate(self, is_runtime = False):
        if self.kernel_name is None:
            raise CSynException("Failed kernel validation. Kernel name is none")
        if self.module is None:
            raise CSynException("Failed kernel validation. Module is none")
        if self.module_version is None:
            raise CSynException("Failed kernel validation. Module version is none")
        if self.module_type is None:
            raise CSynException("Failed kernel validation. Module type is none")
        if self.module_type < 0 or self.module_type > 4:
            raise CSynException("Failed kernel validation. Incorrect module type")
        if is_runtime:
            if self.parameter_list is None:
                raise CSynException("Failed kernel validation. Parameter list is empty")
            if not isinstance(self.parameter_list, list):
                raise CSynException("Failed kernel validation. Parameter list is not list type")
            for parameter in self.parameter_list:
                parameter.validate(True)
        


    ##
	# Get Kernel object size
    # @return size of Kernel object
	#        
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_string_size(self.kernel_name)
        sz = sz + parser.get_string_size(self.kernel_description)
        sz = sz + parser.get_string_size(self.module)
        sz = sz + parser.get_string_size(self.module_version)
        sz = sz + parser.get_int_size() * 2
        if self.parameter_list is not None:
            for parameter in self.parameter_list:
                sz = sz + parameter.get_size()
        return sz

    ##
	# Serialize Kernel object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#      
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.kernel_name, buffer, offset)
        offset = parser.serialize_string(self.kernel_description, buffer, offset)
        offset = parser.serialize_string(self.module, buffer, offset)
        offset = parser.serialize_string(self.module_version, buffer, offset)
        offset = parser.serialize_int(self.module_type, buffer, offset)
        parameter_list_sz = 0
        if self.parameter_list is not None:
            parameter_list_sz = len(self.parameter_list)
        offset = parser.serialize_int(parameter_list_sz, buffer, offset)
        if parameter_list_sz != 0:
            for parameter in self.parameter_list:
                offset = parameter.serialize(buffer, offset)
        return offset

    ##
	# Deserialize Kernel object
    # @param buffer deserialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#      
    def deserialize(self, buffer, offset):
        parser = Parser()
        offset, self.kernel_name = parser.deserialize_string(buffer, offset)
        offset, self.kernel_description = parser.deserialize_string(buffer, offset)
        offset, self.module = parser.deserialize_string(buffer, offset)
        offset, self.module_version = parser.deserialize_string(buffer, offset)
        offset, self.module_type = parser.deserialize_int(buffer, offset)
        offset, parameter_list_sz = parser.deserialize_int(buffer, offset)
        if parameter_list_sz > 0:
            for i in range(parameter_list_sz):
                parameter = Parameter('','','',0,'')
                offset = parameter.deserialize(buffer, offset)
                self.parameter_list.append(parameter)
        return offset
        
    def print_kernel(self):
        print('Kernel name: {0}'.format(self.kernel_name))
        print('Kernel description: {0}'.format(self.kernel_description))
        print('Module: {0}'.format(self.module))
        print('Module version: {0}'.format(self.module_version))
        print('Module typr: {0}'.format(self.module_type))
        if self.parameter_list is not None:
            for parameter in self.parameter_list:
                parameter.print_parameter()
    
    ## @var kernel_name 
    # Kernel name

    ## @var module 
    # Module name

    ## @var module_version 
    # Module version

    ## @var module_type 
    # Module type

    ## @var kernel_description 
    # Kernel description

    ## @var parameter_list 
    # List of Kernel parameter objects

    
##
# class KernelList contains list of kernel objects
#            
class KernelList:
    ##
	# KernelList constructor
    #
    def __init__(self):
        self.kernel_list = []

    ##
	# Validate KernelList object 
    #    
    def validate(self):
        if self.kernel_list is None:
            raise CSynException("Failed kernel list validation. Kernel list is empty")
        if not isinstance(self.kernel_list, list):
            raise CSynException("Failed kernel list validation. Kernel list is not list type")
        for kernel in self.kernel_list:
            kernel.validate()
    
    ##
	# Get KernelList object size
    # @return size of KernelList object
	#   
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_int_size()
        for kernel in self.kernel_list:
            sz = sz + kernel.get_size()
        return sz

    ##
	# Serialize KernelList object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#    
    def serialize(self, buffer, offset):
        parser = Parser()
        kernel_list_sz = 0
        if self.kernel_list is not None:
            kernel_list_sz = len(self.kernel_list)
        offset = parser.serialize_int(kernel_list_sz, buffer, offset)
        if kernel_list_sz != 0:
            for kernel in self.kernel_list:
                offset = kernel.serialize(buffer, offset)
        return offset

    ##
	# Deserialize KernelList object
    # @param buffer deserialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#        
    def deserialize(self, buffer, offset):
        parser = Parser()
        offset, kernel_list_sz = parser.deserialize_int(buffer, offset)
        if kernel_list_sz > 0:
            for i in range(kernel_list_sz):
                kernel = Kernel('','','','')
                offset = kernel.deserialize(buffer, offset)
                self.kernel_list.append(kernel)
        return offset
            
    def print_kernel_list(self):
        if self.kernel_list is not None:
            for kernel in self.kernel_list:
                kernel.print_kernel()

    ## @var kernel_list 
    # List of Kernel objects

##
# class Task defines task properties and kernel that will be executed during job run
#  
class Task:
    ##
	# Task constructor
    # @param task_name Task name
    # @param kernel Kernel object
    #
    def __init__(self, task_name, kernel, gridDimX = 1, gridDimY = 1, gridDimZ = 1, blockDimX = 1, blockDimY = 1, blockDimZ = 1, sharedMemory = 0):
        self.task_name = task_name
        self.gridDimX = gridDimX
        self.gridDimY = gridDimY
        self.gridDimZ = gridDimZ
        self.blockDimX = blockDimX
        self.blockDimY = blockDimY
        self.blockDimZ = blockDimZ
        self.sharedMemory = sharedMemory
        self.kernel = kernel
    
    ##
	# Validate Task object 
    #  
    def validate(self):
        if self.task_name is None:
            raise CSynException("Failed task validation. Task name is none")
        if self.kernel is None:
            raise CSynException("Failed task validation. Kernel is none")
        self.kernel.validate(True)
        
 
    ##
	# Get Task object size
    # @return size of Task object
	#      
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_string_size(self.task_name)
        sz = sz + 7 * parser.get_int_size()
        sz = sz + self.kernel.get_size()
        return sz

    ##
	# Serialize Task object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#     
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.task_name, buffer, offset)        
        offset = parser.serialize_int(self.gridDimX, buffer, offset)
        offset = parser.serialize_int(self.gridDimY, buffer, offset)
        offset = parser.serialize_int(self.gridDimZ, buffer, offset)
        offset = parser.serialize_int(self.blockDimX, buffer, offset)
        offset = parser.serialize_int(self.blockDimY, buffer, offset)
        offset = parser.serialize_int(self.blockDimZ, buffer, offset)
        offset = parser.serialize_int(self.sharedMemory, buffer, offset)
        offset = self.kernel.serialize(buffer, offset)
        return offset

    ##
	# Deserialize Task object
    # @param buffer deserialize buffer
    # @param offset buffer offset
    # @return buffer offset
	#     
    def deserialize(self, buffer, offset):
        parser = Parser()
        offset, self.task_name = parser.deserialize_string(buffer, offset)
        offset, self.gridDimX = parser.deserialize_int(buffer, offset)
        offset, self.gridDimY = parser.deserialize_int(buffer, offset)
        offset, self.gridDimZ = parser.deserialize_int(buffer, offset)
        offset, self.blockDimX = parser.deserialize_int(buffer, offset)
        offset, self.blockDimY = parser.deserialize_int(buffer, offset)
        offset, self.blockDimZ = parser.deserialize_int(buffer, offset)
        offset, self.sharedMemory = parser.deserialize_int(buffer, offset)
        self.kernel = Kernel('','','','')
        offset = self.kernel.deserialize(buffer, offset)
        return offset
                
    def print_task(self):
        print('Task Name: {0}'.format(self.task_name))
        print('GridDimX: {0}'.format(self.gridDimX))
        print('GridDimY: {0}'.format(self.gridDimY))
        print('GridDimZ: {0}'.format(self.gridDimZ))
        print('BlockDimX: {0}'.format(self.blockDimX))
        print('BlockDimY: {0}'.format(self.blockDimY))
        print('BlockDimZ: {0}'.format(self.blockDimZ))
        print('SharedMemory: {0}'.format(self.sharedMemory))
        if self.kernel is not None:
            self.kernel.print_kernel()
    
    ## @var task_name 
    # Task Name

    ## @var gridDimX 
    # Task max threads dimension X

    ## @var gridDimY 
    # Task max threads dimension Y

    ## @var gridDimZ 
    # Task max threads dimension Z

    ## @var blockDimX 
    # Task max threads block X

    ## @var blockDimY 
    # Task max threads block Y

    ## @var blockDimZ 
    # Task max threads block Z

    ## @var sharedMemory 
    # Task shared memory

    ## @var kernel 
    # Task kernel object
   
##
# class TaskStatus contains status of task executed by Csyn service
#         
class TaskStatus:
    ##
	# TaskStatus constructor
    #
    def __init__(self):
        self.task_name = ''
        self.uuid = ''
        self.execution_status = TaskExecutionStatus.task_queue
        self.execution_error = ''
        self.start_time = ''
        self.execution = 0
        self.ip_address = ''
        self.port = 0
      
    
    ##
	# Validate TaskStatus object 
    # 
    def validate(self):
        if self.task_name is None:
            raise CSynException("Failed task status validation. Task status task name is none")

    ##
	# Get TaskStatus object size
    # @return size of TaskStatus object
	#     
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_string_size(self.task_name)
        sz = sz + parser.get_string_size(self.uuid)
        sz = sz + parser.get_byte_size()
        sz = sz + parser.get_string_size(self.execution_error)
        sz = sz + parser.get_string_size(self.start_time)
        sz = sz + parser.get_double_size()
        sz = sz + parser.get_string_size(self.ip_address)
        sz = sz + parser.get_int_size()
        return sz

    ##
	# Serialize TaskStatus object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
    #  
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.task_name, buffer, offset)
        offset = parser.serialize_string(self.uuid, buffer, offset)
        offset = parser.serialize_byte(self.execution_status, buffer, offset)
        offset = parser.serialize_string(self.execution_error, buffer, offset)
        offset = parser.serialize_string(self.start_time, buffer, offset)        
        offset = parser.serialize_double(self.execution, buffer, offset)
        offset = parser.serialize_string(self.ip_address, buffer, offset)        
        offset = parser.serialize_int(self.port, buffer, offset)
        return offset

    ##
	# Deserialize TaskStatus object
    # @param buffer deserialize buffer
    # @param offset buffer offset
    # @return buffer offset
    # 
    def deserialize(self, buffer, offset):
        parser = Parser()
        offset, self.task_name = parser.deserialize_string(buffer, offset)
        offset, self.uuid = parser.deserialize_string(buffer, offset)
        offset, self.execution_status = parser.deserialize_byte(buffer, offset)
        offset, self.execution_error = parser.deserialize_string(buffer, offset)
        offset, self.start_time = parser.deserialize_string(buffer, offset)
        offset, self.execution = parser.deserialize_double(buffer, offset)
        offset, self.ip_address = parser.deserialize_string(buffer, offset)
        offset, self.port = parser.deserialize_int(buffer, offset)
        return offset
                
    def print_task_status(self):
        print('Task name: {0}'.format(self.task_name))
        print('UUID: {0}'.format(self.uuid))
        print('Execution status: {0}'.format(self.execution_status))
        print('Execution error: {0}'.format(self.execution_error))
        print('Start time: {0}'.format(self.start_time))
        print('Execution: {0}'.format(self.execution))
        print('IP Address: {0}'.format(self.ip_address))
        print('Port: {0}'.format(self.port))

 
    ## @var task_name 
    # Task name

    ## @var uuid 
    # Task UUID

    ## @var execution_status 
    # Task execution status

    ## @var execution_error 
    # Task execution error

    ## @var start_time 
    # Task start time

    ## @var execution 
    # Task execution period

    ## @var ip_address 
    # Task run engine ip address

    ## @var port 
    # Task run engine port

       
##
# class TaskResult contains results of task executed by Csyn service
#   
class TaskResult:
    ##
	# TaskResult constructor
    #
    def __init__(self):
        self.task_name = ''
        self.uuid = ''
        self.execution_status = TaskExecutionStatus.task_queue
        self.execution_error = ''
        self.parameter_list= []
 
    ##
	# Validate TaskResult object 
    #    
    def validate(self):
        if self.task_name is None:
            raise CSynException("Failed task result validation. Task result task name is none")
        if self.parameter_list is None:
            raise CSynException("Failed task result validation. Parameter list is empty")
        if not isinstance(self.parameter_list, list):
            raise CSynException("Failed task result validation. Parameter list is not list type")

            
    ##
	# Get TaskResult object size
    # @return size of TaskResult object
	#     
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_string_size(self.task_name)
        sz = sz + parser.get_string_size(self.uuid)
        sz = sz + parser.get_byte_size()
        sz = sz + parser.get_string_size(self.execution_error)
        sz = sz + parser.get_int_size()
        if self.parameter_list is not None:
            for parameter in self.parameter_list:
                sz = sz + parameter.get_size() 
        return sz

    ##
	# Serialize TaskResult object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
    #      
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.task_name, buffer, offset)
        offset = parser.serialize_string(self.uuid, buffer, offset)
        offset = parser.serialize_byte(self.execution_status, buffer, offset)
        offset = parser.serialize_string(self.execution_error, buffer, offset)
        list_sz = 0
        if self.parameter_list is not None:
            list_sz = len(self.parameter_list)
        offset = parser.serialize_int(list_sz, buffer, offset)
        if list_sz != 0:
            for parameter in self.parameter_list:
                offset = parameter.serialize(buffer, offset)
        return offset

    ##
	# Deserialize TaskResult object
    # @param buffer deserialize buffer
    # @param offset buffer offset
    # @return buffer offset
    #      
    def deserialize(self, buffer, offset):
        parser = Parser()
        offset, self.task_name = parser.deserialize_string(buffer, offset)
        offset, self.uuid = parser.deserialize_string(buffer, offset)
        offset, self.execution_status = parser.deserialize_byte(buffer, offset)
        offset, self.execution_error = parser.deserialize_string(buffer, offset)
        offset, parameter_list_sz = parser.deserialize_int(buffer, offset)
        if parameter_list_sz > 0:
            for i in range(parameter_list_sz):
                parameter = Parameter('','','',0,'')
                offset = parameter.deserialize(buffer, offset)
                self.parameter_list.append(parameter)
        return offset

    ##
	# Get Parameter by name
    # @return task result parameter object by name
	#     
    def get_parameter(self, name):
        if self.parameter_list is not None:
            for parameter in self.parameter_list:
                if parameter.name == name:
                    return parameter
        raise CSynException("Failed to get task result parameter by name. Can not find parameter with name {0}".format(name))
                 
    def print_task_result(self):
        print('Task name: {0}'.format(self.task_name))
        print('UUID: {0}'.format(self.uuid))
        print('Execution status: {0}'.format(self.execution_status))
        print('Execution error: {0}'.format(self.execution_error))
        if self.parameter_list is not None:
            for parameter in self.parameter_list:
                parameter.print_parameter()

    ## @var task_name 
    # Task name

    ## @var uuid
    # Task UUID

    ## @var execution_status 
    # Task execution status

    ## @var execution_error 
    # Task execution error

     ## @var parameter_list 
    # List of calculated Parameter objects

##
# class Job contains list of task objects, global parameters and properties. Csyn service will be used these data to execute job 
#  
class Job:
    ##
	# Job constructor
    # @param job_name Job name
    # @param gridDimX Job max threads dimension X
    # @param gridDimY Job max threads dimension Y
    # @param gridDimZ Job max threads dimension Y
    # @param blockDimX Job max threads block X
    # @param blockDimY Job max threads block Y
    # @param blockDimZ Job max threads block Z
    # @param sharedMemory Job max shared memory
    #
    def __init__(self, job_name, gridDimX = 1, gridDimY = 1, gridDimZ = 1, blockDimX = 1, blockDimY = 1, blockDimZ = 1, sharedMemory = 0, maxRunTime = 0, concurrentRun = 0):
        self.job_name = job_name
        self.gridDimX = gridDimX
        self.gridDimY = gridDimY
        self.gridDimZ = gridDimZ
        self.blockDimX = blockDimX
        self.blockDimY = blockDimY
        self.blockDimZ = blockDimZ
        self.sharedMemory = sharedMemory
        self.maxRunTime = maxRunTime
        self.concurrentRun = concurrentRun
        self.task_list = []
        self.global_value_list = []
 
    ##
	# Validate Job object 
    #     
    def validate(self):
        if self.job_name is None:
            raise CSynException("Failed job validation. Job name is none")
        if self.task_list is None:
            raise CSynException("Failed job validation. Task list is empty")
        if not isinstance(self.task_list, list):
            raise CSynException("Failed job validation. Task list is not list type")
        for task in self.task_list:
            task.validate()
        if self.global_value_list is not None:
            if not isinstance(self.global_value_list, list):
                raise CSynException("Failed job validation. Global value list is not list type")
            for value in self.global_value_list:
                value.validate()
        

    ##
	# Get Job object size
    # @return size of Job object
	#      
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_string_size(self.job_name)
        sz = sz + 8 * parser.get_int_size()
        sz = sz + parser.get_byte_size()
        sz = sz + parser.get_int_size()
        sz = sz + parser.get_int_size()
        if self.task_list is not None:
            for task in self.task_list:
                sz = sz + task.get_size()   
        sz = sz + parser.get_int_size()
        if self.global_value_list is not None:
            for value in self.global_value_list:
                sz = sz + parser.get_byte_size()
                sz = sz + value.get_size()     
        return sz

    ##
	# Serialize Job object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
    #      
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.job_name, buffer, offset)        
        offset = parser.serialize_int(self.gridDimX, buffer, offset)
        offset = parser.serialize_int(self.gridDimY, buffer, offset)
        offset = parser.serialize_int(self.gridDimZ, buffer, offset)
        offset = parser.serialize_int(self.blockDimX, buffer, offset)
        offset = parser.serialize_int(self.blockDimY, buffer, offset)
        offset = parser.serialize_int(self.blockDimZ, buffer, offset)
        offset = parser.serialize_int(self.sharedMemory, buffer, offset)
        offset = parser.serialize_int(self.maxRunTime, buffer, offset)
        offset = parser.serialize_byte(self.concurrentRun, buffer, offset)
        gv_sz = 0
        if self.global_value_list is not None:
            gv_sz = len(self.global_value_list)
        offset = parser.serialize_int(gv_sz, buffer, offset)
        if  gv_sz != 0:
            for value in self.global_value_list:
                offset = parser.serialize_byte(value.data_type, buffer, offset)
                offset = value.serialize(buffer, offset)
        task_sz = 0
        if self.task_list is not None:
            task_sz = len(self.task_list)
        offset = parser.serialize_int(task_sz, buffer, offset)        
        if task_sz != 0:
            for task in self.task_list:
                offset = task.serialize(buffer, offset)
        return offset
        

    ##
	# Deserialize Job object
    # @param buffer deserialize buffer
    # @param offset buffer offset
    # @return buffer offset
    #      
    def deserialize(self, buffer, offset):
        parser = Parser()
        offset, self.job_name = parser.deserialize_string(buffer, offset)
        offset, self.gridDimX = parser.deserialize_int(buffer, offset)
        offset, self.gridDimY = parser.deserialize_int(buffer, offset)
        offset, self.gridDimZ = parser.deserialize_int(buffer, offset)
        offset, self.blockDimX = parser.deserialize_int(buffer, offset)
        offset, self.blockDimY = parser.deserialize_int(buffer, offset)
        offset, self.blockDimZ = parser.deserialize_int(buffer, offset)
        offset, self.sharedMemory = parser.deserialize_int(buffer, offset)
        offset, self.maxRunTime = parser.deserialize_int(buffer, offset)
        offset, self.concurrentRun = parser.deserialize_byte(buffer, offset)
        self.global_value_list = []
        offset, global_value_list_sz = parser.deserialize_int(buffer, offset)
        if global_value_list_sz > 0:
            for i in range(global_value_list_sz):
                offset, data_type = parser.deserialize_byte(buffer, offset)
                offset, value = Value.deserialize(data_type, buffer, offset)
                self.global_value_list.append(value)
        self.task_list = []
        offset, task_list_sz = parser.deserialize_int(buffer, offset)
        if task_list_sz > 0:
            for i in range(task_list_sz):
                task = Task('',None)
                offset = task.deserialize(buffer, offset)
                self.task_list.append(task)
        return offset
                
    def print_job(self):
        print('Job Name: {0}'.format(self.job_name))
        print('GridDimX: {0}'.format(self.gridDimX))
        print('GridDimY: {0}'.format(self.gridDimY))
        print('GridDimZ: {0}'.format(self.gridDimZ))
        print('BlockDimX: {0}'.format(self.blockDimX))
        print('BlockDimY: {0}'.format(self.blockDimY))
        print('BlockDimZ: {0}'.format(self.blockDimZ))
        print('SharedMemory: {0}'.format(self.sharedMemory))
        if self.task_list is not None:
            for task in self.task_list:
                task.print_task()

    ## @var job_name 
    # Job Name

    ## @var gridDimX 
    # Job max threads dimension X

    ## @var gridDimY 
    # Job max threads dimension Y

    ## @var gridDimZ 
    # Job max threads dimension Z

    ## @var blockDimX 
    # Job max threads block X

    ## @var blockDimY 
    # Job max threads block Y

    ## @var blockDimZ 
    # Job max threads block Z

    ## @var sharedMemory 
    # Job shared memory

    ## @var maxRunTime 
    # Job max execution time

    ## @var concurrentRun 
    # Job execute tasks concurrently flag

    ## @var task_list 
    # List of Task objects

    ## @var global_value_list 
    # List of global values


##
# class JobStatus contains status of job executed by Csyn service
#          
class JobStatus:
    ##
	# JobStatus constructor
    #
    def __init__(self):
        self.job_name = ''
        self.uuid = ''
        self.execution_status = JobExecutionStatus.job_queue
        self.execution_error = ''
        self.start_time = ''
        self.end_time = ''
        self.execution = 0
        self.task_status_list = []

    ##
	# Validate JobStatus object 
    #     
    def validate(self):
        if self.job_name is None:
            raise CSynException("Failed job validation. Job name is none")
        if self.task_status_list is None:
            raise CSynException("Failed job validation. Task status list is empty")
        if not isinstance(self.task_status_list, list):
            raise CSynException("Failed job validation. Task status list is not list type")
        for task_status in self.task_status_list:
            task_status.validate() 

    ##
	# Check if job is finished
    # @return True if job is finished
	# 
    def is_job_finished(self):
        if self.execution_status == JobExecutionStatus.job_queue or self.execution_status == JobExecutionStatus.job_in_progress:
            return False
        return True

    ##
	# Get task status by task name
    # @return task status object by task name
	#     
    def get_task_status_by_name(self, task_name):
        if self.task_status_list is not None:
            for task_status in self.task_status_list:
                if task_status.task_name == task_name:
                    return task_status
        raise CSynException("Failed to get task status by task name. Can not find task status with name {0}".format(task_name))

    ##
	# Get task status by task uuid
    # @return task status object by task uuid
	#     
    def get_task_status_by_uuid(self, task_uuid):
        if self.task_status_list is not None:
            for task_status in self.task_status_list:
                if task_status.uuid == task_uuid:
                    return task_status
        raise CSynException("Failed to get task status by task uuid. Can not find task status with uuid {0}".format(task_uuid))

    ##
	# Get JobStatus object size
    # @return size of JobStatus object
	#     
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_string_size(self.job_name)
        sz = sz + parser.get_string_size(self.uuid)
        sz = sz + parser.get_byte_size()
        sz = sz + parser.get_string_size(self.execution_error)
        sz = sz + parser.get_string_size(self.start_time)
        sz = sz + parser.get_string_size(self.end_time)
        sz = sz + parser.get_double_size()
        sz = sz + parser.get_int_size()
        for task_status in self.task_status_list:
            sz = sz + task_status.get_size() 
        return sz

    ##
	# Serialize JobStatus object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
    #       
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.job_name, buffer, offset)
        offset = parser.serialize_string(self.uuid, buffer, offset)
        offset = parser.serialize_byte(self.execution_status, buffer, offset)
        offset = parser.serialize_string(self.execution_error, buffer, offset)
        offset = parser.serialize_string(self.start_time, buffer, offset)  
        offset = parser.serialize_string(self.end_time, buffer, offset)      
        offset = parser.serialize_double(self.execution, buffer, offset)
        task_status_sz = 0
        if self.task_status_list is not None:
            task_status_sz = len(self.task_status_list)
        offset = parser.serialize_int(task_status_sz, buffer, offset)        
        if task_status_sz != 0:
            for task_status in self.task_status_list:
                offset = task_status.serialize(buffer, offset)
        return offset

    ##
	# Deserialize JobStatus object
    # @param buffer deserialize buffer
    # @param offset buffer offset
    # @return buffer offset
    #       
    def deserialize(self, buffer, offset):
        parser = Parser()
        offset, self.job_name = parser.deserialize_string(buffer, offset)
        offset, self.uuid = parser.deserialize_string(buffer, offset)
        offset, self.execution_status = parser.deserialize_byte(buffer, offset)
        offset, self.execution_error = parser.deserialize_string(buffer, offset)
        offset, self.start_time = parser.deserialize_string(buffer, offset)
        offset, self.end_time = parser.deserialize_string(buffer, offset)
        offset, self.execution = parser.deserialize_double(buffer, offset)
        self.task_status_list = []
        offset, task_status_list_sz = parser.deserialize_int(buffer, offset)
        if task_status_list_sz > 0:
            for i in range(task_status_list_sz):
                task_status = TaskStatus()
                offset = task_status.deserialize(buffer, offset)
                self.task_status_list.append(task_status)
        return offset
                
    def print_job_performance(self):
        print('Job name: {0}'.format(self.job_name))
        print('UUID: {0}'.format(self.uuid))
        print('Execution status: {0}'.format(self.execution_status))
        print('Execution error: {0}'.format(self.execution_error))
        print('Start time: {0}'.format(self.start_time))
        print('End time: {0}'.format(self.end_time))
        print('Execution: {0}'.format(self.execution))
        if self.task_status_list is not None:
            for task_status in self.task_status_list:
                task_status.print_task_status()

    ## @var job_name 
    # Job name

    ## @var uuid
    # Job UUID

    ## @var execution_status 
    # Job execution status

    ## @var execution_error 
    # Job execution error

    ## @var start_time 
    # Job start time

    ## @var end_time 
    # Job end time

    ## @var execution 
    # Job execution period

     ## @var task_status_list 
    # List of task status objects
        

##
# class JobResult contains results of job executed by Csyn service
# 
class JobResult:
    ##
	# JobResult constructor
    #
    def __init__(self):
        self.job_name = ''
        self.uuid = ''
        self.execution_status = JobExecutionStatus.job_queue
        self.execution_error = ''
        self.task_result_list = []
 
    ##
	# Validate JobResult object 
    #
    def validate(self):
        if self.job_name is None:
            raise CSynException("Failed job result validation. Job result name is none")
        if self.task_result_list is None:
            raise CSynException("Failed job result validation. Task result list is empty")
        if not isinstance(self.task_result_list, list):
            raise CSynException("Failed job result validation. Task result list is not list type")
        for task_result in self.task_result_list:
            task_result.validate()     

    ##
	# Get JobResult object size
    # @return size of JobResult object
	#      
    def get_size(self):
        parser = Parser()
        sz = 0
        sz = sz + parser.get_string_size(self.job_name)
        sz = sz + parser.get_string_size(self.uuid)
        sz = sz + parser.get_byte_size()
        sz = sz + parser.get_string_size(self.execution_error)
        sz = sz + parser.get_int_size()
        if self.task_result_list is not None:
            for task_result in self.task_result_list:
                sz = sz + task_result.get_size()
        return sz

    ##
	# Serialize JobResult object
    # @param buffer serialize buffer
    # @param offset buffer offset
    # @return buffer offset
    #        
    def serialize(self, buffer, offset):
        parser = Parser()
        offset = parser.serialize_string(self.job_name, buffer, offset)        
        offset = parser.serialize_string(self.uuid, buffer, offset)
        offset = parser.serialize_byte(self.execution_status, buffer, offset)
        offset = parser.serialize_string(self.execution_error, buffer, offset)
        list_sz = 0
        if self.task_result_list is not None:
            list_sz = len(self.task_result_list)
        offset = parser.serialize_int(list_sz, buffer, offset)
        if list_sz != 0:
            for task_result in self.task_result_list:
                offset = task_result.serialize(buffer, offset)
        return offset

    ##
	# Deserialize JobResult object
    # @param buffer deserialize buffer
    # @param offset buffer offset
    # @return buffer offset
    #        
    def deserialize(self, buffer, offset):
        parser = Parser()
        offset, self.job_name = parser.deserialize_string(buffer, offset)
        offset, self.uuid = parser.deserialize_string(buffer, offset)
        offset, self.execution_status = parser.deserialize_byte(buffer, offset)
        offset, self.execution_error = parser.deserialize_string(buffer, offset)
        offset, task_result_list_sz = parser.deserialize_int(buffer, offset)
        if task_result_list_sz > 0:
            for i in range(task_result_list_sz):
                task_result = TaskResult()
                offset = task_result.deserialize(buffer, offset)
                self.task_result_list.append(task_result)
        return offset
    

    ##
	# Get task result by task name
    # @return task result object by task name
	#     
    def get_task_result_by_name(self, task_name):
        if self.task_result_list is not None:
            for task_result in self.task_result_list:
                if task_result.task_name == task_name:
                    return task_result
        raise CSynException("Failed to get task result by task name. Can not find task result with name {0}".format(task_name))

    ##
	# Get task result by task uuid
    # @return task result object by task uuid
	#     
    def get_task_result_by_uuid(self, task_uuid):
        if self.task_result_list is not None:
            for task_result in self.task_result_list:
                if task_result.uuid == task_uuid:
                    return task_result
        raise CSynException("Failed to get task result by task uuid. Can not find task result with uuid {0}".format(task_uuid))

    def print_job_result(self):
        print('Job name: {0}'.format(self.job_name))
        print('UUID: {0}'.format(self.uuid))
        print('Execution status: {0}'.format(self.execution_status))
        print('Execution error: {0}'.format(self.execution_error))
        if self.task_result_list is not None:
            for task_result in self.task_result_list:
                task_result.print_task_result()

    ## @var job_name 
    # Job name

    ## @var uuid
    # Job UUID

    ## @var execution_status 
    # Job execution status

    ## @var execution_error 
    # Job execution error

    ## @var task_result_list 
    # List of TaskResult objects 
    



 
 