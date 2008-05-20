import sys
import unittest
import platform

from test import support

class PlatformTest(unittest.TestCase):
    def test_architecture(self):
        res = platform.architecture()

    def test_machine(self):
        res = platform.machine()

    def test_node(self):
        res = platform.node()

    def test_platform(self):
        for aliased in (False, True):
            for terse in (False, True):
                res = platform.platform(aliased, terse)

    def test_processor(self):
        res = platform.processor()

    def test_python_build(self):
        res = platform.python_build()

    def test_python_compiler(self):
        res = platform.python_compiler()

    def test_version(self):
        res1 = platform.version()
        res2 = platform.version_tuple()
        self.assertEqual(res1, ".".join(res2))

    def test_release(self):
        res = platform.release()

    def test_system(self):
        res = platform.system()

    def test_version(self):
        res = platform.version()

    def test_system_alias(self):
        res = platform.system_alias(
            platform.system(),
            platform.release(),
            platform.version(),
        )

    def test_uname(self):
        res = platform.uname()
        self.assert_(any(res))

    def test_java_ver(self):
        res = platform.java_ver()
        if sys.platform == 'java':
            self.assert_(all(res))

    def test_win32_ver(self):
        res = platform.win32_ver()

    def test_mac_ver(self):
        res = platform.mac_ver()
        try:
            import gestalt
        except ImportError: pass
        else:
            if sys.platform == 'darwin':
                self.assert_(all(res))

    def test_dist(self):
        res = platform.dist()

    def test_libc_ver(self):
        import os
        if os.path.isdir(sys.executable) and \
           os.path.exists(sys.executable+'.exe'):
            # Cygwin horror
            executable = executable + '.exe'
        res = platform.libc_ver(sys.executable)

def test_main():
    support.run_unittest(
        PlatformTest
    )

if __name__ == '__main__':
    test_main()
