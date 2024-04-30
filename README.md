## Feditest-test-sandbox: a sandbox protocol to try FediTest with

This repo contains:

* test cases

to try out [FediTest](https://feditest.org/), the testing framework for distributed, heterogeneous systems communicating with complex protocols, such as the Fediverse. FediTest tests for the Fediverse are [here](../feditest-tests-fediverse/).

### To try it out

1. Install `feditest`
1. Check out this repo
1. `feditest run --tap`

This emit a TAP-formatted test report. Most tests pass, but not all.

### What just happened?

You executed FediTest test plan `feditest-default.json`. If you look at the file, you see:

* There are two sessions
* Each runs three tests. They are the same tests in both sessions.
* But the constellations -- which nodes are involved running which implementations of the sandbox protocol -- are different
* One of the implementations is correct, and the other one is faulty.

### How can I run something else than `feditest-default.json`?

You can:

* Manually edit `feditest-default.json`.
* Well, maybe you want to make a copy `cp feditest-default.json feditest-play.json`, edit that, and then run `feditest run --testplan feditest-play.json --tap`
* Run `feditest generate-testplan --session-template session-templates/example-session-all.json --constellation constellations/* --out feditest-play.json` to regenerate a test plan that runs the specified session template against all the constellations defined in that directory.
* Or try out different constellations, or a different session template.
