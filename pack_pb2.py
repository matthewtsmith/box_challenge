# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pack.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pack.proto',
  package='main',
  syntax='proto3',
  serialized_pb=_b('\n\npack.proto\x12\x04main\x1a\x1cgoogle/api/annotations.proto\"S\n\x03\x42ox\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06length\x18\x02 \x01(\x01\x12\r\n\x05width\x18\x03 \x01(\x01\x12\x0e\n\x06height\x18\x04 \x01(\x01\x12\x11\n\tmaxWeight\x18\x05 \x01(\x01\"^\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06length\x18\x02 \x01(\x01\x12\r\n\x05width\x18\x03 \x01(\x01\x12\x0e\n\x06height\x18\x04 \x01(\x01\x12\x0b\n\x03qty\x18\x05 \x01(\x05\x12\x0e\n\x06weight\x18\x06 \x01(\x01\"B\n\x0bPackRequest\x12\x18\n\x05\x62oxes\x18\x01 \x03(\x0b\x32\t.main.Box\x12\x19\n\x05items\x18\x02 \x03(\x0b\x32\n.main.Item\".\n\x0cPackResponse\x12\x1e\n\x05\x62oxes\x18\x01 \x03(\x0b\x32\x0f.main.PackedBox\">\n\tPackedBox\x12\x16\n\x03\x62ox\x18\x01 \x01(\x0b\x32\t.main.Box\x12\x19\n\x05items\x18\x02 \x03(\x0b\x32\n.main.Item2L\n\x06Packer\x12\x42\n\x04Pack\x12\x11.main.PackRequest\x1a\x12.main.PackResponse\"\x13\x82\xd3\xe4\x93\x02\r\"\x08/v1/pack:\x01*B9\n\x1a\x63om.apptreesoftware.packer\xaa\x02\x1a\x63om.apptreesoftware.Packerb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_BOX = _descriptor.Descriptor(
  name='Box',
  full_name='main.Box',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='main.Box.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='main.Box.length', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='main.Box.width', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='main.Box.height', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxWeight', full_name='main.Box.maxWeight', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=50,
  serialized_end=133,
)


_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='main.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='main.Item.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='main.Item.length', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='main.Item.width', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='main.Item.height', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qty', full_name='main.Item.qty', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='main.Item.weight', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=135,
  serialized_end=229,
)


_PACKREQUEST = _descriptor.Descriptor(
  name='PackRequest',
  full_name='main.PackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boxes', full_name='main.PackRequest.boxes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='main.PackRequest.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=231,
  serialized_end=297,
)


_PACKRESPONSE = _descriptor.Descriptor(
  name='PackResponse',
  full_name='main.PackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boxes', full_name='main.PackResponse.boxes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=299,
  serialized_end=345,
)


_PACKEDBOX = _descriptor.Descriptor(
  name='PackedBox',
  full_name='main.PackedBox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='box', full_name='main.PackedBox.box', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='main.PackedBox.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=347,
  serialized_end=409,
)

_PACKREQUEST.fields_by_name['boxes'].message_type = _BOX
_PACKREQUEST.fields_by_name['items'].message_type = _ITEM
_PACKRESPONSE.fields_by_name['boxes'].message_type = _PACKEDBOX
_PACKEDBOX.fields_by_name['box'].message_type = _BOX
_PACKEDBOX.fields_by_name['items'].message_type = _ITEM
DESCRIPTOR.message_types_by_name['Box'] = _BOX
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['PackRequest'] = _PACKREQUEST
DESCRIPTOR.message_types_by_name['PackResponse'] = _PACKRESPONSE
DESCRIPTOR.message_types_by_name['PackedBox'] = _PACKEDBOX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Box = _reflection.GeneratedProtocolMessageType('Box', (_message.Message,), dict(
  DESCRIPTOR = _BOX,
  __module__ = 'pack_pb2'
  # @@protoc_insertion_point(class_scope:main.Box)
  ))
_sym_db.RegisterMessage(Box)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
  DESCRIPTOR = _ITEM,
  __module__ = 'pack_pb2'
  # @@protoc_insertion_point(class_scope:main.Item)
  ))
_sym_db.RegisterMessage(Item)

PackRequest = _reflection.GeneratedProtocolMessageType('PackRequest', (_message.Message,), dict(
  DESCRIPTOR = _PACKREQUEST,
  __module__ = 'pack_pb2'
  # @@protoc_insertion_point(class_scope:main.PackRequest)
  ))
_sym_db.RegisterMessage(PackRequest)

PackResponse = _reflection.GeneratedProtocolMessageType('PackResponse', (_message.Message,), dict(
  DESCRIPTOR = _PACKRESPONSE,
  __module__ = 'pack_pb2'
  # @@protoc_insertion_point(class_scope:main.PackResponse)
  ))
_sym_db.RegisterMessage(PackResponse)

PackedBox = _reflection.GeneratedProtocolMessageType('PackedBox', (_message.Message,), dict(
  DESCRIPTOR = _PACKEDBOX,
  __module__ = 'pack_pb2'
  # @@protoc_insertion_point(class_scope:main.PackedBox)
  ))
_sym_db.RegisterMessage(PackedBox)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032com.apptreesoftware.packer\252\002\032com.apptreesoftware.Packer'))

_PACKER = _descriptor.ServiceDescriptor(
  name='Packer',
  full_name='main.Packer',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=411,
  serialized_end=487,
  methods=[
  _descriptor.MethodDescriptor(
    name='Pack',
    full_name='main.Packer.Pack',
    index=0,
    containing_service=None,
    input_type=_PACKREQUEST,
    output_type=_PACKRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\r\"\010/v1/pack:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_PACKER)

DESCRIPTOR.services_by_name['Packer'] = _PACKER

# @@protoc_insertion_point(module_scope)
