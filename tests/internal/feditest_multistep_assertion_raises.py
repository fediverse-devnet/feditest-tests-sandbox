from feditest import hard_assert_that, soft_assert_that, degrade_assert_that, step, test


@test
class Example:
    """
    A multi-step test class that raises various failures in different steps.
    """
    def __init__(self):
        pass


    @step
    def step1_pass(self) -> None:
        return


    @step
    def step2_soft(self) -> None:
        soft_assert_that(False, 'That was soft!')


    @step
    def step3_pass(self) -> None:
        return


    @step
    def step4_degrade(self) -> None:
        degrade_assert_that(False, 'We are degraded!')


    @step
    def step5_hard(self) -> None:
        hard_assert_that(False, 'That was hard!')


    @step
    def step6_pass(self) -> None:
        return

