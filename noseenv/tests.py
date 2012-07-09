import os, sys, unittest


class SimpleTests(unittest.TestCase):

    def test_simple(self):
        if '--env' in sys.argv:
            # If called by FancyTests.test_env then we expect environment
            # variables to be set
            self.assertEqual(os.getenv('NOSEENV_TEST_1'), 'foo')
            self.assertEqual(os.getenv('NOSEENV_TEST_2'), 'bar')
        else:
            # If not called with --env, then we should see variables set to
            # None; otherwise they must be set in the environment, which would
            # be baaad.
            self.assertEqual(os.getenv('NOSEENV_TEST_1'), None)
            self.assertEqual(os.getenv('NOSEENV_TEST_2'), None)


class FancyTests(unittest.TestCase):

    def test_env(self):
        print("*** sys.executable = %r" % sys.executable)
        print("*** sys.argv = %r" % sys.argv)
        ret = os.system(sys.argv[0] +
                        " --env NOSEENV_TEST_1=foo"
                        " --env NOSEENV_TEST_2=bar"
                        " noseenv.tests:SimpleTests")
        self.assertEqual(ret, 0)
