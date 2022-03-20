# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: addressbook.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61\x64\x64ressbook.proto\x12\x08tutorial\x1a\x1fgoogle/protobuf/timestamp.proto\"\x87\x02\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12,\n\x06phones\x18\x04 \x03(\x0b\x32\x1c.tutorial.Person.PhoneNumber\x12\x30\n\x0clast_updated\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1aG\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x01 \x01(\t\x12(\n\x04type\x18\x02 \x01(\x0e\x32\x1a.tutorial.Person.PhoneType\"+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04HOME\x10\x01\x12\x08\n\x04WORK\x10\x02\")\n\x06\x44\x61ta3d\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"X\n\x08Position\x12\x10\n\x08sensorId\x18\x01 \x01(\x04\x12\x16\n\x0etimestamp_usec\x18\x02 \x01(\x04\x12\"\n\x08position\x18\x03 \x01(\x0b\x32\x10.tutorial.Data3d\"/\n\x0b\x41\x64\x64ressBook\x12 \n\x06people\x18\x01 \x03(\x0b\x32\x10.tutorial.PersonBf\n\x1b\x63om.example.tutorial.protosB\x11\x41\x64\x64ressBookProtosP\x01Z\x0b../tutorial\xaa\x02$Google.Protobuf.Examples.AddressBookb\x06proto3')



_PERSON = DESCRIPTOR.message_types_by_name['Person']
_PERSON_PHONENUMBER = _PERSON.nested_types_by_name['PhoneNumber']
_DATA3D = DESCRIPTOR.message_types_by_name['Data3d']
_POSITION = DESCRIPTOR.message_types_by_name['Position']
_ADDRESSBOOK = DESCRIPTOR.message_types_by_name['AddressBook']
_PERSON_PHONETYPE = _PERSON.enum_types_by_name['PhoneType']
Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {

  'PhoneNumber' : _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), {
    'DESCRIPTOR' : _PERSON_PHONENUMBER,
    '__module__' : 'addressbook_pb2'
    # @@protoc_insertion_point(class_scope:tutorial.Person.PhoneNumber)
    })
  ,
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.Person)
  })
_sym_db.RegisterMessage(Person)
_sym_db.RegisterMessage(Person.PhoneNumber)

Data3d = _reflection.GeneratedProtocolMessageType('Data3d', (_message.Message,), {
  'DESCRIPTOR' : _DATA3D,
  '__module__' : 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.Data3d)
  })
_sym_db.RegisterMessage(Data3d)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.Position)
  })
_sym_db.RegisterMessage(Position)

AddressBook = _reflection.GeneratedProtocolMessageType('AddressBook', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESSBOOK,
  '__module__' : 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.AddressBook)
  })
_sym_db.RegisterMessage(AddressBook)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.example.tutorial.protosB\021AddressBookProtosP\001Z\013../tutorial\252\002$Google.Protobuf.Examples.AddressBook'
  _PERSON._serialized_start=65
  _PERSON._serialized_end=328
  _PERSON_PHONENUMBER._serialized_start=212
  _PERSON_PHONENUMBER._serialized_end=283
  _PERSON_PHONETYPE._serialized_start=285
  _PERSON_PHONETYPE._serialized_end=328
  _DATA3D._serialized_start=330
  _DATA3D._serialized_end=371
  _POSITION._serialized_start=373
  _POSITION._serialized_end=461
  _ADDRESSBOOK._serialized_start=463
  _ADDRESSBOOK._serialized_end=510
# @@protoc_insertion_point(module_scope)
