from feditest import SkipTestException, SpecLevel, InteropLevel, assert_that, test


@test
def default() -> None:
    """
    Always raises the default failure.
    """
    assert_that(False, 'This was the default!')


@test
def must() -> None:
    """
    Always raises an AssertionFailure with spec_level MUST.
    """
    assert_that(False, 'This was MUST!', spec_level=SpecLevel.MUST)


@test
def should() -> None:
    """
    Always raises an AssertionFailure with spec_level SHOULD.
    """
    assert_that(False, 'This was SHOULD!', spec_level=SpecLevel.SHOULD)


@test
def implied() -> None:
    """
    Always raises an AssertionFailure with spec_level IMPLIED.
    """
    assert_that(False, 'This was IMPLIED!', spec_level=SpecLevel.IMPLIED)


@test
def problem() -> None:
    """
    Always raises an AssertionFailure with interop_level PROBLEM.
    """
    assert_that(False, 'This is PROBLEM!', interop_level=InteropLevel.PROBLEM)


@test
def degraded() -> None:
    """
    Always raises an AssertionFailure with interop_level DEGRADED.
    """
    assert_that(False, 'This is DEGRADED!', interop_level=InteropLevel.DEGRADED)


@test
def unaffected() -> None:
    """
    Always raises an AssertionFailure with interop_level UNAFFECTED.
    """
    assert_that(False, 'This is UNAFFECTED!', interop_level=InteropLevel.UNAFFECTED)


@test
def unknown() -> None:
    """
    Always raises an AssertionFailure with interop_level UNKNOWN.
    """
    assert_that(False, 'This is UNKNOWN!', interop_level=InteropLevel.UNKNOWN)


@test
def must_problem() -> None:
    """
    Always raises an AssertionFailure with spec_level MUST, interop_level PROBLEM
    """
    assert_that(False, 'This was MUST, PROBLEM!', spec_level=SpecLevel.MUST, interop_level=InteropLevel.PROBLEM)


@test
def must_degraded() -> None:
    """
    Always raises an AssertionFailure with spec_level MUST, interop_level DEGRADED
    """
    assert_that(False, 'This was MUST, DEGRADED!', spec_level=SpecLevel.MUST, interop_level=InteropLevel.DEGRADED)


@test
def must_unaffected() -> None:
    """
    Always raises an AssertionFailure with spec_level MUST, interop_level UNAFFECTED
    """
    assert_that(False, 'This was MUST, UNAFFECTED!', spec_level=SpecLevel.MUST, interop_level=InteropLevel.UNAFFECTED)


@test
def must_unknown() -> None:
    """
    Always raises an AssertionFailure with spec_level MUST, interop_level UNKNOWN
    """
    assert_that(False, 'This was MUST, UNKNOWN!', spec_level=SpecLevel.MUST, interop_level=InteropLevel.UNKNOWN)


@test
def should_problem() -> None:
    """
    Always raises an AssertionFailure with spec_level SHOULD, interop_level PROBLEM
    """
    assert_that(False, 'This was SHOULD, PROBLEM!', spec_level=SpecLevel.SHOULD, interop_level=InteropLevel.PROBLEM)


@test
def should_degraded() -> None:
    """
    Always raises an AssertionFailure with spec_level SHOULD, interop_level DEGRADED
    """
    assert_that(False, 'This was SHOULD, DEGRADED!', spec_level=SpecLevel.SHOULD, interop_level=InteropLevel.DEGRADED)


@test
def should_unaffected() -> None:
    """
    Always raises an AssertionFailure with spec_level SHOULD, interop_level UNAFFECTED
    """
    assert_that(False, 'This was SHOULD, UNAFFECTED!', spec_level=SpecLevel.SHOULD, interop_level=InteropLevel.UNAFFECTED)


@test
def should_unkown() -> None:
    """
    Always raises an AssertionFailure with spec_level SHOULD, interop_level UNKNOWN
    """
    assert_that(False, 'This was SHOULD, UNKNOWN!', spec_level=SpecLevel.SHOULD, interop_level=InteropLevel.UNKNOWN)


@test
def implied_problem() -> None:
    """
    Always raises an AssertionFailure with spec_level IMPLIED, interop_level PROBLEM
    """
    assert_that(False, 'This was IMPLIED, PROBLEM!', spec_level=SpecLevel.IMPLIED, interop_level=InteropLevel.PROBLEM)


@test
def implied_degraded() -> None:
    """
    Always raises an AssertionFailure with spec_level IMPLIED, interop_level DEGRADED
    """
    assert_that(False, 'This was IMPLIED, DEGRADED!', spec_level=SpecLevel.IMPLIED, interop_level=InteropLevel.DEGRADED)


@test
def implied_unaffected() -> None:
    """
    Always raises an AssertionFailure with spec_level IMPLIED, interop_level UNAFFECTED
    """
    assert_that(False, 'This was IMPLIED, UNAFFECTED!', spec_level=SpecLevel.IMPLIED, interop_level=InteropLevel.UNAFFECTED)


@test
def implied_unknown() -> None:
    """
    Always raises an AssertionFailure with spec_level IMPLIED, interop_level UNKNOWN
    """
    assert_that(False, 'This was IMPLIED, UNKNOWN!', spec_level=SpecLevel.IMPLIED, interop_level=InteropLevel.UNKNOWN)


@test
def unspecified_problem() -> None:
    """
    Always raises an AssertionFailure with spec_level UNSPECIFIED, interop_level PROBLEM
    """
    assert_that(False, 'This was UNSPECIFIED, PROBLEM!', spec_level=SpecLevel.UNSPECIFIED, interop_level=InteropLevel.PROBLEM)


@test
def unspecified_degraded() -> None:
    """
    Always raises an AssertionFailure with spec_level UNSPECIFIED, interop_level DEGRADED
    """
    assert_that(False, 'This was UNSPECIFIED, DEGRADED!', spec_level=SpecLevel.UNSPECIFIED, interop_level=InteropLevel.DEGRADED)


@test
def unspecified_unaffected() -> None:
    """
    Always raises an AssertionFailure with spec_level UNSPECIFIED, interop_level UNAFFECTED
    """
    assert_that(False, 'This was UNSPECIFIED, UNAFFECTED!', spec_level=SpecLevel.UNSPECIFIED, interop_level=InteropLevel.UNAFFECTED)


@test
def unspecified_unknown() -> None:
    """
    Always raises an AssertionFailure with spec_level UNSPECIFIED, interop_level UNKNOWN
    """
    assert_that(False, 'This was UNSPECIFIED, UNKNOWN!', spec_level=SpecLevel.UNSPECIFIED, interop_level=InteropLevel.UNKNOWN)


@test
def skip() -> None:
    """
    Always skips itself.
    """
    raise SkipTestException('We skipped this.')

