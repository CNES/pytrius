
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import java.util.function
import java.util.stream
import typing



class MatchResult:
    @typing.overload
    def end(self) -> int: ...
    @typing.overload
    def end(self, int: int) -> int: ...
    @typing.overload
    def end(self, string: str) -> int: ...
    @typing.overload
    def group(self) -> str: ...
    @typing.overload
    def group(self, int: int) -> str: ...
    @typing.overload
    def group(self, string: str) -> str: ...
    def groupCount(self) -> int: ...
    def hasMatch(self) -> bool: ...
    def namedGroups(self) -> java.util.Map[str, int]: ...
    @typing.overload
    def start(self) -> int: ...
    @typing.overload
    def start(self, int: int) -> int: ...
    @typing.overload
    def start(self, string: str) -> int: ...

class Pattern(java.io.Serializable):
    UNIX_LINES: typing.ClassVar[int] = ...
    CASE_INSENSITIVE: typing.ClassVar[int] = ...
    COMMENTS: typing.ClassVar[int] = ...
    MULTILINE: typing.ClassVar[int] = ...
    LITERAL: typing.ClassVar[int] = ...
    DOTALL: typing.ClassVar[int] = ...
    UNICODE_CASE: typing.ClassVar[int] = ...
    CANON_EQ: typing.ClassVar[int] = ...
    UNICODE_CHARACTER_CLASS: typing.ClassVar[int] = ...
    def asMatchPredicate(self) -> java.util.function.Predicate[str]: ...
    def asPredicate(self) -> java.util.function.Predicate[str]: ...
    @typing.overload
    @staticmethod
    def compile(string: str) -> 'Pattern': ...
    @typing.overload
    @staticmethod
    def compile(string: str, int: int) -> 'Pattern': ...
    def flags(self) -> int: ...
    def matcher(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> 'Matcher': ...
    @staticmethod
    def matches(string: str, charSequence: typing.Union[java.lang.CharSequence, str]) -> bool: ...
    def namedGroups(self) -> java.util.Map[str, int]: ...
    def pattern(self) -> str: ...
    @staticmethod
    def quote(string: str) -> str: ...
    @typing.overload
    def split(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> typing.MutableSequence[str]: ...
    @typing.overload
    def split(self, charSequence: typing.Union[java.lang.CharSequence, str], int: int) -> typing.MutableSequence[str]: ...
    def splitAsStream(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> java.util.stream.Stream[str]: ...
    def splitWithDelimiters(self, charSequence: typing.Union[java.lang.CharSequence, str], int: int) -> typing.MutableSequence[str]: ...
    def toString(self) -> str: ...

class PatternSyntaxException(java.lang.IllegalArgumentException):
    def __init__(self, string: str, string2: str, int: int): ...
    def getDescription(self) -> str: ...
    def getIndex(self) -> int: ...
    def getMessage(self) -> str: ...
    def getPattern(self) -> str: ...

class Matcher(MatchResult):
    @typing.overload
    def appendReplacement(self, stringBuffer: java.lang.StringBuffer, string2: str) -> 'Matcher': ...
    @typing.overload
    def appendReplacement(self, stringBuilder: java.lang.StringBuilder, string2: str) -> 'Matcher': ...
    @typing.overload
    def appendTail(self, stringBuffer: java.lang.StringBuffer) -> java.lang.StringBuffer: ...
    @typing.overload
    def appendTail(self, stringBuilder: java.lang.StringBuilder) -> java.lang.StringBuilder: ...
    @typing.overload
    def end(self) -> int: ...
    @typing.overload
    def end(self, int: int) -> int: ...
    @typing.overload
    def end(self, string: str) -> int: ...
    @typing.overload
    def find(self) -> bool: ...
    @typing.overload
    def find(self, int: int) -> bool: ...
    @typing.overload
    def group(self) -> str: ...
    @typing.overload
    def group(self, int: int) -> str: ...
    @typing.overload
    def group(self, string: str) -> str: ...
    def groupCount(self) -> int: ...
    def hasAnchoringBounds(self) -> bool: ...
    def hasMatch(self) -> bool: ...
    def hasTransparentBounds(self) -> bool: ...
    def hitEnd(self) -> bool: ...
    def lookingAt(self) -> bool: ...
    def matches(self) -> bool: ...
    def namedGroups(self) -> java.util.Map[str, int]: ...
    def pattern(self) -> Pattern: ...
    @staticmethod
    def quoteReplacement(string: str) -> str: ...
    def region(self, int: int, int2: int) -> 'Matcher': ...
    def regionEnd(self) -> int: ...
    def regionStart(self) -> int: ...
    @typing.overload
    def replaceAll(self, string: str) -> str: ...
    @typing.overload
    def replaceAll(self, function: typing.Union[java.util.function.Function[MatchResult, str], typing.Callable[[MatchResult], str]]) -> str: ...
    @typing.overload
    def replaceFirst(self, string: str) -> str: ...
    @typing.overload
    def replaceFirst(self, function: typing.Union[java.util.function.Function[MatchResult, str], typing.Callable[[MatchResult], str]]) -> str: ...
    def requireEnd(self) -> bool: ...
    @typing.overload
    def reset(self) -> 'Matcher': ...
    @typing.overload
    def reset(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> 'Matcher': ...
    def results(self) -> java.util.stream.Stream[MatchResult]: ...
    @typing.overload
    def start(self) -> int: ...
    @typing.overload
    def start(self, int: int) -> int: ...
    @typing.overload
    def start(self, string: str) -> int: ...
    def toMatchResult(self) -> MatchResult: ...
    def toString(self) -> str: ...
    def useAnchoringBounds(self, boolean: bool) -> 'Matcher': ...
    def usePattern(self, pattern: Pattern) -> 'Matcher': ...
    def useTransparentBounds(self, boolean: bool) -> 'Matcher': ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.util.regex")``.

    MatchResult: typing.Type[MatchResult]
    Matcher: typing.Type[Matcher]
    Pattern: typing.Type[Pattern]
    PatternSyntaxException: typing.Type[PatternSyntaxException]
