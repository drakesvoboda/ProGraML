# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: programl/proto/repo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='programl/proto/repo.proto',
  package='programl',
  syntax='proto3',
  serialized_options=b'\n\014com.programlB\tRepoProtoP\001Z\nprogramlpb\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19programl/proto/repo.proto\x12\x08programl\"?\n\x04Repo\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0c\n\x04sha1\x18\x02 \x01(\t\x12\x1c\n\x14\x63reated_ms_timestamp\x18\x03 \x01(\x03\x42*\n\x0c\x63om.programlB\tRepoProtoP\x01Z\nprogramlpb\xf8\x01\x01\x62\x06proto3'
)




_REPO = _descriptor.Descriptor(
  name='Repo',
  full_name='programl.Repo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='programl.Repo.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sha1', full_name='programl.Repo.sha1', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_ms_timestamp', full_name='programl.Repo.created_ms_timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=39,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['Repo'] = _REPO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Repo = _reflection.GeneratedProtocolMessageType('Repo', (_message.Message,), {
  'DESCRIPTOR' : _REPO,
  '__module__' : 'programl.proto.repo_pb2'
  # @@protoc_insertion_point(class_scope:programl.Repo)
  })
_sym_db.RegisterMessage(Repo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)