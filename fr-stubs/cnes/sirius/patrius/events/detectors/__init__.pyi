
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import fr.cnes.sirius.patrius.assembly
import fr.cnes.sirius.patrius.assembly.models
import fr.cnes.sirius.patrius.attitudes.directions
import fr.cnes.sirius.patrius.bodies
import fr.cnes.sirius.patrius.events
import fr.cnes.sirius.patrius.events.postprocessing
import fr.cnes.sirius.patrius.fieldsofview
import fr.cnes.sirius.patrius.frames
import fr.cnes.sirius.patrius.groundstation
import fr.cnes.sirius.patrius.math.geometry.euclidean.threed
import fr.cnes.sirius.patrius.math.linear
import fr.cnes.sirius.patrius.orbits
import fr.cnes.sirius.patrius.orbits.pvcoordinates
import fr.cnes.sirius.patrius.propagation
import fr.cnes.sirius.patrius.signalpropagation
import fr.cnes.sirius.patrius.time
import java.io
import java.lang
import java.util
import jpype
import typing



class AOLDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class AOLDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Detects when the Argument of Latitude of the spacecraft reaches a predetermined value, θ.
    
    
        The Argument of Latitude is not defined for all kinds of orbits: this detector will detect an event only if the
        corresponding orbit is not an equatorial orbit, otherwise it may trigger events randomly.
    
        The default implementation behaviour is to :code:`EventDetector.Action#STOP` stop propagation when the angle θ is
        reached. This can be changed by using provided constructors.
    
        Since:
            1.1
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, positionAngle: fr.cnes.sirius.patrius.orbits.PositionAngle, frame: fr.cnes.sirius.patrius.frames.Frame): ...
    @typing.overload
    def __init__(self, double: float, positionAngle: fr.cnes.sirius.patrius.orbits.PositionAngle, frame: fr.cnes.sirius.patrius.frames.Frame, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, positionAngle: fr.cnes.sirius.patrius.orbits.PositionAngle, frame: fr.cnes.sirius.patrius.frames.Frame, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, double: float, positionAngle: fr.cnes.sirius.patrius.orbits.PositionAngle, frame: fr.cnes.sirius.patrius.frames.Frame, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - refFrame: :class:`~fr.cnes.sirius.patrius.frames.Frame`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getAOL(self) -> float:
        """
            Get the AOL to detect.
        
            Returns:
                the angle triggering the event.
        
        
        """
        ...
    def getAOLFrame(self) -> fr.cnes.sirius.patrius.frames.Frame:
        """
            Get the reference frame.
        
            Returns:
                the reference frame to compute AOL
        
        
        """
        ...
    def getAOLType(self) -> fr.cnes.sirius.patrius.orbits.PositionAngle:
        """
            Get the type of AOL to detect.
        
            Returns:
                the type of angle triggering the event
        
        
        """
        ...
    def getAction(self) -> fr.cnes.sirius.patrius.events.EventDetector.Action:
        """
            Return the action at detection.
        
            Returns:
                action at detection
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class AbstractSignalPropagationDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public abstract class AbstractSignalPropagationDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Common parts shared by several events finders related to signal propagation concept.
    
    
        A default implementation of most of the methods of EventDetector Interface.
    
    
        Make it easier to create a new detector.
    
        Since:
            4.13
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool, linkTypeHandler: 'LinkTypeHandler'): ...
    @typing.overload
    def __init__(self, double: float, double2: float, linkTypeHandler: 'LinkTypeHandler'): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, linkTypeHandler: 'LinkTypeHandler'): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool, linkTypeHandler: 'LinkTypeHandler'): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, linkTypeHandler: 'LinkTypeHandler'): ...
    def getEmitter(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
            Getter for the signal emitter.
        
            Parameters:
                s (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): the spacecraft state used by the detector
        
            Returns:
                the signal emitter
        
        
        """
        ...
    def getEpsilonSignalPropagation(self) -> float:
        """
            Getter for the epsilon for signal propagation when signal propagation is taken into account.
        
            Returns:
                the epsilon for signal propagation when signal propagation is taken into account
        
        
        """
        ...
    def getEventDatationType(self) -> 'AbstractSignalPropagationDetector.EventDatationType':
        """
            Specify if the event datation type corresponds to the emitter date or the receiver date.
        
            Returns:
                the corresponding event datation type
        
        
        """
        ...
    def getInertialFrame(self) -> fr.cnes.sirius.patrius.frames.Frame:
        """
            Getter for the inertial frame used for signal propagation computation.
        
            Returns:
                the inertial frame
        
        
        """
        ...
    def getLinkTypeHandler(self) -> 'LinkTypeHandler':
        """
            Getter for the link type handler.
        
            Returns:
                the link type handler
        
        
        """
        ...
    def getMaxIterSignalPropagation(self) -> int:
        """
            Getter for the maximum number of iterations for signal propagation when signal propagation is taken into account.
        
            Returns:
                the maximum number of iterations for signal propagation
        
        
        """
        ...
    def getOtherDate(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> fr.cnes.sirius.patrius.time.AbsoluteDate: ...
    def getPropagationDelayType(self) -> 'AbstractSignalPropagationDetector.PropagationDelayType':
        """
            Getter for the propagation delay type.
        
            Returns:
                the propagation delay type
        
        
        """
        ...
    def getReceiver(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
            Getter for the signal receiver.
        
            Parameters:
                s (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): the spacecraft state used by the detector
        
            Returns:
                the signal receiver
        
        
        """
        ...
    @typing.overload
    def getSignalEmissionDate(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.time.AbsoluteDate: ...
    @typing.overload
    def getSignalEmissionDate(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> fr.cnes.sirius.patrius.time.AbsoluteDate: ...
    @typing.overload
    def getSignalReceptionDate(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.time.AbsoluteDate: ...
    @typing.overload
    def getSignalReceptionDate(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> fr.cnes.sirius.patrius.time.AbsoluteDate: ...
    def setEpsilonSignalPropagation(self, double: float) -> None:
        """
            Setter for the epsilon for signal propagation when signal propagation is taken into account.
        
        
            This epsilon (in s) directly reflect the accuracy of signal propagation (1s of accuracy = 3E8m of accuracy on distance
            between emitter and receiver)
        
            Parameters:
                epsilon (double): Epsilon for the signal propagation
        
        
        """
        ...
    def setMaxIterSignalPropagation(self, int: int) -> None:
        """
            Setter for the maximum number of iterations for signal propagation when signal propagation is taken into account.
        
            Parameters:
                maxIterSignalPropagationIn (int): Maximum number of iterations for signal propagation
        
        
        """
        ...
    def setPropagationDelayType(self, propagationDelayType: 'AbstractSignalPropagationDetector.PropagationDelayType', frame: fr.cnes.sirius.patrius.frames.Frame) -> None:
        """
            Setter for the propagation delay computation type. Warning: check Javadoc of detector to see if detector takes into
            account propagation time delay. if not, signals are always considered instantaneous. The provided frame is used to
            compute the signal propagation when delay is taken into account.
        
            Parameters:
                propagationDelayTypeIn (:class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.PropagationDelayType`): Propagation delay type used in events computation
                frameIn (:class:`~fr.cnes.sirius.patrius.frames.Frame`): Frame to use for signal propagation with delay (may be null if propagation delay type is considered instantaneous).
                    Warning: the usage of a pseudo inertial frame is tolerated, however it will lead to some inaccuracies due to the
                    non-invariance of the frame with respect to time. For this reason, it is suggested to use the ICRF frame or a frame
                    which is frozen with respect to the ICRF.
        
            Raises:
                : if the provided frame is not pseudo inertial.
        
        
        """
        ...
    class EventDatationType(java.lang.Enum['AbstractSignalPropagationDetector.EventDatationType']):
        EMITTER: typing.ClassVar['AbstractSignalPropagationDetector.EventDatationType'] = ...
        RECEIVER: typing.ClassVar['AbstractSignalPropagationDetector.EventDatationType'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'AbstractSignalPropagationDetector.EventDatationType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['AbstractSignalPropagationDetector.EventDatationType']: ...
    class PropagationDelayType(java.lang.Enum['AbstractSignalPropagationDetector.PropagationDelayType']):
        INSTANTANEOUS: typing.ClassVar['AbstractSignalPropagationDetector.PropagationDelayType'] = ...
        LIGHT_SPEED: typing.ClassVar['AbstractSignalPropagationDetector.PropagationDelayType'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'AbstractSignalPropagationDetector.PropagationDelayType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['AbstractSignalPropagationDetector.PropagationDelayType']: ...

class AlignmentDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class AlignmentDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Finder for satellite/body alignment events.
    
        This class finds alignment events.
    
        Alignment means the conjunction, with some threshold angle, between the satellite position and the projection in the
        orbital plane of some body position.
    
        The default implementation behavior is to :code:`EventDetector.Action#STOP` stop propagation when alignment is reached.
        This can be changed by using provided constructors.
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.propagation.Propagator.addEventDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, orbit: fr.cnes.sirius.patrius.orbits.Orbit, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float): ...
    @typing.overload
    def __init__(self, orbit: fr.cnes.sirius.patrius.orbits.Orbit, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float): ...
    @typing.overload
    def __init__(self, orbit: fr.cnes.sirius.patrius.orbits.Orbit, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, orbit: fr.cnes.sirius.patrius.orbits.Orbit, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - body: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getAlignAngle(self) -> float:
        """
            Get the alignment angle (rad).
        
            Returns:
                the alignment angle
        
        
        """
        ...
    def getPVCoordinatesProvider(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
            Get the body to align.
        
            Returns:
                the body to align
        
        
        """
        ...

class AltitudeDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class AltitudeDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Finder for satellite altitude crossing events.
    
        This class finds altitude events (i.e. satellite crossing a predefined altitude level above ground).
    
        The default implementation behavior is to :code:`EventDetector.Action#CONTINUE` continue propagation when ascending and
        to :code:`EventDetector.Action#STOP` stop propagation when descending. This can be changed by using provided
        constructors.
    
        This class is restricted to be used with :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`.
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.propagation.Propagator.addEventDetector`, :meth:`~serialized`
    """
    ASCENDING: typing.ClassVar[int] = ...
    """
    public static final int ASCENDING
    
        Flag for ascending altitude detection (slopeSelection = 0).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DESCENDING: typing.ClassVar[int] = ...
    """
    public static final int DESCENDING
    
        Flag for descending altitude detection (slopeSelection = 1).
    
        Also see:
            :meth:`~constant`
    
    
    """
    ASCENDING_DESCENDING: typing.ClassVar[int] = ...
    """
    public static final int ASCENDING_DESCENDING
    
        Flag for both ascending and descending altitude detection (slopeSelection = 2).
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, ellipsoidBodyShape: fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape): ...
    @typing.overload
    def __init__(self, double: float, ellipsoidBodyShape: fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, ellipsoidBodyShape: fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, double: float, ellipsoidBodyShape: fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, double: float, ellipsoidBodyShape: fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape, int: int, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - bodyShape: :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getAltitude(self) -> float:
        """
            Getter for the threshold altitude value.
        
            Returns:
                the threshold altitude value (m)
        
        
        """
        ...
    def getBodyShape(self) -> fr.cnes.sirius.patrius.bodies.BodyShape:
        """
            Getter for the body shape.
        
            Returns:
                the body shape
        
        
        """
        ...

class AngularMomentumExcessDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public final class AngularMomentumExcessDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Detector triggered when the angular momentum reaches a maximal threshold
    
        Since:
            4.11
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, frame: fr.cnes.sirius.patrius.frames.Frame, int: int): ...
    @typing.overload
    def __init__(self, double: float, frame: fr.cnes.sirius.patrius.frames.Frame, int: int, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, frame: fr.cnes.sirius.patrius.frames.Frame, int: int, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def setAttitudeRepresentedFrame(self, frame: fr.cnes.sirius.patrius.frames.Frame) -> None:
        """
            Define the frame represented by the attitude law
        
            Parameters:
                frame (:class:`~fr.cnes.sirius.patrius.frames.Frame`): the attitude represented law
        
        
        """
        ...
    def setInertia(self, realMatrix: fr.cnes.sirius.patrius.math.linear.RealMatrix, frame: fr.cnes.sirius.patrius.frames.Frame) -> None:
        """
            Define the inertia matrix (from CoM and in vehicle axis)
        
            Parameters:
                inertia (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the inertia 3x3 matrix expressed in CoM
                frame (:class:`~fr.cnes.sirius.patrius.frames.Frame`): Frame
        
        
        """
        ...

class AnomalyDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class AnomalyDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Detects when the anomaly of the spacecraft reaches a predetermined value, θ.
    
    
        Anomaly is not defined for all kinds of orbits: this detector will detect anomaly events only if the corresponding orbit
        is not a circular orbit, otherwise it may trigger events randomly.
    
        The default implementation behaviour is to :code:`EventDetector.Action#STOP` stop propagation when the anomaly θ is
        reached. This can be changed by using provided constructors.
        This detector is unusable on a circular orbit where the perigee always moves very fast and in any way. This detector
        detects only anomaly going in a growing way.
    
        Since:
            1.1
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, positionAngle: fr.cnes.sirius.patrius.orbits.PositionAngle, double: float): ...
    @typing.overload
    def __init__(self, positionAngle: fr.cnes.sirius.patrius.orbits.PositionAngle, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, positionAngle: fr.cnes.sirius.patrius.orbits.PositionAngle, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, positionAngle: fr.cnes.sirius.patrius.orbits.PositionAngle, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getAction(self) -> fr.cnes.sirius.patrius.events.EventDetector.Action:
        """
            Return the action at detection.
        
            Returns:
                action at detection
        
        
        """
        ...
    def getAnomaly(self) -> float:
        """
            Get the anomaly to detect.
        
            Returns:
                the anomaly triggering the event.
        
        
        """
        ...
    def getAnomalyType(self) -> fr.cnes.sirius.patrius.orbits.PositionAngle:
        """
            Get the type of anomaly to detect.
        
            Returns:
                the anomaly type
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class ApsideDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class ApsideDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Finder for apside crossing events.
    
        This class finds apside crossing events (i.e. apogee and/or perigee crossing).
    
        The default implementation behavior is to :code:`EventDetector.Action#STOP` stop propagation at apogee or/and perigee
        crossing depending on slope selection defined :meth:`~fr.cnes.sirius.patrius.events.detectors.ApsideDetector.PERIGEE`,
        :meth:`~fr.cnes.sirius.patrius.events.detectors.ApsideDetector.APOGEE` and
        :meth:`~fr.cnes.sirius.patrius.events.detectors.ApsideDetector.PERIGEE_APOGEE`. This can be changed by overriding one of
        the following constructors :
    
          - :meth:`~fr.cnes.sirius.patrius.events.detectors.ApsideDetector.ApsideDetector` : the defined action is performed at
            apogee OR/AND perigee depending on slope selection defined.
          - :meth:`~fr.cnes.sirius.patrius.events.detectors.ApsideDetector.ApsideDetector` : the defined actions are performed at
            apogee AND perigee.
    
    
        Beware that apside detection will fail for almost circular orbits.
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.propagation.Propagator.addEventDetector`, :meth:`~serialized`
    """
    PERIGEE: typing.ClassVar[int] = ...
    """
    public static final int PERIGEE
    
        Flag for perigee detection (slopeSelection = 0).
    
        Also see:
            :meth:`~constant`
    
    
    """
    APOGEE: typing.ClassVar[int] = ...
    """
    public static final int APOGEE
    
        Flag for apogee detection (slopeSelection = 1).
    
        Also see:
            :meth:`~constant`
    
    
    """
    PERIGEE_APOGEE: typing.ClassVar[int] = ...
    """
    public static final int PERIGEE_APOGEE
    
        Flag for both perigee and apogee detection (slopeSelection = 2).
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, orbit: fr.cnes.sirius.patrius.orbits.Orbit, int: int): ...
    @typing.overload
    def __init__(self, orbit: fr.cnes.sirius.patrius.orbits.Orbit, int: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...

class CenteredAolPassageDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public final class CenteredAolPassageDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Centered argument of latitude detector
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, positionAngle: fr.cnes.sirius.patrius.orbits.PositionAngle, meanOsculatingElementsProvider: fr.cnes.sirius.patrius.propagation.MeanOsculatingElementsProvider, frame: fr.cnes.sirius.patrius.frames.Frame): ...
    @typing.overload
    def __init__(self, double: float, positionAngle: fr.cnes.sirius.patrius.orbits.PositionAngle, meanOsculatingElementsProvider: fr.cnes.sirius.patrius.propagation.MeanOsculatingElementsProvider, frame: fr.cnes.sirius.patrius.frames.Frame, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, positionAngle: fr.cnes.sirius.patrius.orbits.PositionAngle, meanOsculatingElementsProvider: fr.cnes.sirius.patrius.propagation.MeanOsculatingElementsProvider, frame: fr.cnes.sirius.patrius.frames.Frame, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    def centeredToOsculating(self, circularOrbit: fr.cnes.sirius.patrius.orbits.CircularOrbit) -> fr.cnes.sirius.patrius.orbits.Orbit: ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...

class CombinedPhenomenaDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class CombinedPhenomenaDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
    
        This class finds the events resulting from the combination of two phenomena. Combinations of phenomena can be done using
        the following boolean operators:
    
    
    
          - AND : combined events are detected only both phenomena associated to event1 and event2 are active (i.e. an event is
            detected if event1 is triggered and phenomenon associated to event2 is active, or vice-versa);
          - OR : combined events are detected if at least one of the phenomena associated to event1 and event2 is active (i.e. an
            event is detected if event1 or event2 are triggered);
    
    
    
    
        The default implementation behaviour is to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.CONTINUE`
        propagation when combined phnomena are detected. This can be changed by using one of the provided constructors.
    
        Since:
            1.1
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`,
            :meth:`~fr.cnes.sirius.patrius.propagation.Propagator.addEventDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, eventDetector: fr.cnes.sirius.patrius.events.EventDetector, boolean: bool, eventDetector2: fr.cnes.sirius.patrius.events.EventDetector, boolean2: bool, boolean3: bool): ...
    @typing.overload
    def __init__(self, eventDetector: fr.cnes.sirius.patrius.events.EventDetector, boolean: bool, eventDetector2: fr.cnes.sirius.patrius.events.EventDetector, boolean2: bool, boolean3: bool, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getDetector1(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            Returns first detector.
        
            Returns:
                EventDetector 1
        
        
        """
        ...
    def getDetector2(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            Returns second detector.
        
            Returns:
                EventDetector 2
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None: ...
    def shouldBeRemoved(self) -> bool:
        """
            This method is called after :meth:`~fr.cnes.sirius.patrius.events.EventDetector.eventOccurred` has been triggered. It
            returns true if the current detector should be removed after first event detection. **WARNING:** this method can be
            called only once a event has been triggered. Before, the value is not available.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.shouldBeRemoved` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.shouldBeRemoved` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Returns:
                true if the current detector should be removed after first event detection
        
        
        """
        ...

class DateDetector(fr.cnes.sirius.patrius.events.AbstractDetector, fr.cnes.sirius.patrius.time.TimeStamped):
    """
    public class DateDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector` implements :class:`~fr.cnes.sirius.patrius.time.TimeStamped`
    
        Finder for date events.
    
        This class finds date events (i.e. occurrence of some predefined dates).
    
        As of version 5.1, it is an enhanced date detector:
    
          - it can be defined without prior date (:meth:`~fr.cnes.sirius.patrius.events.detectors.DateDetector.DateDetector`)
          - several dates can be added (:meth:`~fr.cnes.sirius.patrius.events.detectors.DateDetector.addEventDate`)
    
    
        The gap between the added dates must be more than the maxCheck.
    
        The default implementation behavior is to :code:`EventDetector.Action#STOP` stop propagation at the first event date
        occurrence. This can be changed by using provided constructors.
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.propagation.Propagator.addEventDetector`, :meth:`~serialized`
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_THRESHOLD
    
        Default convergence threshold (s).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_MAXCHECK: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_MAXCHECK
    
        Default convergence threshold (s).
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate): ...
    @typing.overload
    def __init__(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, double: float, double2: float): ...
    @typing.overload
    def __init__(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    def addEventDate(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Add an event date.
        
            The date to add must be:
        
              - less than the smallest already registered event date minus the maxCheck
              - or more than the largest already registered event date plus the maxCheck
        
        
            Parameters:
                target (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target date
        
            Raises:
                : if the date is too close from already defined interval
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.events.detectors.DateDetector.DateDetector`
        
        
        """
        ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.copy` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getAction(self) -> fr.cnes.sirius.patrius.events.EventDetector.Action:
        """
            Return the action at detection.
        
            Returns:
                action at detection
        
        
        """
        ...
    def getDate(self) -> fr.cnes.sirius.patrius.time.AbsoluteDate:
        """
            Get the current event date according to the propagator.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.time.TimeStamped.getDate` in interface :class:`~fr.cnes.sirius.patrius.time.TimeStamped`
        
            Returns:
                event date
        
        
        """
        ...

class DistanceDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class DistanceDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Detects when the distance from the spacecraft to a given body reaches a predetermined value.
    
        The default implementation behaviour is to :code:`EventDetector.Action#STOP` stop propagation when the distance is
        reached. This can be changed by using provided constructors.
    
        Since:
            1.1
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`, :meth:`~serialized`
    """
    INCREASING: typing.ClassVar[int] = ...
    """
    public static final int INCREASING
    
        Flag for increasing distance detection (slopeSelection = 0).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DECREASING: typing.ClassVar[int] = ...
    """
    public static final int DECREASING
    
        Flag for decreasing distance detection (slopeSelection = 1).
    
        Also see:
            :meth:`~constant`
    
    
    """
    INCREASING_DECREASING: typing.ClassVar[int] = ...
    """
    public static final int INCREASING_DECREASING
    
        Flag for both increasing and decreasing distance detection (slopeSelection = 2).
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, int: int, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - body: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getBody(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
            Returns the body whose distance is watched.
        
            Returns:
                the body whose distance is watched
        
        
        """
        ...
    def getDistance(self) -> float:
        """
            Returns the distance triggering the event.
        
            Returns:
                the distance triggering the event (m)
        
        
        """
        ...

class DotProductDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public final class DotProductDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Detects when the dot product value between a spacecraft and a target PV coordinates reaches a threshold value.
    
        Since:
            4.11
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, iDirection: fr.cnes.sirius.patrius.attitudes.directions.IDirection, boolean: bool, boolean2: bool, double: float, frame: fr.cnes.sirius.patrius.frames.Frame, int: int): ...
    @typing.overload
    def __init__(self, iDirection: fr.cnes.sirius.patrius.attitudes.directions.IDirection, boolean: bool, boolean2: bool, double: float, frame: fr.cnes.sirius.patrius.frames.Frame, int: int, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, iDirection: fr.cnes.sirius.patrius.attitudes.directions.IDirection, boolean: bool, boolean2: bool, double: float, frame: fr.cnes.sirius.patrius.frames.Frame, int: int, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, iDirection: fr.cnes.sirius.patrius.attitudes.directions.IDirection, iDirection2: fr.cnes.sirius.patrius.attitudes.directions.IDirection, boolean: bool, boolean2: bool, double: float, frame: fr.cnes.sirius.patrius.frames.Frame, int: int, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, boolean: bool, boolean2: bool, double: float, frame: fr.cnes.sirius.patrius.frames.Frame, int: int): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, boolean: bool, boolean2: bool, double: float, frame: fr.cnes.sirius.patrius.frames.Frame, int: int, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, boolean: bool, boolean2: bool, double: float, frame: fr.cnes.sirius.patrius.frames.Frame, int: int, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...

class EarthZoneDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class EarthZoneDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Detects when the satellite enters a ground zone (several zones can be defined at the same time).
    
        The default implementation behaviour is to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.STOP` propagation
        when the spacecraft enters the zone and to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.CONTINUE` when it
        leaves it. This can be changed by using one of the provided constructors.
    
        Beware of the MaxCheck and Threshold parameters : if the zone is complex and the MaxCheck too large, the event detection
        could fail, because it would not manage to converge. To compute an approximative event even if the zone is precise and
        complex, set a large enough Threshold.
    
        Since:
            1.1
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`, :class:`~fr.cnes.sirius.patrius.fieldsofview.PyramidalField`,
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, ellipsoidBodyShape: fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape, list: java.util.List[typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]]): ...
    @typing.overload
    def __init__(self, ellipsoidBodyShape: fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape, list: java.util.List[typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]], double: float, double2: float): ...
    @typing.overload
    def __init__(self, ellipsoidBodyShape: fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape, list: java.util.List[typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]], double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, ellipsoidBodyShape: fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape, list: java.util.List[typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]], double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, list: java.util.List[fr.cnes.sirius.patrius.fieldsofview.IFieldOfView], ellipsoidBodyShape: fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, list: java.util.List[typing.Union[typing.List[fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D], jpype.JArray]], frame: fr.cnes.sirius.patrius.frames.Frame): ...
    @typing.overload
    def __init__(self, list: java.util.List[typing.Union[typing.List[fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D], jpype.JArray]], frame: fr.cnes.sirius.patrius.frames.Frame, double: float, double2: float): ...
    @typing.overload
    def __init__(self, list: java.util.List[typing.Union[typing.List[fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D], jpype.JArray]], frame: fr.cnes.sirius.patrius.frames.Frame, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, list: java.util.List[typing.Union[typing.List[fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D], jpype.JArray]], frame: fr.cnes.sirius.patrius.frames.Frame, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - centralBodyShape: :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
              - fields: list of :class:`~fr.cnes.sirius.patrius.fieldsofview.IFieldOfView`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getCentralBodyShape(self) -> fr.cnes.sirius.patrius.bodies.BodyShape:
        """
            Getter for the central body shape.
        
            Returns:
                the central Body shape
        
        
        """
        ...
    def getFOV(self) -> java.util.List[fr.cnes.sirius.patrius.fieldsofview.IFieldOfView]: ...
    def getFrame(self) -> fr.cnes.sirius.patrius.frames.Frame:
        """
            Getter for the frame.
        
            Returns:
                the frame
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class ElevationDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class ElevationDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Finder for satellite raising/setting events.
    
        This class finds elevation events (i.e. satellite raising and setting).
    
        The default implementation behavior is to :code:`EventDetector.Action#CONTINUE` continue propagation at raising and to
        :code:`EventDetector.Action#STOP` stop propagation at setting. This can be changed by using provided constructors.
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.propagation.Propagator.addEventDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame): ...
    @typing.overload
    def __init__(self, double: float, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, double2: float): ...
    @typing.overload
    def __init__(self, double: float, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, double: float, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - topo: :class:`~fr.cnes.sirius.patrius.frames.TopocentricFrame`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getElevation(self) -> float:
        """
            Get the threshold elevation value.
        
            Returns:
                the threshold elevation value (rad)
        
        
        """
        ...
    def getTopocentricFrame(self) -> fr.cnes.sirius.patrius.frames.TopocentricFrame:
        """
            Get the topocentric frame.
        
            Returns:
                the topocentric frame
        
        
        """
        ...

class ExtremaDistanceDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class ExtremaDistanceDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Detects when the distance from the spacecraft to a given body reaches either a local minimum or a local maximum.
    
        The local minimum or maximum is chosen through a constructor parameter, with values
        :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaDistanceDetector.MIN`,
        :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaDistanceDetector.MAX` and
        :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaDistanceDetector.MIN_MAX` for both.
    
        The default implementation behavior is to :code:`EventDetector.Action#STOP` stop propagation at minimum or/and maximum
        distance depending on extremum type defined. This can be changed by using one of the following constructors :
    
          - :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaDistanceDetector.ExtremaDistanceDetector` : the defined action is
            performed at local minimum OR/AND maximum depending on slope selection defined.
          - :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaDistanceDetector.ExtremaDistanceDetector` : the defined actions
            are performed at local minimum AND maximum.
    
    
    
        Since:
            1.1
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`, :meth:`~serialized`
    """
    MIN: typing.ClassVar[int] = ...
    """
    public static final int MIN
    
        Flag for local minimum distance detection (g increasing).
    
        Also see:
            :meth:`~constant`
    
    
    """
    MAX: typing.ClassVar[int] = ...
    """
    public static final int MAX
    
        Flag for local maximum distance detection (g decreasing).
    
        Also see:
            :meth:`~constant`
    
    
    """
    MIN_MAX: typing.ClassVar[int] = ...
    """
    public static final int MIN_MAX
    
        Flag for both local minimum and maximum distance detection.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, int: int): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, int: int, double: float, double2: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - body: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getBody(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
        
            Returns:
                the body
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

_ExtremaGenericDetector__D = typing.TypeVar('_ExtremaGenericDetector__D', bound=fr.cnes.sirius.patrius.events.EventDetector)  # <D>
class ExtremaGenericDetector(fr.cnes.sirius.patrius.events.AbstractDetector, typing.Generic[_ExtremaGenericDetector__D]):
    """
    public class ExtremaGenericDetector<D extends :class:`~fr.cnes.sirius.patrius.events.EventDetector`> extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Detector for extrema of the switching value of
        :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaGenericDetector.underlyingDetector`.
    
        The extrema detector switching function simply returns the difference of the switching function values of underlying
        detector assessed at {date+:meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaGenericDetector.halfComputationStep`
        and {date-:meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaGenericDetector.halfComputationStep` .
    
        The default implementation behavior is to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.CONTINUE`
        propagation at min detection and to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.CONTINUE` propagation at
        max detection. This can be changed by using provided constructors.
    
        Since:
            4.9
    
        Also see:
            :meth:`~serialized`
    """
    DEFAULT_MAXCHECK: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_MAXCHECK
    
        Default maximum checking interval in seconds
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_HALF_COMPUTATION_STEP: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_HALF_COMPUTATION_STEP
    
        Default half computation step.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, d: _ExtremaGenericDetector__D, extremumType: 'ExtremaGenericDetector.ExtremumType'): ...
    @typing.overload
    def __init__(self, d: _ExtremaGenericDetector__D, extremumType: 'ExtremaGenericDetector.ExtremumType', double: float): ...
    @typing.overload
    def __init__(self, d: _ExtremaGenericDetector__D, extremumType: 'ExtremaGenericDetector.ExtremumType', double: float, double2: float): ...
    @typing.overload
    def __init__(self, d: _ExtremaGenericDetector__D, extremumType: 'ExtremaGenericDetector.ExtremumType', double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, d: _ExtremaGenericDetector__D, extremumType: 'ExtremaGenericDetector.ExtremumType', double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, d: _ExtremaGenericDetector__D, extremumType: 'ExtremaGenericDetector.ExtremumType', double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    def copy(self) -> 'ExtremaGenericDetector'[_ExtremaGenericDetector__D]: ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def logExtremaEventsOverTimeInterval(self, codedEventsLogger: fr.cnes.sirius.patrius.events.postprocessing.CodedEventsLogger, propagator: fr.cnes.sirius.patrius.propagation.Propagator, absoluteDateInterval: fr.cnes.sirius.patrius.time.AbsoluteDateInterval) -> fr.cnes.sirius.patrius.propagation.SpacecraftState: ...
    class ExtremumType(java.lang.Enum['ExtremaGenericDetector.ExtremumType']):
        MIN: typing.ClassVar['ExtremaGenericDetector.ExtremumType'] = ...
        MAX: typing.ClassVar['ExtremaGenericDetector.ExtremumType'] = ...
        MIN_MAX: typing.ClassVar['ExtremaGenericDetector.ExtremumType'] = ...
        @staticmethod
        def find(int: int) -> 'ExtremaGenericDetector.ExtremumType': ...
        def getSlopeSelection(self) -> int: ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'ExtremaGenericDetector.ExtremumType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['ExtremaGenericDetector.ExtremumType']: ...

class ExtremaLatitudeDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class ExtremaLatitudeDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Detects when the spacecraft reaches the maximal or minimal local latitude. The local minimum or maximum is chosen
        through a constructor parameter, with values
        :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaLatitudeDetector.MIN`,
        :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaLatitudeDetector.MAX` and
        :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaLatitudeDetector.MIN_MAX` for both.
    
        The default implementation behaviour is to :code:`EventDetector.Action#STOP` stop propagation when the minimum/maximum
        latitude is reached. This can be changed by using provided constructors.
    
        Since:
            1.1
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`, :meth:`~serialized`
    """
    MIN: typing.ClassVar[int] = ...
    """
    public static final int MIN
    
        Flag for local minimum latitude detection (g increasing).
    
        Also see:
            :meth:`~constant`
    
    
    """
    MAX: typing.ClassVar[int] = ...
    """
    public static final int MAX
    
        Flag for local maximum latitude detection (g decreasing).
    
        Also see:
            :meth:`~constant`
    
    
    """
    MIN_MAX: typing.ClassVar[int] = ...
    """
    public static final int MIN_MAX
    
        Flag for both local minimum and maximum distance detection.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, int: int, frame: fr.cnes.sirius.patrius.frames.Frame): ...
    @typing.overload
    def __init__(self, int: int, frame: fr.cnes.sirius.patrius.frames.Frame, double: float, double2: float): ...
    @typing.overload
    def __init__(self, int: int, frame: fr.cnes.sirius.patrius.frames.Frame, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, int: int, frame: fr.cnes.sirius.patrius.frames.Frame, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - bodyFrameIn: :class:`~fr.cnes.sirius.patrius.frames.Frame`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getBodyFrame(self) -> fr.cnes.sirius.patrius.frames.Frame:
        """
            Returns the body frame.
        
            Returns:
                the body frame
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class ExtremaLongitudeDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class ExtremaLongitudeDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Detects when the spacecraft reaches the maximal or minimal local longitude. The local minimum or maximum is chosen
        through a constructor parameter, with values
        :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaLongitudeDetector.MIN`,
        :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaLongitudeDetector.MAX` and
        :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaLongitudeDetector.MIN_MAX` for both.
    
        The default implementation behaviour is to :code:`EventDetector.Action#STOP` stop propagation when the minimum/maximum
        longitude is reached. This can be changed by using provided constructors.
    
        Since:
            1.3
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`, :meth:`~serialized`
    """
    MIN: typing.ClassVar[int] = ...
    """
    public static final int MIN
    
        Flag for local minimum longitude detection (g increasing).
    
        Also see:
            :meth:`~constant`
    
    
    """
    MAX: typing.ClassVar[int] = ...
    """
    public static final int MAX
    
        Flag for local maximum longitude detection (g decreasing).
    
        Also see:
            :meth:`~constant`
    
    
    """
    MIN_MAX: typing.ClassVar[int] = ...
    """
    public static final int MIN_MAX
    
        Flag for both local minimum and maximum distance detection.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, int: int, frame: fr.cnes.sirius.patrius.frames.Frame): ...
    @typing.overload
    def __init__(self, int: int, frame: fr.cnes.sirius.patrius.frames.Frame, double: float, double2: float): ...
    @typing.overload
    def __init__(self, int: int, frame: fr.cnes.sirius.patrius.frames.Frame, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, int: int, frame: fr.cnes.sirius.patrius.frames.Frame, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - bodyFrameIn: :class:`~fr.cnes.sirius.patrius.frames.Frame`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getBodyFrame(self) -> fr.cnes.sirius.patrius.frames.Frame:
        """
            Returns the body frame.
        
            Returns:
                the body frame
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class ExtremaThreeBodiesAngleDetector(fr.cnes.sirius.patrius.events.AbstractDetector, fr.cnes.sirius.patrius.events.MultiEventDetector):
    """
    public class ExtremaThreeBodiesAngleDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector` implements :class:`~fr.cnes.sirius.patrius.events.MultiEventDetector`
    
        Detects the maximal or minimal angle between three bodies is reached, the spacecraft eventually being one of the bodies.
        If body :sub:`1` , body :sub:`2` and body :sub:`3` are the three bodies, the detector computes the angle between the two
        vectors v :sub:`21` (vector from body :sub:`2` to body :sub:`1` ) and v :sub:`23` (vector from body :sub:`2` to body
        :sub:`3` ). The local minimum or maximum is chosen through a constructor parameter, with values
        :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaLatitudeDetector.MIN`,
        :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaLatitudeDetector.MAX` and
        :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaLatitudeDetector.MIN_MAX` for both.
    
        The default implementation behavior is to :code:`EventDetector.Action#STOP` stop propagation at minimum or/and maximum
        angle between three bodies depending on extremum type defined. This can be changed by overriding one of the following
        constructors :
    
          - :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaThreeBodiesAngleDetector.ExtremaThreeBodiesAngleDetector` or
            :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaThreeBodiesAngleDetector.ExtremaThreeBodiesAngleDetector`: the
            defined action is performed at maximal OR/AND minimal angle depending on slope selection defined.
          - :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaThreeBodiesAngleDetector.ExtremaThreeBodiesAngleDetector` or
            :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaThreeBodiesAngleDetector.ExtremaThreeBodiesAngleDetector` : the
            defined actions are performed at minimal AND maximal angle.
    
    
        A multi spacecraft propagation could be performed using the following constructors :
    
          - :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaThreeBodiesAngleDetector.ExtremaThreeBodiesAngleDetector`: the
            defined action is performed at maximal OR/AND minimal angle depending on slope selection defined.
          - :meth:`~fr.cnes.sirius.patrius.events.detectors.ExtremaThreeBodiesAngleDetector.ExtremaThreeBodiesAngleDetector` : the
            defined actions are performed at minimal AND maximal angle.
    
    
        Since:
            1.1
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`, :meth:`~serialized`
    """
    MIN: typing.ClassVar[int] = ...
    """
    public static final int MIN
    
        Flag for local minimum angle detection (g increasing).
    
        Also see:
            :meth:`~constant`
    
    
    """
    MAX: typing.ClassVar[int] = ...
    """
    public static final int MAX
    
        Flag for local maximum angle detection (g decreasing).
    
        Also see:
            :meth:`~constant`
    
    
    """
    MIN_MAX: typing.ClassVar[int] = ...
    """
    public static final int MIN_MAX
    
        Flag for both local minimum and maximum angle detection.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, bodyOrder: 'ExtremaThreeBodiesAngleDetector.BodyOrder', double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, bodyOrder: 'ExtremaThreeBodiesAngleDetector.BodyOrder', double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, bodyOrder: 'ExtremaThreeBodiesAngleDetector.BodyOrder', int: int): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, bodyOrder: 'ExtremaThreeBodiesAngleDetector.BodyOrder', int: int, double: float, double2: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, bodyOrder: 'ExtremaThreeBodiesAngleDetector.BodyOrder', int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, bodyOrder: 'ExtremaThreeBodiesAngleDetector.BodyOrder', int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider3: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider3: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider3: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, int: int): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider3: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, int: int, double: float, double2: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider3: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider3: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - body1: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
              - body2: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
              - body3: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.copy` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    @typing.overload
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    @typing.overload
    def eventOccurred(self, map: typing.Union[java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState], typing.Mapping[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]], boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    @typing.overload
    def filterEvent(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> bool: ...
    @typing.overload
    def filterEvent(self, map: typing.Union[java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState], typing.Mapping[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]], boolean: bool, boolean2: bool) -> bool: ...
    def findFirstCommonPseudoInertial(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, spacecraftState2: fr.cnes.sirius.patrius.propagation.SpacecraftState, spacecraftState3: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> fr.cnes.sirius.patrius.frames.Frame:
        """
            Returns the first common pseudo inertial ancestor between the frames of 3 SpacecraftStates
        
            Parameters:
                s1 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): : The first SpacecraftState
                s2 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): : The second SpacecraftState
                s3 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): : The third SpacecraftState
        
            Returns:
                the first common pseudo inertial ancestor between the frames of 3 SpacecraftStates
        
        
        """
        ...
    @typing.overload
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    @typing.overload
    def g(self, map: typing.Union[java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState], typing.Mapping[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]]) -> float: ...
    def getFirstBody(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
            Get 1st body
        
            Returns:
                the 1st body
        
        
        """
        ...
    def getInSpacecraftId1(self) -> str:
        """
            Get the first spacecraft id
        
            Returns:
                the first spacecraft id
        
        
        """
        ...
    def getInSpacecraftId2(self) -> str:
        """
            Get the second spacecraft id
        
            Returns:
                the second spacecraft id
        
        
        """
        ...
    def getInSpacecraftId3(self) -> str:
        """
            Get the third spacecraft id
        
            Returns:
                the third spacecraft id
        
        
        """
        ...
    def getSecondBody(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
            Get 2nd body
        
            Returns:
                the 2nd body
        
        
        """
        ...
    def getThirdBody(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
            Get 3rd body
        
            Returns:
                the 3rd body
        
        
        """
        ...
    @typing.overload
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        public void init(`Map <http://docs.oracle.com/javase/8/docs/api/java/util/Map.html?is-external=true>`<`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`,:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`> s0, :class:`~fr.cnes.sirius.patrius.time.AbsoluteDate` t)
        
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.MultiEventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.MultiEventDetector`
        
            Parameters:
                s0 (`Map <http://docs.oracle.com/javase/8/docs/api/java/util/Map.html?is-external=true>`<`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`,:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`> s0): map of initial states
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...
    @typing.overload
    def init(self, map: typing.Union[java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState], typing.Mapping[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]], absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None: ...
    def resetStates(self, map: typing.Union[java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState], typing.Mapping[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]]) -> java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]: ...
    class BodyOrder(java.lang.Enum['ExtremaThreeBodiesAngleDetector.BodyOrder']):
        FIRST: typing.ClassVar['ExtremaThreeBodiesAngleDetector.BodyOrder'] = ...
        SECOND: typing.ClassVar['ExtremaThreeBodiesAngleDetector.BodyOrder'] = ...
        THIRD: typing.ClassVar['ExtremaThreeBodiesAngleDetector.BodyOrder'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'ExtremaThreeBodiesAngleDetector.BodyOrder': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['ExtremaThreeBodiesAngleDetector.BodyOrder']: ...

class FlightDomainExcessDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public final class FlightDomainExcessDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, rotationOrder: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], frame: fr.cnes.sirius.patrius.frames.Frame): ...
    @typing.overload
    def __init__(self, rotationOrder: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], frame: fr.cnes.sirius.patrius.frames.Frame, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, rotationOrder: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], frame: fr.cnes.sirius.patrius.frames.Frame, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def setAttitudeRepresentedFrame(self, frame: fr.cnes.sirius.patrius.frames.Frame, frame2: fr.cnes.sirius.patrius.frames.Frame) -> None:
        """
            Define the frame represented by the attitude law and the desired flight domain represented frame
        
            Parameters:
                desiredRepFrame (:class:`~fr.cnes.sirius.patrius.frames.Frame`): the desired represented frame of the flight domain
                satAttFrame (:class:`~fr.cnes.sirius.patrius.frames.Frame`): the satellite attitude law frame
        
        
        """
        ...

class IntervalOccurrenceDetector(fr.cnes.sirius.patrius.events.EventDetector):
    @typing.overload
    def __init__(self, eventDetector: fr.cnes.sirius.patrius.events.EventDetector, int: int, int2: int, int3: int, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, eventDetector: fr.cnes.sirius.patrius.events.EventDetector, int: int, int2: int, int3: int, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector: ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def filterEvent(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> bool: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getActionAtOccurrence(self) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def getCurrentOccurrence(self) -> int: ...
    def getEvent(self) -> fr.cnes.sirius.patrius.events.EventDetector: ...
    def getFirstOccurrence(self) -> int: ...
    def getLastOccurrence(self) -> int: ...
    def getMaxCheckInterval(self) -> float: ...
    def getMaxIterationCount(self) -> int: ...
    def getSlopeSelection(self) -> int: ...
    def getStep(self) -> int: ...
    def getThreshold(self) -> float: ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None: ...
    def isRemoveAtOccurrence(self) -> bool: ...
    def resetState(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> fr.cnes.sirius.patrius.propagation.SpacecraftState: ...
    def shouldBeRemoved(self) -> bool: ...
    def toString(self) -> str: ...

class LatitudeDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class LatitudeDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Detects when the spacecraft reaches a given local latitude.
    
        The default implementation behavior is to :code:`stop` propagation when the expected latitude is reached. This can be
        changed by overriding one of the following constructors :
    
          - :code:`LatitudeDetector` : the defined action is performed at latitude detection depending on slope type defined.
          - :code:`LatitudeDetector` : the defined actions are performed for local increasing AND decreasing latitude.
    
    
    
        Since:
            1.2
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`, :meth:`~serialized`
    """
    UP: typing.ClassVar[int] = ...
    """
    public static final int UP
    
        Flag for local increasing latitude detection (g increasing).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DOWN: typing.ClassVar[int] = ...
    """
    public static final int DOWN
    
        Flag for local decreasing latitude detection (g decreasing).
    
        Also see:
            :meth:`~constant`
    
    
    """
    UP_DOWN: typing.ClassVar[int] = ...
    """
    public static final int UP_DOWN
    
        Flag for both local increasing and decreasing latitude detection.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, ellipsoidBodyShape: fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, double: float, ellipsoidBodyShape: fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, double: float, ellipsoidBodyShape: fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape, int: int): ...
    @typing.overload
    def __init__(self, double: float, ellipsoidBodyShape: fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape, int: int, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, ellipsoidBodyShape: fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape, int: int, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, double: float, ellipsoidBodyShape: fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape, int: int, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - earthShape: :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getEarthShape(self) -> fr.cnes.sirius.patrius.bodies.BodyShape:
        """
            Getter for the Earth shape.
        
            Returns:
                the earthShape
        
        
        """
        ...
    def getLatitudeToDetect(self) -> float:
        """
            Getter for the latitude to detect.
        
            Returns:
                the latitude to detect
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class LinkTypeHandler(java.io.Serializable):
    """
    public class LinkTypeHandler extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Define the role of the main element (SpacecraftState) in the signal propagation (emitter or receiver) and the other
        element.
    
        Since:
            4.14
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, signalPropagationRole: 'LinkTypeHandler.SignalPropagationRole', pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider): ...
    @typing.overload
    def __init__(self, satToSatLinkType: 'SatToSatMutualVisibilityDetector.SatToSatLinkType', pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider): ...
    @typing.overload
    def __init__(self, linkType: 'VisibilityFromStationDetector.LinkType', pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider): ...
    def getMainRole(self) -> 'LinkTypeHandler.SignalPropagationRole':
        """
            Getter for the role of the main element (SpacecraftState) in the signal propagation (emitter or receiver).
        
            Returns:
                the role of the main element
        
        
        """
        ...
    def getOtherElement(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
            Getter for the other element involved in the signal propagation.
        
            Returns:
                the other element involved in the signal propagation
        
        
        """
        ...
    class SignalPropagationRole(java.lang.Enum['LinkTypeHandler.SignalPropagationRole']):
        EMITTER: typing.ClassVar['LinkTypeHandler.SignalPropagationRole'] = ...
        RECEIVER: typing.ClassVar['LinkTypeHandler.SignalPropagationRole'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'LinkTypeHandler.SignalPropagationRole': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['LinkTypeHandler.SignalPropagationRole']: ...

class LongitudeDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class LongitudeDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Detects when the spacecraft reaches a given local longitude.
    
        The default implementation behaviour is to :code:`stop` propagation when the longitude is reached. This can be changed
        by using provided constructors.
    
        Since:
            1.3
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, frame: fr.cnes.sirius.patrius.frames.Frame): ...
    @typing.overload
    def __init__(self, double: float, frame: fr.cnes.sirius.patrius.frames.Frame, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, frame: fr.cnes.sirius.patrius.frames.Frame, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, double: float, frame: fr.cnes.sirius.patrius.frames.Frame, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, double: float, frame: fr.cnes.sirius.patrius.frames.Frame, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, int: int): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - earthcentralBoyFrame: :class:`~fr.cnes.sirius.patrius.frames.Frame`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def filterEvent(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> bool: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getBodyFrame(self) -> fr.cnes.sirius.patrius.frames.Frame:
        """
            Returns central body frame.
        
            Returns:
                the frame of the central body
        
        
        """
        ...
    def getLongitudeToDetect(self) -> float:
        """
            Returns longitude to detect.
        
            Returns:
                the longitude triggering the event.
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class NullMassDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class NullMassDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        This class creates an event detector that detects when the global mass of the satellite becomes null. This detector is
        automatically added (in first position) to every propagator and stops the propagation once it detects a null global
        mass. Since the initial mass is positive or null, the first time where g = 0 will indicate the first time when the mass
        becomes null.
    
        Since:
            2.3
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, double2: float, massProvider: fr.cnes.sirius.patrius.propagation.MassProvider): ...
    @typing.overload
    def __init__(self, massProvider: fr.cnes.sirius.patrius.propagation.MassProvider): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, massProvider: fr.cnes.sirius.patrius.propagation.MassProvider): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - mass: :class:`~fr.cnes.sirius.patrius.propagation.MassProvider`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action:
        """
            If the global mass of the satellite becomes negative, the propagation is stopped.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.eventOccurred` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.eventOccurred` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): the current state information : date, kinematics, attitude
                increasing (boolean): if true, the value of the switching function increases when times increases around event (note that increase is measured
                    with respect to physical time, not with respect to propagation which may go backward in time)
                forward (boolean): if true, the integration variable (time) increases during integration.
        
            Returns:
                EventDetector.Action.STOP
        
        
        """
        ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def isTriggered(self) -> bool:
        """
            Returns true if detector has been triggered.
        
            Returns:
                true if detector has been triggered
        
        
        """
        ...
    def shouldBeRemoved(self) -> bool:
        """
            This method is called after :meth:`~fr.cnes.sirius.patrius.events.EventDetector.eventOccurred` has been triggered. It
            returns true if the current detector should be removed after first event detection. **WARNING:** this method can be
            called only once a event has been triggered. Before, the value is not available.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.shouldBeRemoved` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.shouldBeRemoved` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Returns:
                true if the current detector should be removed after first event detection
        
        
        """
        ...

class NullMassPartDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class NullMassPartDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        This class creates an event detector that detects when the mass of the element becomes null. This detector is
        automatically added (through the continuous thrust) to every propagator and throws a reset_derivatives (because the
        thrust became null) once it detects a null mass and the mass is set to exactly zero. Since the initial mass of the part
        is positive or null, the first time where g = 0 will indicate the first time when the mass becomes null.
    
        Since:
            2.3
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, double2: float, massProvider: fr.cnes.sirius.patrius.propagation.MassProvider, string: str): ...
    @typing.overload
    def __init__(self, massProvider: fr.cnes.sirius.patrius.propagation.MassProvider, string: str): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, massProvider: fr.cnes.sirius.patrius.propagation.MassProvider, string: str): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - mass: :class:`~fr.cnes.sirius.patrius.propagation.MassProvider`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action:
        """
            If the mass of the element becomes negative, a reset_state is performed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.eventOccurred` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.eventOccurred` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): the current state information : date, kinematics, attitude
                increasing (boolean): if true, the value of the switching function increases when times increases around event (note that increase is measured
                    with respect to physical time, not with respect to propagation which may go backward in time)
                forward (boolean): if true, the integration variable (time) increases during integration.
        
            Returns:
                EventDetector.Action.RESET_DERIVATIVES
        
        
        """
        ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getPartName(self) -> str:
        """
            Get the name of the part (attribute).
        
            Returns:
                partName String : name of the part.
        
        
        """
        ...
    def resetState(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> fr.cnes.sirius.patrius.propagation.SpacecraftState: ...
    def shouldBeRemoved(self) -> bool:
        """
            This method is called after :meth:`~fr.cnes.sirius.patrius.events.EventDetector.eventOccurred` has been triggered. It
            returns true if the current detector should be removed after first event detection. **WARNING:** this method can be
            called only once a event has been triggered. Before, the value is not available.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.shouldBeRemoved` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.shouldBeRemoved` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Returns:
                true if the current detector should be removed after first event detection
        
        
        """
        ...

class PlaneCrossingDetector(fr.cnes.sirius.patrius.events.AbstractDetector):
    """
    public class PlaneCrossingDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
    
        Class for plane crossing events detection.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool, double: float, double2: float): ...
    @typing.overload
    def __init__(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, int: int, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, double: float, double2: float): ...
    @typing.overload
    def __init__(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, vector3D2: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool, double: float, double2: float): ...
    @typing.overload
    def __init__(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, vector3D2: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, int: int, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, double: float, double2: float): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            Description copied from interface: :meth:`~fr.cnes.sirius.patrius.events.EventDetector.copy`
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            Returns:
                a copy of the considered PlaneCrossingDetector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getFrame(self) -> fr.cnes.sirius.patrius.frames.Frame:
        """
            Getter for the frame for plane definition.
        
            Returns:
                referenceFrame
        
        
        """
        ...
    def getNormalVector(self) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D:
        """
            Getter for the normal vector to the plane used for plane definition.
        
            Returns:
                normalVector
        
        
        """
        ...
    def getPoint(self) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D:
        """
            Getter for the point belonging to the plane used for plane definition.
        
            Returns:
                point
        
        
        """
        ...

class ThreeBodiesAngleDetector(fr.cnes.sirius.patrius.events.AbstractDetector, fr.cnes.sirius.patrius.events.MultiEventDetector):
    """
    public class ThreeBodiesAngleDetector extends :class:`~fr.cnes.sirius.patrius.events.AbstractDetector` implements :class:`~fr.cnes.sirius.patrius.events.MultiEventDetector`
    
        Detects when the angle between three bodies is equal to a predetermined value.
    
        If body :sub:`1` , body :sub:`2` and body :sub:`3` are the three bodies, the detector computes the angle between the two
        vectors v :sub:`21` (vector from body :sub:`2` to body :sub:`1` ) and v :sub:`23` (vector from body :sub:`2` to body
        :sub:`3` ), and compare it with the threshold angle value.
    
        The default implementation behavior is to :code:`stop` propagation when the angle between the three bodies is reached.
        This can be changed by using provided constructors.
    
        Since:
            1.1
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, bodyOrder: 'ThreeBodiesAngleDetector.BodyOrder', double: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, bodyOrder: 'ThreeBodiesAngleDetector.BodyOrder', double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, bodyOrder: 'ThreeBodiesAngleDetector.BodyOrder', double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, bodyOrder: 'ThreeBodiesAngleDetector.BodyOrder', double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider3: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider3: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, pVCoordinatesProvider3: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - body1: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
              - body2: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
              - body3: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.copy` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    @typing.overload
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    @typing.overload
    def eventOccurred(self, map: typing.Union[java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState], typing.Mapping[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]], boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    @typing.overload
    def filterEvent(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> bool: ...
    @typing.overload
    def filterEvent(self, map: typing.Union[java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState], typing.Mapping[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]], boolean: bool, boolean2: bool) -> bool: ...
    @typing.overload
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    @typing.overload
    def g(self, map: typing.Union[java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState], typing.Mapping[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]]) -> float: ...
    def getAlignmentAngle(self) -> float:
        """
            Get the alignment angle.
        
            Returns:
                the Alignment angle (rad).
        
        
        """
        ...
    def getFirstBody(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
            Get 1st body.
        
            Returns:
                the 1st body
        
        
        """
        ...
    def getInSpacecraftId1(self) -> str:
        """
            Get the first spacecraft id.
        
            Returns:
                the first spacecraft id
        
        
        """
        ...
    def getInSpacecraftId2(self) -> str:
        """
            Get the second spacecraft id.
        
            Returns:
                the second spacecraft id
        
        
        """
        ...
    def getInSpacecraftId3(self) -> str:
        """
            Get the third spacecraft id.
        
            Returns:
                the third spacecraft id
        
        
        """
        ...
    def getSecondBody(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
            Get 2nd body.
        
            Returns:
                the 2nd body
        
        
        """
        ...
    def getThirdBody(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
            Get 3rd body.
        
            Returns:
                the 3rd body
        
        
        """
        ...
    @typing.overload
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        public void init(`Map <http://docs.oracle.com/javase/8/docs/api/java/util/Map.html?is-external=true>`<`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`,:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`> s0, :class:`~fr.cnes.sirius.patrius.time.AbsoluteDate` t)
        
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.MultiEventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.MultiEventDetector`
        
            Parameters:
                s0 (`Map <http://docs.oracle.com/javase/8/docs/api/java/util/Map.html?is-external=true>`<`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`,:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`> s0): map of initial states
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...
    @typing.overload
    def init(self, map: typing.Union[java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState], typing.Mapping[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]], absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None: ...
    def resetStates(self, map: typing.Union[java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState], typing.Mapping[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]]) -> java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]: ...
    class BodyOrder(java.lang.Enum['ThreeBodiesAngleDetector.BodyOrder']):
        FIRST: typing.ClassVar['ThreeBodiesAngleDetector.BodyOrder'] = ...
        SECOND: typing.ClassVar['ThreeBodiesAngleDetector.BodyOrder'] = ...
        THIRD: typing.ClassVar['ThreeBodiesAngleDetector.BodyOrder'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'ThreeBodiesAngleDetector.BodyOrder': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['ThreeBodiesAngleDetector.BodyOrder']: ...

class AbstractEclipseDetector(AbstractSignalPropagationDetector):
    EXIT: typing.ClassVar[int] = ...
    ENTRY: typing.ClassVar[int] = ...
    ENTRY_EXIT: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool, int: int): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double2: float, int: int, double3: float, double4: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double2: float, int: int, double3: float, double4: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def getEmitter(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider: ...
    def getEventDatationType(self) -> AbstractSignalPropagationDetector.EventDatationType: ...
    def getOcculted(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider: ...
    def getOccultedRadius(self) -> float: ...
    def getOcculting(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider: ...
    def getOccultingRadiusProvider(self) -> fr.cnes.sirius.patrius.bodies.ApparentRadiusProvider: ...
    def getReceiver(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider: ...
    def isInEclipse(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> bool: ...
    def isTotalEclipse(self) -> bool: ...
    def setPropagationDelayType(self, propagationDelayType: AbstractSignalPropagationDetector.PropagationDelayType, frame: fr.cnes.sirius.patrius.frames.Frame) -> None: ...

class AbstractStationToSatDetector(AbstractSignalPropagationDetector):
    """
    public abstract class AbstractStationToSatDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
    
    
        Abstract event detector using a station elevation correction.
    
        Since:
            1.2
    
        Also see:
            :meth:`~serialized`
    """
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getAssembly(self) -> fr.cnes.sirius.patrius.assembly.Assembly:
        """
            Get the assembly.
        
            Returns:
                the assembly
        
        
        """
        ...
    def getCorrection(self) -> fr.cnes.sirius.patrius.signalpropagation.AngularCorrection:
        """
            Get the correction.
        
            Returns:
                the correction
        
        
        """
        ...
    def getLinkType(self) -> 'VisibilityFromStationDetector.LinkType':
        """
            Returns the type of link (it can be uplink or downlink).
        
            Returns:
                the type of link (it can be uplink or downlink)
        
        
        """
        ...
    def getSensor(self) -> fr.cnes.sirius.patrius.assembly.models.SensorModel:
        """
            Get the sensor.
        
            Returns:
                the sensor
        
        
        """
        ...
    def getStation(self) -> fr.cnes.sirius.patrius.groundstation.GeometricStationAntenna:
        """
            Get the station.
        
            Returns:
                the station antenna geometric model
        
        
        """
        ...
    def isMaskingCheck(self) -> bool:
        """
            True if masking are taken into account.
        
            Returns:
                true if masking are taken into account, false otherwise
        
        
        """
        ...

class ApparentElevationDetector(AbstractSignalPropagationDetector):
    """
    public class ApparentElevationDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
    
        Finder for satellite apparent elevation events.
    
        This class finds apparent elevation events (i.e. apparent satellite raising and setting from a terrestrial viewpoint).
    
        Apparent elevation is the sum of geometrical elevation and refraction angle, the latter is 0 at zenith, about 1
        arcminute at 45°, and 34 arcminutes at the horizon for optical wavelengths.
    
        This event only makes sense for positive apparent elevation in the Earth environment and it is not suited for near
        zenithal detection, where the simple :class:`~fr.cnes.sirius.patrius.events.detectors.ElevationDetector` fits better.
    
        Refraction angle is computed according to Saemundssen formula quoted by Meeus. For reference, see **Astronomical
        Algorithms** (1998), 2nd ed, (ISBN 0-943396-61-1), chap. 15.
    
        This formula is about 30 arcseconds of accuracy very close to the horizon, as variable atmospheric effects become very
        important.
    
        Local pressure and temperature can be set to correct refraction at the viewpoint.
    
        The default implementation behavior is to :code:`EventDetector.Action#CONTINUE` continue propagation at raising and to
        :code:`EventDetector.Action#STOP` stop propagation at setting. This can be changed by using the constructor
        :meth:`~fr.cnes.sirius.patrius.events.detectors.ApparentElevationDetector.ApparentElevationDetector`.
    
        This detector can takes into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` (default is
        signal being instantaneous).
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.propagation.Propagator.addEventDetector`, :meth:`~serialized`
    """
    DEFAULT_PRESSURE: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_PRESSURE
    
        Default local pressure at viewpoint (Pa).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_TEMPERATURE: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_TEMPERATURE
    
        Default local temperature at viewpoint (K).
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame): ...
    @typing.overload
    def __init__(self, double: float, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, double2: float): ...
    @typing.overload
    def __init__(self, double: float, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, double: float, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - topo: :class:`~fr.cnes.sirius.patrius.frames.TopocentricFrame`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getElevation(self) -> float:
        """
            Get the threshold apparent elevation value.
        
            Returns:
                the threshold apparent elevation value (rad)
        
        
        """
        ...
    def getPressure(self) -> float:
        """
            Get the local pressure at topocentric frame origin.
        
            Returns:
                the pressure
        
        
        """
        ...
    def getTemperature(self) -> float:
        """
            Get the local temperature at topocentric frame origin.
        
            Returns:
                the temperature
        
        
        """
        ...
    def getTopocentricFrame(self) -> fr.cnes.sirius.patrius.frames.TopocentricFrame:
        """
            Get the topocentric frame.
        
            Returns:
                the topocentric frame
        
        
        """
        ...
    def setPressure(self, double: float) -> None:
        """
            Set the local pressure at topocentric frame origin if needed.
        
            Otherwise the default value for the local pressure is set to
            :meth:`~fr.cnes.sirius.patrius.events.detectors.ApparentElevationDetector.DEFAULT_PRESSURE`.
        
            Parameters:
                pressureIn (double): the pressure to set (Pa)
        
        
        """
        ...
    def setPropagationDelayType(self, propagationDelayType: AbstractSignalPropagationDetector.PropagationDelayType, frame: fr.cnes.sirius.patrius.frames.Frame) -> None:
        """
            Description copied from
            class: :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType`
            Setter for the propagation delay computation type. Warning: check Javadoc of detector to see if detector takes into
            account propagation time delay. if not, signals are always considered instantaneous. The provided frame is used to
            compute the signal propagation when delay is taken into account.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` in
                class :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
        
            Parameters:
                propagationDelayType (:class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.PropagationDelayType`): Propagation delay type used in events computation
                frame (:class:`~fr.cnes.sirius.patrius.frames.Frame`): Frame to use for signal propagation with delay (may be null if propagation delay type is considered instantaneous).
                    Warning: the usage of a pseudo inertial frame is tolerated, however it will lead to some inaccuracies due to the
                    non-invariance of the frame with respect to time. For this reason, it is suggested to use the ICRF frame or a frame
                    which is frozen with respect to the ICRF.
        
        
        """
        ...
    def setTemperature(self, double: float) -> None:
        """
            Set the local temperature at topocentric frame origin if needed.
        
            Otherwise the default value for the local temperature is set to
            :meth:`~fr.cnes.sirius.patrius.events.detectors.ApparentElevationDetector.DEFAULT_TEMPERATURE`.
        
            Parameters:
                temperatureIn (double): the temperature to set (K)
        
        
        """
        ...

class BetaAngleDetector(AbstractSignalPropagationDetector):
    """
    public class BetaAngleDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
    
        Detects when the beta angle of the spacecraft reaches a predetermined value.
    
    
        The beta angle is the angle between the orbit plane and the vector from the central body to the sun. The angle is
        positive on the side of the plane containing the spacecraft's momentum vector. The bodies considered are :
    
          - the spacecraft
          - the central body for the spacecraft
          - the Sun
    
    
        The default implementation behaviour is to :code:`EventDetector.Action#STOP` stop propagation when the beta angle is
        reached. This can be changed by using provided constructors.
    
        This detector can takes into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` (default is
        signal being instantaneous).
    
        Since:
            1.1
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - sun: :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getAngle(self) -> float:
        """
            Returns beta angle triggering the event.
        
            Returns:
                the Angle triggering the event.
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...
    def setPropagationDelayType(self, propagationDelayType: AbstractSignalPropagationDetector.PropagationDelayType, frame: fr.cnes.sirius.patrius.frames.Frame) -> None:
        """
            Description copied from
            class: :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType`
            Setter for the propagation delay computation type. Warning: check Javadoc of detector to see if detector takes into
            account propagation time delay. if not, signals are always considered instantaneous. The provided frame is used to
            compute the signal propagation when delay is taken into account.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` in
                class :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
        
            Parameters:
                propagationDelayType (:class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.PropagationDelayType`): Propagation delay type used in events computation
                frame (:class:`~fr.cnes.sirius.patrius.frames.Frame`): Frame to use for signal propagation with delay (may be null if propagation delay type is considered instantaneous).
                    Warning: the usage of a pseudo inertial frame is tolerated, however it will lead to some inaccuracies due to the
                    non-invariance of the frame with respect to time. For this reason, it is suggested to use the ICRF frame or a frame
                    which is frozen with respect to the ICRF.
        
        
        """
        ...

class CentralBodyMaskCircularFOVDetector(AbstractSignalPropagationDetector):
    """
    public class CentralBodyMaskCircularFOVDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
    
        Finder for target entry/exit events with respect to a satellite sensor FOV defined by a vector3D giving the direction in
        satellite frame and taking into account masking from the central body
    
        This class handles fields of view with a circular boundary.
    
        This class handles central body as a :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`.
    
        The default implementation behaviour is to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.STOP` propagation
        when the target is in the field of view outside of eclipse. This can be changed by using one of the provided
        constructors.
    
        This detector can takes into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` (default is
        signal being instantaneous).
    
        Since:
            1.3
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.propagation.Propagator.addEventDetector`,
            :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`,
            :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid`,
            :class:`~fr.cnes.sirius.patrius.events.detectors.EclipseDetector`,
            :class:`~fr.cnes.sirius.patrius.events.detectors.CircularFieldOfViewDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, eclipseDetector: 'EclipseDetector', circularFieldOfViewDetector: 'CircularFieldOfViewDetector', double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, boolean: bool, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double2: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, boolean: bool, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, boolean: bool, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double2: float, double3: float, double4: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, boolean: bool, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double2: float, double3: float, double4: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean2: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - circularFOVDetector: :class:`~fr.cnes.sirius.patrius.events.detectors.CircularFieldOfViewDetector`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getCircularFOVDetector(self) -> 'CircularFieldOfViewDetector':
        """
            Get the circular FOV detector.
        
            Returns:
                The circular field of view detector
        
        
        """
        ...
    def getEclipseDetector(self) -> 'EclipseDetector':
        """
            Get the eclipse detector.
        
            Returns:
                the eclipse detector taking into account ellipsoid body shape
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class CircularFieldOfViewDetector(AbstractSignalPropagationDetector):
    """
    public class CircularFieldOfViewDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
    
        Finder for target entry/exit events with respect to a satellite sensor field of view.
    
        This class handle fields of view with a circular boundary.
    
        The default implementation behavior is to :code:`EventDetector.Action#CONTINUE` continue propagation at fov entry and to
        :code:`EventDetector.Action#STOP` stop propagation at fov exit. This can be changed by using the constructor
        :code:`#CircularFieldOfViewDetector(PVCoordinatesProvider, Vector3D, double, double, double,
        fr.cnes.sirius.patrius.events.EventDetector.Action, fr.cnes.sirius.patrius.events.EventDetector.Action))
        CircularFieldOfViewDetector`.
    
        This detector can takes into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` (default is
        signal being instantaneous).
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.propagation.Propagator.addEventDetector`,
            :class:`~fr.cnes.sirius.patrius.events.detectors.DihedralFieldOfViewDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double: float, double2: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - targetPVProvider: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getCenter(self) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D:
        """
            Get the direction of fov center.
        
            Returns:
                the direction of fov center
        
        
        """
        ...
    def getHalfAperture(self) -> float:
        """
            Get fov half aperture angle.
        
            Returns:
                the fov half aperture angle
        
        
        """
        ...
    def getPVTarget(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
            Get the position/velocity provider of the target .
        
            Returns:
                the position/velocity provider of the target
        
        
        """
        ...

class DihedralFieldOfViewDetector(AbstractSignalPropagationDetector):
    """
    public class DihedralFieldOfViewDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
    
        Finder for body entering/exiting dihedral fov events.
    
        This class finds dihedral field of view events (i.e. body entry and exit in fov).
    
        The default implementation behavior is to :code:`EventDetector.Action#CONTINUE` continue propagation at entry and to
        :code:`EventDetector.Action#STOP` stop propagation at exit. This can be changed by using provided constructors.
    
        This detector can takes into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` (default is
        signal being instantaneous).
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.propagation.Propagator.addEventDetector`,
            :class:`~fr.cnes.sirius.patrius.events.detectors.CircularFieldOfViewDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, vector3D2: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double: float, vector3D3: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, vector3D2: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double: float, vector3D3: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, vector3D2: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double: float, vector3D3: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, vector3D2: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double: float, vector3D3: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, vector3D2: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double: float, vector3D3: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool, double4: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, vector3D2: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double: float, vector3D3: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, double4: float): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - targetPVProvider: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getAxis1(self) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D:
        """
            Get the direction of fov 1st dihedral axis.
        
            Returns:
                the direction of fov 1st dihedral axis
        
        
        """
        ...
    def getAxis2(self) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D:
        """
            Get the direction of fov 2nd dihedral axis.
        
            Returns:
                the direction of fov 2nd dihedral axis
        
        
        """
        ...
    def getCenter(self) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D:
        """
            Get the direction of fov center.
        
            Returns:
                the direction of fov center
        
        
        """
        ...
    def getHalfAperture1(self) -> float:
        """
            Get the half aperture angle of fov 1st dihedra.
        
            Returns:
                the half aperture angle of fov 1st dihedras
        
        
        """
        ...
    def getHalfAperture2(self) -> float:
        """
            Get the half aperture angle of fov 2nd dihedra.
        
            Returns:
                the half aperture angle of fov 2nd dihedras
        
        
        """
        ...
    def getPVTarget(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
            Get the position/velocity provider of the target .
        
            Returns:
                the position/velocity provider of the target
        
        
        """
        ...

class ExtremaElevationDetector(AbstractSignalPropagationDetector):
    MIN: typing.ClassVar[int] = ...
    MAX: typing.ClassVar[int] = ...
    MIN_MAX: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, int: int, double: float): ...
    @typing.overload
    def __init__(self, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, int: int, double: float, double2: float): ...
    @typing.overload
    def __init__(self, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, linkType: 'VisibilityFromStationDetector.LinkType'): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector: ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getLinkType(self) -> 'VisibilityFromStationDetector.LinkType': ...
    def getTopocentricFrame(self) -> fr.cnes.sirius.patrius.frames.TopocentricFrame: ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None: ...

class ExtremaSightAxisDetector(AbstractSignalPropagationDetector):
    """
    public class ExtremaSightAxisDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
    
        Detects the minimum angle between a sight view line and a PVCoordinateProvider target view from a Frame which origin is
        on the line.
    
        The detector is similar to the extrema three body angle detector : body one is the target point, body two is the frame
        origin on the line, and body three is the direction vector of the line. Each one are expressed in the frame with origin
        on the line.
    
        The detector doesn't take into account potential masking.
    
        The default implementation behavior is to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.STOP` propagation
        when the minimum angle is detected.
    
        This detector can takes into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.getPropagationDelayType` (default is
        signal being instantaneous).
    
        Since:
            1.3
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`,
            :class:`~fr.cnes.sirius.patrius.events.detectors.ExtremaThreeBodiesAngleDetector`, :meth:`~serialized`
    """
    MIN: typing.ClassVar[int] = ...
    """
    public static final int MIN
    
        Flag for local minimum angle detection (g increasing).
    
        Also see:
            :meth:`~constant`
    
    
    """
    MAX: typing.ClassVar[int] = ...
    """
    public static final int MAX
    
        Flag for local maximum angle detection (g decreasing).
    
        Also see:
            :meth:`~constant`
    
    
    """
    MIN_MAX: typing.ClassVar[int] = ...
    """
    public static final int MIN_MAX
    
        Flag for both local minimum and maximum angle detection.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, assembly: fr.cnes.sirius.patrius.assembly.Assembly, string: str, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, assembly: fr.cnes.sirius.patrius.assembly.Assembly, string: str, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, int: int, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, assembly: fr.cnes.sirius.patrius.assembly.Assembly, string: str): ...
    @typing.overload
    def __init__(self, int: int, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, assembly: fr.cnes.sirius.patrius.assembly.Assembly, string: str, double: float, double2: float): ...
    @typing.overload
    def __init__(self, int: int, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, assembly: fr.cnes.sirius.patrius.assembly.Assembly, string: str, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, int: int, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, assembly: fr.cnes.sirius.patrius.assembly.Assembly, string: str, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, int: int, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, assembly: fr.cnes.sirius.patrius.assembly.Assembly, string: str, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, int: int, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, int: int, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double: float, double2: float): ...
    @typing.overload
    def __init__(self, int: int, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, int: int, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, int: int, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - targetPoint: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
              - vehicle (if defined): :class:`~fr.cnes.sirius.patrius.assembly.Assembly`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getSensorName(self) -> str:
        """
            Get the sensor name.
        
            Returns:
                the sensor name
        
        
        """
        ...
    def getSightAxis(self) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D:
        """
            Get the sight axis
        
            Returns:
                the sight axis
        
        
        """
        ...
    def getTargetPoint(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
            Get the target point.
        
            Returns:
                the target point
        
        
        """
        ...
    def getVehicle(self) -> fr.cnes.sirius.patrius.assembly.Assembly:
        """
            Get the vehicle.
        
            Returns:
                the vehicle
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class GroundMaskElevationDetector(AbstractSignalPropagationDetector):
    """
    public class GroundMaskElevationDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
    
        Finder for satellite azimuth-elevation events with respect to a mask.
    
        This class finds elevation events (i.e. satellite raising and setting) with respect to an azimuth-elevation mask.
    
        An azimuth-elevation mask defines the physical horizon for a local point, origin of some topocentric frame.
    
        Azimuth is defined according to :meth:`~fr.cnes.sirius.patrius.frames.TopocentricFrame.getAzimuth`.
    
    
        Elevation is defined according to :meth:`~fr.cnes.sirius.patrius.frames.TopocentricFrame.getElevation`.
    
        The azimuth elevation mask must be supplied as a twodimensional array with multiples lines of pairs of azimuth-elevation
        angles. First row will be filled with azimuth values, second row with elevation values, as in the following snippet:
    
        .. code-block: java
        
        
         double[][] mask = { { FastMath.toRadians(0), FastMath.toRadians(10) },
             { FastMath.toRadians(45), FastMath.toRadians(8) },
             { FastMath.toRadians(90), FastMath.toRadians(6) },
             { FastMath.toRadians(135), FastMath.toRadians(4) },
             { FastMath.toRadians(180), FastMath.toRadians(5) },
             { FastMath.toRadians(225), FastMath.toRadians(6) },
             { FastMath.toRadians(270), FastMath.toRadians(8) },
             { FastMath.toRadians(315), FastMath.toRadians(9) } };
         
    
        No assumption is made on azimuth values and ordering. The only restraint is that only one elevation value can be
        associated to identical azimuths modulo 2PI.
    
        The default implementation behavior is to :code:`EventDetector.Action#CONTINUE` continue propagation at raising and to
        :code:`EventDetector.Action#STOP` stop propagation at setting. This can be changed by using provided constructors.
    
        This detector can takes into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` (default is
        signal being instantaneous).
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.propagation.Propagator.addEventDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, double2: float): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - topo: :class:`~fr.cnes.sirius.patrius.frames.TopocentricFrame`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getElevation(self, double: float) -> float:
        """
            Get the interpolated elevation for a given azimuth according to the mask.
        
            Parameters:
                azimuth (double): azimuth (rad)
        
            Returns:
                elevation angle (rad)
        
        
        """
        ...
    def getTopocentricFrame(self) -> fr.cnes.sirius.patrius.frames.TopocentricFrame:
        """
            Get the topocentric frame.
        
            Returns:
                the topocentric frame
        
        
        """
        ...

class LineMaskingDetector(AbstractSignalPropagationDetector):
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, signalPropagationRole: LinkTypeHandler.SignalPropagationRole, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, list: java.util.List[fr.cnes.sirius.patrius.bodies.BodyShape]): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, signalPropagationRole: LinkTypeHandler.SignalPropagationRole, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, list: java.util.List[fr.cnes.sirius.patrius.bodies.BodyShape], double: float, double2: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, signalPropagationRole: LinkTypeHandler.SignalPropagationRole, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, list: java.util.List[fr.cnes.sirius.patrius.bodies.BodyShape], double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, signalPropagationRole: LinkTypeHandler.SignalPropagationRole, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, list: java.util.List[fr.cnes.sirius.patrius.bodies.BodyShape], int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    def copy(self) -> 'LineMaskingDetector': ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getMainElement(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider: ...
    def getMaskingBodies(self) -> java.util.List[fr.cnes.sirius.patrius.bodies.BodyShape]: ...
    def isDirectionOcculted(self, propagator: fr.cnes.sirius.patrius.propagation.Propagator, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> bool: ...

class LocalTimeAngleDetector(AbstractSignalPropagationDetector):
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, int: int): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector: ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def filterEvent(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> bool: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getAction(self) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def getFrame(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    def getSun(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider: ...
    def getTime(self) -> float: ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None: ...

class MaskingDetector(AbstractSignalPropagationDetector):
    """
    public class MaskingDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
    
    
        Sensor masking detector.
    
        The default implementation behaviour is to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.CONTINUE`
        propagation at raising and to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.STOP` propagation at setting.
        This can be changed by using provided constructors.
    
        Since:
            1.2
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.assembly.models.SensorModel`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, assembly: fr.cnes.sirius.patrius.assembly.Assembly, string: str, double: float, double2: float): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, double: float, double2: float): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - sensor: :class:`~fr.cnes.sirius.patrius.assembly.models.SensorModel`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getAssembly(self) -> fr.cnes.sirius.patrius.assembly.Assembly:
        """
            Get the assembly.
        
            Returns:
                the assembly
        
        
        """
        ...
    def getMaskingObjectName(self) -> str:
        """
            Get the masking object.
        
            Returns:
                the first masking object name (to be used in the user eventOccured method)
        
        
        """
        ...
    def getMaskingPartName(self) -> str:
        """
            Get the masking part.
        
            Returns:
                first masking spacecraft's part name if the first masking part is a spacecraft, "none" otherwise (to be used in the user
                eventOccured method)
        
        
        """
        ...
    def getSensor(self) -> fr.cnes.sirius.patrius.assembly.models.SensorModel:
        """
            Get the sensor.
        
            Returns:
                the sensor
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class NadirSolarIncidenceDetector(AbstractSignalPropagationDetector):
    """
    public class NadirSolarIncidenceDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
    
        Spacecraft's nadir point solar incidence detector.
    
        The solar incidence is the angle between the nadir-satellite vector and the nadir-sun vector.
    
    
        This detector discriminates among increasing g events and decreasing g events.
    
    
        The default implementation is to :code:`stop` propagation when the reference solar incidence is reached. This can be
        changed by using provided constructors.
    
        This detector can take into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` (default is
        signal being instantaneous).
    
        Since:
            1.1
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, double: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, double: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider): ...
    @typing.overload
    def __init__(self, int: int, double: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - inbodyShape: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getBodyShape(self) -> fr.cnes.sirius.patrius.bodies.BodyShape:
        """
            Getter for the body shape.
        
            Returns:
                the body shape
        
        
        """
        ...
    def getIncidence(self) -> float:
        """
            Getter for the incidence.
        
            Returns:
                incidence to detect
        
        
        """
        ...
    def getSun(self) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
            Getter for the Sun.
        
            Returns:
                the Sun
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...
    def setSun(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider) -> None:
        """
            Setter for the sun :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
        
            Parameters:
                sun (:class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`): the sun
        
        
        """
        ...

class NodeDetector(PlaneCrossingDetector):
    """
    public class NodeDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.PlaneCrossingDetector`
    
        Finder for node crossing events.
    
        This class finds equator crossing events (i.e. ascending and/or descending node crossing).
    
        The default implementation behavior is to :code:`stop` propagation at node crossing. This can be changed by overriding
        one of the following constructors :
    
          - :meth:`~fr.cnes.sirius.patrius.events.detectors.NodeDetector.NodeDetector` : the defined action is performed at
            ascending OR/AND descending node depending on slope selection defined.
          - :meth:`~fr.cnes.sirius.patrius.events.detectors.NodeDetector.NodeDetector` : the defined actions are performed at
            ascending AND descending node.
    
    
        Beware that node detection will fail for almost equatorial orbits.
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.propagation.Propagator.addEventDetector`, :meth:`~serialized`
    """
    ASCENDING: typing.ClassVar[int] = ...
    """
    public static final int ASCENDING
    
        Flag for ascending node crossing (slopeSelection = 0).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DESCENDING: typing.ClassVar[int] = ...
    """
    public static final int DESCENDING
    
        Flag for descending node crossing (slopeSelection = 1).
    
        Also see:
            :meth:`~constant`
    
    
    """
    ASCENDING_DESCENDING: typing.ClassVar[int] = ...
    """
    public static final int ASCENDING_DESCENDING
    
        Flag for both ascending and descending node detection (slopeSelection = 2).
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, frame: fr.cnes.sirius.patrius.frames.Frame, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, frame: fr.cnes.sirius.patrius.frames.Frame, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, frame: fr.cnes.sirius.patrius.frames.Frame, int: int, double: float, double2: float): ...
    @typing.overload
    def __init__(self, frame: fr.cnes.sirius.patrius.frames.Frame, int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, frame: fr.cnes.sirius.patrius.frames.Frame, int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, orbit: fr.cnes.sirius.patrius.orbits.Orbit, frame: fr.cnes.sirius.patrius.frames.Frame, int: int): ...
    @typing.overload
    def __init__(self, orbit: fr.cnes.sirius.patrius.orbits.Orbit, frame: fr.cnes.sirius.patrius.frames.Frame, int: int, double: float): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - frame: :class:`~fr.cnes.sirius.patrius.frames.Frame`
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.copy` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.detectors.PlaneCrossingDetector.copy` in
                class :class:`~fr.cnes.sirius.patrius.events.detectors.PlaneCrossingDetector`
        
            Returns:
                a copy of the considered PlaneCrossingDetector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...

class NthOccurrenceDetector(IntervalOccurrenceDetector):
    """
    public class NthOccurrenceDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.IntervalOccurrenceDetector`
    
        This event detector detects the nth occurrence of an underlying event detector.
    
        However the :meth:`~fr.cnes.sirius.patrius.events.detectors.IntervalOccurrenceDetector.eventOccurred` method is
        triggered at every event of the underlying detector. As a result, the behaviour of this detector is the following:
    
          - Before and after the nth occurrence, the
            :meth:`~fr.cnes.sirius.patrius.events.detectors.IntervalOccurrenceDetector.eventOccurred` returns Action.CONTINUE.
          - At the nth occurrence, the :meth:`~fr.cnes.sirius.patrius.events.detectors.IntervalOccurrenceDetector.eventOccurred`
            returns the user-provided action.
    
    
        **Warning:** the :meth:`~fr.cnes.sirius.patrius.events.detectors.IntervalOccurrenceDetector.eventOccurred` method is
        triggered at every occurrence of the underlying detector, not only at nth occurrence. Hence, overloading this detector
        should be performed carefully: in the overloaded eventOccurred() method, the check
        :meth:`~fr.cnes.sirius.patrius.events.detectors.IntervalOccurrenceDetector.getCurrentOccurrence` ==
        :meth:`~fr.cnes.sirius.patrius.events.detectors.NthOccurrenceDetector.getOccurence` should be performed first to ensure
        we are at nth occurrence before calling super.eventOccurred().
    
        Since:
            1.3
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, eventDetector: fr.cnes.sirius.patrius.events.EventDetector, int: int, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, eventDetector: fr.cnes.sirius.patrius.events.EventDetector, int: int, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    def getOccurence(self) -> int:
        """
            Get the occurrence to detect.
        
            Returns:
                occurrence to detect
        
        
        """
        ...

class RFVisibilityDetector(AbstractSignalPropagationDetector):
    """
    public class RFVisibilityDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
    
        Finder for ground station / satellite RF visibility events.
    
        The default implementation behavior is to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.CONTINUE`
        propagation at raising and to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.STOP` propagation at setting.
        This can be changed by This can be changed by using provided constructors.
    
        This detector can takes into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.getPropagationDelayType` (default is
        signal being instantaneous).
    
        Since:
            1.2
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, rFLinkBudgetModel: fr.cnes.sirius.patrius.assembly.models.RFLinkBudgetModel, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, rFLinkBudgetModel: fr.cnes.sirius.patrius.assembly.models.RFLinkBudgetModel, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, rFLinkBudgetModel: fr.cnes.sirius.patrius.assembly.models.RFLinkBudgetModel, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - lbModel: :class:`~fr.cnes.sirius.patrius.assembly.models.RFLinkBudgetModel`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getLbModel(self) -> fr.cnes.sirius.patrius.assembly.models.RFLinkBudgetModel:
        """
            Get the RF link budget model.
        
            Returns:
                the RF link budget model
        
        
        """
        ...
    def getLbThreshold(self) -> float:
        """
            Get the RF link budget threshold.
        
            Returns:
                the RF link budget threshold
        
        
        """
        ...

class RelativeDateDetector(DateDetector):
    """
    public class RelativeDateDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.DateDetector`
    
        Date detector defined by relative date.
    
        Since:
            4.1
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, timeScale: fr.cnes.sirius.patrius.time.TimeScale): ...
    @typing.overload
    def __init__(self, double: float, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, timeScale: fr.cnes.sirius.patrius.time.TimeScale, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.copy` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.detectors.DateDetector.copy` in
                class :class:`~fr.cnes.sirius.patrius.events.detectors.DateDetector`
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def getReferenceDate(self) -> fr.cnes.sirius.patrius.time.AbsoluteDate:
        """
            Getter for the reference date of the event.
        
            Returns:
                the reference date of the event.
        
        
        """
        ...
    def getRelativeDate(self) -> float:
        """
            Getter for the target relative date in seconds.
        
            Returns:
                the target relative date in seconds.
        
        
        """
        ...
    def getTimeScale(self) -> fr.cnes.sirius.patrius.time.TimeScale:
        """
            Getter for the time scale of the event.
        
            Returns:
                the time scale of the event.
        
        
        """
        ...

class SatToSatMutualVisibilityDetector(AbstractSignalPropagationDetector, fr.cnes.sirius.patrius.events.MultiEventDetector):
    """
    public class SatToSatMutualVisibilityDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector` implements :class:`~fr.cnes.sirius.patrius.events.MultiEventDetector`
    
    
        Mutual spacecraft visibility detector : the g function is positive only if each spacecraft is in the main field of view
        of the other one's sensor. In a single spacecraft propagation mode (
        :class:`~fr.cnes.sirius.patrius.propagation.Propagator`), this event detector shall be used in the propagation of a main
        spacecraft, and will use internally a given propagator to get the position of the secondary spacecraft.
    
        The default implementation behavior is to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.CONTINUE`
        propagation when entering the visibility zone and to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.STOP`
        propagation when exiting the visibility zone.
    
        This detector can takes into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` (default is
        signal being instantaneous).
    
        Detection is between two spacecrafts in a symmetrical way (no station), therefore
        :class:`~fr.cnes.sirius.patrius.events.detectors.SatToSatMutualVisibilityDetector.SatToSatLinkType` needs to be
        clarified. What is called :code:`Downlink` is signal propagation from each spacecraft to the target one with signal
        emission at the date defined by the spacecraft state of the g function. Visibilities are therefore checked at the date
        state.getDate()+propagation_time: this date is called reception date. :code:`Uplink` corresponds to the opposite: the
        date of the spacecraft state is a reception date by each satellite, meaning signal emission happended before this date.
        Default linktype is :code:`Downlink` .
    
        Since:
            1.2
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, sensorModel2: fr.cnes.sirius.patrius.assembly.models.SensorModel, propagator: fr.cnes.sirius.patrius.propagation.Propagator, boolean: bool, double: float, double2: float): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, sensorModel2: fr.cnes.sirius.patrius.assembly.models.SensorModel, propagator: fr.cnes.sirius.patrius.propagation.Propagator, boolean: bool, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, sensorModel2: fr.cnes.sirius.patrius.assembly.models.SensorModel, propagator: fr.cnes.sirius.patrius.propagation.Propagator, boolean: bool, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean2: bool, boolean3: bool): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, sensorModel2: fr.cnes.sirius.patrius.assembly.models.SensorModel, propagator: fr.cnes.sirius.patrius.propagation.Propagator, boolean: bool, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean2: bool, boolean3: bool, satToSatLinkType: 'SatToSatMutualVisibilityDetector.SatToSatLinkType'): ...
    @typing.overload
    def __init__(self, string: str, string2: str, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, sensorModel2: fr.cnes.sirius.patrius.assembly.models.SensorModel, boolean: bool, double: float, double2: float): ...
    @typing.overload
    def __init__(self, string: str, string2: str, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, sensorModel2: fr.cnes.sirius.patrius.assembly.models.SensorModel, boolean: bool, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, string: str, string2: str, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, sensorModel2: fr.cnes.sirius.patrius.assembly.models.SensorModel, boolean: bool, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean2: bool, boolean3: bool): ...
    @typing.overload
    def __init__(self, string: str, string2: str, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, sensorModel2: fr.cnes.sirius.patrius.assembly.models.SensorModel, boolean: bool, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean2: bool, boolean3: bool, satToSatLinkType: 'SatToSatMutualVisibilityDetector.SatToSatLinkType'): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - inSensorMainSpacecraft: :class:`~fr.cnes.sirius.patrius.assembly.models.SensorModel`
              - inSensorSecondarySpacecraft: :class:`~fr.cnes.sirius.patrius.assembly.models.SensorModel`
              - secondPropagator: :class:`~fr.cnes.sirius.patrius.propagation.Propagator`
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.copy` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    @typing.overload
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    @typing.overload
    def eventOccurred(self, map: typing.Union[java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState], typing.Mapping[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]], boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    @typing.overload
    def filterEvent(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> bool: ...
    @typing.overload
    def filterEvent(self, map: typing.Union[java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState], typing.Mapping[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]], boolean: bool, boolean2: bool) -> bool: ...
    @typing.overload
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    @typing.overload
    def g(self, map: typing.Union[java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState], typing.Mapping[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]]) -> float: ...
    def getInMainSpacecraftId(self) -> str:
        """
            Get the main spacecraft id.
        
            Returns:
                the main spacecraft id
        
        
        """
        ...
    def getInSecondarySpacecraftId(self) -> str:
        """
            Get the secondary spacecraft id.
        
            Returns:
                the secondary spacecraft id
        
        
        """
        ...
    def getLinkType(self) -> 'SatToSatMutualVisibilityDetector.SatToSatLinkType':
        """
            Returns the type of link (it can be uplink or downlink).
        
            Returns:
                the type of link (it can be uplink or downlink)
        
        
        """
        ...
    def getMainSpacecraft(self) -> fr.cnes.sirius.patrius.assembly.Assembly:
        """
            Get the main assembly to consider.
        
            Returns:
                the main assembly to consider.
        
        
        """
        ...
    def getSecondarySpacecraft(self) -> fr.cnes.sirius.patrius.assembly.Assembly:
        """
            Get the secondary assembly to consider.
        
            Returns:
                the secondary assembly to consider
        
        
        """
        ...
    def getSensorMainSpacecraft(self) -> fr.cnes.sirius.patrius.assembly.models.SensorModel:
        """
            Get the main spacecraft sensor.
        
            Returns:
                the main spacecraft sensor.
        
        
        """
        ...
    def getSensorSecondarySpacecraft(self) -> fr.cnes.sirius.patrius.assembly.models.SensorModel:
        """
            Get the secondary spacecraft sensor.
        
            Returns:
                the secondary spacecraft sensor.
        
        
        """
        ...
    @typing.overload
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        public void init(`Map <http://docs.oracle.com/javase/8/docs/api/java/util/Map.html?is-external=true>`<`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`,:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`> s0, :class:`~fr.cnes.sirius.patrius.time.AbsoluteDate` t)
        
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.MultiEventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.MultiEventDetector`
        
            Parameters:
                s0 (`Map <http://docs.oracle.com/javase/8/docs/api/java/util/Map.html?is-external=true>`<`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`,:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`> s0): map of initial states
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...
    @typing.overload
    def init(self, map: typing.Union[java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState], typing.Mapping[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]], absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None: ...
    def isMaskingCheck(self) -> bool:
        """
            Check maskings.
        
            Returns:
                true if maskings must be computed
        
        
        """
        ...
    def resetStates(self, map: typing.Union[java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState], typing.Mapping[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]]) -> java.util.Map[str, fr.cnes.sirius.patrius.propagation.SpacecraftState]: ...
    class SatToSatLinkType(java.lang.Enum['SatToSatMutualVisibilityDetector.SatToSatLinkType']):
        SECONDARY_TO_MAIN: typing.ClassVar['SatToSatMutualVisibilityDetector.SatToSatLinkType'] = ...
        MAIN_TO_SECONDARY: typing.ClassVar['SatToSatMutualVisibilityDetector.SatToSatLinkType'] = ...
        def getLinkType(self) -> 'VisibilityFromStationDetector.LinkType': ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'SatToSatMutualVisibilityDetector.SatToSatLinkType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['SatToSatMutualVisibilityDetector.SatToSatLinkType']: ...

class SensorInhibitionDetector(AbstractSignalPropagationDetector):
    """
    public class SensorInhibitionDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
    
    
        Event detector for the inhibition of a sensor. The g function is positive if one of the inhibition target is in its
        inhibition field.
    
        The default implementation behaviour is to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.CONTINUE`
        propagation when entering the zone and to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.STOP` when exiting
        the zone. This can be changed by using provided constructors.
    
        This detector can takes into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` (default is
        signal being instantaneous).
    
        Since:
            1.2
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.assembly.models.SensorModel`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, assembly: fr.cnes.sirius.patrius.assembly.Assembly, string: str, double: float, double2: float): ...
    @typing.overload
    def __init__(self, assembly: fr.cnes.sirius.patrius.assembly.Assembly, string: str, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, double: float, double2: float): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - sensor: :class:`~fr.cnes.sirius.patrius.assembly.models.SensorModel`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getAssembly(self) -> fr.cnes.sirius.patrius.assembly.Assembly:
        """
            Get the assembly.
        
            Returns:
                the assembly
        
        
        """
        ...
    def getEmitter(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider:
        """
            Getter for the signal emitter.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.getEmitter` in
                class :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
        
            Parameters:
                s (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): the spacecraft state used by the detector
        
            Returns:
                the signal emitter
        
            Raises:
                : As the emitter is not obviously the sensor main target
        
        
        """
        ...
    def getInhibitionNumber(self) -> int:
        """
            Get the inhibition number.
        
            Returns:
                the first inhibition target to enter the field (to be used in the user eventOccured method) The first inhibition target
                is the number 1.
        
        
        """
        ...
    def getSensor(self) -> fr.cnes.sirius.patrius.assembly.models.SensorModel:
        """
            Get the sensor.
        
            Returns:
                the sensor
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class SensorVisibilityDetector(AbstractSignalPropagationDetector):
    """
    public class SensorVisibilityDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
    
    
        Event detector for the visibility of a sensor. The g function is positive if none of the inhibition target is in its
        inhibition field, no masking object cuts the line segment between the sensor and the target and if the main target is in
        the field of view.
    
        The default implementation behaviour is to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.CONTINUE`
        propagation when entering the zone and to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.STOP` when exiting
        the zone. This can be changed by using provided constructors.
    
        This detector can takes into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` (default is
        signal being instantaneous).
    
        Since:
            1.2
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.assembly.models.SensorModel`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, assembly: fr.cnes.sirius.patrius.assembly.Assembly, string: str, double: float, double2: float): ...
    @typing.overload
    def __init__(self, assembly: fr.cnes.sirius.patrius.assembly.Assembly, string: str, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, double: float, double2: float): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - sensor: :class:`~fr.cnes.sirius.patrius.assembly.models.SensorModel`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getAssembly(self) -> fr.cnes.sirius.patrius.assembly.Assembly:
        """
            Getter for the assembly.
        
            Returns:
                the assembly
        
        
        """
        ...
    def getInhibitionNumber(self) -> int:
        """
            Getter for the inhibition number.
        
            Returns:
                the first inhibition target to enter the field (to be used in the user eventOccured method)
        
        
        """
        ...
    def getMaskingObjectName(self) -> str:
        """
            Getter for the masking object.
        
            Returns:
                the first masking object name (to be used in the user eventOccured method)
        
        
        """
        ...
    def getMaskingPartName(self) -> str:
        """
            Getter for the masking part.
        
            Returns:
                first masking spacecraft's part name if the first masking part is a spacecraft, "none" otherwise (to be used in the user
                eventOccured method)
        
        
        """
        ...
    def getSensor(self) -> fr.cnes.sirius.patrius.assembly.models.SensorModel:
        """
            Getter for the sensor.
        
            Returns:
                the sensor
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...
    def setPropagationDelayType(self, propagationDelayType: AbstractSignalPropagationDetector.PropagationDelayType, frame: fr.cnes.sirius.patrius.frames.Frame) -> None:
        """
            Setter for the propagation delay computation type. Warning: check Javadoc of detector to see if detector takes into
            account propagation time delay. if not, signals are always considered instantaneous. The provided frame is used to
            compute the signal propagation when delay is taken into account.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` in
                class :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
        
            Parameters:
                propagationDelayType (:class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.PropagationDelayType`): Propagation delay type used in events computation
                frame (:class:`~fr.cnes.sirius.patrius.frames.Frame`): Frame to use for signal propagation with delay (may be null if propagation delay type is considered instantaneous).
                    Warning: the usage of a pseudo inertial frame is tolerated, however it will lead to some inaccuracies due to the
                    non-invariance of the frame with respect to time. For this reason, it is suggested to use the ICRF frame or a frame
                    which is frozen with respect to the ICRF.
        
        
        """
        ...

class SolarTimeAngleDetector(AbstractSignalPropagationDetector):
    """
    public class SolarTimeAngleDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
    
        Detects when the solar time angle of a spacecraft is equal to a predetermined value.
    
    
        The solar time is represented by the angle between the projections of the Sun in the osculator orbital plane and the
        satellite position; therefore this angle is equal to zero when the solar time is 12.00h and Π when the solar time is
        0.00h (Solar Time In Hours = 12.00h + solar time angle * 12 / Π).
    
        The default implementation is to :code:`stop` propagation when the solar time is reached. This can be changed by using
        provided constructors.
    
        This detector can takes into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` (default is
        signal being instantaneous).
    
        Since:
            1.2
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame, action: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, double: float, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    @typing.overload
    def __init__(self, double: float, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double2: float, double3: float, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getFrame(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame:
        """
            Returns the frame used for solar time computation.
        
            Returns:
                the frame used for solar time computation
        
        
        """
        ...
    def getTime(self) -> float:
        """
            Get solar time angle to detect.
        
            Returns:
                the solar time angle triggering the event.
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...
    def setPropagationDelayType(self, propagationDelayType: AbstractSignalPropagationDetector.PropagationDelayType, frame: fr.cnes.sirius.patrius.frames.Frame) -> None:
        """
            Description copied from
            class: :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType`
            Setter for the propagation delay computation type. Warning: check Javadoc of detector to see if detector takes into
            account propagation time delay. if not, signals are always considered instantaneous. The provided frame is used to
            compute the signal propagation when delay is taken into account.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` in
                class :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
        
            Parameters:
                propagationDelayType (:class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.PropagationDelayType`): Propagation delay type used in events computation
                frameIn (:class:`~fr.cnes.sirius.patrius.frames.Frame`): Frame to use for signal propagation with delay (may be null if propagation delay type is considered instantaneous).
                    Warning: the usage of a pseudo inertial frame is tolerated, however it will lead to some inaccuracies due to the
                    non-invariance of the frame with respect to time. For this reason, it is suggested to use the ICRF frame or a frame
                    which is frozen with respect to the ICRF.
        
        
        """
        ...

class SurfaceDistanceDetector(DistanceDetector):
    """
    public class SurfaceDistanceDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.DistanceDetector`
    
        Detects when the distance from the spacecraft to the surface of a given body reaches a predetermined value.
    
        The default implementation behaviour is to :code:`stop` propagation when the distance is reached. This can be changed by
        using provided constructors.
    
        Since:
            4.11
    
        Also see:
            :code:`DistanceDetector}`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, celestialBody: fr.cnes.sirius.patrius.bodies.CelestialBody, double: float, bodyDistanceType: 'SurfaceDistanceDetector.BodyDistanceType'): ...
    @typing.overload
    def __init__(self, celestialBody: fr.cnes.sirius.patrius.bodies.CelestialBody, double: float, bodyDistanceType: 'SurfaceDistanceDetector.BodyDistanceType', double2: float, double3: float): ...
    @typing.overload
    def __init__(self, celestialBody: fr.cnes.sirius.patrius.bodies.CelestialBody, double: float, bodyDistanceType: 'SurfaceDistanceDetector.BodyDistanceType', double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, celestialBody: fr.cnes.sirius.patrius.bodies.CelestialBody, double: float, bodyDistanceType: 'SurfaceDistanceDetector.BodyDistanceType', double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, celestialBody: fr.cnes.sirius.patrius.bodies.CelestialBody, double: float, bodyDistanceType: 'SurfaceDistanceDetector.BodyDistanceType', int: int, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - body: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
        
        
            The following attributes are not deeply copied:
        
              - body: :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.copy` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.detectors.DistanceDetector.copy` in
                class :class:`~fr.cnes.sirius.patrius.events.detectors.DistanceDetector`
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getBody(self) -> fr.cnes.sirius.patrius.bodies.CelestialBody:
        """
            Getter for the body.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.detectors.DistanceDetector.getBody` in
                class :class:`~fr.cnes.sirius.patrius.events.detectors.DistanceDetector`
        
            Returns:
                the body
        
        
        """
        ...
    def getBodyDistanceType(self) -> 'SurfaceDistanceDetector.BodyDistanceType':
        """
            Getter for the chosen body distance type for the detector.
        
            Returns:
                the chosen body distance type for the detector
        
        
        """
        ...
    def getBodyFixedFrame(self) -> fr.cnes.sirius.patrius.frames.Frame:
        """
            Getter for the body fixed frame.
        
            Returns:
                the body fixed frame
        
        
        """
        ...
    def getBodyShape(self) -> fr.cnes.sirius.patrius.bodies.BodyShape:
        """
            Getter for the body shape.
        
            Returns:
                the body shape
        
        
        """
        ...
    class BodyDistanceType(java.lang.Enum['SurfaceDistanceDetector.BodyDistanceType']):
        CLOSEST: typing.ClassVar['SurfaceDistanceDetector.BodyDistanceType'] = ...
        RADIAL: typing.ClassVar['SurfaceDistanceDetector.BodyDistanceType'] = ...
        def getDistance(self, bodyPoint: fr.cnes.sirius.patrius.bodies.BodyPoint) -> float: ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'SurfaceDistanceDetector.BodyDistanceType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['SurfaceDistanceDetector.BodyDistanceType']: ...

class TargetInFieldOfViewDetector(AbstractSignalPropagationDetector):
    """
    public class TargetInFieldOfViewDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
    
    
        Event detector for the main target visibility of a sensor. The g function is positive if the main target is in the field
        of view.
    
        The default implementation behavior is to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.CONTINUE`
        propagation when entering the zone and to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.STOP` propagation
        when exiting the zone. This can be changed by using one of the provided constructors.
    
        This detector can takes into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` (default is
        signal being instantaneous).
    
        Since:
            1.2
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.assembly.models.SensorModel`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, assembly: fr.cnes.sirius.patrius.assembly.Assembly, string: str, double: float, double2: float): ...
    @typing.overload
    def __init__(self, assembly: fr.cnes.sirius.patrius.assembly.Assembly, string: str, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, double: float, double2: float): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - sensor: :class:`~fr.cnes.sirius.patrius.assembly.models.SensorModel`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getAssembly(self) -> fr.cnes.sirius.patrius.assembly.Assembly:
        """
            Get the assembly.
        
            Returns:
                the assembly
        
        
        """
        ...
    def getSensor(self) -> fr.cnes.sirius.patrius.assembly.models.SensorModel:
        """
            Get the sensor.
        
            Returns:
                the sensor
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...
    def setPropagationDelayType(self, propagationDelayType: AbstractSignalPropagationDetector.PropagationDelayType, frame: fr.cnes.sirius.patrius.frames.Frame) -> None:
        """
            Description copied from
            class: :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType`
            Setter for the propagation delay computation type. Warning: check Javadoc of detector to see if detector takes into
            account propagation time delay. if not, signals are always considered instantaneous. The provided frame is used to
            compute the signal propagation when delay is taken into account.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` in
                class :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
        
            Parameters:
                propagationDelayType (:class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.PropagationDelayType`): Propagation delay type used in events computation
                frame (:class:`~fr.cnes.sirius.patrius.frames.Frame`): Frame to use for signal propagation with delay (may be null if propagation delay type is considered instantaneous).
                    Warning: the usage of a pseudo inertial frame is tolerated, however it will lead to some inaccuracies due to the
                    non-invariance of the frame with respect to time. For this reason, it is suggested to use the ICRF frame or a frame
                    which is frozen with respect to the ICRF.
        
        
        """
        ...

class BodyInEclipseDetector(AbstractEclipseDetector):
    """
    public class BodyInEclipseDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractEclipseDetector`
    
        Finder for events related to a celestial body in eclipse.
    
        This class finds eclipse events, i.e. celestial body within umbra (total eclipse) or penumbra (partial eclipse).
    
        The default implementation behavior is to :code:`EventDetector.Action#CONTINUE` continue propagation when entering the
        eclipse and to :code:`EventDetector.Action#STOP` stop propagation when exiting the eclipse. This can be changed by using
        some constructors.
    
        This detector takes into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` (default is
        signal being instantaneous).
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.propagation.Propagator.addEventDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double2: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, boolean: bool, boolean2: bool, bodyInEclipseModelEnum: 'BodyInEclipseDetector.BodyInEclipseModelEnum', int: int, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double2: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, boolean: bool, boolean2: bool, bodyInEclipseModelEnum: 'BodyInEclipseDetector.BodyInEclipseModelEnum', int: int, double3: float, double4: float, boolean3: bool, boolean4: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double2: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, boolean: bool, boolean2: bool, bodyInEclipseModelEnum: 'BodyInEclipseDetector.BodyInEclipseModelEnum', int: int, double3: float, double4: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean3: bool, boolean4: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double2: float, pVCoordinatesProvider3: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double3: float, boolean: bool, boolean2: bool, bodyInEclipseModelEnum: 'BodyInEclipseDetector.BodyInEclipseModelEnum', int: int, double4: float, double5: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double2: float, pVCoordinatesProvider3: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double3: float, boolean: bool, boolean2: bool, bodyInEclipseModelEnum: 'BodyInEclipseDetector.BodyInEclipseModelEnum', int: int, double4: float, double5: float, boolean3: bool, boolean4: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double2: float, pVCoordinatesProvider3: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double3: float, boolean: bool, boolean2: bool, bodyInEclipseModelEnum: 'BodyInEclipseDetector.BodyInEclipseModelEnum', int: int, double4: float, double5: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean3: bool, boolean4: bool): ...
    def copy(self) -> 'BodyInEclipseDetector':
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - occultingBody: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
              - occultedBody: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
              - occultingRadiusProvider: :class:`~fr.cnes.sirius.patrius.bodies.ApparentRadiusProvider`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    @typing.overload
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    @typing.overload
    def g(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> float: ...
    @typing.overload
    def isInEclipse(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> bool: ...
    @typing.overload
    def isInEclipse(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> bool: ...
    def isTotalEclipse(self) -> bool:
        """
            Get the total eclipse detection flag.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractEclipseDetector.isTotalEclipse` in
                class :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractEclipseDetector`
        
            Returns:
                the total eclipse detection flag (true for umbra events detection, false for penumbra events detection)
        
        
        """
        ...
    class BodyInEclipseModelEnum(java.lang.Enum['BodyInEclipseDetector.BodyInEclipseModelEnum']):
        EXACT_MODEL: typing.ClassVar['BodyInEclipseDetector.BodyInEclipseModelEnum'] = ...
        APPROX_MODEL: typing.ClassVar['BodyInEclipseDetector.BodyInEclipseModelEnum'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'BodyInEclipseDetector.BodyInEclipseModelEnum': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['BodyInEclipseDetector.BodyInEclipseModelEnum']: ...

class BodyPointLocalTimeAngleDetector(LocalTimeAngleDetector):
    """
    public class BodyPointLocalTimeAngleDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.LocalTimeAngleDetector`
    
        Detects when the local time angle of point on a spacecraft is equal to a predetermined value.
    
    
        The local time is represented by the angle between the projections of the Sun and the zenithal direction of the point;
        therefore this angle is equal to zero when the local time is 12.00h and Π when the local time is 0.00h (Local Time In
        Hours = 12.00h + local time angle * 12 / Π).
    
        Since:
            4.16
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.events.detectors.LocalTimeAngleDetector`, :meth:`~serialized`
    """
    def __init__(self, double: float, bodyPoint: fr.cnes.sirius.patrius.bodies.BodyPoint, double2: float, double3: float, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, int: int): ...
    def copy(self) -> 'BodyPointLocalTimeAngleDetector':
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.copy` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.detectors.LocalTimeAngleDetector.copy` in
                class :class:`~fr.cnes.sirius.patrius.events.detectors.LocalTimeAngleDetector`
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def getBodyPoint(self) -> fr.cnes.sirius.patrius.bodies.BodyPoint:
        """
            Getter for the body point
        
            Returns:
                the body point
        
        
        """
        ...

class EclipseDetector(AbstractEclipseDetector):
    """
    public class EclipseDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractEclipseDetector`
    
        Finder for satellite eclipse related events.
    
        This class finds eclipse events, i.e. satellite within umbra (total eclipse) or penumbra (partial eclipse).
    
        The default implementation behavior is to :code:`EventDetector.Action#CONTINUE` continue propagation when entering the
        eclipse and to :code:`EventDetector.Action#STOP` stop propagation when exiting the eclipse. This can be changed by using
        some constructors.
    
        This detector can takes into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` (default is
        signal being instantaneous).
    
    
        It can be taken only if the occulted body is defined through a
        :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider` and not an
        :class:`~fr.cnes.sirius.patrius.attitudes.directions.IDirection`.
    
        **WARNING** : Do not use this detector to detect ground target visibilities or occulted bodies with null radius.
        Actually, the lighting ratio used to compute g function is based on geometric angle comparison and considers that if the
        vehicle is closer to the occulted body than to the occulting body then the occulted body is not occulted. This is not
        true if the occulted body is a target on the ground of the occulting body and In this case, it will detect a period out
        of eclipse longer than it should be.
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.propagation.Propagator.addEventDetector`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, iDirection: fr.cnes.sirius.patrius.attitudes.directions.IDirection, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, iDirection: fr.cnes.sirius.patrius.attitudes.directions.IDirection, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, iDirection: fr.cnes.sirius.patrius.attitudes.directions.IDirection, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, iDirection: fr.cnes.sirius.patrius.attitudes.directions.IDirection, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, double2: float, double3: float, double4: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, int: int): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, double2: float, double3: float, double4: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, double2: float, double3: float, double4: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, double2: float, double3: float, double4: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool, int: int): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, bodyShape: fr.cnes.sirius.patrius.bodies.BodyShape, double2: float, double3: float, double4: float, int: int): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double2: float, double3: float, double4: float, double5: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double2: float, double3: float, double4: float, double5: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double2: float, double3: float, double4: float, double5: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double2: float, double3: float, int: int, double4: float, double5: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - occultingBody: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
              - occultedBody: :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
              - occultingRadiusProvider: :class:`~fr.cnes.sirius.patrius.bodies.ApparentRadiusProvider`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getOccultedDirection(self) -> fr.cnes.sirius.patrius.attitudes.directions.IDirection:
        """
            Returns the occulted body direction.
        
            Returns:
                the occulted direction
        
        
        """
        ...
    def isTotalEclipse(self) -> bool:
        """
            Get the total eclipse detection flag.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractEclipseDetector.isTotalEclipse` in
                class :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractEclipseDetector`
        
            Returns:
                the total eclipse detection flag (true for umbra events detection, false for penumbra events detection)
        
        
        """
        ...

class StationToSatMutualVisibilityDetector(AbstractStationToSatDetector):
    """
    public class StationToSatMutualVisibilityDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractStationToSatDetector`
    
    
        Mutual station to spacecraft visibility detector : the g function is positive only if the station's sensor sees the
        spacecraft's sensor AND the spacecraft's sensor sees the station's sensor.
    
        The default implementation behavior is to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.CONTINUE`
        propagation when entering the eclipse and to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.STOP`
        propagation when exiting the eclipse. This can be changed by using one of the provided contructors.
    
        This detector can take into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` (default is
        signal being instantaneous).
    
    
        Default linktype is :meth:`~fr.cnes.sirius.patrius.events.detectors.VisibilityFromStationDetector.LinkType.DOWNLINK`.
    
        Since:
            1.2
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.assembly.Assembly`,
            :class:`~fr.cnes.sirius.patrius.groundstation.GeometricStationAntenna`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool, linkType: 'VisibilityFromStationDetector.LinkType'): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, geometricStationAntenna: fr.cnes.sirius.patrius.groundstation.GeometricStationAntenna, angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, boolean: bool, double: float, double2: float): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, geometricStationAntenna: fr.cnes.sirius.patrius.groundstation.GeometricStationAntenna, angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, boolean: bool, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, geometricStationAntenna: fr.cnes.sirius.patrius.groundstation.GeometricStationAntenna, angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, boolean: bool, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean2: bool, boolean3: bool): ...
    @typing.overload
    def __init__(self, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, geometricStationAntenna: fr.cnes.sirius.patrius.groundstation.GeometricStationAntenna, angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, boolean: bool, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean2: bool, boolean3: bool, linkType: 'VisibilityFromStationDetector.LinkType'): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - inSensorSpacecraft: :class:`~fr.cnes.sirius.patrius.assembly.models.SensorModel`
              - correction: :class:`~fr.cnes.sirius.patrius.signalpropagation.AngularCorrection`
              - station: :class:`~fr.cnes.sirius.patrius.groundstation.GeometricStationAntenna`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...
    def setPropagationDelayType(self, propagationDelayType: AbstractSignalPropagationDetector.PropagationDelayType, frame: fr.cnes.sirius.patrius.frames.Frame) -> None:
        """
            Setter for the propagation delay computation type. Warning: check Javadoc of detector to see if detector takes into
            account propagation time delay. if not, signals are always considered instantaneous. The provided frame is used to
            compute the signal propagation when delay is taken into account.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` in
                class :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
        
            Parameters:
                propagationDelayType (:class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.PropagationDelayType`): Propagation delay type used in events computation
                frame (:class:`~fr.cnes.sirius.patrius.frames.Frame`): Frame to use for signal propagation with delay (may be null if propagation delay type is considered instantaneous).
                    Warning: the usage of a pseudo inertial frame is tolerated, however it will lead to some inaccuracies due to the
                    non-invariance of the frame with respect to time. For this reason, it is suggested to use the ICRF frame or a frame
                    which is frozen with respect to the ICRF.
        
        
        """
        ...
    def shouldBeRemoved(self) -> bool:
        """
            This method is called after :meth:`~fr.cnes.sirius.patrius.events.EventDetector.eventOccurred` has been triggered. It
            returns true if the current detector should be removed after first event detection. **WARNING:** this method can be
            called only once a event has been triggered. Before, the value is not available.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.shouldBeRemoved` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.shouldBeRemoved` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Returns:
                true if the current detector should be removed after first event detection
        
        
        """
        ...

class VisibilityFromStationDetector(AbstractStationToSatDetector):
    """
    public class VisibilityFromStationDetector extends :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractStationToSatDetector`
    
        Finder for satellite apparent entering in a station's field of view.
    
        The tropospheric correction used can be set by the user.
    
        The default implementation behavior is to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.CONTINUE`
        propagation at raising and to :meth:`~fr.cnes.sirius.patrius.events.EventDetector.Action.STOP` propagation at setting.
        This can be changed by using one of the provided constructors.
    
        This detector can takes into account signal propagation duration through
        :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` (default is
        signal being instantaneous).
    
        Since:
            1.1
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.signalpropagation.troposphere.TroposphericCorrection`,
            :class:`~fr.cnes.sirius.patrius.events.EventDetector`,
            :class:`~fr.cnes.sirius.patrius.groundstation.GeometricStationAntenna`, :meth:`~serialized`
    """
    RAISING: typing.ClassVar[int] = ...
    """
    public static final int RAISING
    
        Flag for raising detection (slopeSelection = 0).
    
        Also see:
            :meth:`~constant`
    
    
    """
    SETTING: typing.ClassVar[int] = ...
    """
    public static final int SETTING
    
        Flag for setting detection (slopeSelection = 1).
    
        Also see:
            :meth:`~constant`
    
    
    """
    RAISING_SETTING: typing.ClassVar[int] = ...
    """
    public static final int RAISING_SETTING
    
        Flag for raising/setting detection (slopeSelection = 2).
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, boolean: bool, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean2: bool, boolean3: bool, linkType: 'VisibilityFromStationDetector.LinkType'): ...
    @typing.overload
    def __init__(self, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool, linkType: 'VisibilityFromStationDetector.LinkType'): ...
    @typing.overload
    def __init__(self, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, double2: float, double3: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, linkType: 'VisibilityFromStationDetector.LinkType'): ...
    @typing.overload
    def __init__(self, topocentricFrame: fr.cnes.sirius.patrius.frames.TopocentricFrame, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, double2: float, double3: float, linkType: 'VisibilityFromStationDetector.LinkType'): ...
    @typing.overload
    def __init__(self, geometricStationAntenna: fr.cnes.sirius.patrius.groundstation.GeometricStationAntenna, sensorModel: fr.cnes.sirius.patrius.assembly.models.SensorModel, angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, boolean: bool, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean2: bool, boolean3: bool, linkType: 'VisibilityFromStationDetector.LinkType'): ...
    @typing.overload
    def __init__(self, geometricStationAntenna: fr.cnes.sirius.patrius.groundstation.GeometricStationAntenna, angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, boolean2: bool, linkType: 'VisibilityFromStationDetector.LinkType'): ...
    @typing.overload
    def __init__(self, geometricStationAntenna: fr.cnes.sirius.patrius.groundstation.GeometricStationAntenna, angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, action2: fr.cnes.sirius.patrius.events.EventDetector.Action, linkType: 'VisibilityFromStationDetector.LinkType'): ...
    @typing.overload
    def __init__(self, geometricStationAntenna: fr.cnes.sirius.patrius.groundstation.GeometricStationAntenna, angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, double: float, double2: float, linkType: 'VisibilityFromStationDetector.LinkType'): ...
    @typing.overload
    def __init__(self, geometricStationAntenna: fr.cnes.sirius.patrius.groundstation.GeometricStationAntenna, angularCorrection: fr.cnes.sirius.patrius.signalpropagation.AngularCorrection, int: int, double: float, double2: float, action: fr.cnes.sirius.patrius.events.EventDetector.Action, boolean: bool, linkType: 'VisibilityFromStationDetector.LinkType'): ...
    def copy(self) -> fr.cnes.sirius.patrius.events.EventDetector:
        """
            A copy of the detector. By default copy is deep. If not, detector javadoc will specify which attribute is not fully
            copied. In that case, the attribute reference is passed.
        
            The following attributes are not deeply copied:
        
              - correction: :class:`~fr.cnes.sirius.patrius.signalpropagation.AngularCorrection`
              - station: :class:`~fr.cnes.sirius.patrius.groundstation.GeometricStationAntenna`
        
        
            Returns:
                a copy of the detector.
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, boolean: bool, boolean2: bool) -> fr.cnes.sirius.patrius.events.EventDetector.Action: ...
    def g(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState) -> float: ...
    def getBodyShape(self) -> fr.cnes.sirius.patrius.bodies.BodyShape:
        """
            Getter for the body shape.
        
            Returns:
                the body shape
        
        
        """
        ...
    def getStationBodyPoint(self) -> fr.cnes.sirius.patrius.bodies.BodyPoint:
        """
            Getter for the station body point.
        
            Returns:
                the station body point
        
        
        """
        ...
    def init(self, spacecraftState: fr.cnes.sirius.patrius.propagation.SpacecraftState, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.events.EventDetector.init` in
                interface :class:`~fr.cnes.sirius.patrius.events.EventDetector`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.AbstractDetector.init` in
                class :class:`~fr.cnes.sirius.patrius.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~fr.cnes.sirius.patrius.propagation.SpacecraftState`): initial state
                t (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...
    def setPropagationDelayType(self, propagationDelayType: AbstractSignalPropagationDetector.PropagationDelayType, frame: fr.cnes.sirius.patrius.frames.Frame) -> None:
        """
            Setter for the propagation delay computation type. Warning: check Javadoc of detector to see if detector takes into
            account propagation time delay. if not, signals are always considered instantaneous. The provided frame is used to
            compute the signal propagation when delay is taken into account.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.setPropagationDelayType` in
                class :class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector`
        
            Parameters:
                propagationDelayType (:class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.PropagationDelayType`): Propagation delay type used in events computation
                frame (:class:`~fr.cnes.sirius.patrius.frames.Frame`): Frame to use for signal propagation with delay (may be null if propagation delay type is considered instantaneous).
                    Warning: the usage of a pseudo inertial frame is tolerated, however it will lead to some inaccuracies due to the
                    non-invariance of the frame with respect to time. For this reason, it is suggested to use the ICRF frame or a frame
                    which is frozen with respect to the ICRF.
        
        
        """
        ...
    class LinkType(java.lang.Enum['VisibilityFromStationDetector.LinkType']):
        UPLINK: typing.ClassVar['VisibilityFromStationDetector.LinkType'] = ...
        DOWNLINK: typing.ClassVar['VisibilityFromStationDetector.LinkType'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'VisibilityFromStationDetector.LinkType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['VisibilityFromStationDetector.LinkType']: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("fr.cnes.sirius.patrius.events.detectors")``.

    AOLDetector: typing.Type[AOLDetector]
    AbstractEclipseDetector: typing.Type[AbstractEclipseDetector]
    AbstractSignalPropagationDetector: typing.Type[AbstractSignalPropagationDetector]
    AbstractStationToSatDetector: typing.Type[AbstractStationToSatDetector]
    AlignmentDetector: typing.Type[AlignmentDetector]
    AltitudeDetector: typing.Type[AltitudeDetector]
    AngularMomentumExcessDetector: typing.Type[AngularMomentumExcessDetector]
    AnomalyDetector: typing.Type[AnomalyDetector]
    ApparentElevationDetector: typing.Type[ApparentElevationDetector]
    ApsideDetector: typing.Type[ApsideDetector]
    BetaAngleDetector: typing.Type[BetaAngleDetector]
    BodyInEclipseDetector: typing.Type[BodyInEclipseDetector]
    BodyPointLocalTimeAngleDetector: typing.Type[BodyPointLocalTimeAngleDetector]
    CenteredAolPassageDetector: typing.Type[CenteredAolPassageDetector]
    CentralBodyMaskCircularFOVDetector: typing.Type[CentralBodyMaskCircularFOVDetector]
    CircularFieldOfViewDetector: typing.Type[CircularFieldOfViewDetector]
    CombinedPhenomenaDetector: typing.Type[CombinedPhenomenaDetector]
    DateDetector: typing.Type[DateDetector]
    DihedralFieldOfViewDetector: typing.Type[DihedralFieldOfViewDetector]
    DistanceDetector: typing.Type[DistanceDetector]
    DotProductDetector: typing.Type[DotProductDetector]
    EarthZoneDetector: typing.Type[EarthZoneDetector]
    EclipseDetector: typing.Type[EclipseDetector]
    ElevationDetector: typing.Type[ElevationDetector]
    ExtremaDistanceDetector: typing.Type[ExtremaDistanceDetector]
    ExtremaElevationDetector: typing.Type[ExtremaElevationDetector]
    ExtremaGenericDetector: typing.Type[ExtremaGenericDetector]
    ExtremaLatitudeDetector: typing.Type[ExtremaLatitudeDetector]
    ExtremaLongitudeDetector: typing.Type[ExtremaLongitudeDetector]
    ExtremaSightAxisDetector: typing.Type[ExtremaSightAxisDetector]
    ExtremaThreeBodiesAngleDetector: typing.Type[ExtremaThreeBodiesAngleDetector]
    FlightDomainExcessDetector: typing.Type[FlightDomainExcessDetector]
    GroundMaskElevationDetector: typing.Type[GroundMaskElevationDetector]
    IntervalOccurrenceDetector: typing.Type[IntervalOccurrenceDetector]
    LatitudeDetector: typing.Type[LatitudeDetector]
    LineMaskingDetector: typing.Type[LineMaskingDetector]
    LinkTypeHandler: typing.Type[LinkTypeHandler]
    LocalTimeAngleDetector: typing.Type[LocalTimeAngleDetector]
    LongitudeDetector: typing.Type[LongitudeDetector]
    MaskingDetector: typing.Type[MaskingDetector]
    NadirSolarIncidenceDetector: typing.Type[NadirSolarIncidenceDetector]
    NodeDetector: typing.Type[NodeDetector]
    NthOccurrenceDetector: typing.Type[NthOccurrenceDetector]
    NullMassDetector: typing.Type[NullMassDetector]
    NullMassPartDetector: typing.Type[NullMassPartDetector]
    PlaneCrossingDetector: typing.Type[PlaneCrossingDetector]
    RFVisibilityDetector: typing.Type[RFVisibilityDetector]
    RelativeDateDetector: typing.Type[RelativeDateDetector]
    SatToSatMutualVisibilityDetector: typing.Type[SatToSatMutualVisibilityDetector]
    SensorInhibitionDetector: typing.Type[SensorInhibitionDetector]
    SensorVisibilityDetector: typing.Type[SensorVisibilityDetector]
    SolarTimeAngleDetector: typing.Type[SolarTimeAngleDetector]
    StationToSatMutualVisibilityDetector: typing.Type[StationToSatMutualVisibilityDetector]
    SurfaceDistanceDetector: typing.Type[SurfaceDistanceDetector]
    TargetInFieldOfViewDetector: typing.Type[TargetInFieldOfViewDetector]
    ThreeBodiesAngleDetector: typing.Type[ThreeBodiesAngleDetector]
    VisibilityFromStationDetector: typing.Type[VisibilityFromStationDetector]
