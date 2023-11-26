from typing import Optional

from ghostcoder.codeblocks.parser.java import JavaParser
from ghostcoder.codeblocks.parser.javascript import JavaScriptParser
from ghostcoder.codeblocks.parser.parser import CodeParser
from ghostcoder.codeblocks.parser.python import PythonParser
from ghostcoder.codeblocks.parser.typescript import TypeScriptParser


def create_parser(language: str, **kwargs) -> Optional[CodeParser]:
    if language == "java":
        return JavaParser(**kwargs)
    elif language == "python":
        return PythonParser(**kwargs)
    elif language == "typescript" or language == "tsx":
        return TypeScriptParser(language, **kwargs)
    elif language == "javascript" or language == "jsx":
        return JavaScriptParser(language, **kwargs)
    else:
        return CodeParser(language, **kwargs)
