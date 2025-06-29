
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import jpype
import typing



class Clipboard:
    def __init__(self, string: str): ...
    def addFlavorListener(self, flavorListener: typing.Union['FlavorListener', typing.Callable]) -> None: ...
    def getAvailableDataFlavors(self) -> typing.MutableSequence['DataFlavor']: ...
    def getContents(self, object: typing.Any) -> 'Transferable': ...
    def getData(self, dataFlavor: 'DataFlavor') -> typing.Any: ...
    def getFlavorListeners(self) -> typing.MutableSequence['FlavorListener']: ...
    def getName(self) -> str: ...
    def isDataFlavorAvailable(self, dataFlavor: 'DataFlavor') -> bool: ...
    def removeFlavorListener(self, flavorListener: typing.Union['FlavorListener', typing.Callable]) -> None: ...
    def setContents(self, transferable: 'Transferable', clipboardOwner: typing.Union['ClipboardOwner', typing.Callable]) -> None: ...

class ClipboardOwner:
    def lostOwnership(self, clipboard: Clipboard, transferable: 'Transferable') -> None: ...

class DataFlavor(java.io.Externalizable, java.lang.Cloneable):
    stringFlavor: typing.ClassVar['DataFlavor'] = ...
    imageFlavor: typing.ClassVar['DataFlavor'] = ...
    plainTextFlavor: typing.ClassVar['DataFlavor'] = ...
    javaSerializedObjectMimeType: typing.ClassVar[str] = ...
    javaFileListFlavor: typing.ClassVar['DataFlavor'] = ...
    javaJVMLocalObjectMimeType: typing.ClassVar[str] = ...
    javaRemoteObjectMimeType: typing.ClassVar[str] = ...
    selectionHtmlFlavor: typing.ClassVar['DataFlavor'] = ...
    fragmentHtmlFlavor: typing.ClassVar['DataFlavor'] = ...
    allHtmlFlavor: typing.ClassVar['DataFlavor'] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, class_: typing.Type[typing.Any], string: str): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, classLoader: java.lang.ClassLoader): ...
    def clone(self) -> typing.Any: ...
    @typing.overload
    def equals(self, dataFlavor: 'DataFlavor') -> bool: ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    def equals(self, string: str) -> bool: ...
    def getDefaultRepresentationClass(self) -> typing.Type[typing.Any]: ...
    def getDefaultRepresentationClassAsString(self) -> str: ...
    def getHumanPresentableName(self) -> str: ...
    def getMimeType(self) -> str: ...
    def getParameter(self, string: str) -> str: ...
    def getPrimaryType(self) -> str: ...
    def getReaderForText(self, transferable: 'Transferable') -> java.io.Reader: ...
    def getRepresentationClass(self) -> typing.Type[typing.Any]: ...
    def getSubType(self) -> str: ...
    @staticmethod
    def getTextPlainUnicodeFlavor() -> 'DataFlavor': ...
    def hashCode(self) -> int: ...
    def isFlavorJavaFileListType(self) -> bool: ...
    def isFlavorRemoteObjectType(self) -> bool: ...
    def isFlavorSerializedObjectType(self) -> bool: ...
    def isFlavorTextType(self) -> bool: ...
    @typing.overload
    def isMimeTypeEqual(self, string: str) -> bool: ...
    @typing.overload
    def isMimeTypeEqual(self, dataFlavor: 'DataFlavor') -> bool: ...
    def isMimeTypeSerializedObject(self) -> bool: ...
    def isRepresentationClassByteBuffer(self) -> bool: ...
    def isRepresentationClassCharBuffer(self) -> bool: ...
    def isRepresentationClassInputStream(self) -> bool: ...
    def isRepresentationClassReader(self) -> bool: ...
    def isRepresentationClassRemote(self) -> bool: ...
    def isRepresentationClassSerializable(self) -> bool: ...
    def match(self, dataFlavor: 'DataFlavor') -> bool: ...
    def readExternal(self, objectInput: java.io.ObjectInput) -> None: ...
    @staticmethod
    def selectBestTextFlavor(dataFlavorArray: typing.Union[typing.List['DataFlavor'], jpype.JArray]) -> 'DataFlavor': ...
    def setHumanPresentableName(self, string: str) -> None: ...
    def toString(self) -> str: ...
    def writeExternal(self, objectOutput: java.io.ObjectOutput) -> None: ...

class FlavorEvent(java.util.EventObject):
    def __init__(self, clipboard: Clipboard): ...

class FlavorListener(java.util.EventListener):
    def flavorsChanged(self, flavorEvent: FlavorEvent) -> None: ...

class FlavorMap:
    def getFlavorsForNatives(self, stringArray: typing.Union[typing.List[str], jpype.JArray]) -> java.util.Map[str, DataFlavor]: ...
    def getNativesForFlavors(self, dataFlavorArray: typing.Union[typing.List[DataFlavor], jpype.JArray]) -> java.util.Map[DataFlavor, str]: ...

class MimeTypeParseException(java.lang.Exception):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class Transferable:
    def getTransferData(self, dataFlavor: DataFlavor) -> typing.Any: ...
    def getTransferDataFlavors(self) -> typing.MutableSequence[DataFlavor]: ...
    def isDataFlavorSupported(self, dataFlavor: DataFlavor) -> bool: ...

class UnsupportedFlavorException(java.lang.Exception):
    def __init__(self, dataFlavor: DataFlavor): ...

class FlavorTable(FlavorMap):
    def getFlavorsForNative(self, string: str) -> java.util.List[DataFlavor]: ...
    def getNativesForFlavor(self, dataFlavor: DataFlavor) -> java.util.List[str]: ...

class StringSelection(Transferable, ClipboardOwner):
    def __init__(self, string: str): ...
    def getTransferData(self, dataFlavor: DataFlavor) -> typing.Any: ...
    def getTransferDataFlavors(self) -> typing.MutableSequence[DataFlavor]: ...
    def isDataFlavorSupported(self, dataFlavor: DataFlavor) -> bool: ...
    def lostOwnership(self, clipboard: Clipboard, transferable: Transferable) -> None: ...

class SystemFlavorMap(FlavorMap, FlavorTable):
    def addFlavorForUnencodedNative(self, string: str, dataFlavor: DataFlavor) -> None: ...
    def addUnencodedNativeForFlavor(self, dataFlavor: DataFlavor, string: str) -> None: ...
    @staticmethod
    def decodeDataFlavor(string: str) -> DataFlavor: ...
    @staticmethod
    def decodeJavaMIMEType(string: str) -> str: ...
    @staticmethod
    def encodeDataFlavor(dataFlavor: DataFlavor) -> str: ...
    @staticmethod
    def encodeJavaMIMEType(string: str) -> str: ...
    @staticmethod
    def getDefaultFlavorMap() -> FlavorMap: ...
    def getFlavorsForNative(self, string: str) -> java.util.List[DataFlavor]: ...
    def getFlavorsForNatives(self, stringArray: typing.Union[typing.List[str], jpype.JArray]) -> java.util.Map[str, DataFlavor]: ...
    def getNativesForFlavor(self, dataFlavor: DataFlavor) -> java.util.List[str]: ...
    def getNativesForFlavors(self, dataFlavorArray: typing.Union[typing.List[DataFlavor], jpype.JArray]) -> java.util.Map[DataFlavor, str]: ...
    @staticmethod
    def isJavaMIMEType(string: str) -> bool: ...
    def setFlavorsForNative(self, string: str, dataFlavorArray: typing.Union[typing.List[DataFlavor], jpype.JArray]) -> None: ...
    def setNativesForFlavor(self, dataFlavor: DataFlavor, stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.awt.datatransfer")``.

    Clipboard: typing.Type[Clipboard]
    ClipboardOwner: typing.Type[ClipboardOwner]
    DataFlavor: typing.Type[DataFlavor]
    FlavorEvent: typing.Type[FlavorEvent]
    FlavorListener: typing.Type[FlavorListener]
    FlavorMap: typing.Type[FlavorMap]
    FlavorTable: typing.Type[FlavorTable]
    MimeTypeParseException: typing.Type[MimeTypeParseException]
    StringSelection: typing.Type[StringSelection]
    SystemFlavorMap: typing.Type[SystemFlavorMap]
    Transferable: typing.Type[Transferable]
    UnsupportedFlavorException: typing.Type[UnsupportedFlavorException]
