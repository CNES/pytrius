
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import datetime
import java
import java.io
import java.lang
import java.time
import java.time.format
import java.time.temporal
import java.util
import typing



class ChronoLocalDate(java.time.temporal.Temporal, java.time.temporal.TemporalAdjuster, java.lang.Comparable['ChronoLocalDate']):
    def adjustInto(self, temporal: java.time.temporal.Temporal) -> java.time.temporal.Temporal: ...
    def atTime(self, localTime: java.time.LocalTime) -> 'ChronoLocalDateTime'[typing.Any]: ...
    def compareTo(self, chronoLocalDate: 'ChronoLocalDate') -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def format(self, dateTimeFormatter: java.time.format.DateTimeFormatter) -> str: ...
    @staticmethod
    def from_(temporalAccessor: java.time.temporal.TemporalAccessor) -> 'ChronoLocalDate': ...
    def getChronology(self) -> 'Chronology': ...
    def getEra(self) -> 'Era': ...
    def hashCode(self) -> int: ...
    def isAfter(self, chronoLocalDate: 'ChronoLocalDate') -> bool: ...
    def isBefore(self, chronoLocalDate: 'ChronoLocalDate') -> bool: ...
    def isEqual(self, chronoLocalDate: 'ChronoLocalDate') -> bool: ...
    def isLeapYear(self) -> bool: ...
    @typing.overload
    def isSupported(self, temporalField: java.time.temporal.TemporalField) -> bool: ...
    @typing.overload
    def isSupported(self, temporalUnit: java.time.temporal.TemporalUnit) -> bool: ...
    def lengthOfMonth(self) -> int: ...
    def lengthOfYear(self) -> int: ...
    @typing.overload
    def minus(self, temporalAmount: java.time.temporal.TemporalAmount) -> 'ChronoLocalDate': ...
    @typing.overload
    def minus(self, long: int, temporalUnit: java.time.temporal.TemporalUnit) -> 'ChronoLocalDate': ...
    @typing.overload
    def plus(self, temporalAmount: java.time.temporal.TemporalAmount) -> 'ChronoLocalDate': ...
    @typing.overload
    def plus(self, long: int, temporalUnit: java.time.temporal.TemporalUnit) -> 'ChronoLocalDate': ...
    _query__R = typing.TypeVar('_query__R')  # <R>
    def query(self, temporalQuery: typing.Union[java.time.temporal.TemporalQuery[_query__R], typing.Callable[[java.time.temporal.TemporalAccessor], _query__R]]) -> _query__R: ...
    @staticmethod
    def timeLineOrder() -> java.util.Comparator['ChronoLocalDate']: ...
    def toEpochDay(self) -> int: ...
    def toString(self) -> str: ...
    @typing.overload
    def until(self, chronoLocalDate: 'ChronoLocalDate') -> 'ChronoPeriod': ...
    @typing.overload
    def until(self, temporal: java.time.temporal.Temporal, temporalUnit: java.time.temporal.TemporalUnit) -> int: ...
    @typing.overload
    def with_(self, temporalAdjuster: typing.Union[java.time.temporal.TemporalAdjuster, typing.Callable]) -> 'ChronoLocalDate': ...
    @typing.overload
    def with_(self, temporalField: java.time.temporal.TemporalField, long: int) -> 'ChronoLocalDate': ...

_ChronoLocalDateTime__D = typing.TypeVar('_ChronoLocalDateTime__D', bound=ChronoLocalDate)  # <D>
class ChronoLocalDateTime(java.time.temporal.Temporal, java.time.temporal.TemporalAdjuster, java.lang.Comparable['ChronoLocalDateTime'[typing.Any]], typing.Generic[_ChronoLocalDateTime__D]):
    def adjustInto(self, temporal: java.time.temporal.Temporal) -> java.time.temporal.Temporal: ...
    def atZone(self, zoneId: java.time.ZoneId) -> 'ChronoZonedDateTime'[_ChronoLocalDateTime__D]: ...
    def compareTo(self, chronoLocalDateTime: 'ChronoLocalDateTime'[typing.Any]) -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def format(self, dateTimeFormatter: java.time.format.DateTimeFormatter) -> str: ...
    @staticmethod
    def from_(temporalAccessor: java.time.temporal.TemporalAccessor) -> 'ChronoLocalDateTime'[typing.Any]: ...
    def getChronology(self) -> 'Chronology': ...
    def hashCode(self) -> int: ...
    def isAfter(self, chronoLocalDateTime: 'ChronoLocalDateTime'[typing.Any]) -> bool: ...
    def isBefore(self, chronoLocalDateTime: 'ChronoLocalDateTime'[typing.Any]) -> bool: ...
    def isEqual(self, chronoLocalDateTime: 'ChronoLocalDateTime'[typing.Any]) -> bool: ...
    @typing.overload
    def isSupported(self, temporalField: java.time.temporal.TemporalField) -> bool: ...
    @typing.overload
    def isSupported(self, temporalUnit: java.time.temporal.TemporalUnit) -> bool: ...
    @typing.overload
    def minus(self, temporalAmount: java.time.temporal.TemporalAmount) -> 'ChronoLocalDateTime'[_ChronoLocalDateTime__D]: ...
    @typing.overload
    def minus(self, long: int, temporalUnit: java.time.temporal.TemporalUnit) -> 'ChronoLocalDateTime'[_ChronoLocalDateTime__D]: ...
    @typing.overload
    def plus(self, long: int, temporalUnit: java.time.temporal.TemporalUnit) -> 'ChronoLocalDateTime'[_ChronoLocalDateTime__D]: ...
    @typing.overload
    def plus(self, temporalAmount: java.time.temporal.TemporalAmount) -> 'ChronoLocalDateTime'[_ChronoLocalDateTime__D]: ...
    _query__R = typing.TypeVar('_query__R')  # <R>
    def query(self, temporalQuery: typing.Union[java.time.temporal.TemporalQuery[_query__R], typing.Callable[[java.time.temporal.TemporalAccessor], _query__R]]) -> _query__R: ...
    @staticmethod
    def timeLineOrder() -> java.util.Comparator['ChronoLocalDateTime'[typing.Any]]: ...
    def toEpochSecond(self, zoneOffset: java.time.ZoneOffset) -> int: ...
    def toInstant(self, zoneOffset: java.time.ZoneOffset) -> java.time.Instant: ...
    def toLocalDate(self) -> _ChronoLocalDateTime__D: ...
    def toLocalTime(self) -> java.time.LocalTime: ...
    def toString(self) -> str: ...
    @typing.overload
    def with_(self, temporalField: java.time.temporal.TemporalField, long: int) -> 'ChronoLocalDateTime'[_ChronoLocalDateTime__D]: ...
    @typing.overload
    def with_(self, temporalAdjuster: typing.Union[java.time.temporal.TemporalAdjuster, typing.Callable]) -> 'ChronoLocalDateTime'[_ChronoLocalDateTime__D]: ...

class ChronoPeriod(java.time.temporal.TemporalAmount):
    def addTo(self, temporal: java.time.temporal.Temporal) -> java.time.temporal.Temporal: ...
    @staticmethod
    def between(chronoLocalDate: ChronoLocalDate, chronoLocalDate2: ChronoLocalDate) -> 'ChronoPeriod': ...
    def equals(self, object: typing.Any) -> bool: ...
    def get(self, temporalUnit: java.time.temporal.TemporalUnit) -> int: ...
    def getChronology(self) -> 'Chronology': ...
    def getUnits(self) -> java.util.List[java.time.temporal.TemporalUnit]: ...
    def hashCode(self) -> int: ...
    def isNegative(self) -> bool: ...
    def isZero(self) -> bool: ...
    def minus(self, temporalAmount: java.time.temporal.TemporalAmount) -> 'ChronoPeriod': ...
    def multipliedBy(self, int: int) -> 'ChronoPeriod': ...
    def negated(self) -> 'ChronoPeriod': ...
    def normalized(self) -> 'ChronoPeriod': ...
    def plus(self, temporalAmount: java.time.temporal.TemporalAmount) -> 'ChronoPeriod': ...
    def subtractFrom(self, temporal: java.time.temporal.Temporal) -> java.time.temporal.Temporal: ...
    def toString(self) -> str: ...

_ChronoZonedDateTime__D = typing.TypeVar('_ChronoZonedDateTime__D', bound=ChronoLocalDate)  # <D>
class ChronoZonedDateTime(java.time.temporal.Temporal, java.lang.Comparable['ChronoZonedDateTime'[typing.Any]], typing.Generic[_ChronoZonedDateTime__D]):
    def compareTo(self, chronoZonedDateTime: 'ChronoZonedDateTime'[typing.Any]) -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def format(self, dateTimeFormatter: java.time.format.DateTimeFormatter) -> str: ...
    @staticmethod
    def from_(temporalAccessor: java.time.temporal.TemporalAccessor) -> 'ChronoZonedDateTime'[typing.Any]: ...
    def get(self, temporalField: java.time.temporal.TemporalField) -> int: ...
    def getChronology(self) -> 'Chronology': ...
    def getLong(self, temporalField: java.time.temporal.TemporalField) -> int: ...
    def getOffset(self) -> java.time.ZoneOffset: ...
    def getZone(self) -> java.time.ZoneId: ...
    def hashCode(self) -> int: ...
    def isAfter(self, chronoZonedDateTime: 'ChronoZonedDateTime'[typing.Any]) -> bool: ...
    def isBefore(self, chronoZonedDateTime: 'ChronoZonedDateTime'[typing.Any]) -> bool: ...
    def isEqual(self, chronoZonedDateTime: 'ChronoZonedDateTime'[typing.Any]) -> bool: ...
    @typing.overload
    def isSupported(self, temporalField: java.time.temporal.TemporalField) -> bool: ...
    @typing.overload
    def isSupported(self, temporalUnit: java.time.temporal.TemporalUnit) -> bool: ...
    @typing.overload
    def minus(self, temporalAmount: java.time.temporal.TemporalAmount) -> 'ChronoZonedDateTime'[_ChronoZonedDateTime__D]: ...
    @typing.overload
    def minus(self, long: int, temporalUnit: java.time.temporal.TemporalUnit) -> 'ChronoZonedDateTime'[_ChronoZonedDateTime__D]: ...
    @typing.overload
    def plus(self, long: int, temporalUnit: java.time.temporal.TemporalUnit) -> 'ChronoZonedDateTime'[_ChronoZonedDateTime__D]: ...
    @typing.overload
    def plus(self, temporalAmount: java.time.temporal.TemporalAmount) -> 'ChronoZonedDateTime'[_ChronoZonedDateTime__D]: ...
    _query__R = typing.TypeVar('_query__R')  # <R>
    def query(self, temporalQuery: typing.Union[java.time.temporal.TemporalQuery[_query__R], typing.Callable[[java.time.temporal.TemporalAccessor], _query__R]]) -> _query__R: ...
    def range(self, temporalField: java.time.temporal.TemporalField) -> java.time.temporal.ValueRange: ...
    @staticmethod
    def timeLineOrder() -> java.util.Comparator['ChronoZonedDateTime'[typing.Any]]: ...
    def toEpochSecond(self) -> int: ...
    def toInstant(self) -> java.time.Instant: ...
    def toLocalDate(self) -> _ChronoZonedDateTime__D: ...
    def toLocalDateTime(self) -> ChronoLocalDateTime[_ChronoZonedDateTime__D]: ...
    def toLocalTime(self) -> java.time.LocalTime: ...
    def toString(self) -> str: ...
    def withEarlierOffsetAtOverlap(self) -> 'ChronoZonedDateTime'[_ChronoZonedDateTime__D]: ...
    def withLaterOffsetAtOverlap(self) -> 'ChronoZonedDateTime'[_ChronoZonedDateTime__D]: ...
    def withZoneSameInstant(self, zoneId: java.time.ZoneId) -> 'ChronoZonedDateTime'[_ChronoZonedDateTime__D]: ...
    def withZoneSameLocal(self, zoneId: java.time.ZoneId) -> 'ChronoZonedDateTime'[_ChronoZonedDateTime__D]: ...
    @typing.overload
    def with_(self, temporalField: java.time.temporal.TemporalField, long: int) -> 'ChronoZonedDateTime'[_ChronoZonedDateTime__D]: ...
    @typing.overload
    def with_(self, temporalAdjuster: typing.Union[java.time.temporal.TemporalAdjuster, typing.Callable]) -> 'ChronoZonedDateTime'[_ChronoZonedDateTime__D]: ...

class Chronology(java.lang.Comparable['Chronology']):
    def compareTo(self, chronology: 'Chronology') -> int: ...
    @typing.overload
    def date(self, int: int, int2: int, int3: int) -> ChronoLocalDate: ...
    @typing.overload
    def date(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> ChronoLocalDate: ...
    @typing.overload
    def date(self, era: typing.Union['Era', typing.Callable], int: int, int2: int, int3: int) -> ChronoLocalDate: ...
    def dateEpochDay(self, long: int) -> ChronoLocalDate: ...
    @typing.overload
    def dateNow(self) -> ChronoLocalDate: ...
    @typing.overload
    def dateNow(self, clock: java.time.Clock) -> ChronoLocalDate: ...
    @typing.overload
    def dateNow(self, zoneId: java.time.ZoneId) -> ChronoLocalDate: ...
    @typing.overload
    def dateYearDay(self, int: int, int2: int) -> ChronoLocalDate: ...
    @typing.overload
    def dateYearDay(self, era: typing.Union['Era', typing.Callable], int: int, int2: int) -> ChronoLocalDate: ...
    @typing.overload
    def epochSecond(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int, zoneOffset: java.time.ZoneOffset) -> int: ...
    @typing.overload
    def epochSecond(self, era: typing.Union['Era', typing.Callable], int: int, int2: int, int3: int, int4: int, int5: int, int6: int, zoneOffset: java.time.ZoneOffset) -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def eraOf(self, int: int) -> 'Era': ...
    def eras(self) -> java.util.List['Era']: ...
    @staticmethod
    def from_(temporalAccessor: java.time.temporal.TemporalAccessor) -> 'Chronology': ...
    @staticmethod
    def getAvailableChronologies() -> java.util.Set['Chronology']: ...
    def getCalendarType(self) -> str: ...
    def getDisplayName(self, textStyle: java.time.format.TextStyle, locale: java.util.Locale) -> str: ...
    def getId(self) -> str: ...
    def hashCode(self) -> int: ...
    def isIsoBased(self) -> bool: ...
    def isLeapYear(self, long: int) -> bool: ...
    def localDateTime(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> ChronoLocalDateTime[ChronoLocalDate]: ...
    @staticmethod
    def of(string: str) -> 'Chronology': ...
    @staticmethod
    def ofLocale(locale: java.util.Locale) -> 'Chronology': ...
    def period(self, int: int, int2: int, int3: int) -> ChronoPeriod: ...
    def prolepticYear(self, era: typing.Union['Era', typing.Callable], int: int) -> int: ...
    def range(self, chronoField: java.time.temporal.ChronoField) -> java.time.temporal.ValueRange: ...
    def resolveDate(self, map: typing.Union[java.util.Map[java.time.temporal.TemporalField, int], typing.Mapping[java.time.temporal.TemporalField, int]], resolverStyle: java.time.format.ResolverStyle) -> ChronoLocalDate: ...
    def toString(self) -> str: ...
    @typing.overload
    def zonedDateTime(self, instant: typing.Union[java.time.Instant, datetime.datetime], zoneId: java.time.ZoneId) -> ChronoZonedDateTime[ChronoLocalDate]: ...
    @typing.overload
    def zonedDateTime(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> ChronoZonedDateTime[ChronoLocalDate]: ...

class Era(java.time.temporal.TemporalAccessor, java.time.temporal.TemporalAdjuster):
    def adjustInto(self, temporal: java.time.temporal.Temporal) -> java.time.temporal.Temporal: ...
    def get(self, temporalField: java.time.temporal.TemporalField) -> int: ...
    def getDisplayName(self, textStyle: java.time.format.TextStyle, locale: java.util.Locale) -> str: ...
    def getLong(self, temporalField: java.time.temporal.TemporalField) -> int: ...
    def getValue(self) -> int: ...
    def isSupported(self, temporalField: java.time.temporal.TemporalField) -> bool: ...
    _query__R = typing.TypeVar('_query__R')  # <R>
    def query(self, temporalQuery: typing.Union[java.time.temporal.TemporalQuery[_query__R], typing.Callable[[java.time.temporal.TemporalAccessor], _query__R]]) -> _query__R: ...
    def range(self, temporalField: java.time.temporal.TemporalField) -> java.time.temporal.ValueRange: ...

class AbstractChronology(Chronology):
    def compareTo(self, chronology: Chronology) -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def resolveDate(self, map: typing.Union[java.util.Map[java.time.temporal.TemporalField, int], typing.Mapping[java.time.temporal.TemporalField, int]], resolverStyle: java.time.format.ResolverStyle) -> ChronoLocalDate: ...
    def toString(self) -> str: ...

class HijrahEra(java.lang.Enum['HijrahEra'], Era):
    AH: typing.ClassVar['HijrahEra'] = ...
    def getDisplayName(self, textStyle: java.time.format.TextStyle, locale: java.util.Locale) -> str: ...
    def getValue(self) -> int: ...
    @staticmethod
    def of(int: int) -> 'HijrahEra': ...
    def range(self, temporalField: java.time.temporal.TemporalField) -> java.time.temporal.ValueRange: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'HijrahEra': ...
    @staticmethod
    def values() -> typing.MutableSequence['HijrahEra']: ...

class IsoEra(java.lang.Enum['IsoEra'], Era):
    BCE: typing.ClassVar['IsoEra'] = ...
    CE: typing.ClassVar['IsoEra'] = ...
    def getValue(self) -> int: ...
    @staticmethod
    def of(int: int) -> 'IsoEra': ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'IsoEra': ...
    @staticmethod
    def values() -> typing.MutableSequence['IsoEra']: ...

class JapaneseEra(Era, java.io.Serializable):
    MEIJI: typing.ClassVar['JapaneseEra'] = ...
    TAISHO: typing.ClassVar['JapaneseEra'] = ...
    SHOWA: typing.ClassVar['JapaneseEra'] = ...
    HEISEI: typing.ClassVar['JapaneseEra'] = ...
    REIWA: typing.ClassVar['JapaneseEra'] = ...
    def getDisplayName(self, textStyle: java.time.format.TextStyle, locale: java.util.Locale) -> str: ...
    def getValue(self) -> int: ...
    @staticmethod
    def of(int: int) -> 'JapaneseEra': ...
    def range(self, temporalField: java.time.temporal.TemporalField) -> java.time.temporal.ValueRange: ...
    def toString(self) -> str: ...
    @staticmethod
    def valueOf(string: str) -> 'JapaneseEra': ...
    @staticmethod
    def values() -> typing.MutableSequence['JapaneseEra']: ...

class MinguoEra(java.lang.Enum['MinguoEra'], Era):
    BEFORE_ROC: typing.ClassVar['MinguoEra'] = ...
    ROC: typing.ClassVar['MinguoEra'] = ...
    def getDisplayName(self, textStyle: java.time.format.TextStyle, locale: java.util.Locale) -> str: ...
    def getValue(self) -> int: ...
    @staticmethod
    def of(int: int) -> 'MinguoEra': ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'MinguoEra': ...
    @staticmethod
    def values() -> typing.MutableSequence['MinguoEra']: ...

class ThaiBuddhistEra(java.lang.Enum['ThaiBuddhistEra'], Era):
    BEFORE_BE: typing.ClassVar['ThaiBuddhistEra'] = ...
    BE: typing.ClassVar['ThaiBuddhistEra'] = ...
    def getDisplayName(self, textStyle: java.time.format.TextStyle, locale: java.util.Locale) -> str: ...
    def getValue(self) -> int: ...
    @staticmethod
    def of(int: int) -> 'ThaiBuddhistEra': ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ThaiBuddhistEra': ...
    @staticmethod
    def values() -> typing.MutableSequence['ThaiBuddhistEra']: ...

class HijrahChronology(AbstractChronology, java.io.Serializable):
    INSTANCE: typing.ClassVar['HijrahChronology'] = ...
    @typing.overload
    def date(self, int: int, int2: int, int3: int) -> 'HijrahDate': ...
    @typing.overload
    def date(self, era: typing.Union[Era, typing.Callable], int: int, int2: int, int3: int) -> 'HijrahDate': ...
    @typing.overload
    def date(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> 'HijrahDate': ...
    def dateEpochDay(self, long: int) -> 'HijrahDate': ...
    @typing.overload
    def dateNow(self) -> 'HijrahDate': ...
    @typing.overload
    def dateNow(self, clock: java.time.Clock) -> 'HijrahDate': ...
    @typing.overload
    def dateNow(self, zoneId: java.time.ZoneId) -> 'HijrahDate': ...
    @typing.overload
    def dateYearDay(self, int: int, int2: int) -> 'HijrahDate': ...
    @typing.overload
    def dateYearDay(self, era: typing.Union[Era, typing.Callable], int: int, int2: int) -> 'HijrahDate': ...
    def eraOf(self, int: int) -> HijrahEra: ...
    def eras(self) -> java.util.List[Era]: ...
    def getCalendarType(self) -> str: ...
    def getId(self) -> str: ...
    def isLeapYear(self, long: int) -> bool: ...
    def localDateTime(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> ChronoLocalDateTime['HijrahDate']: ...
    def prolepticYear(self, era: typing.Union[Era, typing.Callable], int: int) -> int: ...
    def range(self, chronoField: java.time.temporal.ChronoField) -> java.time.temporal.ValueRange: ...
    def resolveDate(self, map: typing.Union[java.util.Map[java.time.temporal.TemporalField, int], typing.Mapping[java.time.temporal.TemporalField, int]], resolverStyle: java.time.format.ResolverStyle) -> 'HijrahDate': ...
    @typing.overload
    def zonedDateTime(self, instant: typing.Union[java.time.Instant, datetime.datetime], zoneId: java.time.ZoneId) -> ChronoZonedDateTime['HijrahDate']: ...
    @typing.overload
    def zonedDateTime(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> ChronoZonedDateTime['HijrahDate']: ...

class IsoChronology(AbstractChronology, java.io.Serializable):
    INSTANCE: typing.ClassVar['IsoChronology'] = ...
    @typing.overload
    def date(self, int: int, int2: int, int3: int) -> java.time.LocalDate: ...
    @typing.overload
    def date(self, era: typing.Union[Era, typing.Callable], int: int, int2: int, int3: int) -> java.time.LocalDate: ...
    @typing.overload
    def date(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> java.time.LocalDate: ...
    def dateEpochDay(self, long: int) -> java.time.LocalDate: ...
    @typing.overload
    def dateNow(self) -> java.time.LocalDate: ...
    @typing.overload
    def dateNow(self, clock: java.time.Clock) -> java.time.LocalDate: ...
    @typing.overload
    def dateNow(self, zoneId: java.time.ZoneId) -> java.time.LocalDate: ...
    @typing.overload
    def dateYearDay(self, int: int, int2: int) -> java.time.LocalDate: ...
    @typing.overload
    def dateYearDay(self, era: typing.Union[Era, typing.Callable], int: int, int2: int) -> java.time.LocalDate: ...
    @typing.overload
    def epochSecond(self, era: typing.Union[Era, typing.Callable], int: int, int2: int, int3: int, int4: int, int5: int, int6: int, zoneOffset: java.time.ZoneOffset) -> int: ...
    @typing.overload
    def epochSecond(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int, zoneOffset: java.time.ZoneOffset) -> int: ...
    def eraOf(self, int: int) -> IsoEra: ...
    def eras(self) -> java.util.List[Era]: ...
    def getCalendarType(self) -> str: ...
    def getId(self) -> str: ...
    def isIsoBased(self) -> bool: ...
    def isLeapYear(self, long: int) -> bool: ...
    def localDateTime(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> java.time.LocalDateTime: ...
    def period(self, int: int, int2: int, int3: int) -> java.time.Period: ...
    def prolepticYear(self, era: typing.Union[Era, typing.Callable], int: int) -> int: ...
    def range(self, chronoField: java.time.temporal.ChronoField) -> java.time.temporal.ValueRange: ...
    def resolveDate(self, map: typing.Union[java.util.Map[java.time.temporal.TemporalField, int], typing.Mapping[java.time.temporal.TemporalField, int]], resolverStyle: java.time.format.ResolverStyle) -> java.time.LocalDate: ...
    @typing.overload
    def zonedDateTime(self, instant: typing.Union[java.time.Instant, datetime.datetime], zoneId: java.time.ZoneId) -> java.time.ZonedDateTime: ...
    @typing.overload
    def zonedDateTime(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> java.time.ZonedDateTime: ...

class JapaneseChronology(AbstractChronology, java.io.Serializable):
    INSTANCE: typing.ClassVar['JapaneseChronology'] = ...
    @typing.overload
    def date(self, int: int, int2: int, int3: int) -> 'JapaneseDate': ...
    @typing.overload
    def date(self, era: typing.Union[Era, typing.Callable], int: int, int2: int, int3: int) -> 'JapaneseDate': ...
    @typing.overload
    def date(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> 'JapaneseDate': ...
    def dateEpochDay(self, long: int) -> 'JapaneseDate': ...
    @typing.overload
    def dateNow(self) -> 'JapaneseDate': ...
    @typing.overload
    def dateNow(self, clock: java.time.Clock) -> 'JapaneseDate': ...
    @typing.overload
    def dateNow(self, zoneId: java.time.ZoneId) -> 'JapaneseDate': ...
    @typing.overload
    def dateYearDay(self, int: int, int2: int) -> 'JapaneseDate': ...
    @typing.overload
    def dateYearDay(self, era: typing.Union[Era, typing.Callable], int: int, int2: int) -> 'JapaneseDate': ...
    def eraOf(self, int: int) -> JapaneseEra: ...
    def eras(self) -> java.util.List[Era]: ...
    def getCalendarType(self) -> str: ...
    def getId(self) -> str: ...
    def isIsoBased(self) -> bool: ...
    def isLeapYear(self, long: int) -> bool: ...
    def localDateTime(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> ChronoLocalDateTime['JapaneseDate']: ...
    def prolepticYear(self, era: typing.Union[Era, typing.Callable], int: int) -> int: ...
    def range(self, chronoField: java.time.temporal.ChronoField) -> java.time.temporal.ValueRange: ...
    def resolveDate(self, map: typing.Union[java.util.Map[java.time.temporal.TemporalField, int], typing.Mapping[java.time.temporal.TemporalField, int]], resolverStyle: java.time.format.ResolverStyle) -> 'JapaneseDate': ...
    @typing.overload
    def zonedDateTime(self, instant: typing.Union[java.time.Instant, datetime.datetime], zoneId: java.time.ZoneId) -> ChronoZonedDateTime['JapaneseDate']: ...
    @typing.overload
    def zonedDateTime(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> ChronoZonedDateTime['JapaneseDate']: ...

class MinguoChronology(AbstractChronology, java.io.Serializable):
    INSTANCE: typing.ClassVar['MinguoChronology'] = ...
    @typing.overload
    def date(self, int: int, int2: int, int3: int) -> 'MinguoDate': ...
    @typing.overload
    def date(self, era: typing.Union[Era, typing.Callable], int: int, int2: int, int3: int) -> 'MinguoDate': ...
    @typing.overload
    def date(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> 'MinguoDate': ...
    def dateEpochDay(self, long: int) -> 'MinguoDate': ...
    @typing.overload
    def dateNow(self) -> 'MinguoDate': ...
    @typing.overload
    def dateNow(self, clock: java.time.Clock) -> 'MinguoDate': ...
    @typing.overload
    def dateNow(self, zoneId: java.time.ZoneId) -> 'MinguoDate': ...
    @typing.overload
    def dateYearDay(self, int: int, int2: int) -> 'MinguoDate': ...
    @typing.overload
    def dateYearDay(self, era: typing.Union[Era, typing.Callable], int: int, int2: int) -> 'MinguoDate': ...
    def eraOf(self, int: int) -> MinguoEra: ...
    def eras(self) -> java.util.List[Era]: ...
    def getCalendarType(self) -> str: ...
    def getId(self) -> str: ...
    def isIsoBased(self) -> bool: ...
    def isLeapYear(self, long: int) -> bool: ...
    def localDateTime(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> ChronoLocalDateTime['MinguoDate']: ...
    def prolepticYear(self, era: typing.Union[Era, typing.Callable], int: int) -> int: ...
    def range(self, chronoField: java.time.temporal.ChronoField) -> java.time.temporal.ValueRange: ...
    def resolveDate(self, map: typing.Union[java.util.Map[java.time.temporal.TemporalField, int], typing.Mapping[java.time.temporal.TemporalField, int]], resolverStyle: java.time.format.ResolverStyle) -> 'MinguoDate': ...
    @typing.overload
    def zonedDateTime(self, instant: typing.Union[java.time.Instant, datetime.datetime], zoneId: java.time.ZoneId) -> ChronoZonedDateTime['MinguoDate']: ...
    @typing.overload
    def zonedDateTime(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> ChronoZonedDateTime['MinguoDate']: ...

class ThaiBuddhistChronology(AbstractChronology, java.io.Serializable):
    INSTANCE: typing.ClassVar['ThaiBuddhistChronology'] = ...
    @typing.overload
    def date(self, int: int, int2: int, int3: int) -> 'ThaiBuddhistDate': ...
    @typing.overload
    def date(self, era: typing.Union[Era, typing.Callable], int: int, int2: int, int3: int) -> 'ThaiBuddhistDate': ...
    @typing.overload
    def date(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> 'ThaiBuddhistDate': ...
    def dateEpochDay(self, long: int) -> 'ThaiBuddhistDate': ...
    @typing.overload
    def dateNow(self) -> 'ThaiBuddhistDate': ...
    @typing.overload
    def dateNow(self, clock: java.time.Clock) -> 'ThaiBuddhistDate': ...
    @typing.overload
    def dateNow(self, zoneId: java.time.ZoneId) -> 'ThaiBuddhistDate': ...
    @typing.overload
    def dateYearDay(self, int: int, int2: int) -> 'ThaiBuddhistDate': ...
    @typing.overload
    def dateYearDay(self, era: typing.Union[Era, typing.Callable], int: int, int2: int) -> 'ThaiBuddhistDate': ...
    def eraOf(self, int: int) -> ThaiBuddhistEra: ...
    def eras(self) -> java.util.List[Era]: ...
    def getCalendarType(self) -> str: ...
    def getId(self) -> str: ...
    def isIsoBased(self) -> bool: ...
    def isLeapYear(self, long: int) -> bool: ...
    def localDateTime(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> ChronoLocalDateTime['ThaiBuddhistDate']: ...
    def prolepticYear(self, era: typing.Union[Era, typing.Callable], int: int) -> int: ...
    def range(self, chronoField: java.time.temporal.ChronoField) -> java.time.temporal.ValueRange: ...
    def resolveDate(self, map: typing.Union[java.util.Map[java.time.temporal.TemporalField, int], typing.Mapping[java.time.temporal.TemporalField, int]], resolverStyle: java.time.format.ResolverStyle) -> 'ThaiBuddhistDate': ...
    @typing.overload
    def zonedDateTime(self, instant: typing.Union[java.time.Instant, datetime.datetime], zoneId: java.time.ZoneId) -> ChronoZonedDateTime['ThaiBuddhistDate']: ...
    @typing.overload
    def zonedDateTime(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> ChronoZonedDateTime['ThaiBuddhistDate']: ...

class HijrahDate(java.time.chrono.ChronoLocalDateImpl['HijrahDate'], ChronoLocalDate, java.io.Serializable):
    def atTime(self, localTime: java.time.LocalTime) -> ChronoLocalDateTime['HijrahDate']: ...
    def equals(self, object: typing.Any) -> bool: ...
    @staticmethod
    def from_(temporalAccessor: java.time.temporal.TemporalAccessor) -> 'HijrahDate': ...
    def getChronology(self) -> HijrahChronology: ...
    def getEra(self) -> HijrahEra: ...
    def getLong(self, temporalField: java.time.temporal.TemporalField) -> int: ...
    def hashCode(self) -> int: ...
    def isLeapYear(self) -> bool: ...
    def lengthOfMonth(self) -> int: ...
    def lengthOfYear(self) -> int: ...
    @typing.overload
    def minus(self, temporalAmount: java.time.temporal.TemporalAmount) -> 'HijrahDate': ...
    @typing.overload
    def minus(self, long: int, temporalUnit: java.time.temporal.TemporalUnit) -> 'HijrahDate': ...
    @typing.overload
    @staticmethod
    def now() -> 'HijrahDate': ...
    @typing.overload
    @staticmethod
    def now(clock: java.time.Clock) -> 'HijrahDate': ...
    @typing.overload
    @staticmethod
    def now(zoneId: java.time.ZoneId) -> 'HijrahDate': ...
    @staticmethod
    def of(int: int, int2: int, int3: int) -> 'HijrahDate': ...
    @typing.overload
    def plus(self, temporalAmount: java.time.temporal.TemporalAmount) -> 'HijrahDate': ...
    @typing.overload
    def plus(self, long: int, temporalUnit: java.time.temporal.TemporalUnit) -> 'HijrahDate': ...
    def range(self, temporalField: java.time.temporal.TemporalField) -> java.time.temporal.ValueRange: ...
    def toEpochDay(self) -> int: ...
    def until(self, chronoLocalDate: ChronoLocalDate) -> ChronoPeriod: ...
    def withVariant(self, hijrahChronology: HijrahChronology) -> 'HijrahDate': ...
    @typing.overload
    def with_(self, temporalAdjuster: typing.Union[java.time.temporal.TemporalAdjuster, typing.Callable]) -> 'HijrahDate': ...
    @typing.overload
    def with_(self, temporalField: java.time.temporal.TemporalField, long: int) -> 'HijrahDate': ...

class JapaneseDate(java.time.chrono.ChronoLocalDateImpl['JapaneseDate'], ChronoLocalDate, java.io.Serializable):
    def atTime(self, localTime: java.time.LocalTime) -> ChronoLocalDateTime['JapaneseDate']: ...
    def equals(self, object: typing.Any) -> bool: ...
    @staticmethod
    def from_(temporalAccessor: java.time.temporal.TemporalAccessor) -> 'JapaneseDate': ...
    def getChronology(self) -> JapaneseChronology: ...
    def getEra(self) -> JapaneseEra: ...
    def getLong(self, temporalField: java.time.temporal.TemporalField) -> int: ...
    def hashCode(self) -> int: ...
    @typing.overload
    def isSupported(self, temporalField: java.time.temporal.TemporalField) -> bool: ...
    @typing.overload
    def isSupported(self, temporalUnit: java.time.temporal.TemporalUnit) -> bool: ...
    def lengthOfMonth(self) -> int: ...
    def lengthOfYear(self) -> int: ...
    @typing.overload
    def minus(self, temporalAmount: java.time.temporal.TemporalAmount) -> 'JapaneseDate': ...
    @typing.overload
    def minus(self, long: int, temporalUnit: java.time.temporal.TemporalUnit) -> 'JapaneseDate': ...
    @typing.overload
    @staticmethod
    def now() -> 'JapaneseDate': ...
    @typing.overload
    @staticmethod
    def now(clock: java.time.Clock) -> 'JapaneseDate': ...
    @typing.overload
    @staticmethod
    def now(zoneId: java.time.ZoneId) -> 'JapaneseDate': ...
    @typing.overload
    @staticmethod
    def of(int: int, int2: int, int3: int) -> 'JapaneseDate': ...
    @typing.overload
    @staticmethod
    def of(japaneseEra: JapaneseEra, int: int, int2: int, int3: int) -> 'JapaneseDate': ...
    @typing.overload
    def plus(self, temporalAmount: java.time.temporal.TemporalAmount) -> 'JapaneseDate': ...
    @typing.overload
    def plus(self, long: int, temporalUnit: java.time.temporal.TemporalUnit) -> 'JapaneseDate': ...
    def range(self, temporalField: java.time.temporal.TemporalField) -> java.time.temporal.ValueRange: ...
    def toEpochDay(self) -> int: ...
    def until(self, chronoLocalDate: ChronoLocalDate) -> ChronoPeriod: ...
    @typing.overload
    def with_(self, temporalAdjuster: typing.Union[java.time.temporal.TemporalAdjuster, typing.Callable]) -> 'JapaneseDate': ...
    @typing.overload
    def with_(self, temporalField: java.time.temporal.TemporalField, long: int) -> 'JapaneseDate': ...

class MinguoDate(java.time.chrono.ChronoLocalDateImpl['MinguoDate'], ChronoLocalDate, java.io.Serializable):
    def atTime(self, localTime: java.time.LocalTime) -> ChronoLocalDateTime['MinguoDate']: ...
    def equals(self, object: typing.Any) -> bool: ...
    @staticmethod
    def from_(temporalAccessor: java.time.temporal.TemporalAccessor) -> 'MinguoDate': ...
    def getChronology(self) -> MinguoChronology: ...
    def getEra(self) -> MinguoEra: ...
    def getLong(self, temporalField: java.time.temporal.TemporalField) -> int: ...
    def hashCode(self) -> int: ...
    def lengthOfMonth(self) -> int: ...
    @typing.overload
    def minus(self, temporalAmount: java.time.temporal.TemporalAmount) -> 'MinguoDate': ...
    @typing.overload
    def minus(self, long: int, temporalUnit: java.time.temporal.TemporalUnit) -> 'MinguoDate': ...
    @typing.overload
    @staticmethod
    def now() -> 'MinguoDate': ...
    @typing.overload
    @staticmethod
    def now(clock: java.time.Clock) -> 'MinguoDate': ...
    @typing.overload
    @staticmethod
    def now(zoneId: java.time.ZoneId) -> 'MinguoDate': ...
    @staticmethod
    def of(int: int, int2: int, int3: int) -> 'MinguoDate': ...
    @typing.overload
    def plus(self, temporalAmount: java.time.temporal.TemporalAmount) -> 'MinguoDate': ...
    @typing.overload
    def plus(self, long: int, temporalUnit: java.time.temporal.TemporalUnit) -> 'MinguoDate': ...
    def range(self, temporalField: java.time.temporal.TemporalField) -> java.time.temporal.ValueRange: ...
    def toEpochDay(self) -> int: ...
    def until(self, chronoLocalDate: ChronoLocalDate) -> ChronoPeriod: ...
    @typing.overload
    def with_(self, temporalAdjuster: typing.Union[java.time.temporal.TemporalAdjuster, typing.Callable]) -> 'MinguoDate': ...
    @typing.overload
    def with_(self, temporalField: java.time.temporal.TemporalField, long: int) -> 'MinguoDate': ...

class ThaiBuddhistDate(java.time.chrono.ChronoLocalDateImpl['ThaiBuddhistDate'], ChronoLocalDate, java.io.Serializable):
    def atTime(self, localTime: java.time.LocalTime) -> ChronoLocalDateTime['ThaiBuddhistDate']: ...
    def equals(self, object: typing.Any) -> bool: ...
    @staticmethod
    def from_(temporalAccessor: java.time.temporal.TemporalAccessor) -> 'ThaiBuddhistDate': ...
    def getChronology(self) -> ThaiBuddhistChronology: ...
    def getEra(self) -> ThaiBuddhistEra: ...
    def getLong(self, temporalField: java.time.temporal.TemporalField) -> int: ...
    def hashCode(self) -> int: ...
    def lengthOfMonth(self) -> int: ...
    @typing.overload
    def minus(self, temporalAmount: java.time.temporal.TemporalAmount) -> 'ThaiBuddhistDate': ...
    @typing.overload
    def minus(self, long: int, temporalUnit: java.time.temporal.TemporalUnit) -> 'ThaiBuddhistDate': ...
    @typing.overload
    @staticmethod
    def now() -> 'ThaiBuddhistDate': ...
    @typing.overload
    @staticmethod
    def now(clock: java.time.Clock) -> 'ThaiBuddhistDate': ...
    @typing.overload
    @staticmethod
    def now(zoneId: java.time.ZoneId) -> 'ThaiBuddhistDate': ...
    @staticmethod
    def of(int: int, int2: int, int3: int) -> 'ThaiBuddhistDate': ...
    @typing.overload
    def plus(self, temporalAmount: java.time.temporal.TemporalAmount) -> 'ThaiBuddhistDate': ...
    @typing.overload
    def plus(self, long: int, temporalUnit: java.time.temporal.TemporalUnit) -> 'ThaiBuddhistDate': ...
    def range(self, temporalField: java.time.temporal.TemporalField) -> java.time.temporal.ValueRange: ...
    def toEpochDay(self) -> int: ...
    def until(self, chronoLocalDate: ChronoLocalDate) -> ChronoPeriod: ...
    @typing.overload
    def with_(self, temporalAdjuster: typing.Union[java.time.temporal.TemporalAdjuster, typing.Callable]) -> 'ThaiBuddhistDate': ...
    @typing.overload
    def with_(self, temporalField: java.time.temporal.TemporalField, long: int) -> 'ThaiBuddhistDate': ...

class ChronoLocalDateImpl: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.time.chrono")``.

    AbstractChronology: typing.Type[AbstractChronology]
    ChronoLocalDate: typing.Type[ChronoLocalDate]
    ChronoLocalDateImpl: typing.Type[ChronoLocalDateImpl]
    ChronoLocalDateTime: typing.Type[ChronoLocalDateTime]
    ChronoPeriod: typing.Type[ChronoPeriod]
    ChronoZonedDateTime: typing.Type[ChronoZonedDateTime]
    Chronology: typing.Type[Chronology]
    Era: typing.Type[Era]
    HijrahChronology: typing.Type[HijrahChronology]
    HijrahDate: typing.Type[HijrahDate]
    HijrahEra: typing.Type[HijrahEra]
    IsoChronology: typing.Type[IsoChronology]
    IsoEra: typing.Type[IsoEra]
    JapaneseChronology: typing.Type[JapaneseChronology]
    JapaneseDate: typing.Type[JapaneseDate]
    JapaneseEra: typing.Type[JapaneseEra]
    MinguoChronology: typing.Type[MinguoChronology]
    MinguoDate: typing.Type[MinguoDate]
    MinguoEra: typing.Type[MinguoEra]
    ThaiBuddhistChronology: typing.Type[ThaiBuddhistChronology]
    ThaiBuddhistDate: typing.Type[ThaiBuddhistDate]
    ThaiBuddhistEra: typing.Type[ThaiBuddhistEra]
