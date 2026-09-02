import unittest

from run import parser_arguments


class ParserArgumentsTest(unittest.TestCase):
    def test_supported_operations(self):
        for operation in ("r", "c", "t"):
            with self.subTest(operation=operation):
                self.assertEqual(parser_arguments([operation]).operate, operation)

    def test_unknown_operation_is_rejected(self):
        with self.assertRaises(SystemExit) as context:
            parser_arguments(["unknown"])
        self.assertEqual(context.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
