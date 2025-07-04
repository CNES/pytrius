
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.awt
import java.awt.datatransfer
import java.awt.dnd.peer
import java.awt.event
import java.io
import java.lang
import java.util
import jpype
import typing



class Autoscroll:
    def autoscroll(self, point: java.awt.Point) -> None: ...
    def getAutoscrollInsets(self) -> java.awt.Insets: ...

class DnDConstants:
    ACTION_NONE: typing.ClassVar[int] = ...
    ACTION_COPY: typing.ClassVar[int] = ...
    ACTION_MOVE: typing.ClassVar[int] = ...
    ACTION_COPY_OR_MOVE: typing.ClassVar[int] = ...
    ACTION_LINK: typing.ClassVar[int] = ...
    ACTION_REFERENCE: typing.ClassVar[int] = ...

class DragGestureEvent(java.util.EventObject):
    def __init__(self, dragGestureRecognizer: 'DragGestureRecognizer', int: int, point: java.awt.Point, list: java.util.List[java.awt.event.InputEvent]): ...
    def getComponent(self) -> java.awt.Component: ...
    def getDragAction(self) -> int: ...
    def getDragOrigin(self) -> java.awt.Point: ...
    def getDragSource(self) -> 'DragSource': ...
    def getSourceAsDragGestureRecognizer(self) -> 'DragGestureRecognizer': ...
    def getTriggerEvent(self) -> java.awt.event.InputEvent: ...
    def iterator(self) -> java.util.Iterator[java.awt.event.InputEvent]: ...
    @typing.overload
    def startDrag(self, cursor: java.awt.Cursor, image: java.awt.Image, point: java.awt.Point, transferable: java.awt.datatransfer.Transferable, dragSourceListener: 'DragSourceListener') -> None: ...
    @typing.overload
    def startDrag(self, cursor: java.awt.Cursor, transferable: java.awt.datatransfer.Transferable) -> None: ...
    @typing.overload
    def startDrag(self, cursor: java.awt.Cursor, transferable: java.awt.datatransfer.Transferable, dragSourceListener: 'DragSourceListener') -> None: ...
    @typing.overload
    def toArray(self) -> typing.MutableSequence[typing.Any]: ...
    @typing.overload
    def toArray(self, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.MutableSequence[typing.Any]: ...

class DragGestureListener(java.util.EventListener):
    def dragGestureRecognized(self, dragGestureEvent: DragGestureEvent) -> None: ...

class DragGestureRecognizer(java.io.Serializable):
    def addDragGestureListener(self, dragGestureListener: typing.Union[DragGestureListener, typing.Callable]) -> None: ...
    def getComponent(self) -> java.awt.Component: ...
    def getDragSource(self) -> 'DragSource': ...
    def getSourceActions(self) -> int: ...
    def getTriggerEvent(self) -> java.awt.event.InputEvent: ...
    def removeDragGestureListener(self, dragGestureListener: typing.Union[DragGestureListener, typing.Callable]) -> None: ...
    def resetRecognizer(self) -> None: ...
    def setComponent(self, component: java.awt.Component) -> None: ...
    def setSourceActions(self, int: int) -> None: ...

class DragSource(java.io.Serializable):
    DefaultCopyDrop: typing.ClassVar[java.awt.Cursor] = ...
    DefaultMoveDrop: typing.ClassVar[java.awt.Cursor] = ...
    DefaultLinkDrop: typing.ClassVar[java.awt.Cursor] = ...
    DefaultCopyNoDrop: typing.ClassVar[java.awt.Cursor] = ...
    DefaultMoveNoDrop: typing.ClassVar[java.awt.Cursor] = ...
    DefaultLinkNoDrop: typing.ClassVar[java.awt.Cursor] = ...
    def __init__(self): ...
    def addDragSourceListener(self, dragSourceListener: 'DragSourceListener') -> None: ...
    def addDragSourceMotionListener(self, dragSourceMotionListener: typing.Union['DragSourceMotionListener', typing.Callable]) -> None: ...
    def createDefaultDragGestureRecognizer(self, component: java.awt.Component, int: int, dragGestureListener: typing.Union[DragGestureListener, typing.Callable]) -> DragGestureRecognizer: ...
    _createDragGestureRecognizer__T = typing.TypeVar('_createDragGestureRecognizer__T', bound=DragGestureRecognizer)  # <T>
    def createDragGestureRecognizer(self, class_: typing.Type[_createDragGestureRecognizer__T], component: java.awt.Component, int: int, dragGestureListener: typing.Union[DragGestureListener, typing.Callable]) -> _createDragGestureRecognizer__T: ...
    @staticmethod
    def getDefaultDragSource() -> 'DragSource': ...
    def getDragSourceListeners(self) -> typing.MutableSequence['DragSourceListener']: ...
    def getDragSourceMotionListeners(self) -> typing.MutableSequence['DragSourceMotionListener']: ...
    @staticmethod
    def getDragThreshold() -> int: ...
    def getFlavorMap(self) -> java.awt.datatransfer.FlavorMap: ...
    _getListeners__T = typing.TypeVar('_getListeners__T', bound=java.util.EventListener)  # <T>
    def getListeners(self, class_: typing.Type[_getListeners__T]) -> typing.MutableSequence[_getListeners__T]: ...
    @staticmethod
    def isDragImageSupported() -> bool: ...
    def removeDragSourceListener(self, dragSourceListener: 'DragSourceListener') -> None: ...
    def removeDragSourceMotionListener(self, dragSourceMotionListener: typing.Union['DragSourceMotionListener', typing.Callable]) -> None: ...
    @typing.overload
    def startDrag(self, dragGestureEvent: DragGestureEvent, cursor: java.awt.Cursor, image: java.awt.Image, point: java.awt.Point, transferable: java.awt.datatransfer.Transferable, dragSourceListener: 'DragSourceListener') -> None: ...
    @typing.overload
    def startDrag(self, dragGestureEvent: DragGestureEvent, cursor: java.awt.Cursor, image: java.awt.Image, point: java.awt.Point, transferable: java.awt.datatransfer.Transferable, dragSourceListener: 'DragSourceListener', flavorMap: java.awt.datatransfer.FlavorMap) -> None: ...
    @typing.overload
    def startDrag(self, dragGestureEvent: DragGestureEvent, cursor: java.awt.Cursor, transferable: java.awt.datatransfer.Transferable, dragSourceListener: 'DragSourceListener') -> None: ...
    @typing.overload
    def startDrag(self, dragGestureEvent: DragGestureEvent, cursor: java.awt.Cursor, transferable: java.awt.datatransfer.Transferable, dragSourceListener: 'DragSourceListener', flavorMap: java.awt.datatransfer.FlavorMap) -> None: ...

class DragSourceEvent(java.util.EventObject):
    @typing.overload
    def __init__(self, dragSourceContext: 'DragSourceContext'): ...
    @typing.overload
    def __init__(self, dragSourceContext: 'DragSourceContext', int: int, int2: int): ...
    def getDragSourceContext(self) -> 'DragSourceContext': ...
    def getLocation(self) -> java.awt.Point: ...
    def getX(self) -> int: ...
    def getY(self) -> int: ...

class DragSourceListener(java.util.EventListener):
    def dragDropEnd(self, dragSourceDropEvent: 'DragSourceDropEvent') -> None: ...
    def dragEnter(self, dragSourceDragEvent: 'DragSourceDragEvent') -> None: ...
    def dragExit(self, dragSourceEvent: DragSourceEvent) -> None: ...
    def dragOver(self, dragSourceDragEvent: 'DragSourceDragEvent') -> None: ...
    def dropActionChanged(self, dragSourceDragEvent: 'DragSourceDragEvent') -> None: ...

class DragSourceMotionListener(java.util.EventListener):
    def dragMouseMoved(self, dragSourceDragEvent: 'DragSourceDragEvent') -> None: ...

class DropTargetContext(java.io.Serializable):
    def dropComplete(self, boolean: bool) -> None: ...
    def getComponent(self) -> java.awt.Component: ...
    def getDropTarget(self) -> 'DropTarget': ...

class DropTargetEvent(java.util.EventObject):
    def __init__(self, dropTargetContext: DropTargetContext): ...
    def getDropTargetContext(self) -> DropTargetContext: ...

class DropTargetListener(java.util.EventListener):
    def dragEnter(self, dropTargetDragEvent: 'DropTargetDragEvent') -> None: ...
    def dragExit(self, dropTargetEvent: DropTargetEvent) -> None: ...
    def dragOver(self, dropTargetDragEvent: 'DropTargetDragEvent') -> None: ...
    def drop(self, dropTargetDropEvent: 'DropTargetDropEvent') -> None: ...
    def dropActionChanged(self, dropTargetDragEvent: 'DropTargetDragEvent') -> None: ...

class InvalidDnDOperationException(java.lang.IllegalStateException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class DragSourceAdapter(DragSourceListener, DragSourceMotionListener):
    def dragDropEnd(self, dragSourceDropEvent: 'DragSourceDropEvent') -> None: ...
    def dragEnter(self, dragSourceDragEvent: 'DragSourceDragEvent') -> None: ...
    def dragExit(self, dragSourceEvent: DragSourceEvent) -> None: ...
    def dragMouseMoved(self, dragSourceDragEvent: 'DragSourceDragEvent') -> None: ...
    def dragOver(self, dragSourceDragEvent: 'DragSourceDragEvent') -> None: ...
    def dropActionChanged(self, dragSourceDragEvent: 'DragSourceDragEvent') -> None: ...

class DragSourceContext(DragSourceListener, DragSourceMotionListener, java.io.Serializable):
    def __init__(self, dragGestureEvent: DragGestureEvent, cursor: java.awt.Cursor, image: java.awt.Image, point: java.awt.Point, transferable: java.awt.datatransfer.Transferable, dragSourceListener: DragSourceListener): ...
    def addDragSourceListener(self, dragSourceListener: DragSourceListener) -> None: ...
    def dragDropEnd(self, dragSourceDropEvent: 'DragSourceDropEvent') -> None: ...
    def dragEnter(self, dragSourceDragEvent: 'DragSourceDragEvent') -> None: ...
    def dragExit(self, dragSourceEvent: DragSourceEvent) -> None: ...
    def dragMouseMoved(self, dragSourceDragEvent: 'DragSourceDragEvent') -> None: ...
    def dragOver(self, dragSourceDragEvent: 'DragSourceDragEvent') -> None: ...
    def dropActionChanged(self, dragSourceDragEvent: 'DragSourceDragEvent') -> None: ...
    def getComponent(self) -> java.awt.Component: ...
    def getCursor(self) -> java.awt.Cursor: ...
    def getDragSource(self) -> DragSource: ...
    def getSourceActions(self) -> int: ...
    def getTransferable(self) -> java.awt.datatransfer.Transferable: ...
    def getTrigger(self) -> DragGestureEvent: ...
    def removeDragSourceListener(self, dragSourceListener: DragSourceListener) -> None: ...
    def setCursor(self, cursor: java.awt.Cursor) -> None: ...
    def transferablesFlavorsChanged(self) -> None: ...

class DragSourceDragEvent(DragSourceEvent):
    @typing.overload
    def __init__(self, dragSourceContext: DragSourceContext, int: int, int2: int, int3: int): ...
    @typing.overload
    def __init__(self, dragSourceContext: DragSourceContext, int: int, int2: int, int3: int, int4: int, int5: int): ...
    def getDropAction(self) -> int: ...
    def getGestureModifiers(self) -> int: ...
    def getGestureModifiersEx(self) -> int: ...
    def getTargetActions(self) -> int: ...
    def getUserAction(self) -> int: ...

class DragSourceDropEvent(DragSourceEvent):
    @typing.overload
    def __init__(self, dragSourceContext: DragSourceContext): ...
    @typing.overload
    def __init__(self, dragSourceContext: DragSourceContext, int: int, boolean: bool): ...
    @typing.overload
    def __init__(self, dragSourceContext: DragSourceContext, int: int, boolean: bool, int2: int, int3: int): ...
    def getDropAction(self) -> int: ...
    def getDropSuccess(self) -> bool: ...

class DropTarget(DropTargetListener, java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, dropTargetListener: DropTargetListener): ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, dropTargetListener: DropTargetListener, boolean: bool): ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, dropTargetListener: DropTargetListener, boolean: bool, flavorMap: java.awt.datatransfer.FlavorMap): ...
    @typing.overload
    def __init__(self, component: java.awt.Component, dropTargetListener: DropTargetListener): ...
    def addDropTargetListener(self, dropTargetListener: DropTargetListener) -> None: ...
    def addNotify(self) -> None: ...
    def dragEnter(self, dropTargetDragEvent: 'DropTargetDragEvent') -> None: ...
    def dragExit(self, dropTargetEvent: DropTargetEvent) -> None: ...
    def dragOver(self, dropTargetDragEvent: 'DropTargetDragEvent') -> None: ...
    def drop(self, dropTargetDropEvent: 'DropTargetDropEvent') -> None: ...
    def dropActionChanged(self, dropTargetDragEvent: 'DropTargetDragEvent') -> None: ...
    def getComponent(self) -> java.awt.Component: ...
    def getDefaultActions(self) -> int: ...
    def getDropTargetContext(self) -> DropTargetContext: ...
    def getFlavorMap(self) -> java.awt.datatransfer.FlavorMap: ...
    def isActive(self) -> bool: ...
    def removeDropTargetListener(self, dropTargetListener: DropTargetListener) -> None: ...
    def removeNotify(self) -> None: ...
    def setActive(self, boolean: bool) -> None: ...
    def setComponent(self, component: java.awt.Component) -> None: ...
    def setDefaultActions(self, int: int) -> None: ...
    def setFlavorMap(self, flavorMap: java.awt.datatransfer.FlavorMap) -> None: ...

class DropTargetAdapter(DropTargetListener):
    def dragEnter(self, dropTargetDragEvent: 'DropTargetDragEvent') -> None: ...
    def dragExit(self, dropTargetEvent: DropTargetEvent) -> None: ...
    def dragOver(self, dropTargetDragEvent: 'DropTargetDragEvent') -> None: ...
    def dropActionChanged(self, dropTargetDragEvent: 'DropTargetDragEvent') -> None: ...

class DropTargetDragEvent(DropTargetEvent):
    def __init__(self, dropTargetContext: DropTargetContext, point: java.awt.Point, int: int, int2: int): ...
    def acceptDrag(self, int: int) -> None: ...
    def getCurrentDataFlavors(self) -> typing.MutableSequence[java.awt.datatransfer.DataFlavor]: ...
    def getCurrentDataFlavorsAsList(self) -> java.util.List[java.awt.datatransfer.DataFlavor]: ...
    def getDropAction(self) -> int: ...
    def getLocation(self) -> java.awt.Point: ...
    def getSourceActions(self) -> int: ...
    def getTransferable(self) -> java.awt.datatransfer.Transferable: ...
    def isDataFlavorSupported(self, dataFlavor: java.awt.datatransfer.DataFlavor) -> bool: ...
    def rejectDrag(self) -> None: ...

class DropTargetDropEvent(DropTargetEvent):
    @typing.overload
    def __init__(self, dropTargetContext: DropTargetContext, point: java.awt.Point, int: int, int2: int): ...
    @typing.overload
    def __init__(self, dropTargetContext: DropTargetContext, point: java.awt.Point, int: int, int2: int, boolean: bool): ...
    def acceptDrop(self, int: int) -> None: ...
    def dropComplete(self, boolean: bool) -> None: ...
    def getCurrentDataFlavors(self) -> typing.MutableSequence[java.awt.datatransfer.DataFlavor]: ...
    def getCurrentDataFlavorsAsList(self) -> java.util.List[java.awt.datatransfer.DataFlavor]: ...
    def getDropAction(self) -> int: ...
    def getLocation(self) -> java.awt.Point: ...
    def getSourceActions(self) -> int: ...
    def getTransferable(self) -> java.awt.datatransfer.Transferable: ...
    def isDataFlavorSupported(self, dataFlavor: java.awt.datatransfer.DataFlavor) -> bool: ...
    def isLocalTransfer(self) -> bool: ...
    def rejectDrop(self) -> None: ...

class MouseDragGestureRecognizer(DragGestureRecognizer, java.awt.event.MouseListener, java.awt.event.MouseMotionListener):
    def mouseClicked(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
    def mouseDragged(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
    def mouseEntered(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
    def mouseExited(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
    def mouseMoved(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
    def mousePressed(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
    def mouseReleased(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.awt.dnd")``.

    Autoscroll: typing.Type[Autoscroll]
    DnDConstants: typing.Type[DnDConstants]
    DragGestureEvent: typing.Type[DragGestureEvent]
    DragGestureListener: typing.Type[DragGestureListener]
    DragGestureRecognizer: typing.Type[DragGestureRecognizer]
    DragSource: typing.Type[DragSource]
    DragSourceAdapter: typing.Type[DragSourceAdapter]
    DragSourceContext: typing.Type[DragSourceContext]
    DragSourceDragEvent: typing.Type[DragSourceDragEvent]
    DragSourceDropEvent: typing.Type[DragSourceDropEvent]
    DragSourceEvent: typing.Type[DragSourceEvent]
    DragSourceListener: typing.Type[DragSourceListener]
    DragSourceMotionListener: typing.Type[DragSourceMotionListener]
    DropTarget: typing.Type[DropTarget]
    DropTargetAdapter: typing.Type[DropTargetAdapter]
    DropTargetContext: typing.Type[DropTargetContext]
    DropTargetDragEvent: typing.Type[DropTargetDragEvent]
    DropTargetDropEvent: typing.Type[DropTargetDropEvent]
    DropTargetEvent: typing.Type[DropTargetEvent]
    DropTargetListener: typing.Type[DropTargetListener]
    InvalidDnDOperationException: typing.Type[InvalidDnDOperationException]
    MouseDragGestureRecognizer: typing.Type[MouseDragGestureRecognizer]
    peer: java.awt.dnd.peer.__module_protocol__
