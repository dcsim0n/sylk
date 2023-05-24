# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SylkOrganization.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor

from typing import overload, Iterator, List, Dict
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import SylkUser_pb2 as SylkUser__pb2
from . import SylkProject_pb2 as SylkProject__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16SylkOrganization.proto\x12\x18sylk.SylkOrganization.v1\x1a\x0eSylkUser.proto\x1a\x11SylkProject.proto\"N\n\x10SylkOrganization\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x64omain\x18\x03 \x01(\t\x12\r\n\x05owner\x18\x04 \x01(\t\"\xc8\x01\n\x17SylkOrganizationDisplay\x12@\n\x0corganization\x18\x01 \x01(\x0b\x32*.sylk.SylkOrganization.v1.SylkOrganization\x12\x30\n\x05users\x18\x02 \x03(\x0b\x32!.sylk.SylkUser.v1.SylkUserDisplay\x12\x39\n\x08projects\x18\x03 \x03(\x0b\x32\'.sylk.SylkProject.v1.SylkProjectDisplayB#Z!/services/protos/SylkOrganizationb\x06proto3')



_SYLKORGANIZATION = DESCRIPTOR.message_types_by_name['SylkOrganization']
_SYLKORGANIZATIONDISPLAY = DESCRIPTOR.message_types_by_name['SylkOrganizationDisplay']

@overload
class SylkOrganization(_message.Message):
	"""webezyio generated message [sylk.SylkOrganization.v1.SylkOrganization]
	A class respresent a SylkOrganization type
	
		"""
	orgId = str # type: str
	name = str # type: str
	domain = str # type: str
	owner = str # type: str

	def __init__(self, orgId=str, name=str, domain=str, owner=str):
		"""
		Attributes:
		----------
		orgId : str
			
		name : str
			
		domain : str
			
		owner : str
			
		"""
		pass
SylkOrganization = _reflection.GeneratedProtocolMessageType('SylkOrganization', (_message.Message,), {
  'DESCRIPTOR' : _SYLKORGANIZATION,
  '__module__' : 'SylkOrganization_pb2'
  # @@protoc_insertion_point(class_scope:sylk.SylkOrganization.v1.SylkOrganization)
  })
_sym_db.RegisterMessage(SylkOrganization)


@overload
class SylkOrganizationDisplay(_message.Message):
	"""webezyio generated message [sylk.SylkOrganization.v1.SylkOrganizationDisplay]
	A class respresent a SylkOrganizationDisplay type
	
		"""
	organization = SylkOrganization # type: SylkOrganization
	users = List[SylkUser__pb2.SylkUserDisplay] # type: List[SylkUser__pb2.SylkUserDisplay]
	projects = List[SylkProject__pb2.SylkProjectDisplay] # type: List[SylkProject__pb2.SylkProjectDisplay]

	def __init__(self, organization=SylkOrganization, users=List[SylkUser__pb2.SylkUserDisplay], projects=List[SylkProject__pb2.SylkProjectDisplay]):
		"""
		Attributes:
		----------
		organization : SylkOrganization
			
		users : List[SylkUser__pb2.SylkUserDisplay]
			
		projects : List[SylkProject__pb2.SylkProjectDisplay]
			
		"""
		pass
SylkOrganizationDisplay = _reflection.GeneratedProtocolMessageType('SylkOrganizationDisplay', (_message.Message,), {
  'DESCRIPTOR' : _SYLKORGANIZATIONDISPLAY,
  '__module__' : 'SylkOrganization_pb2'
  # @@protoc_insertion_point(class_scope:sylk.SylkOrganization.v1.SylkOrganizationDisplay)
  })
_sym_db.RegisterMessage(SylkOrganizationDisplay)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z!/services/protos/SylkOrganization'
  _SYLKORGANIZATION._serialized_start=87
  _SYLKORGANIZATION._serialized_end=165
  _SYLKORGANIZATIONDISPLAY._serialized_start=168
  _SYLKORGANIZATIONDISPLAY._serialized_end=368
# @@protoc_insertion_point(module_scope)