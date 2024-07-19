from feditest import SpecLevel, InteropLevel, assert_that, step, test
from feditest.protocols import SkipTestException


@test
class Example:
    """
    A multi-step test class that raises various failures in different steps.
    """
    def __init__(self):
        pass


    @step
    def step1_default(self) -> None:
        """
        Always raises the default failure.
        """
        assert_that(False, 'This was the default!')


    @step
    def step2_must(self) -> None:
        """
        Always raises an AssertionFailure with spec_level MUST.
        """
        assert_that(False, 'This was MUST!', spec_level=SpecLevel.MUST)


    @step
    def step3_should(self) -> None:
        """
        Always raises an AssertionFailure with spec_level SHOULD.
        """
        assert_that(False, 'This was SHOULD!', spec_level=SpecLevel.SHOULD)


    @step
    def step4_implied(self) -> None:
        """
        Always raises an AssertionFailure with spec_level IMPLIED.
        """
        assert_that(False, 'This was IMPLIED!', spec_level=SpecLevel.IMPLIED)


    @step
    def step5_problem(self) -> None:
        """
        Always raises an AssertionFailure with interop_level PROBLEM.
        """
        assert_that(False, 'This is PROBLEM!', interop_level=InteropLevel.PROBLEM)


    @step
    def step6_degraded(self) -> None:
        """
        Always raises an AssertionFailure with interop_level DEGRADED.
        """
        assert_that(False, 'This is DEGRADED!', interop_level=InteropLevel.DEGRADED)


    @step
    def step7_unaffected(self) -> None:
        """
        Always raises an AssertionFailure with interop_level UNAFFECTED.
        """
        assert_that(False, 'This is UNAFFECTED!', interop_level=InteropLevel.UNAFFECTED)


    @step
    def step8_unknown(self) -> None:
        """
        Always raises an AssertionFailure with interop_level UNKNOWN.
        """
        assert_that(False, 'This is UNKNOWN!', interop_level=InteropLevel.UNKNOWN)


    @step
    def step9_must_problem(self) -> None:
        """
        Always raises an AssertionFailure with spec_level MUST, interop_level PROBLEM
        """
        assert_that(False, 'This was MUST, PROBLEM!', spec_level=SpecLevel.MUST, interop_level=InteropLevel.PROBLEM)


    @step
    def step10_must_degraded(self) -> None:
        """
        Always raises an AssertionFailure with spec_level MUST, interop_level DEGRADED
        """
        assert_that(False, 'This was MUST, DEGRADED!', spec_level=SpecLevel.MUST, interop_level=InteropLevel.DEGRADED)


    @step
    def step11_must_unaffected(self) -> None:
        """
        Always raises an AssertionFailure with spec_level MUST, interop_level UNAFFECTED
        """
        assert_that(False, 'This was MUST, UNAFFECTED!', spec_level=SpecLevel.MUST, interop_level=InteropLevel.UNAFFECTED)


    @step
    def step12_must_unknown(self) -> None:
        """
        Always raises an AssertionFailure with spec_level MUST, interop_level UNKNOWN
        """
        assert_that(False, 'This was MUST, UNKNOWN!', spec_level=SpecLevel.MUST, interop_level=InteropLevel.UNKNOWN)


    @step
    def step13_should_problem(self) -> None:
        """
        Always raises an AssertionFailure with spec_level SHOULD, interop_level PROBLEM
        """
        assert_that(False, 'This was SHOULD, PROBLEM!', spec_level=SpecLevel.SHOULD, interop_level=InteropLevel.PROBLEM)


    @step
    def step14_should_degraded(self) -> None:
        """
        Always raises an AssertionFailure with spec_level SHOULD, interop_level DEGRADED
        """
        assert_that(False, 'This was SHOULD, DEGRADED!', spec_level=SpecLevel.SHOULD, interop_level=InteropLevel.DEGRADED)


    @step
    def step15_should_unaffected(self) -> None:
        """
        Always raises an AssertionFailure with spec_level SHOULD, interop_level UNAFFECTED
        """
        assert_that(False, 'This was SHOULD, UNAFFECTED!', spec_level=SpecLevel.SHOULD, interop_level=InteropLevel.UNAFFECTED)


    @step
    def step16_should_unkown(self) -> None:
        """
        Always raises an AssertionFailure with spec_level SHOULD, interop_level UNKNOWN
        """
        assert_that(False, 'This was SHOULD, UNKNOWN!', spec_level=SpecLevel.SHOULD, interop_level=InteropLevel.UNKNOWN)


    @step
    def step17_implied_problem(self) -> None:
        """
        Always raises an AssertionFailure with spec_level IMPLIED, interop_level PROBLEM
        """
        assert_that(False, 'This was IMPLIED, PROBLEM!', spec_level=SpecLevel.IMPLIED, interop_level=InteropLevel.PROBLEM)


    @step
    def step18_implied_degraded(self) -> None:
        """
        Always raises an AssertionFailure with spec_level IMPLIED, interop_level DEGRADED
        """
        assert_that(False, 'This was IMPLIED, DEGRADED!', spec_level=SpecLevel.IMPLIED, interop_level=InteropLevel.DEGRADED)


    @step
    def step19_implied_unaffected(self) -> None:
        """
        Always raises an AssertionFailure with spec_level IMPLIED, interop_level UNAFFECTED
        """
        assert_that(False, 'This was IMPLIED, UNAFFECTED!', spec_level=SpecLevel.IMPLIED, interop_level=InteropLevel.UNAFFECTED)


    @step
    def step20_implied_unknown(self) -> None:
        """
        Always raises an AssertionFailure with spec_level IMPLIED, interop_level UNKNOWN
        """
        assert_that(False, 'This was IMPLIED, UNKNOWN!', spec_level=SpecLevel.IMPLIED, interop_level=InteropLevel.UNKNOWN)


    @step
    def step21_unspecified_problem(self) -> None:
        """
        Always raises an AssertionFailure with spec_level UNSPECIFIED, interop_level PROBLEM
        """
        assert_that(False, 'This was UNSPECIFIED, PROBLEM!', spec_level=SpecLevel.UNSPECIFIED, interop_level=InteropLevel.PROBLEM)


    @step
    def step22_unspecified_degraded(self) -> None:
        """
        Always raises an AssertionFailure with spec_level UNSPECIFIED, interop_level DEGRADED
        """
        assert_that(False, 'This was UNSPECIFIED, DEGRADED!', spec_level=SpecLevel.UNSPECIFIED, interop_level=InteropLevel.DEGRADED)


    @step
    def step23_unspecified_unaffected(self) -> None:
        """
        Always raises an AssertionFailure with spec_level UNSPECIFIED, interop_level UNAFFECTED
        """
        assert_that(False, 'This was UNSPECIFIED, UNAFFECTED!', spec_level=SpecLevel.UNSPECIFIED, interop_level=InteropLevel.UNAFFECTED)


    @step
    def step24_unspecified_unknown(self) -> None:
        """
        Always raises an AssertionFailure with spec_level UNSPECIFIED, interop_level UNKNOWN
        """
        assert_that(False, 'This was UNSPECIFIED, UNKNOWN!', spec_level=SpecLevel.UNSPECIFIED, interop_level=InteropLevel.UNKNOWN)


    @step
    def step25_skip(self) -> None:
        """
        Always skips itself.
        """
        raise SkipTestException('We skipped this.')

