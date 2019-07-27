# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: second/protos/voxel_generator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='second/protos/voxel_generator.proto',
  package='second.protos',
  syntax='proto3',
  serialized_pb=_b('\n#second/protos/voxel_generator.proto\x12\rsecond.protos\"\xcd\x01\n\x0eVoxelGenerator\x12\x12\n\nvoxel_size\x18\x01 \x03(\x02\x12\x19\n\x11point_cloud_range\x18\x02 \x03(\x02\x12&\n\x1emax_number_of_points_per_voxel\x18\x03 \x01(\r\x12\x19\n\x11submanifold_group\x18\x04 \x01(\x08\x12\x18\n\x10submanifold_size\x18\x05 \x03(\r\x12\x1e\n\x16submanifold_max_points\x18\x06 \x01(\r\x12\x0f\n\x07rnn_num\x18\x07 \x01(\rb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_VOXELGENERATOR = _descriptor.Descriptor(
  name='VoxelGenerator',
  full_name='second.protos.VoxelGenerator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='voxel_size', full_name='second.protos.VoxelGenerator.voxel_size', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point_cloud_range', full_name='second.protos.VoxelGenerator.point_cloud_range', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_number_of_points_per_voxel', full_name='second.protos.VoxelGenerator.max_number_of_points_per_voxel', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='submanifold_group', full_name='second.protos.VoxelGenerator.submanifold_group', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='submanifold_size', full_name='second.protos.VoxelGenerator.submanifold_size', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='submanifold_max_points', full_name='second.protos.VoxelGenerator.submanifold_max_points', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rnn_num', full_name='second.protos.VoxelGenerator.rnn_num', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=260,
)

DESCRIPTOR.message_types_by_name['VoxelGenerator'] = _VOXELGENERATOR

VoxelGenerator = _reflection.GeneratedProtocolMessageType('VoxelGenerator', (_message.Message,), dict(
  DESCRIPTOR = _VOXELGENERATOR,
  __module__ = 'second.protos.voxel_generator_pb2'
  # @@protoc_insertion_point(class_scope:second.protos.VoxelGenerator)
  ))
_sym_db.RegisterMessage(VoxelGenerator)


# @@protoc_insertion_point(module_scope)
