from typing import Any

from feditest import test
from feditest.protocols import (
    Node,
    NodeDriver,
    NodeSpecificationInsufficientError,
    NodeSpecificationInvalidError,
    NotImplementedByNodeDriverError,
    NotImplementedByNodeError
)


class DummyNode(Node):
    def missing_method(self):
        pass


class DummyNodeDriver(NodeDriver):
    def __init__(self):
        super().__init__('Dummy for testing only')


    def _provision_node(self, rolename: str, parameters: dict[str,Any]) -> Node:
        return DummyNode(rolename, parameters, self)


    def missing_method(self):
        pass


@test
def not_implemented_by_node_error() -> None:
    """
    A Node does not implement a method.
    """
    driver = DummyNodeDriver()
    node = driver.provision_node('testrole', [])

    raise NotImplementedByNodeError(node, DummyNode.missing_method)


@test
def not_implemented_by_node_driver_error() -> None:
    """
    A NodeDriver does not implement a method.
    """
    driver = DummyNodeDriver()
    raise NotImplementedByNodeDriverError(driver, DummyNodeDriver.missing_method)


@test
def node_specification_insufficient_error() -> None:
    """
    Not enough parameters have been provided to create the Node.
    """
    driver = DummyNodeDriver()
    raise NodeSpecificationInsufficientError(driver, 'Some important parameter is missing')


@test
def node_specification_invalid_error() -> None:
    """
    An invalid parameter has been provided to create the Node.
    """
    driver = DummyNodeDriver()
    raise NodeSpecificationInvalidError(driver, 'myparam', 'Some parameter is invalid')

