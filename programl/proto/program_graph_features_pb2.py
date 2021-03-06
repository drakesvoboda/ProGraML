# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: programl/proto/program_graph_features.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from programl.proto import features_pb2 as programl_dot_proto_dot_features__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='programl/proto/program_graph_features.proto',
  package='programl',
  syntax='proto3',
  serialized_options=b'\n\014com.programlB\031ProgramGraphFeaturesProtoP\001Z\nprogramlpb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+programl/proto/program_graph_features.proto\x12\x08programl\x1a\x1dprograml/proto/features.proto\"\xfe\x01\n\x14ProgramGraphFeatures\x12-\n\rnode_features\x18\x01 \x01(\x0b\x32\x16.programl.FeatureLists\x12-\n\redge_features\x18\x02 \x01(\x0b\x32\x16.programl.FeatureLists\x12\x31\n\x11\x66unction_features\x18\x03 \x01(\x0b\x32\x16.programl.FeatureLists\x12/\n\x0fmodule_features\x18\x04 \x01(\x0b\x32\x16.programl.FeatureLists\x12$\n\x08\x66\x65\x61tures\x18\x05 \x01(\x0b\x32\x12.programl.Features\"n\n\x18ProgramGraphFeaturesList\x12#\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x12.programl.Features\x12-\n\x05graph\x18\x02 \x03(\x0b\x32\x1e.programl.ProgramGraphFeaturesB7\n\x0c\x63om.programlB\x19ProgramGraphFeaturesProtoP\x01Z\nprogramlpbb\x06proto3'
  ,
  dependencies=[programl_dot_proto_dot_features__pb2.DESCRIPTOR,])




_PROGRAMGRAPHFEATURES = _descriptor.Descriptor(
  name='ProgramGraphFeatures',
  full_name='programl.ProgramGraphFeatures',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_features', full_name='programl.ProgramGraphFeatures.node_features', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='edge_features', full_name='programl.ProgramGraphFeatures.edge_features', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='function_features', full_name='programl.ProgramGraphFeatures.function_features', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module_features', full_name='programl.ProgramGraphFeatures.module_features', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='features', full_name='programl.ProgramGraphFeatures.features', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=343,
)


_PROGRAMGRAPHFEATURESLIST = _descriptor.Descriptor(
  name='ProgramGraphFeaturesList',
  full_name='programl.ProgramGraphFeaturesList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='programl.ProgramGraphFeaturesList.context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='graph', full_name='programl.ProgramGraphFeaturesList.graph', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=345,
  serialized_end=455,
)

_PROGRAMGRAPHFEATURES.fields_by_name['node_features'].message_type = programl_dot_proto_dot_features__pb2._FEATURELISTS
_PROGRAMGRAPHFEATURES.fields_by_name['edge_features'].message_type = programl_dot_proto_dot_features__pb2._FEATURELISTS
_PROGRAMGRAPHFEATURES.fields_by_name['function_features'].message_type = programl_dot_proto_dot_features__pb2._FEATURELISTS
_PROGRAMGRAPHFEATURES.fields_by_name['module_features'].message_type = programl_dot_proto_dot_features__pb2._FEATURELISTS
_PROGRAMGRAPHFEATURES.fields_by_name['features'].message_type = programl_dot_proto_dot_features__pb2._FEATURES
_PROGRAMGRAPHFEATURESLIST.fields_by_name['context'].message_type = programl_dot_proto_dot_features__pb2._FEATURES
_PROGRAMGRAPHFEATURESLIST.fields_by_name['graph'].message_type = _PROGRAMGRAPHFEATURES
DESCRIPTOR.message_types_by_name['ProgramGraphFeatures'] = _PROGRAMGRAPHFEATURES
DESCRIPTOR.message_types_by_name['ProgramGraphFeaturesList'] = _PROGRAMGRAPHFEATURESLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProgramGraphFeatures = _reflection.GeneratedProtocolMessageType('ProgramGraphFeatures', (_message.Message,), {
  'DESCRIPTOR' : _PROGRAMGRAPHFEATURES,
  '__module__' : 'programl.proto.program_graph_features_pb2'
  # @@protoc_insertion_point(class_scope:programl.ProgramGraphFeatures)
  })
_sym_db.RegisterMessage(ProgramGraphFeatures)

ProgramGraphFeaturesList = _reflection.GeneratedProtocolMessageType('ProgramGraphFeaturesList', (_message.Message,), {
  'DESCRIPTOR' : _PROGRAMGRAPHFEATURESLIST,
  '__module__' : 'programl.proto.program_graph_features_pb2'
  # @@protoc_insertion_point(class_scope:programl.ProgramGraphFeaturesList)
  })
_sym_db.RegisterMessage(ProgramGraphFeaturesList)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
