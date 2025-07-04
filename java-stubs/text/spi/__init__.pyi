
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.text
import java.util
import java.util.spi
import typing



class BreakIteratorProvider(java.util.spi.LocaleServiceProvider):
    def getCharacterInstance(self, locale: java.util.Locale) -> java.text.BreakIterator: ...
    def getLineInstance(self, locale: java.util.Locale) -> java.text.BreakIterator: ...
    def getSentenceInstance(self, locale: java.util.Locale) -> java.text.BreakIterator: ...
    def getWordInstance(self, locale: java.util.Locale) -> java.text.BreakIterator: ...

class CollatorProvider(java.util.spi.LocaleServiceProvider):
    def getInstance(self, locale: java.util.Locale) -> java.text.Collator: ...

class DateFormatProvider(java.util.spi.LocaleServiceProvider):
    def getDateInstance(self, int: int, locale: java.util.Locale) -> java.text.DateFormat: ...
    def getDateTimeInstance(self, int: int, int2: int, locale: java.util.Locale) -> java.text.DateFormat: ...
    def getTimeInstance(self, int: int, locale: java.util.Locale) -> java.text.DateFormat: ...

class DateFormatSymbolsProvider(java.util.spi.LocaleServiceProvider):
    def getInstance(self, locale: java.util.Locale) -> java.text.DateFormatSymbols: ...

class DecimalFormatSymbolsProvider(java.util.spi.LocaleServiceProvider):
    def getInstance(self, locale: java.util.Locale) -> java.text.DecimalFormatSymbols: ...

class NumberFormatProvider(java.util.spi.LocaleServiceProvider):
    def getCompactNumberInstance(self, locale: java.util.Locale, style: java.text.NumberFormat.Style) -> java.text.NumberFormat: ...
    def getCurrencyInstance(self, locale: java.util.Locale) -> java.text.NumberFormat: ...
    def getIntegerInstance(self, locale: java.util.Locale) -> java.text.NumberFormat: ...
    def getNumberInstance(self, locale: java.util.Locale) -> java.text.NumberFormat: ...
    def getPercentInstance(self, locale: java.util.Locale) -> java.text.NumberFormat: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.text.spi")``.

    BreakIteratorProvider: typing.Type[BreakIteratorProvider]
    CollatorProvider: typing.Type[CollatorProvider]
    DateFormatProvider: typing.Type[DateFormatProvider]
    DateFormatSymbolsProvider: typing.Type[DateFormatSymbolsProvider]
    DecimalFormatSymbolsProvider: typing.Type[DecimalFormatSymbolsProvider]
    NumberFormatProvider: typing.Type[NumberFormatProvider]
