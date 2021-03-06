# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import transfer_pb2 as transfer__pb2


class TransferServiceStub(object):
  """TODO: use transfer lib
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.send = channel.stream_unary(
        '/com.webank.eggroll.core.transfer.TransferService/send',
        request_serializer=transfer__pb2.TransferBatch.SerializeToString,
        response_deserializer=transfer__pb2.TransferBatch.FromString,
        )
    self.recv = channel.unary_stream(
        '/com.webank.eggroll.core.transfer.TransferService/recv',
        request_serializer=transfer__pb2.TransferBatch.SerializeToString,
        response_deserializer=transfer__pb2.TransferBatch.FromString,
        )
    self.sendRecv = channel.stream_stream(
        '/com.webank.eggroll.core.transfer.TransferService/sendRecv',
        request_serializer=transfer__pb2.TransferBatch.SerializeToString,
        response_deserializer=transfer__pb2.TransferBatch.FromString,
        )


class TransferServiceServicer(object):
  """TODO: use transfer lib
  """

  def send(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def recv(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def sendRecv(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TransferServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'send': grpc.stream_unary_rpc_method_handler(
          servicer.send,
          request_deserializer=transfer__pb2.TransferBatch.FromString,
          response_serializer=transfer__pb2.TransferBatch.SerializeToString,
      ),
      'recv': grpc.unary_stream_rpc_method_handler(
          servicer.recv,
          request_deserializer=transfer__pb2.TransferBatch.FromString,
          response_serializer=transfer__pb2.TransferBatch.SerializeToString,
      ),
      'sendRecv': grpc.stream_stream_rpc_method_handler(
          servicer.sendRecv,
          request_deserializer=transfer__pb2.TransferBatch.FromString,
          response_serializer=transfer__pb2.TransferBatch.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.webank.eggroll.core.transfer.TransferService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
