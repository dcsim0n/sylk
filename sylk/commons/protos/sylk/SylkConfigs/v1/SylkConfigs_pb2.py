# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sylk/SylkConfigs/v1/SylkConfigs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%sylk/SylkConfigs/v1/SylkConfigs.proto\x12\x13sylk.SylkConfigs.v1\"\x92\x01\n\x13SylkTemplateConfigs\x12\x0f\n\x07include\x18\x03 \x03(\t\x12\x0f\n\x07\x65xclude\x18\x02 \x03(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x10\n\x08out_path\x18\x06 \x01(\t\x12\x14\n\x0cinclude_code\x18\x01 \x01(\x08\x12\x0e\n\x06\x61uthor\x18\x07 \x01(\t\"\xc2\x02\n\x12SylkProjectConfigs\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04host\x18\x01 \x01(\t\x12:\n\x08template\x18\x05 \x01(\x0b\x32(.sylk.SylkConfigs.v1.SylkTemplateConfigs\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x17\n\x0f\x63urrent_version\x18\x04 \x01(\t\x12\x0f\n\x07plugins\x18\x06 \x03(\t\x12\x17\n\x0fproto_base_path\x18\x07 \x01(\t\x12\x1b\n\x13proto_compiled_path\x18\x08 \x01(\t\x12\x16\n\x0e\x63ode_base_path\x18\t \x01(\t\x12\x36\n\tframework\x18\n \x01(\x0e\x32#.sylk.SylkConfigs.v1.SylkFrameworks\x12\x0f\n\x07license\x18\x0b \x01(\t\"\xdd\x02\n\x0eSylkCliConfigs\x12\x16\n\x0esylk_templates\x18\x06 \x03(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\r\n\x05token\x18\x03 \x01(\t\x12\x11\n\tanalytics\x18\x04 \x01(\x08\x12\x11\n\tfirst_run\x18\x05 \x01(\x08\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0f\n\x07plugins\x18\x07 \x03(\t\x12\x17\n\x0fproto_base_path\x18\x08 \x01(\t\x12\x1b\n\x13proto_compiled_path\x18\t \x01(\t\x12:\n\x08template\x18\n \x01(\x0b\x32(.sylk.SylkConfigs.v1.SylkTemplateConfigs\x12\x16\n\x0e\x63ode_base_path\x18\x0b \x01(\t\x12\x36\n\tframework\x18\x0c \x01(\x0e\x32#.sylk.SylkConfigs.v1.SylkFrameworks\x12\x0f\n\x07license\x18\r \x01(\t*>\n\x0eSylkFrameworks\x12\x15\n\x11UNKNOWN_FRAMEWORK\x10\x00\x12\x08\n\x04GRPC\x10\x01\x12\x0b\n\x07SYLK_JS\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sylk.SylkConfigs.v1.SylkConfigs_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_SYLKFRAMEWORKS']._serialized_start=888
  _globals['_SYLKFRAMEWORKS']._serialized_end=950
  _globals['_SYLKTEMPLATECONFIGS']._serialized_start=63
  _globals['_SYLKTEMPLATECONFIGS']._serialized_end=209
  _globals['_SYLKPROJECTCONFIGS']._serialized_start=212
  _globals['_SYLKPROJECTCONFIGS']._serialized_end=534
  _globals['_SYLKCLICONFIGS']._serialized_start=537
  _globals['_SYLKCLICONFIGS']._serialized_end=886
# @@protoc_insertion_point(module_scope)
