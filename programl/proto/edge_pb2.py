# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: programl/proto/edge.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from programl.proto import features_pb2 as programl_dot_proto_dot_features__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='programl/proto/edge.proto',
  package='programl',
  syntax='proto3',
  serialized_options=b'\n\014com.programlB\tEdgeProtoP\001Z\nprogramlpb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19programl/proto/edge.proto\x12\x08programl\x1a\x1dprograml/proto/features.proto\"\xaa\x01\n\x04\x45\x64ge\x12!\n\x04\x66low\x18\x01 \x01(\x0e\x32\x13.programl.Edge.Flow\x12\x10\n\x08position\x18\x02 \x01(\x05\x12\x0e\n\x06source\x18\x03 \x01(\x05\x12\x0e\n\x06target\x18\x04 \x01(\x05\x12$\n\x08\x66\x65\x61tures\x18\x05 \x01(\x0b\x32\x12.programl.Features\"\'\n\x04\x46low\x12\x0b\n\x07\x43ONTROL\x10\x00\x12\x08\n\x04\x44\x41TA\x10\x01\x12\x08\n\x04\x43\x41LL\x10\x02\x42\'\n\x0c\x63om.programlB\tEdgeProtoP\x01Z\nprogramlpbb\x06proto3'
  ,
  dependencies=[programl_dot_proto_dot_features__pb2.DESCRIPTOR,])



_EDGE_FLOW = _descriptor.EnumDescriptor(
  name='Flow',
  full_name='programl.Edge.Flow',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONTROL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DATA', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CALL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=202,
  serialized_end=241,
)
_sym_db.RegisterEnumDescriptor(_EDGE_FLOW)


_EDGE = _descriptor.Descriptor(
  name='Edge',
  full_name='programl.Edge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flow', full_name='programl.Edge.flow', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='position', full_name='programl.Edge.position', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='programl.Edge.source', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='programl.Edge.target', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='features', full_name='programl.Edge.features', index=4,
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
    _EDGE_FLOW,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=241,
)

_EDGE.fields_by_name['flow'].enum_type = _EDGE_FLOW
_EDGE.fields_by_name['features'].message_type = programl_dot_proto_dot_features__pb2._FEATURES
_EDGE_FLOW.containing_type = _EDGE
DESCRIPTOR.message_types_by_name['Edge'] = _EDGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Edge = _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), {
  'DESCRIPTOR' : _EDGE,
  '__module__' : 'programl.proto.edge_pb2'
  # @@protoc_insertion_point(class_scope:programl.Edge)
  })
_sym_db.RegisterMessage(Edge)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
