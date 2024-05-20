from feditest import SkipTestException, hard_assert_that, soft_assert_that, degrade_assert_that, test


@test
def hard() -> None:
    """
    Always raises a HardAssertionFailure.
    """
    hard_assert_that(False, 'This was hard!')


@test
def soft() -> None:
    """
    Always raises a SoftAssertionFailure.
    """
    soft_assert_that(False, 'This was soft!')


@test
def degrade() -> None:
    """
    Always raises a DegradeAssertionFailure.
    """
    degrade_assert_that(False, 'This is degraded!')


@test
def skip() -> None:
    """
    Always skips itself.
    """
    raise SkipTestException('We skipped this.')

