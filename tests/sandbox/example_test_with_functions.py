"""
Simple example tests against a client and a server of the Sandbox protocol.

Each test is a independent, standalone function annotated with @test.
Each @test function runs independently of any other and can be invoked individually.

The parameters of the @test function are assigned by name to the nodes in the active
constellation, potentially after mapping per the TestPlan.
"""

from typing import List

from hamcrest import close_to, equal_to

from feditest import hard_assert_that, soft_assert_that, test
from feditest.protocols.sandbox import SandboxLogEvent, SandboxMultClient, SandboxMultServer


@test
def example_test1(
        client: SandboxMultClient,
        server: SandboxMultServer
) -> None:
    """
    Tests the sandbox toy protocol using a FedTest test function with hard asserts.
    """
    a : float = 2
    b : int = 7

    server.start_logging()

    c : float = client.cause_mult(server, a, b)

    hard_assert_that(c, equal_to(14.0))

    log: List[SandboxLogEvent] = server.get_and_clear_log()

    hard_assert_that(len(log), equal_to(1))
    hard_assert_that(log[0].a, equal_to(a))
    hard_assert_that(log[0].b, equal_to(b))
    hard_assert_that(log[0].c, equal_to(c))


@test
def example_test2(
        customer: SandboxMultClient,
        calculator: SandboxMultServer
) -> None:
    """
    Tests the sandbox toy protocol using a FedTest test function with hard asserts.
    """
    a : float = 2.1
    b : int = 7

    c : float = customer.cause_mult(calculator, a, b)

    soft_assert_that(c, equal_to(14.0))


@test
def example_test3(
        client: SandboxMultClient,
        server: SandboxMultServer
) -> None:
    """
    Tests the sandbox toy protocol using a FedTest test function.
    """
    a : int = -7
    b : int = 8

    c = client.cause_mult(server, a, b)

    hard_assert_that(c, equal_to(a * b))
