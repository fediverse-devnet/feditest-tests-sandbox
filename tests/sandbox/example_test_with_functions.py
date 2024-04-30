"""
Simple example tests against a client and a server of the Sandbox protocol.

Each test is a independent, standalone function annotated with @test.
Each @test function runs independently of any other and can be invoked individually.

The parameters of the @test function are assigned by name to the nodes in the active
constellation, potentially after mapping per the TestPlan.
"""

from typing import List

from hamcrest import assert_that, equal_to

from feditest import test
from feditest.protocols.sandbox import SandboxLogEvent, SandboxMultClient, SandboxMultServer


@test
def example_test1(
        client: SandboxMultClient,
        server: SandboxMultServer
) -> None:
    a : int = 2
    b : int = 7

    server.start_logging()

    c = client.cause_mult(server, a, b)

    assert_that(c, equal_to(14))

    log: List[SandboxLogEvent] = server.get_and_clear_log()

    assert_that(len(log), equal_to(1))
    assert_that(log[0].a, equal_to(a))
    assert_that(log[0].b, equal_to(b))
    assert_that(log[0].c, equal_to(c))


@test
def example_test2(
        customer: SandboxMultClient,
        calculator: SandboxMultServer
) -> None:
    a : int = -7
    b : int = 8

    c = customer.cause_mult(calculator, a, b)

    assert_that(c, equal_to(-56))
