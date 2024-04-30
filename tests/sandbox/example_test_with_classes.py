"""
Simple example tests against a client and a server of the Sandbox protocol.

Each test consists of multiple steps. The steps in a test are collected in a
class annotated with @test. Each individual step is a member function annotated
with @step. They are executed in sequence.

Each @test class runs independently of any other and can be invoked individually.
Each @step can only be invoked as part of running the @test class. However,
the @steps share the same @test class instance, they can share state.

The parameters of the constructor of the @test class are assigned by name to the nodes
in the active constellation, potentially after mapping per the TestPlan. By
storing them as part of the @test class instance, the @steps can access them.
"""

from typing import List

from hamcrest import assert_that, equal_to

from feditest import step, test
from feditest.protocols.sandbox import SandboxLogEvent, SandboxMultClient, SandboxMultServer


@test
class ExampleTest1:
    def __init__(self,
        client: SandboxMultClient,
        server: SandboxMultServer
    ) -> None:
        self.client = client
        self.server = server

    @step
    def step1(self):
        a : int = 2
        b : int = 7

        self.server.start_logging()

        c = self.client.cause_mult(self.server, a, b)

        assert_that(c, equal_to(14))

        log: List[SandboxLogEvent] = self.server.get_and_clear_log()

        assert_that(len(log), equal_to(1))
        assert_that(log[0].a, equal_to(a))
        assert_that(log[0].b, equal_to(b))
        assert_that(log[0].c, equal_to(c))

        self.c = c

    @step
    def step2(self):

        c_squared = self.client.cause_mult(self.server, self.c, self.c)

        assert_that(c_squared, equal_to(self.c * self.c))