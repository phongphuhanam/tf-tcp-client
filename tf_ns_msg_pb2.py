# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tf_ns_msg.proto

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
  name='tf_ns_msg.proto',
  package='TFNSmessage',
  syntax='proto3',
  serialized_pb=_b('\n\x0ftf_ns_msg.proto\x12\x0bTFNSmessage\"\xea\x03\n\x07\x43ommand\x12\r\n\x05\x63\x61rid\x18\x01 \x01(\r\x12\x36\n\x0c\x63ommand_type\x18\x02 \x01(\x0e\x32 .TFNSmessage.Command.CommandType\x12\x17\n\x0fsimulattionTime\x18\x03 \x01(\x01\x12\x11\n\tweightLen\x18\x04 \x01(\r\x12\x34\n\rplatform_type\x18\x05 \x01(\x0e\x32\x1d.TFNSmessage.Command.Platform\x12\x36\n\x0crequest_type\x18\x06 \x01(\x0e\x32 .TFNSmessage.Command.RequestType\"\x97\x01\n\x0b\x43ommandType\x12\r\n\tCMD_UNDEF\x10\x00\x12\x10\n\x0c\x43MD_FINISTED\x10\x01\x12\x15\n\x11\x43MD_RECEIVED_DATA\x10\x02\x12\x14\n\x10\x43MD_SENDING_DATA\x10\x03\x12\x0f\n\x0b\x43MD_STARTED\x10\x04\x12\x13\n\x0f\x43MD_CLEAR_QUEUE\x10\x05\x12\x14\n\x10\x43MD_REQUEST_LIST\x10\x06\"&\n\x08Platform\x12\n\n\x06PLA_NS\x10\x00\x12\x0e\n\nPLA_TENSOR\x10\x01\"<\n\x0bRequestType\x12\t\n\x05UNDEF\x10\x00\x12\x12\n\x0eIDENTIFICATION\x10\x01\x12\x0e\n\nDECTECTION\x10\x02\"\xfe\x03\n\x0bWeightArray\x12\r\n\x05\x63\x61rid\x18\x01 \x01(\r\x12\x14\n\x0ctotal_object\x18\x02 \x01(\r\x12\x38\n\x07payload\x18\x03 \x03(\x0b\x32\'.TFNSmessage.WeightArray.VehiclePayload\x12\x16\n\x0esimulationTime\x18\x04 \x01(\x01\x12\x0b\n\x03lat\x18\x05 \x01(\x01\x12\x0b\n\x03lon\x18\x06 \x01(\x01\x12\x36\n\nmsg_status\x18\x07 \x01(\x0e\x32\".TFNSmessage.WeightArray.MsgStatus\x12\x19\n\x11\x63omparision_carid\x18\x08 \x01(\r\x12\x36\n\x0crequest_type\x18\t \x01(\x0e\x32 .TFNSmessage.Command.RequestType\x12\x11\n\tsended_id\x18\n \x01(\r\x1a\x89\x01\n\x0eVehiclePayload\x12\x11\n\tobject_id\x18\x01 \x01(\r\x12\x0e\n\x06length\x18\x02 \x01(\r\x12\x13\n\x07weights\x18\x03 \x03(\x01\x42\x02\x10\x01\x12\r\n\x05\x61ngle\x18\x04 \x01(\x01\x12\x12\n\nclass_name\x18\x05 \x01(\t\x12\x1c\n\x14\x63omparison_object_id\x18\x06 \x01(\r\"4\n\tMsgStatus\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06\x46INISH\x10\x01\x12\x11\n\rEMPTY_PAYLOAD\x10\x02\x62\x06proto3')
)



_COMMAND_COMMANDTYPE = _descriptor.EnumDescriptor(
  name='CommandType',
  full_name='TFNSmessage.Command.CommandType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CMD_UNDEF', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CMD_FINISTED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CMD_RECEIVED_DATA', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CMD_SENDING_DATA', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CMD_STARTED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CMD_CLEAR_QUEUE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CMD_REQUEST_LIST', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=270,
  serialized_end=421,
)
_sym_db.RegisterEnumDescriptor(_COMMAND_COMMANDTYPE)

_COMMAND_PLATFORM = _descriptor.EnumDescriptor(
  name='Platform',
  full_name='TFNSmessage.Command.Platform',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLA_NS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLA_TENSOR', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=423,
  serialized_end=461,
)
_sym_db.RegisterEnumDescriptor(_COMMAND_PLATFORM)

_COMMAND_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='TFNSmessage.Command.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEF', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IDENTIFICATION', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DECTECTION', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=463,
  serialized_end=523,
)
_sym_db.RegisterEnumDescriptor(_COMMAND_REQUESTTYPE)

_WEIGHTARRAY_MSGSTATUS = _descriptor.EnumDescriptor(
  name='MsgStatus',
  full_name='TFNSmessage.WeightArray.MsgStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINISH', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMPTY_PAYLOAD', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=984,
  serialized_end=1036,
)
_sym_db.RegisterEnumDescriptor(_WEIGHTARRAY_MSGSTATUS)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='TFNSmessage.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='carid', full_name='TFNSmessage.Command.carid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='command_type', full_name='TFNSmessage.Command.command_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simulattionTime', full_name='TFNSmessage.Command.simulattionTime', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weightLen', full_name='TFNSmessage.Command.weightLen', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='platform_type', full_name='TFNSmessage.Command.platform_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_type', full_name='TFNSmessage.Command.request_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMAND_COMMANDTYPE,
    _COMMAND_PLATFORM,
    _COMMAND_REQUESTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=523,
)


_WEIGHTARRAY_VEHICLEPAYLOAD = _descriptor.Descriptor(
  name='VehiclePayload',
  full_name='TFNSmessage.WeightArray.VehiclePayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='TFNSmessage.WeightArray.VehiclePayload.object_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='TFNSmessage.WeightArray.VehiclePayload.length', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weights', full_name='TFNSmessage.WeightArray.VehiclePayload.weights', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='angle', full_name='TFNSmessage.WeightArray.VehiclePayload.angle', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='class_name', full_name='TFNSmessage.WeightArray.VehiclePayload.class_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comparison_object_id', full_name='TFNSmessage.WeightArray.VehiclePayload.comparison_object_id', index=5,
      number=6, type=13, cpp_type=3, label=1,
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
  serialized_start=845,
  serialized_end=982,
)

_WEIGHTARRAY = _descriptor.Descriptor(
  name='WeightArray',
  full_name='TFNSmessage.WeightArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='carid', full_name='TFNSmessage.WeightArray.carid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_object', full_name='TFNSmessage.WeightArray.total_object', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='TFNSmessage.WeightArray.payload', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simulationTime', full_name='TFNSmessage.WeightArray.simulationTime', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lat', full_name='TFNSmessage.WeightArray.lat', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lon', full_name='TFNSmessage.WeightArray.lon', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_status', full_name='TFNSmessage.WeightArray.msg_status', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comparision_carid', full_name='TFNSmessage.WeightArray.comparision_carid', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_type', full_name='TFNSmessage.WeightArray.request_type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sended_id', full_name='TFNSmessage.WeightArray.sended_id', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_WEIGHTARRAY_VEHICLEPAYLOAD, ],
  enum_types=[
    _WEIGHTARRAY_MSGSTATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=526,
  serialized_end=1036,
)

_COMMAND.fields_by_name['command_type'].enum_type = _COMMAND_COMMANDTYPE
_COMMAND.fields_by_name['platform_type'].enum_type = _COMMAND_PLATFORM
_COMMAND.fields_by_name['request_type'].enum_type = _COMMAND_REQUESTTYPE
_COMMAND_COMMANDTYPE.containing_type = _COMMAND
_COMMAND_PLATFORM.containing_type = _COMMAND
_COMMAND_REQUESTTYPE.containing_type = _COMMAND
_WEIGHTARRAY_VEHICLEPAYLOAD.containing_type = _WEIGHTARRAY
_WEIGHTARRAY.fields_by_name['payload'].message_type = _WEIGHTARRAY_VEHICLEPAYLOAD
_WEIGHTARRAY.fields_by_name['msg_status'].enum_type = _WEIGHTARRAY_MSGSTATUS
_WEIGHTARRAY.fields_by_name['request_type'].enum_type = _COMMAND_REQUESTTYPE
_WEIGHTARRAY_MSGSTATUS.containing_type = _WEIGHTARRAY
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['WeightArray'] = _WEIGHTARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND,
  __module__ = 'tf_ns_msg_pb2'
  # @@protoc_insertion_point(class_scope:TFNSmessage.Command)
  ))
_sym_db.RegisterMessage(Command)

WeightArray = _reflection.GeneratedProtocolMessageType('WeightArray', (_message.Message,), dict(

  VehiclePayload = _reflection.GeneratedProtocolMessageType('VehiclePayload', (_message.Message,), dict(
    DESCRIPTOR = _WEIGHTARRAY_VEHICLEPAYLOAD,
    __module__ = 'tf_ns_msg_pb2'
    # @@protoc_insertion_point(class_scope:TFNSmessage.WeightArray.VehiclePayload)
    ))
  ,
  DESCRIPTOR = _WEIGHTARRAY,
  __module__ = 'tf_ns_msg_pb2'
  # @@protoc_insertion_point(class_scope:TFNSmessage.WeightArray)
  ))
_sym_db.RegisterMessage(WeightArray)
_sym_db.RegisterMessage(WeightArray.VehiclePayload)


_WEIGHTARRAY_VEHICLEPAYLOAD.fields_by_name['weights'].has_options = True
_WEIGHTARRAY_VEHICLEPAYLOAD.fields_by_name['weights']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
