
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.net
import java.nio.channels
import java.nio.file
import java.nio.file.attribute
import java.util
import java.util.concurrent
import jpype.protocol
import typing



class FileSystemProvider:
    def checkAccess(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], *accessMode: java.nio.file.AccessMode) -> None: ...
    def copy(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], path2: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], *copyOption: java.nio.file.CopyOption) -> None: ...
    def createDirectory(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], *fileAttribute: java.nio.file.attribute.FileAttribute[typing.Any]) -> None: ...
    def createLink(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], path2: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath]) -> None: ...
    def createSymbolicLink(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], path2: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], *fileAttribute: java.nio.file.attribute.FileAttribute[typing.Any]) -> None: ...
    def delete(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath]) -> None: ...
    def deleteIfExists(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath]) -> bool: ...
    def exists(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], *linkOption: java.nio.file.LinkOption) -> bool: ...
    _getFileAttributeView__V = typing.TypeVar('_getFileAttributeView__V', bound=java.nio.file.attribute.FileAttributeView)  # <V>
    def getFileAttributeView(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], class_: typing.Type[_getFileAttributeView__V], *linkOption: java.nio.file.LinkOption) -> _getFileAttributeView__V: ...
    def getFileStore(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath]) -> java.nio.file.FileStore: ...
    def getFileSystem(self, uRI: java.net.URI) -> java.nio.file.FileSystem: ...
    def getPath(self, uRI: java.net.URI) -> java.nio.file.Path: ...
    def getScheme(self) -> str: ...
    @staticmethod
    def installedProviders() -> java.util.List['FileSystemProvider']: ...
    def isHidden(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath]) -> bool: ...
    def isSameFile(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], path2: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath]) -> bool: ...
    def move(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], path2: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], *copyOption: java.nio.file.CopyOption) -> None: ...
    def newAsynchronousFileChannel(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], set: java.util.Set[java.nio.file.OpenOption], executorService: java.util.concurrent.ExecutorService, *fileAttribute: java.nio.file.attribute.FileAttribute[typing.Any]) -> java.nio.channels.AsynchronousFileChannel: ...
    def newByteChannel(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], set: java.util.Set[java.nio.file.OpenOption], *fileAttribute: java.nio.file.attribute.FileAttribute[typing.Any]) -> java.nio.channels.SeekableByteChannel: ...
    def newDirectoryStream(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], filter: typing.Union[java.nio.file.DirectoryStream.Filter[java.nio.file.Path], typing.Callable[[java.nio.file.Path], bool]]) -> java.nio.file.DirectoryStream[java.nio.file.Path]: ...
    def newFileChannel(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], set: java.util.Set[java.nio.file.OpenOption], *fileAttribute: java.nio.file.attribute.FileAttribute[typing.Any]) -> java.nio.channels.FileChannel: ...
    @typing.overload
    def newFileSystem(self, uRI: java.net.URI, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]) -> java.nio.file.FileSystem: ...
    @typing.overload
    def newFileSystem(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]) -> java.nio.file.FileSystem: ...
    def newInputStream(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], *openOption: java.nio.file.OpenOption) -> java.io.InputStream: ...
    def newOutputStream(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], *openOption: java.nio.file.OpenOption) -> java.io.OutputStream: ...
    _readAttributes_0__A = typing.TypeVar('_readAttributes_0__A', bound=java.nio.file.attribute.BasicFileAttributes)  # <A>
    @typing.overload
    def readAttributes(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], class_: typing.Type[_readAttributes_0__A], *linkOption: java.nio.file.LinkOption) -> _readAttributes_0__A: ...
    @typing.overload
    def readAttributes(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], string: str, *linkOption: java.nio.file.LinkOption) -> java.util.Map[str, typing.Any]: ...
    _readAttributesIfExists__A = typing.TypeVar('_readAttributesIfExists__A', bound=java.nio.file.attribute.BasicFileAttributes)  # <A>
    def readAttributesIfExists(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], class_: typing.Type[_readAttributesIfExists__A], *linkOption: java.nio.file.LinkOption) -> _readAttributesIfExists__A: ...
    def readSymbolicLink(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath]) -> java.nio.file.Path: ...
    def setAttribute(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], string: str, object: typing.Any, *linkOption: java.nio.file.LinkOption) -> None: ...

class FileTypeDetector:
    def probeContentType(self, path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath]) -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.nio.file.spi")``.

    FileSystemProvider: typing.Type[FileSystemProvider]
    FileTypeDetector: typing.Type[FileTypeDetector]
