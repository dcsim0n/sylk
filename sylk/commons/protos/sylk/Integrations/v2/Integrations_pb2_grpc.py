# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from sylk.commons.protos.sylk.Integrations.v2 import Integrations_pb2 as sylk_dot_Integrations_dot_v2_dot_Integrations__pb2


class IntegrationsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetIntegration = channel.unary_unary(
                '/sylk.Integrations.v2.Integrations/GetIntegration',
                request_serializer=sylk_dot_Integrations_dot_v2_dot_Integrations__pb2.GetIntegrationRequest.SerializeToString,
                response_deserializer=sylk_dot_Integrations_dot_v2_dot_Integrations__pb2.GetIntegrationResponse.FromString,
                )


class IntegrationsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetIntegration(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IntegrationsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetIntegration': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIntegration,
                    request_deserializer=sylk_dot_Integrations_dot_v2_dot_Integrations__pb2.GetIntegrationRequest.FromString,
                    response_serializer=sylk_dot_Integrations_dot_v2_dot_Integrations__pb2.GetIntegrationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sylk.Integrations.v2.Integrations', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Integrations(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetIntegration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sylk.Integrations.v2.Integrations/GetIntegration',
            sylk_dot_Integrations_dot_v2_dot_Integrations__pb2.GetIntegrationRequest.SerializeToString,
            sylk_dot_Integrations_dot_v2_dot_Integrations__pb2.GetIntegrationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)