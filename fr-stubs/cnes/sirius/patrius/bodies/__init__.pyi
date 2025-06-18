
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import fr.cnes.sirius.patrius.attitudes
import fr.cnes.sirius.patrius.attitudes.directions
import fr.cnes.sirius.patrius.bodies.bsp
import fr.cnes.sirius.patrius.bodies.mesh
import fr.cnes.sirius.patrius.events.detectors
import fr.cnes.sirius.patrius.forces.gravity
import fr.cnes.sirius.patrius.frames
import fr.cnes.sirius.patrius.math.analysis.differentiation
import fr.cnes.sirius.patrius.math.geometry.euclidean.threed
import fr.cnes.sirius.patrius.orbits.pvcoordinates
import fr.cnes.sirius.patrius.time
import fr.cnes.sirius.patrius.utils
import java.io
import java.lang
import java.util
import jpype
import typing



class ApparentRadiusProvider(java.io.Serializable):
    """
    public interface ApparentRadiusProvider extends `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Interface to represent apparent radius providers.
    """
    def getApparentRadius(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, propagationDelayType: fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.PropagationDelayType) -> float:
        """
            Compute the apparent radius (in meters) of the occulting body from the spacecraft (observer) position. Given a plane
            containing the spacecraft (observer) position, the center of the occulting body and the center of the occulted body, and
            given a line contained within this plane, passing by the spacecraft (observer) position and tangent to the mesh of the
            occulting body, the apparent radius corresponds to the length of the line starting from the center of the occulting
            body, perpendicular to the first given line and ending at the intersection of the two lines.
        
            Please notice that this method will for the moment be used only with an instantaneous propagation delay type.
        
        
            Parameters:
                pvObserver (:class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`): the spacecraft (observer) position-velocity
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): the date at which the signal is received by the observer (reception date)
                occultedBody (:class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`): the body which is occulted to the spacecraft (observer) by the occulting body
                propagationDelayType (:class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.PropagationDelayType`): propagation delay type
        
            Returns:
                the apparent radius (in meters) of the occulting body from the spacecraft (observer) position
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.utils.exception.PatriusException`: if the :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider` computation fails
        
        
        """
        ...

class BasicBoardSun(fr.cnes.sirius.patrius.attitudes.directions.IDirection):
    """
    public class BasicBoardSun extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.attitudes.directions.IDirection`
    
        This class provides the Sun direction at a specific date, according to a simple analytical model.
    
    
    
        Since:
            1.3
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    def getLine(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, frame: fr.cnes.sirius.patrius.frames.Frame) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line: ...
    def getVector(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, frame: fr.cnes.sirius.patrius.frames.Frame) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D: ...

class BodyPoint(fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider):
    def angularSeparation(self, bodyPoint: 'BodyPoint') -> float: ...
    def distance(self, bodyPoint: 'BodyPoint') -> float: ...
    def getBodyShape(self) -> 'BodyShape': ...
    def getClosestPointOnShape(self) -> 'BodyPoint': ...
    @typing.overload
    def getLLHCoordinates(self, lLHCoordinatesSystem: 'LLHCoordinatesSystem') -> 'LLHCoordinates': ...
    @typing.overload
    def getLLHCoordinates(self) -> 'LLHCoordinates': ...
    def getName(self) -> str: ...
    def getNativeFrame(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.frames.Frame: ...
    @typing.overload
    def getNormal(self) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getNormal(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, frame: fr.cnes.sirius.patrius.frames.Frame) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D: ...
    def getNormalHeight(self) -> float: ...
    def getPVCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, frame: fr.cnes.sirius.patrius.frames.Frame) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates: ...
    def getPosition(self) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D: ...
    def getRadialProjectionOnShape(self) -> 'BodyPoint': ...
    def isInsideShape(self) -> bool: ...
    def isOnShapeSurface(self) -> bool: ...
    def toString(self, lLHCoordinatesSystem: 'LLHCoordinatesSystem') -> str: ...
    class BodyPointName:
        DEFAULT: typing.ClassVar[str] = ...
        INTERSECTION: typing.ClassVar[str] = ...
        INTERSECTION_AT_ALTITUDE: typing.ClassVar[str] = ...
        CLOSEST_ON_SHAPE: typing.ClassVar[str] = ...
        RADIAL_ON_SHAPE: typing.ClassVar[str] = ...
        CLOSEST_ON_LINE: typing.ClassVar[str] = ...
        NAMES_LIST: typing.ClassVar[java.util.List] = ...
        @staticmethod
        def join(string: str, string2: str) -> str: ...

class BodyShape(fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider):
    """
    public interface BodyShape extends :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
    
        Extended interface for celestial bodies shapes : extends the OREKIT's BodyShape interface by adding geometric methods.
    
        Since:
            1.2
    """
    DEFAULT_DISTANCE_EPSILON: typing.ClassVar[float] = ...
    """
    static final double DEFAULT_DISTANCE_EPSILON
    
        Default value of distance epsilon below which the height coordinate is neglected: below this value,the method
        :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.getIntersectionPoint` will be automatically used instead of
        :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.getIntersectionPoint`. This distance epsilon is also used to assess if a
        body point is on the shape surface or not (method :meth:`~fr.cnes.sirius.patrius.bodies.BodyPoint.isOnShapeSurface`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DIRECTION_FACTOR: typing.ClassVar[float] = ...
    """
    static final double DIRECTION_FACTOR
    
        Factor to be multiplied to the direction in order to improve the accuracy of the line creation by increasing the
        distance between the origin and the second point.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def buildPoint(self, lLHCoordinatesSystem: 'LLHCoordinatesSystem', double: float, double2: float, double3: float, string: str) -> BodyPoint:
        """
            Build a :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` from LLH coordinates. Type of returned body point depends on
            body.
        
            Parameters:
                coordSystem (:class:`~fr.cnes.sirius.patrius.bodies.LLHCoordinatesSystem`): LLH coordinates system in which are expressed the entered lat/long/height
                latitude (double): input latitude
                longitude (double): input longitude
                height (double): input height
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): name of the point
        
            Returns:
                a body point
        
        """
        ...
    @typing.overload
    def buildPoint(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, string: str) -> BodyPoint: ...
    @typing.overload
    def buildPoint(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, string: str) -> BodyPoint:
        """
            Build a :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` from position in body frame. Type of returned body point
            depends on body.
        
            Parameters:
                position (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): position in body frame
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): name of the point
        
            Returns:
                :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` from position in body frame
        
        :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` buildPoint(:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` position, :class:`~fr.cnes.sirius.patrius.frames.Frame` frame, :class:`~fr.cnes.sirius.patrius.time.AbsoluteDate` date, `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` name) throws :class:`~fr.cnes.sirius.patrius.utils.exception.PatriusException`
        
            Build a :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` from position in provided frame at provided date. Type of
            returned body point depends on body.
        
            Parameters:
                position (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): position in provided frame at provided date
                frame (:class:`~fr.cnes.sirius.patrius.frames.Frame`): frame
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): date
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): name of the point
        
            Returns:
                :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` from position in provided frame at provided date
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.utils.exception.PatriusException`: if failed to build point
        
        
        """
        ...
    def buildRadialPointOnShapeSurface(self, double: float, double2: float) -> BodyPoint:
        """
            Build a body point on the radial direction corresponding to entered bodycentric latitude and longitude: if more than one
            intersection, the method considers the one farthest to the body frame origin (having the largest norm).
        
            Parameters:
                bodycentricLatitude (double): bodycentric latitude
                bodycentricLongitude (double): bodycentric longitude
        
            Returns:
                the radial point at the surface of the body shape
        
        
        """
        ...
    @typing.overload
    def closestPointTo(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D) -> BodyPoint:
        """
            This method computes the two points, on the line and on the body, that are the closest to each other. The returned
            points are identical if the line intersects the shape: this point is the one with the lowest abscissa. The returned
            point with index 0 is the point on the Line, while the returned point with index 1 is the point on this.
        
            Note: calculations take the line's minimum abscissa into account.
        
            In this method we consider that the line's frame is the body frame, and the date is the
            :meth:`~fr.cnes.sirius.patrius.time.AbsoluteDate.J2000_EPOCH`.
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the original line for the shortest distance computation
        
            Returns:
                an array of length 2 containing the point of the line (slot [0]) and the point of the shape (slot [1]) expressed as
                :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` (depending on body shape)
        
        :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` closestPointTo(:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` point, :class:`~fr.cnes.sirius.patrius.frames.Frame` frame, :class:`~fr.cnes.sirius.patrius.time.AbsoluteDate` date) throws :class:`~fr.cnes.sirius.patrius.utils.exception.PatriusException`
        
            Computes the point on body surface that is the closest to provided point.
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): a point expressed in provided frame
                frame (:class:`~fr.cnes.sirius.patrius.frames.Frame`): frame
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): date
        
            Returns:
                the closest point to the provided point on the body surface
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.utils.exception.PatriusException`: if computation failed
        
            Computes the point on body surface that is the closest to provided point.
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): a point expressed in body frame
        
            Returns:
                the closest point to the provided point on the body surface
        
            Computes the point on body surface that is the closest to provided point.
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): a point expressed in body frame
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): name of the point
        
            Returns:
                the closest point to the provided point on the body surface
        
        
        """
        ...
    @typing.overload
    def closestPointTo(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> BodyPoint: ...
    @typing.overload
    def closestPointTo(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, string: str) -> BodyPoint: ...
    @typing.overload
    def closestPointTo(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line) -> typing.MutableSequence[BodyPoint]: ...
    @typing.overload
    def closestPointTo(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> typing.MutableSequence[BodyPoint]: ...
    def distanceTo(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> float: ...
    def getApparentRadius(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, propagationDelayType: fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.PropagationDelayType) -> float: ...
    def getBodyFrame(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame:
        """
            Getter for the body frame related to body shape.
        
            Returns:
                the body frame related to body shape
        
        
        """
        ...
    def getDistanceEpsilon(self) -> float:
        """
            Return the distance epsilon below which the height coordinate is neglected. This epsilon value can be modified using
            dedicated setter.
        
              - Below this distance epsilon, the method :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.getIntersectionPoint` will be
                automatically used instead of :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.getIntersectionPoint`,
              - The method :meth:`~fr.cnes.sirius.patrius.bodies.BodyPoint.isOnShapeSurface` will return true if the absolute value of
                its normal height is lower than this distance epsilon.
        
        
            Returns:
                the altitude epsilon
        
        
        """
        ...
    def getEncompassingSphereRadius(self) -> float:
        """
            Getter for the radius, in meters, of a sphere centered on the body frame origin and encompassing the shape.
        
            Returns:
                the encompassing radius
        
        
        """
        ...
    def getEpsilonSignalPropagation(self) -> float:
        """
            Getter for the epsilon for signal propagation used in :code:`#getApparentRadius(PVCoordinatesProvider, AbsoluteDate,
            PVCoordinatesProvider, PropagationDelayType)` method. This epsilon (in s) directly reflect the accuracy of signal
            propagation (1s of accuracy = 3E8m of accuracy on distance between emitter and receiver).
        
            Returns:
                the epsilon for signal propagation
        
        
        """
        ...
    @typing.overload
    def getIntersectionPoint(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> BodyPoint: ...
    @typing.overload
    def getIntersectionPoint(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, double: float) -> BodyPoint: ...
    @typing.overload
    def getIntersectionPoint(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, string: str) -> BodyPoint: ...
    def getIntersectionPoints(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> typing.MutableSequence[BodyPoint]: ...
    def getLLHCoordinatesSystem(self) -> 'LLHCoordinatesSystem':
        """
            Getter for the LLH coordinates system used by the computed :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint`.
        
            Returns:
                the coordinates system
        
        
        """
        ...
    def getName(self) -> str:
        """
            Getter for the name of the shape.
        
            Returns:
                the name of the shape
        
        
        """
        ...
    def isDefaultLLHCoordinatesSystem(self) -> bool:
        """
            Indicate if the current LLH coordinates system set for the body is the default one or not.
        
            Returns:
                :code:`true` if the current LLH coordinates system is the default one, :code:`false` otherwise
        
        
        """
        ...
    def resize(self, marginType: 'BodyShape.MarginType', double: float) -> 'BodyShape': ...
    def setDistanceEpsilon(self, double: float) -> None:
        """
            Setter for the distance epsilon below which the height coordinate is neglected.
        
            Parameters:
                epsilon (double): distance epsilon to be set
        
        
        """
        ...
    def setEpsilonSignalPropagation(self, double: float) -> None:
        """
            Setter for the epsilon for signal propagation used in :code:`#getApparentRadius(PVCoordinatesProvider, AbsoluteDate,
            PVCoordinatesProvider, PropagationDelayType)` method. This epsilon (in s) directly reflect the accuracy of signal
            propagation (1s of accuracy = 3E8m of accuracy on distance between emitter and receiver).
        
            Parameters:
                epsilon (double): epsilon for signal propagation
        
        
        """
        ...
    def setLLHCoordinatesSystem(self, lLHCoordinatesSystem: 'LLHCoordinatesSystem') -> None:
        """
            Setter for the LLH coordinates system to be used by the computed :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint`.
        
            Parameters:
                coordSystem (:class:`~fr.cnes.sirius.patrius.bodies.LLHCoordinatesSystem`): LLH coordinates system to be set
        
        
        """
        ...
    class MarginType(java.lang.Enum['BodyShape.MarginType']):
        DISTANCE: typing.ClassVar['BodyShape.MarginType'] = ...
        SCALE_FACTOR: typing.ClassVar['BodyShape.MarginType'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'BodyShape.MarginType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['BodyShape.MarginType']: ...

class CelestialBodyEphemeris(fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider):
    """
    public interface CelestialBodyEphemeris extends :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
    
        Interface for celestial body ephemeris.
    
        Since:
            4.10
    """
    ...

class CelestialBodyEphemerisLoader(java.io.Serializable):
    """
    public interface CelestialBodyEphemerisLoader extends `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Interface for loading celestial bodies ephemeris.
    
        Since:
            4.10
    """
    def loadCelestialBodyEphemeris(self, string: str) -> CelestialBodyEphemeris: ...

class CelestialBodyFactory:
    SOLAR_SYSTEM_BARYCENTER: typing.ClassVar[str] = ...
    SUN: typing.ClassVar[str] = ...
    MERCURY: typing.ClassVar[str] = ...
    VENUS: typing.ClassVar[str] = ...
    EARTH_MOON: typing.ClassVar[str] = ...
    EARTH: typing.ClassVar[str] = ...
    MOON: typing.ClassVar[str] = ...
    MARS: typing.ClassVar[str] = ...
    MARS_BARY: typing.ClassVar[str] = ...
    JUPITER: typing.ClassVar[str] = ...
    JUPITER_BARY: typing.ClassVar[str] = ...
    SATURN: typing.ClassVar[str] = ...
    SATURN_BARY: typing.ClassVar[str] = ...
    URANUS: typing.ClassVar[str] = ...
    URANUS_BARY: typing.ClassVar[str] = ...
    NEPTUNE: typing.ClassVar[str] = ...
    NEPTUNE_BARY: typing.ClassVar[str] = ...
    PLUTO: typing.ClassVar[str] = ...
    PLUTO_BARY: typing.ClassVar[str] = ...
    @staticmethod
    def addCelestialBodyLoader(string: str, celestialBodyLoader: 'CelestialBodyLoader') -> None: ...
    @typing.overload
    @staticmethod
    def addDefaultCelestialBodyLoader(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def addDefaultCelestialBodyLoader(string: str, string2: str) -> None: ...
    @typing.overload
    @staticmethod
    def clearCelestialBodyLoaders() -> None: ...
    @typing.overload
    @staticmethod
    def clearCelestialBodyLoaders(string: str) -> None: ...
    @staticmethod
    def getBodies() -> java.util.Map[str, 'CelestialPoint']: ...
    @staticmethod
    def getBody(string: str) -> 'CelestialBody': ...
    @staticmethod
    def getEarth() -> 'CelestialBody': ...
    @staticmethod
    def getEarthMoonBarycenter() -> 'CelestialPoint': ...
    @staticmethod
    def getJupiter() -> 'CelestialBody': ...
    @staticmethod
    def getLoader(string: str) -> 'CelestialBodyLoader': ...
    @staticmethod
    def getMars() -> 'CelestialBody': ...
    @staticmethod
    def getMercury() -> 'CelestialBody': ...
    @staticmethod
    def getMoon() -> 'CelestialBody': ...
    @staticmethod
    def getNeptune() -> 'CelestialBody': ...
    @staticmethod
    def getPluto() -> 'CelestialBody': ...
    @staticmethod
    def getPoint(string: str) -> 'CelestialPoint': ...
    @staticmethod
    def getSaturn() -> 'CelestialBody': ...
    @staticmethod
    def getSolarSystemBarycenter() -> 'CelestialPoint': ...
    @staticmethod
    def getSun() -> 'CelestialBody': ...
    @staticmethod
    def getUranus() -> 'CelestialBody': ...
    @staticmethod
    def getVenus() -> 'CelestialBody': ...
    @staticmethod
    def hasNoLoader(string: str) -> bool: ...

class CelestialBodyLoader(java.io.Serializable):
    """
    public interface CelestialBodyLoader extends `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Interface for loading celestial bodies/points.
    
        A point :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint` is simpler than a
        :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`: it does not contains a gravity field, a shape or IAU data.
    
        The two methods :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyLoader.loadCelestialPoint` and
        :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyLoader.loadCelestialBody` returns the same data but built in
        different objects type (:class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint` or
        :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`).
    """
    def getName(self, string: str) -> str:
        """
            Returns name of body as known by the loader corresponding to PATRIUS body name.
        
            Parameters:
                patriusName (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): PATRIUS body name
        
            Returns:
                name of body as known by the loader corresponding to PATRIUS body name
        
        
        """
        ...
    def loadCelestialBody(self, string: str) -> 'CelestialBody': ...
    def loadCelestialPoint(self, string: str) -> 'CelestialPoint': ...

class CelestialBodyOrientation(java.io.Serializable):
    """
    public interface CelestialBodyOrientation extends `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Interface to represent a celestial body orientation.
    
        Since:
            4.13
    """
    @typing.overload
    def getAngularCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, orientationType: 'CelestialBodyOrientation.OrientationType') -> fr.cnes.sirius.patrius.utils.AngularCoordinates: ...
    @typing.overload
    def getAngularCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.utils.AngularCoordinates: ...
    def getPole(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D: ...
    def getPoleDerivative(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D: ...
    def getPrimeMeridianAngle(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> float: ...
    def getPrimeMeridianAngleDerivative(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> float: ...
    def toString(self) -> str:
        """
            Returns a string representation of the body orientation.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of the body orientation
        
        
        """
        ...
    class OrientationType(java.lang.Enum['CelestialBodyOrientation.OrientationType']):
        ICRF_TO_ROTATING: typing.ClassVar['CelestialBodyOrientation.OrientationType'] = ...
        ICRF_TO_INERTIAL: typing.ClassVar['CelestialBodyOrientation.OrientationType'] = ...
        INERTIAL_TO_ROTATING: typing.ClassVar['CelestialBodyOrientation.OrientationType'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'CelestialBodyOrientation.OrientationType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['CelestialBodyOrientation.OrientationType']: ...

class CelestialPoint(fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider):
    """
    public interface CelestialPoint extends :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
    
        Interface for celestial points like Sun, Moon or solar system planets (without modeling the shape, orientation, etc).
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyFactory`,
            :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyIAUOrientation`
    """
    ICRF_FRAME_NAME: typing.ClassVar[str] = ...
    """
    static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` ICRF_FRAME_NAME
    
        ICRF frame name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EME2000_FRAME_NAME: typing.ClassVar[str] = ...
    """
    static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` EME2000_FRAME_NAME
    
        EME2000 frame name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ECLIPTICJ2000_FRAME_NAME: typing.ClassVar[str] = ...
    """
    static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` ECLIPTICJ2000_FRAME_NAME
    
        EclipticJ2000 frame name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getBodyNature(self) -> 'CelestialPoint.BodyNature':
        """
            Getter for the celestial point nature.
        
            Returns:
                the celestial point nature
        
        
        """
        ...
    def getEME2000(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    def getEclipticJ2000(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    def getEphemeris(self) -> CelestialBodyEphemeris:
        """
            Get the ephemeris of the celestial point.
        
            Returns:
                the ephemeris
        
        
        """
        ...
    def getGM(self) -> float:
        """
            Get the central attraction coefficient of the celestial point.
        
            Warning: attraction model should not be null (it is not null by default).
        
            Returns:
                central attraction coefficient of the celestial point (m :sup:`3` /s :sup:`2` )
        
        
        """
        ...
    def getICRF(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    def getName(self) -> str:
        """
            Get the name of the celestial point.
        
            Returns:
                name of the celestial point
        
        
        """
        ...
    def setEphemeris(self, celestialBodyEphemeris: CelestialBodyEphemeris) -> None:
        """
            Set an ephemeris to the celestial point.
        
            Parameters:
                ephemerisIn (:class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyEphemeris`): the ephemeris
        
        
        """
        ...
    def setGM(self, double: float) -> None:
        """
            Set a central attraction coefficient to the celestial point.
        
            Parameters:
                gmIn (double): the central attraction coefficient (m :sup:`3` /s :sup:`2` )
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns a string representation of the celestial point and its attributes.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of the celestial point and its attributes
        
        
        """
        ...
    class BodyNature(java.lang.Enum['CelestialPoint.BodyNature']):
        PHYSICAL_BODY: typing.ClassVar['CelestialPoint.BodyNature'] = ...
        POINT: typing.ClassVar['CelestialPoint.BodyNature'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'CelestialPoint.BodyNature': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['CelestialPoint.BodyNature']: ...

class IAUPoleCoefficients(java.io.Serializable):
    """
    public class IAUPoleCoefficients extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        IAU coefficients for generic IAU pole model for pole and prime meridian orientations.
    
        This class represents the coefficients compliant with the report of the IAU/IAG Working Group on Cartographic
        Coordinates and Rotational Elements of the Planets and Satellites (WGCCRE). These definitions are common for all recent
        versions of this report published every three years.
    
        The precise values of pole direction and W angle coefficients may vary from publication year as models are adjusted. The
        latest value of constants for implementing this interface can be found in the `working group site
        <http://astrogeology.usgs.gov/Projects/WGCCRE/>`.
    
        Expressions for pole and prime meridian orientation have the same structure. They are defined with class
        :class:`~fr.cnes.sirius.patrius.bodies.IAUPoleCoefficients1D`.
    
        Since:
            4.7
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, iAUPoleCoefficients1D: 'IAUPoleCoefficients1D', iAUPoleCoefficients1D2: 'IAUPoleCoefficients1D', iAUPoleCoefficients1D3: 'IAUPoleCoefficients1D'): ...
    def getAlpha0Coeffs(self) -> 'IAUPoleCoefficients1D':
        """
            Returns the coefficients for α :sub:`0` component.
        
            Returns:
                the coefficients for α :sub:`0` component
        
        
        """
        ...
    def getDelta0Coeffs(self) -> 'IAUPoleCoefficients1D':
        """
            Returns the coefficients for δ :sub:`0` component.
        
            Returns:
                the coefficients for δ :sub:`0` component
        
        
        """
        ...
    def getWCoeffs(self) -> 'IAUPoleCoefficients1D':
        """
            Returns the coefficients for W component.
        
            Returns:
                the coefficients for W component
        
        
        """
        ...

class IAUPoleCoefficients1D(java.io.Serializable):
    """
    public class IAUPoleCoefficients1D extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        IAU pole coefficients for one elements (pole or prime meridian angle).
    
        Since:
            4.7
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, list: java.util.List['IAUPoleFunction']): ...
    def getFunctions(self) -> java.util.List['IAUPoleFunction']: ...

class IAUPoleFactory:
    """
    public final class IAUPoleFactory extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`
    
        Factory class for IAU poles.
    
        The pole models provided here come from the 2009 report "http://astropedia.astrogeology.usgs.gov/alfresco/d/d/
        workspace/SpacesStore/28fd9e81-1964-44d6-a58b-fbbf61e64e15/WGCCRE2009reprint.pdf" and the 2011 erratum
        "http://astropedia.astrogeology.usgs.gov/alfresco/d/d/workspace/SpacesStore/
        04d348b0-eb2b-46a2-abe9-6effacb37763/WGCCRE-Erratum-2011reprint.pdf" of the IAU/IAG Working Group on Cartographic
        Coordinates and Rotational Elements of the Planets and Satellites (WGCCRE). Note that these value differ from earliest
        reports (before 2005).
    
        By default, IAU pole data for planetary bodies (including Sun and Moon) are available in PATRIUS through use of method
        :meth:`~fr.cnes.sirius.patrius.bodies.IAUPoleFactory.getIAUPole`. Data come from the IAU 2009 working group Technical
        Note (see above).
    
        IAUPoleFactory does not allow user-defined data.
    
        Since:
            5.1
    """
    @staticmethod
    def getIAUPole(predefinedEphemerisType: 'PredefinedEphemerisType') -> 'CelestialBodyIAUOrientation':
        """
            Get an IAU pole.
        
            Parameters:
                body (:class:`~fr.cnes.sirius.patrius.bodies.PredefinedEphemerisType`): body for which the pole is requested
        
            Returns:
                IAU pole for the body, or dummy EME2000 aligned pole for barycenters
        
        
        """
        ...

class IAUPoleFunction(java.io.Serializable):
    """
    public class IAUPoleFunction extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        IAU pole function: this class is used to define an atomic element of IAU pole computation.
    
        Since:
            4.9
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, iAUPoleFunctionType: 'IAUPoleFunctionType', univariateDifferentiableFunction: fr.cnes.sirius.patrius.math.analysis.differentiation.UnivariateDifferentiableFunction, iAUTimeDependency: 'IAUPoleFunction.IAUTimeDependency'): ...
    def getFunction(self) -> fr.cnes.sirius.patrius.math.analysis.differentiation.UnivariateDifferentiableFunction:
        """
            Returns the IAU pole function.
        
            Returns:
                the IAU pole function
        
        
        """
        ...
    def getTimeDependency(self) -> 'IAUPoleFunction.IAUTimeDependency':
        """
            Returns the IAU time dependency (days or centuries).
        
            Returns:
                the IAU time dependency (days or centuries)
        
        
        """
        ...
    def getType(self) -> 'IAUPoleFunctionType':
        """
            Returns the IAU pole type.
        
            Returns:
                the IAU pole type
        
        
        """
        ...
    class IAUTimeDependency(java.lang.Enum['IAUPoleFunction.IAUTimeDependency']):
        DAYS: typing.ClassVar['IAUPoleFunction.IAUTimeDependency'] = ...
        CENTURIES: typing.ClassVar['IAUPoleFunction.IAUTimeDependency'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'IAUPoleFunction.IAUTimeDependency': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['IAUPoleFunction.IAUTimeDependency']: ...

class IAUPoleFunctionType(java.lang.Enum['IAUPoleFunctionType']):
    """
    public enum IAUPoleFunctionType extends `Enum <http://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.bodies.IAUPoleFunctionType`>
    
        IAU pole type: this enumeration lists all possible IAU pole effects (constant, secular, harmonics) used to convert from
        ICRF body centered frame to true equator/rotating body centered frame. This class is used for defining effects alone.
        They cannot however be used alone for transformation computation. For transformation computation, effects are used
        cumulatively through :class:`~fr.cnes.sirius.patrius.bodies.IAUPoleModelType` class.
    """
    CONSTANT: typing.ClassVar['IAUPoleFunctionType'] = ...
    SECULAR: typing.ClassVar['IAUPoleFunctionType'] = ...
    HARMONICS: typing.ClassVar['IAUPoleFunctionType'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'IAUPoleFunctionType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.MutableSequence['IAUPoleFunctionType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (IAUPoleFunctionType c : IAUPoleFunctionType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class IAUPoleModelType(java.lang.Enum['IAUPoleModelType']):
    """
    public enum IAUPoleModelType extends `Enum <http://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.bodies.IAUPoleModelType`>
    
        IAU pole type: this enumeration lists all possible IAU pole effects (constant, secular, harmonics) used to convert from
        ICRF body centered frame to true equator/rotating body centered frame. Note that when used in
        :class:`~fr.cnes.sirius.patrius.bodies.UserIAUPole`, effects are cumulative. One cannot only get the harmonic effects
        alone for instance.
    """
    CONSTANT: typing.ClassVar['IAUPoleModelType'] = ...
    MEAN: typing.ClassVar['IAUPoleModelType'] = ...
    TRUE: typing.ClassVar['IAUPoleModelType'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'IAUPoleModelType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.MutableSequence['IAUPoleModelType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (IAUPoleModelType c : IAUPoleModelType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class LLHCoordinates(java.io.Serializable):
    """
    public class LLHCoordinates extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        This class aims at gathering in one single object the three coordinates latitude, longitude and height, and the
        associated coordinates system in which they are expressed. The user can define a name for the coordinates by using the
        dedicated constructeur :meth:`~fr.cnes.sirius.patrius.bodies.LLHCoordinates.LLHCoordinates`, otherwise the default value
        for the corresponding attribute is an empty String.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, lLHCoordinatesSystem: 'LLHCoordinatesSystem', double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, lLHCoordinatesSystem: 'LLHCoordinatesSystem', double: float, double2: float, double3: float, string: str): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getHeight(self) -> float:
        """
            Getter for the height in meters with respect to the shape surface. Following the convention, it can be the distance to
            shape (if normal height) or the radial height (if radial height). This is a signed value.
        
            If the used height system is NORMAL, a positive value means the point is outside the shape, a negative value means the
            point is inside the shape.
        
            Returns:
                the height in meters
        
        
        """
        ...
    def getLLHCoordinatesSystem(self) -> 'LLHCoordinatesSystem':
        """
            Getter for the used LLH coordinates system.
        
            Returns:
                the coordinates system
        
        
        """
        ...
    def getLatitude(self) -> float:
        """
            Getter for the latitude.
        
            Returns:
                the latitude
        
        
        """
        ...
    def getLongitude(self) -> float:
        """
            Getter for the longitude.
        
            Returns:
                the longitude
        
        
        """
        ...
    def getName(self) -> str:
        """
            Getter for the name of the coordinates. It returns an empty String if the user created object without using constructor
            with name option.
        
            Returns:
                the name of the coordinates.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class LLHCoordinatesSystem(java.lang.Enum['LLHCoordinatesSystem']):
    """
    public enum LLHCoordinatesSystem extends `Enum <http://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.bodies.LLHCoordinatesSystem`>
    
        This enumerate define the handled LLH (Latitude/Longitude/Height) coordinates systems.
    
    
        Each coordinates system is defined by:
    
          - A lat/long coordinates system
          - An height coordinate system
    """
    ELLIPSODETIC: typing.ClassVar['LLHCoordinatesSystem'] = ...
    BODYCENTRIC_RADIAL: typing.ClassVar['LLHCoordinatesSystem'] = ...
    BODYCENTRIC_NORMAL: typing.ClassVar['LLHCoordinatesSystem'] = ...
    def computeLLHRates(self, bodyShape: BodyShape, pVCoordinates: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> typing.MutableSequence[float]: ...
    def getHeightSystemLabel(self) -> str:
        """
            Getter for the label for the managed height coordinate system.
        
            Returns:
                the label for the managed height coordinate system
        
        
        """
        ...
    def getLatLongSystemLabel(self) -> str:
        """
            Getter for the label for the managed lat/long coordinates system.
        
            Returns:
                the label for the managed lat/long coordinates system
        
        
        """
        ...
    def jacobianFromCartesian(self, bodyPoint: BodyPoint) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    def jacobianToCartesian(self, bodyPoint: BodyPoint) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Compute the jacobian from the LLHCoordinate system to the cartesian system.
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.bodies.BodyPoint`): The pivot point for the jacobian computation
        
            Returns:
                the jacobian with the following columns: latitude, longitude, height
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LLHCoordinatesSystem':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.MutableSequence['LLHCoordinatesSystem']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (LLHCoordinatesSystem c : LLHCoordinatesSystem.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class PosVelChebyshev(fr.cnes.sirius.patrius.time.TimeStamped, java.io.Serializable):
    """
    public class PosVelChebyshev extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.time.TimeStamped`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Position-Velocity-Acceleration model based on Chebyshev polynomials.
    
        This class represent the most basic element of the piecewise ephemerides for solar system bodies like JPL DE 405
        ephemerides.
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.bodies.JPLCelestialBodyLoader`, :meth:`~serialized`
    """
    def __init__(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[float], jpype.JArray]): ...
    def getDate(self) -> fr.cnes.sirius.patrius.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.time.TimeStamped.getDate` in interface :class:`~fr.cnes.sirius.patrius.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getPositionVelocity(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates:
        """
            Get the position-velocity-acceleration at a specified date.
        
            Parameters:
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): date at which position-velocity-acceleration is requested
        
            Returns:
                position-velocity-acceleration at specified date
        
        
        """
        ...
    def getValidityDuration(self) -> float:
        """
            Get model validity duration.
        
            Returns:
                model validity duration in seconds
        
        
        """
        ...
    def inRange(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> bool:
        """
            Check if a date is in validity range.
        
            Parameters:
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): date to check
        
            Returns:
                true if date is in validity range
        
        
        """
        ...
    def isSuccessorOf(self, posVelChebyshev: 'PosVelChebyshev') -> bool:
        """
            Check if the instance is the exact successor of another model.
        
            The instance is the successor of another model if its start date is within a 1ms tolerance interval of the end date of
            the other model.
        
            Parameters:
                predecessor (:class:`~fr.cnes.sirius.patrius.bodies.PosVelChebyshev`): model to check instance against
        
            Returns:
                true if the instance is the successor of the predecessor model
        
        
        """
        ...

class PredefinedEphemerisType(java.lang.Enum['PredefinedEphemerisType']):
    """
    public enum PredefinedEphemerisType extends `Enum <http://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.bodies.PredefinedEphemerisType`>
    
        List of predefined ephemerides types (for use in JPL loaders classes).
    
        Since:
            4.10
    """
    SOLAR_SYSTEM_BARYCENTER: typing.ClassVar['PredefinedEphemerisType'] = ...
    SUN: typing.ClassVar['PredefinedEphemerisType'] = ...
    MERCURY: typing.ClassVar['PredefinedEphemerisType'] = ...
    VENUS: typing.ClassVar['PredefinedEphemerisType'] = ...
    EARTH_MOON: typing.ClassVar['PredefinedEphemerisType'] = ...
    EARTH: typing.ClassVar['PredefinedEphemerisType'] = ...
    MOON: typing.ClassVar['PredefinedEphemerisType'] = ...
    MARS: typing.ClassVar['PredefinedEphemerisType'] = ...
    MARS_BARY: typing.ClassVar['PredefinedEphemerisType'] = ...
    JUPITER: typing.ClassVar['PredefinedEphemerisType'] = ...
    JUPITER_BARY: typing.ClassVar['PredefinedEphemerisType'] = ...
    SATURN: typing.ClassVar['PredefinedEphemerisType'] = ...
    SATURN_BARY: typing.ClassVar['PredefinedEphemerisType'] = ...
    URANUS: typing.ClassVar['PredefinedEphemerisType'] = ...
    URANUS_BARY: typing.ClassVar['PredefinedEphemerisType'] = ...
    NEPTUNE: typing.ClassVar['PredefinedEphemerisType'] = ...
    NEPTUNE_BARY: typing.ClassVar['PredefinedEphemerisType'] = ...
    PLUTO: typing.ClassVar['PredefinedEphemerisType'] = ...
    PLUTO_BARY: typing.ClassVar['PredefinedEphemerisType'] = ...
    @staticmethod
    def getEphemerisType(string: str) -> 'PredefinedEphemerisType':
        """
            Get ephemeris type from JPL/PATRIUS name.
        
            Parameters:
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): a name
        
            Returns:
                ephemeris type from JPL/PATRIUS name, null if unknown
        
        
        """
        ...
    def getName(self) -> str:
        """
            Returns the JPL/PATRIUS name.
        
            Returns:
                the JPL/PATRIUS name
        
        
        """
        ...
    def isBarycenter(self) -> bool:
        """
        
            Returns:
                true if the PredefinedEphemerisType is a barycenter.
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PredefinedEphemerisType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.MutableSequence['PredefinedEphemerisType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (PredefinedEphemerisType c : PredefinedEphemerisType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AbstractBodyPoint(BodyPoint):
    def getBodyShape(self) -> BodyShape: ...
    def getClosestPointOnShape(self) -> BodyPoint: ...
    @typing.overload
    def getLLHCoordinates(self) -> LLHCoordinates: ...
    @typing.overload
    def getLLHCoordinates(self, lLHCoordinatesSystem: LLHCoordinatesSystem) -> LLHCoordinates: ...
    def getName(self) -> str: ...
    @typing.overload
    def getNormal(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, frame: fr.cnes.sirius.patrius.frames.Frame) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getNormal(self) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D: ...
    def getNormalHeight(self) -> float: ...
    def getPosition(self) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D: ...
    def getRadialProjectionOnShape(self) -> BodyPoint: ...
    @typing.overload
    def toString(self) -> str: ...
    @typing.overload
    def toString(self, lLHCoordinatesSystem: LLHCoordinatesSystem) -> str: ...

class AbstractBodyShape(BodyShape):
    """
    public abstract class AbstractBodyShape extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
    
        Abstract class for a body shape to mutualize parameters and features.
    
        Since:
            4.12
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`, :meth:`~serialized`
    """
    DEFAULT_EPSILON_SIGNAL_PROPAGATION: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_EPSILON_SIGNAL_PROPAGATION
    
        Default epsilon (s) for signal propagation computation.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, string: str, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame): ...
    def getBodyFrame(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame:
        """
            Getter for the body frame related to body shape.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.getBodyFrame` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Returns:
                the body frame related to body shape
        
        
        """
        ...
    def getDistanceEpsilon(self) -> float:
        """
            Return the distance epsilon below which the height coordinate is neglected. This epsilon value can be modified using
            dedicated setter.
        
              - Below this distance epsilon, the method :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.getIntersectionPoint` will be
                automatically used instead of :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.getIntersectionPoint`,
              - The method :meth:`~fr.cnes.sirius.patrius.bodies.BodyPoint.isOnShapeSurface` will return true if the absolute value of
                its normal height is lower than this distance epsilon.
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.getDistanceEpsilon` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Returns:
                the altitude epsilon
        
        
        """
        ...
    def getEpsilonSignalPropagation(self) -> float:
        """
            Getter for the epsilon for signal propagation used in :code:`#getApparentRadius(PVCoordinatesProvider, AbsoluteDate,
            PVCoordinatesProvider, PropagationDelayType)` method. This epsilon (in s) directly reflect the accuracy of signal
            propagation (1s of accuracy = 3E8m of accuracy on distance between emitter and receiver).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.getEpsilonSignalPropagation` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Returns:
                the epsilon for signal propagation
        
        
        """
        ...
    def getLLHCoordinatesSystem(self) -> LLHCoordinatesSystem:
        """
            Getter for the LLH coordinates system used by the computed :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.getLLHCoordinatesSystem` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Returns:
                the coordinates system
        
        
        """
        ...
    def getName(self) -> str:
        """
            Getter for the name of the shape.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.getName` in interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Returns:
                the name of the shape
        
        
        """
        ...
    def getNativeFrame(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.frames.Frame:
        """
            Get the native frame, i.e. the raw frame in which PVCoordinates are expressed before transformation to user output
            frame.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider.getNativeFrame` in
                interface :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
        
            Parameters:
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): a date
        
            Returns:
                the native frame
        
        
        """
        ...
    def getPVCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, frame: fr.cnes.sirius.patrius.frames.Frame) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates: ...
    def setDistanceEpsilon(self, double: float) -> None:
        """
            Setter for the distance epsilon below which the height coordinate is neglected.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.setDistanceEpsilon` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Parameters:
                epsilon (double): distance epsilon to be set
        
        
        """
        ...
    def setEpsilonSignalPropagation(self, double: float) -> None:
        """
            Setter for the epsilon for signal propagation used in :code:`#getApparentRadius(PVCoordinatesProvider, AbsoluteDate,
            PVCoordinatesProvider, PropagationDelayType)` method. This epsilon (in s) directly reflect the accuracy of signal
            propagation (1s of accuracy = 3E8m of accuracy on distance between emitter and receiver).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.setEpsilonSignalPropagation` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Parameters:
                epsilon (double): epsilon for signal propagation
        
        
        """
        ...
    def setLLHCoordinatesSystem(self, lLHCoordinatesSystem: LLHCoordinatesSystem) -> None:
        """
            Setter for the LLH coordinates system to be used by the computed :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.setLLHCoordinatesSystem` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Parameters:
                coordSystem (:class:`~fr.cnes.sirius.patrius.bodies.LLHCoordinatesSystem`): LLH coordinates system to be set
        
        
        """
        ...

class AbstractCelestialPoint(CelestialPoint):
    """
    public abstract class AbstractCelestialPoint extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
    
        Abstract implementation of the :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint` interface.
    
        This abstract implementation provides basic services that can be shared by most implementations of the
        :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint` interface. It holds the gravitational attraction coefficient and
        build some body-centered frames automatically (ICRF, EME2000, etc.).
    
        Since:
            4.13
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str, double: float, celestialBodyEphemeris: CelestialBodyEphemeris, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame): ...
    @typing.overload
    def __init__(self, string: str, double: float, celestialBodyEphemeris: CelestialBodyEphemeris, frame: fr.cnes.sirius.patrius.frames.Frame, spiceJ2000ConventionEnum: fr.cnes.sirius.patrius.bodies.bsp.BSPEphemerisLoader.SpiceJ2000ConventionEnum): ...
    @typing.overload
    def __init__(self, string: str, double: float, frame: fr.cnes.sirius.patrius.frames.Frame, celestialBodyEphemeris: CelestialBodyEphemeris): ...
    def getEME2000(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame:
        """
            Get an EME2000, celestial point centered frame.
        
            The frame is always bound to the celestial point center, and its axes are colinear to Earth EME2000 frame.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.getEME2000` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Returns:
                an EME2000, celestial point centered frame
        
        
        """
        ...
    def getEclipticJ2000(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame:
        """
            Get an Ecliptic J200, celestial point centered frame.
        
            The frame is always bound to the celestial point center with constant rotation relative to the ICRF.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.getEclipticJ2000` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Returns:
                an EclipticJ200, celestial point centered frame
        
        
        """
        ...
    def getEphemeris(self) -> CelestialBodyEphemeris:
        """
            Get the ephemeris of the celestial point.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.getEphemeris` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Returns:
                the ephemeris
        
        
        """
        ...
    def getGM(self) -> float:
        """
            Get the central attraction coefficient of the celestial point.
        
            Warning: attraction model should not be null (it is not null by default).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.getGM` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Returns:
                central attraction coefficient of the celestial point (m :sup:`3` /s :sup:`2` )
        
        
        """
        ...
    def getICRF(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame:
        """
            Get an ICRF, celestial point centered frame.
        
            The frame is always bound to the celestial point, and its axes have a fixed orientation with respect to other inertial
            frames.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.getICRF` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Returns:
                an inertially oriented, celestial point centered frame
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.getRotatingFrame`
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the celestial point.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.getName` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Returns:
                name of the celestial point
        
        
        """
        ...
    def getNativeFrame(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.frames.Frame: ...
    def getPVCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, frame: fr.cnes.sirius.patrius.frames.Frame) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates: ...
    def setEphemeris(self, celestialBodyEphemeris: CelestialBodyEphemeris) -> None:
        """
            Set an ephemeris to the celestial point.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.setEphemeris` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Parameters:
                ephemerisIn (:class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyEphemeris`): the ephemeris
        
        
        """
        ...
    def setGM(self, double: float) -> None:
        """
            Set a central attraction coefficient to the celestial point.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.setGM` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Parameters:
                gmIn (double): the central attraction coefficient (m :sup:`3` /s :sup:`2` )
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns a string representation of the celestial point and its attributes.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.toString` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of the celestial point and its attributes
        
        
        """
        ...

class AbstractJPLCelestialBodyLoader(CelestialBodyLoader):
    """
    public abstract class AbstractJPLCelestialBodyLoader extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyLoader`
    
        Abstract class for all JPL celestial body loaders.
    
        Since:
            4.11.1
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, jPLEphemerisLoader: 'JPLEphemerisLoader'): ...
    def getEphemerisLoader(self) -> 'JPLEphemerisLoader':
        """
            Returns the ephemeris loader.
        
            Returns:
                the ephemeris loader
        
        
        """
        ...
    def getLoadedGravitationalCoefficient(self, predefinedEphemerisType: PredefinedEphemerisType) -> float: ...
    def getSupportedNames(self) -> str:
        """
            Returns the supported file names.
        
            Returns:
                the supported file names
        
        
        """
        ...

class CelestialBody(CelestialPoint):
    """
    public interface CelestialBody extends :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
    
        Interface for celestial bodies like Sun, Moon or solar system planets.
    
        Celestial Barycenters are handled by class :class:`~fr.cnes.sirius.patrius.bodies.BasicCelestialPoint`.
    
        Since:
            4.13
    """
    def getBodyNature(self) -> CelestialPoint.BodyNature:
        """
            Getter for the celestial body nature.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.getBodyNature` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Returns:
                the celestial body nature
        
        
        """
        ...
    def getGravityModel(self) -> fr.cnes.sirius.patrius.forces.gravity.GravityModel:
        """
            Getter for the gravitational attraction model of the body.
        
            Returns:
                the gravitational attraction model
        
        
        """
        ...
    def getInertialFrame(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    def getName(self) -> str:
        """
            Getter for the name of the body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.getName` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Returns:
                name of the body
        
        
        """
        ...
    def getOrientation(self) -> CelestialBodyOrientation:
        """
            Getter for the celestial body orientation and primer meridians orientation.
        
            Returns:
                the celestial body orientation
        
        
        """
        ...
    def getRotatingFrame(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    def getShape(self) -> BodyShape:
        """
            Getter for the geometric shape of the body.
        
            Returns:
                geometric shape of the body
        
        
        """
        ...
    def setGravityModel(self, gravityModel: fr.cnes.sirius.patrius.forces.gravity.GravityModel) -> None:
        """
            Setter for a gravitational attraction model to the body.
        
            Parameters:
                gravityModelIn (:class:`~fr.cnes.sirius.patrius.forces.gravity.GravityModel`): the gravitational attraction model
        
        
        """
        ...
    def setOrientation(self, celestialBodyOrientation: CelestialBodyOrientation) -> None:
        """
            Setter for a celestial body orientation to define the body frames.
        
            Parameters:
                celestialBodyOrientation (:class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation`): the celestial body orientation
        
        
        """
        ...
    def setShape(self, bodyShape: BodyShape) -> None:
        """
            Setter for a geometric shape to the body.
        
            Parameters:
                shapeIn (:class:`~fr.cnes.sirius.patrius.bodies.BodyShape`): the shape of the body
        
        
        """
        ...
    def toString(self) -> str: ...

class CelestialBodyIAUOrientation(CelestialBodyOrientation):
    """
    public interface CelestialBodyIAUOrientation extends :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation`
    
        Interface for IAU pole and primer meridian orientations.
    
        This interface defines methods compliant with the report of the IAU/IAG Working Group on Cartographic Coordinates and
        Rotational Elements of the Planets and Satellites (WGCCRE). These definitions are common for all recent versions of this
        report published every three years.
    
        The precise values of pole direction and W angle coefficients may vary from publication year as models are adjusted. The
        latest value of constants for implementing this interface can be found in the `working group site
        <http://astrogeology.usgs.gov/Projects/WGCCRE/>`.
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyFactory`
    """
    @typing.overload
    def getAngularCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, orientationType: CelestialBodyOrientation.OrientationType, iAUPoleModelType: IAUPoleModelType) -> fr.cnes.sirius.patrius.utils.AngularCoordinates: ...
    @typing.overload
    def getAngularCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, orientationType: CelestialBodyOrientation.OrientationType) -> fr.cnes.sirius.patrius.utils.AngularCoordinates: ...
    @typing.overload
    def getAngularCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, iAUPoleModelType: IAUPoleModelType) -> fr.cnes.sirius.patrius.utils.AngularCoordinates: ...
    @typing.overload
    def getAngularCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.utils.AngularCoordinates: ...
    @typing.overload
    def getPole(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, iAUPoleModelType: IAUPoleModelType) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D:
        """
            Getter for the body North pole direction with respect to a reference frame.
        
            Parameters:
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): Current date
                iauPoleType (:class:`~fr.cnes.sirius.patrius.bodies.IAUPoleModelType`): IAUPole data to take into account for ICRF/inertial/mean equator/true equator transformation
        
            Returns:
                the body North pole direction with respect to a reference frame
        
        
        """
        ...
    @typing.overload
    def getPole(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getPoleDerivative(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, iAUPoleModelType: IAUPoleModelType) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D:
        """
            Getter for the body North pole direction derivative with respect to a reference frame.
        
        
            It takes into account constant, secular and harmonics terms (conversion from ICRF to true equator).
        
            Parameters:
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): Current date
                iauPoleType (:class:`~fr.cnes.sirius.patrius.bodies.IAUPoleModelType`): IAUPole data to take into account for ICRF/inertial/mean equator/true equator transformation
        
            Returns:
                the body North pole direction derivative with respect to a reference frame
        
        
        """
        ...
    @typing.overload
    def getPoleDerivative(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getPrimeMeridianAngle(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, iAUPoleModelType: IAUPoleModelType) -> float:
        """
            Getter for the prime meridian angle.
        
            The prime meridian angle is the angle between the Q node and the prime meridian. Represents the body rotation.
        
            Parameters:
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): Current date
                iauPoleType (:class:`~fr.cnes.sirius.patrius.bodies.IAUPoleModelType`): IAUPole data to take into account for ICRF/inertial/mean rotating/true rotating transformation
        
            Returns:
                the prime meridian vector
        
        
        """
        ...
    @typing.overload
    def getPrimeMeridianAngle(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> float: ...
    @typing.overload
    def getPrimeMeridianAngleDerivative(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, iAUPoleModelType: IAUPoleModelType) -> float:
        """
            Getter for the prime meridian angle derivative.
        
            The prime meridian angle is the angle between the Q node and the prime meridian. Represents the body rotation.
        
            Parameters:
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): Current date
                iauPoleType (:class:`~fr.cnes.sirius.patrius.bodies.IAUPoleModelType`): IAUPole data to take into account for ICRF/inertial/mean rotating/true rotating transformation
        
            Returns:
                the prime meridian angle derivative
        
        
        """
        ...
    @typing.overload
    def getPrimeMeridianAngleDerivative(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> float: ...
    def toString(self) -> str: ...

class CelestialBodyTabulatedOrientation(CelestialBodyOrientation):
    """
    public class CelestialBodyTabulatedOrientation extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation`
    
        Celestial body orientation represented by a tabulated attitude leg (quaternions).
    
        Since:
            4.13
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, tabulatedAttitude: fr.cnes.sirius.patrius.attitudes.TabulatedAttitude): ...
    @typing.overload
    def getAngularCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.utils.AngularCoordinates: ...
    @typing.overload
    def getAngularCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, orientationType: CelestialBodyOrientation.OrientationType) -> fr.cnes.sirius.patrius.utils.AngularCoordinates: ...
    def getDH(self) -> float:
        """
            Getter for the finite difference delta value.
        
            This value is used to compute the body pole directions by finite difference (see
            :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyTabulatedOrientation.getPole` and
            :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyTabulatedOrientation.getPoleDerivative`.
        
            Note that the body pole directions can only be computed on the interval:
        
        
            :code:`[tabulated attitude's lower date + 2 * dH ; tabulated attitude's upper date - 2 * dH]`.
        
            Returns:
                the finite difference delta value
        
        
        """
        ...
    @typing.overload
    def getOrientation(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.utils.TimeStampedAngularCoordinates: ...
    @typing.overload
    def getOrientation(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, frame: fr.cnes.sirius.patrius.frames.Frame) -> fr.cnes.sirius.patrius.utils.TimeStampedAngularCoordinates: ...
    def getPole(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D: ...
    def getPoleDerivative(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D: ...
    def getPrimeMeridianAngle(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> float: ...
    def getPrimeMeridianAngleDerivative(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> float: ...
    def getTabulatedAttitude(self) -> fr.cnes.sirius.patrius.attitudes.TabulatedAttitude:
        """
            Getter for the tabulated attitude leg representing the celestial body orientation.
        
            Returns:
                the tabulated attitude leg
        
        
        """
        ...
    def setDH(self, double: float) -> None:
        """
            Setter for the finite difference delta value.
        
            This value is used to compute the body pole directions by finite difference (see
            :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyTabulatedOrientation.getPole` and
            :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyTabulatedOrientation.getPoleDerivative`.
        
            Note that the body pole directions can only be computed on the interval:
        
        
            :code:`[tabulated attitude's lower date + 2 * dH ; tabulated attitude's upper date - 2 * dH]`.
        
            Parameters:
                dHIn (double): the finite difference delta value to set (0.5s by default)
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NotStrictlyPositiveException`: if :code:`dH < Precision.DOUBLE_COMPARISON_EPSILON`
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns a string representation of the body orientation.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation.toString` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation`
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of the body orientation
        
        
        """
        ...

class ConstantRadiusProvider(ApparentRadiusProvider):
    """
    public class ConstantRadiusProvider extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.bodies.ApparentRadiusProvider`
    
        Implementation for constant radius provider.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, double: float): ...
    def getApparentRadius(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, propagationDelayType: fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.PropagationDelayType) -> float:
        """
            Compute the apparent radius (in meters) of the occulting body from the spacecraft (observer) position. Given a plane
            containing the spacecraft (observer) position, the center of the occulting body and the center of the occulted body, and
            given a line contained within this plane, passing by the spacecraft (observer) position and tangent to the mesh of the
            occulting body, the apparent radius corresponds to the length of the line starting from the center of the occulting
            body, perpendicular to the first given line and ending at the intersection of the two lines.
        
            Please notice that this method will for the moment be used only with an instantaneous propagation delay type.
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.ApparentRadiusProvider.getApparentRadius` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.ApparentRadiusProvider`
        
            Parameters:
                pvObserver (:class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`): the spacecraft (observer) position-velocity
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): the date at which the signal is received by the observer (reception date)
                occultedBody (:class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`): the body which is occulted to the spacecraft (observer) by the occulting body
                propagationDelayType (:class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.PropagationDelayType`): propagation delay type
        
            Returns:
                the apparent radius (in meters) of the occulting body from the spacecraft (observer) position
        
        
        """
        ...

class EarthEphemeris(CelestialBodyEphemeris):
    """
    public class EarthEphemeris extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyEphemeris`
    
        Earth ephemeris.
    
        Since:
            4.11
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def getNativeFrame(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.frames.Frame:
        """
            Get the native frame, i.e. the raw frame in which PVCoordinates are expressed before transformation to user output
            frame.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider.getNativeFrame` in
                interface :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`
        
            Parameters:
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): a date
        
            Returns:
                the native frame
        
        
        """
        ...
    def getPVCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, frame: fr.cnes.sirius.patrius.frames.Frame) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates: ...

class JPLEphemerisLoader(CelestialBodyEphemerisLoader):
    """
    public interface JPLEphemerisLoader extends :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyEphemerisLoader`
    
        Interface for JPL ephemeris loaders.
    
        Since:
            4.11
    """
    def getLoadedGravitationalCoefficient(self, predefinedEphemerisType: PredefinedEphemerisType) -> float: ...

class StarConvexBodyShape(BodyShape):
    """
    public interface StarConvexBodyShape extends :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
    
    
        Extended interface for star-convex bodies shapes : extends the :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        interface by adding a method to get a :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` of the shape from given
        latitude,longitude and altitude.
    
        Since:
            4.11
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
    """
    ...

class UserCelestialBodyLoader(CelestialBodyLoader):
    """
    public class UserCelestialBodyLoader extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyLoader`
    
        Loader for :class:`~fr.cnes.sirius.patrius.bodies.UserCelestialBody` or
        :class:`~fr.cnes.sirius.patrius.bodies.BasicCelestialPoint`.
    
        This loader is to be used in conjunction with :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyFactory`.
    
        Since:
            4.13
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, celestialBodyOrientation: CelestialBodyOrientation, frame: fr.cnes.sirius.patrius.frames.Frame, bodyShape: BodyShape): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, celestialBodyOrientation: CelestialBodyOrientation, frame: fr.cnes.sirius.patrius.frames.Frame, bodyShape: BodyShape, spiceJ2000ConventionEnum: fr.cnes.sirius.patrius.bodies.bsp.BSPEphemerisLoader.SpiceJ2000ConventionEnum): ...
    def getName(self, string: str) -> str:
        """
            Returns name of body as known by the loader corresponding to PATRIUS body name.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyLoader.getName` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyLoader`
        
            Parameters:
                patriusName (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): PATRIUS body name
        
            Returns:
                name of body as known by the loader corresponding to PATRIUS body name
        
        
        """
        ...
    def loadCelestialBody(self, string: str) -> CelestialBody:
        """
            Load celestial body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyLoader.loadCelestialBody` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyLoader`
        
            Parameters:
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): name of the celestial body
        
            Returns:
                loaded celestial body
        
        
        """
        ...
    def loadCelestialPoint(self, string: str) -> CelestialPoint: ...

class VariableRadiusProvider(ApparentRadiusProvider):
    """
    public class VariableRadiusProvider extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.bodies.ApparentRadiusProvider`
    
        Implementation for variable radius providers.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, bodyShape: BodyShape): ...
    def getApparentRadius(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, propagationDelayType: fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.PropagationDelayType) -> float:
        """
            Compute the apparent radius (in meters) of the occulting body from the spacecraft (observer) position. Given a plane
            containing the spacecraft (observer) position, the center of the occulting body and the center of the occulted body, and
            given a line contained within this plane, passing by the spacecraft (observer) position and tangent to the mesh of the
            occulting body, the apparent radius corresponds to the length of the line starting from the center of the occulting
            body, perpendicular to the first given line and ending at the intersection of the two lines.
        
            Please notice that this method will for the moment be used only with an instantaneous propagation delay type.
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.ApparentRadiusProvider.getApparentRadius` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.ApparentRadiusProvider`
        
            Parameters:
                pvObserver (:class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`): the spacecraft (observer) position-velocity
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): the date at which the signal is received by the observer (reception date)
                occultedBody (:class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider`): the body which is occulted to the spacecraft (observer) by the occulting body
                propagationDelayType (:class:`~fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.PropagationDelayType`): propagation delay type
        
            Returns:
                the apparent radius (in meters) of the occulting body from the spacecraft (observer) position
        
        
        """
        ...
    def getBodyShape(self) -> BodyShape:
        """
            Getter for boy shape.
        
            Returns:
                body shape
        
        
        """
        ...

class AbstractCelestialBody(AbstractCelestialPoint, CelestialBody):
    """
    public abstract class AbstractCelestialBody extends :class:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialPoint` implements :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
    
        Abstract implementation of the :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody` interface.
    
        This abstract implementation provides basic services that can be shared by most implementations of the
        :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody` interface. It holds the gravitational attraction coefficient and
        build the body-centered frames.
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation`, :meth:`~serialized`
    """
    INERTIAL_FRAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` INERTIAL_FRAME
    
        Inertial, body-centered frame name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ROTATING_FRAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` ROTATING_FRAME
    
        Body-centered frame name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SPACE: typing.ClassVar[str] = ...
    """
    public static final char SPACE
    
        Space.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getGM(self) -> float:
        """
            Get the central attraction coefficient of the celestial point.
        
            Warning: attraction model should not be null (it is not null by default).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.getGM` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialPoint.getGM` in
                class :class:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialPoint`
        
            Returns:
                central attraction coefficient of the celestial point (m :sup:`3` /s :sup:`2` )
        
        
        """
        ...
    def getGravityModel(self) -> fr.cnes.sirius.patrius.forces.gravity.GravityModel:
        """
            Getter for the gravitational attraction model of the body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.getGravityModel` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
            Returns:
                the gravitational attraction model
        
        
        """
        ...
    def getInertialFrame(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    def getOrientation(self) -> CelestialBodyOrientation:
        """
            Getter for the celestial body orientation and primer meridians orientation.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.getOrientation` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
            Returns:
                the celestial body orientation
        
        
        """
        ...
    def getRotatingFrame(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    def getShape(self) -> BodyShape:
        """
            Getter for the geometric shape of the body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.getShape` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
            Returns:
                geometric shape of the body
        
        
        """
        ...
    def setGM(self, double: float) -> None:
        """
            Set a central attraction coefficient to the celestial point.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.setGM` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialPoint.setGM` in
                class :class:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialPoint`
        
            Parameters:
                gmIn (double): the central attraction coefficient (m :sup:`3` /s :sup:`2` )
        
        
        """
        ...
    def setGravityModel(self, gravityModel: fr.cnes.sirius.patrius.forces.gravity.GravityModel) -> None:
        """
            Setter for a gravitational attraction model to the body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.setGravityModel` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
            Parameters:
                modelIn (:class:`~fr.cnes.sirius.patrius.forces.gravity.GravityModel`): the gravitational attraction model
        
        
        """
        ...
    def setOrientation(self, celestialBodyOrientation: CelestialBodyOrientation) -> None:
        """
            Setter for a celestial body orientation to define the body frames.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.setOrientation` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
            Parameters:
                celestialBodyOrientationIn (:class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation`): the celestial body orientation
        
        
        """
        ...
    def setShape(self, bodyShape: BodyShape) -> None:
        """
            Setter for a geometric shape to the body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.setShape` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
            Parameters:
                shapeIn (:class:`~fr.cnes.sirius.patrius.bodies.BodyShape`): the shape of the body
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns a string representation of the celestial point and its attributes.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.toString` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialPoint.toString` in
                class :class:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialPoint`
        
            Returns:
                a string representation of the celestial point and its attributes
        
        
        """
        ...

class BSPCelestialBodyLoader(AbstractJPLCelestialBodyLoader):
    """
    public class BSPCelestialBodyLoader extends :class:`~fr.cnes.sirius.patrius.bodies.AbstractJPLCelestialBodyLoader`
    
        Loader for JPL ephemerides binary files BSP type.
    
    
        It loads the whole :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`. For
        :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyEphemeris` loader only, see dedicated class.
    
        BSP ephemerides binary files contain ephemerides for any solar system body (depending on what is included in the file).
    
        Since:
            4.11.1
    
        Also see:
            :meth:`~serialized`
    """
    DEFAULT_BSP_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` DEFAULT_BSP_SUPPORTED_NAMES
    
        Default supported files name pattern for BSP files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EARTH_MOON: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` EARTH_MOON
    
        Predefined name for Earth-Moon barycenter in BSP files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, string: str): ...
    def declareAsCelestialPoint(self, string: str) -> None:
        """
            Declare a name of a body as a :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`.
        
        
            Object will be built as :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint` instead of
            :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`.
        
            Parameters:
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): a body name
        
        
        """
        ...
    def getName(self, string: str) -> str:
        """
            Returns name of body as known by the loader corresponding to PATRIUS body name.
        
            Parameters:
                patriusName (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): PATRIUS body name
        
            Returns:
                name of body as known by the loader corresponding to PATRIUS body name
        
        
        """
        ...
    def loadCelestialBody(self, string: str) -> CelestialBody: ...
    def loadCelestialPoint(self, string: str) -> CelestialPoint: ...
    @staticmethod
    def toSpiceName(string: str) -> str:
        """
            Convert a PATRIUS body name to a SPICE body name.
        
            Parameters:
                patriusName (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): PATRIUS body name
        
            Returns:
                SPICE body name
        
        
        """
        ...
    class SSBEphemeris(CelestialBodyEphemeris):
        def __init__(self): ...
        def getNativeFrame(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.frames.Frame: ...
        def getPVCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, frame: fr.cnes.sirius.patrius.frames.Frame) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates: ...

class BasicCelestialPoint(AbstractCelestialPoint):
    """
    public class BasicCelestialPoint extends :class:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialPoint`
    
        Basic celestial point. It can be used to define any celestial point with:
    
          - Its name
          - A :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider` or a
            :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyEphemeris` providing body position-velocity through time
    
    
        For user-defined Celestial bodies, use :class:`~fr.cnes.sirius.patrius.bodies.UserCelestialBody`
    
        Since:
            4.13
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame, string: str, double: float, celestialBodyEphemeris: CelestialBodyEphemeris): ...
    @typing.overload
    def __init__(self, string: str, double: float, celestialBodyEphemeris: CelestialBodyEphemeris, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame): ...
    @typing.overload
    def __init__(self, string: str, double: float, celestialBodyEphemeris: CelestialBodyEphemeris, frame: fr.cnes.sirius.patrius.frames.Frame, spiceJ2000ConventionEnum: fr.cnes.sirius.patrius.bodies.bsp.BSPEphemerisLoader.SpiceJ2000ConventionEnum): ...
    @typing.overload
    def __init__(self, string: str, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, frame: fr.cnes.sirius.patrius.frames.Frame): ...
    @typing.overload
    def __init__(self, string: str, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, frame: fr.cnes.sirius.patrius.frames.Frame, spiceJ2000ConventionEnum: fr.cnes.sirius.patrius.bodies.bsp.BSPEphemerisLoader.SpiceJ2000ConventionEnum): ...
    def toString(self) -> str:
        """
            Returns a string representation of the celestial point and its attributes.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.toString` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialPoint.toString` in
                class :class:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialPoint`
        
            Returns:
                a string representation of the celestial point and its attributes
        
        
        """
        ...

class EllipsoidBodyShape(StarConvexBodyShape):
    """
    public interface EllipsoidBodyShape extends :class:`~fr.cnes.sirius.patrius.bodies.StarConvexBodyShape`
    
        Extended interface for spheroid model to represent celestial bodies shape : extends the
        :class:`~fr.cnes.sirius.patrius.bodies.StarConvexBodyShape` interface by adding getters to access the spheroid
        parameters.
    
        Since:
            4.3
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.bodies.StarConvexBodyShape`
    """
    @typing.overload
    def buildPoint(self, lLHCoordinatesSystem: LLHCoordinatesSystem, double: float, double2: float, double3: float, string: str) -> 'EllipsoidPoint':
        """
            Build a :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` from LLH coordinates. Type of returned body point depends on
            body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.buildPoint` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Parameters:
                coordSystem (:class:`~fr.cnes.sirius.patrius.bodies.LLHCoordinatesSystem`): LLH coordinates system in which are expressed the entered lat/long/height
                latitude (double): input latitude
                longitude (double): input longitude
                height (double): input height
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): name of the point
        
            Returns:
                a body point
        
        
        """
        ...
    @typing.overload
    def buildPoint(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, string: str) -> 'EllipsoidPoint': ...
    @typing.overload
    def buildPoint(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, string: str) -> 'EllipsoidPoint':
        """
            Build a :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` from position in body frame. Type of returned body point
            depends on body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.buildPoint` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Parameters:
                position (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): position in body frame
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): name of the point
        
            Returns:
                :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` from position in body frame
        
        :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidPoint` buildPoint(:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` position, :class:`~fr.cnes.sirius.patrius.frames.Frame` frame, :class:`~fr.cnes.sirius.patrius.time.AbsoluteDate` date, `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` name) throws :class:`~fr.cnes.sirius.patrius.utils.exception.PatriusException`
        
            Build a :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` from position in provided frame at provided date. Type of
            returned body point depends on body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.buildPoint` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Parameters:
                position (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): position in provided frame at provided date
                frame (:class:`~fr.cnes.sirius.patrius.frames.Frame`): frame
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): date
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): name of the point
        
            Returns:
                :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` from position in provided frame at provided date
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.utils.exception.PatriusException`: if failed to build point
        
        """
        ...
    @typing.overload
    def closestPointTo(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D) -> 'EllipsoidPoint':
        """
            This method computes the two points, on the line and on the body, that are the closest to each other. The returned
            points are identical if the line intersects the shape: this point is the one with the lowest abscissa. The returned
            point with index 0 is the point on the Line, while the returned point with index 1 is the point on this.
        
            Note: calculations take the line's minimum abscissa into account.
        
            In this method we consider that the line's frame is the body frame, and the date is the
            :meth:`~fr.cnes.sirius.patrius.time.AbsoluteDate.J2000_EPOCH`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the original line for the shortest distance computation
        
            Returns:
                an array of length 2 containing the point of the line (slot [0]) and the point of the shape (slot [1]) expressed as
                :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` (depending on body shape)
        
        :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidPoint` closestPointTo(:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` point, :class:`~fr.cnes.sirius.patrius.frames.Frame` frame, :class:`~fr.cnes.sirius.patrius.time.AbsoluteDate` date) throws :class:`~fr.cnes.sirius.patrius.utils.exception.PatriusException`
        
            Computes the point on body surface that is the closest to provided point.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): a point expressed in provided frame
                frame (:class:`~fr.cnes.sirius.patrius.frames.Frame`): frame
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): date
        
            Returns:
                the closest point to the provided point on the body surface
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.utils.exception.PatriusException`: if computation failed
        
            Computes the point on body surface that is the closest to provided point.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): a point expressed in body frame
        
            Returns:
                the closest point to the provided point on the body surface
        
            Computes the point on body surface that is the closest to provided point.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): a point expressed in body frame
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): name of the point
        
            Returns:
                the closest point to the provided point on the body surface
        
        
        """
        ...
    @typing.overload
    def closestPointTo(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> 'EllipsoidPoint': ...
    @typing.overload
    def closestPointTo(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, string: str) -> 'EllipsoidPoint': ...
    @typing.overload
    def closestPointTo(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line) -> typing.MutableSequence['EllipsoidPoint']: ...
    @typing.overload
    def closestPointTo(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> typing.MutableSequence['EllipsoidPoint']: ...
    def computePositionFromEllipsodeticCoordinates(self, double: float, double2: float, double3: float) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D:
        """
            Compute the position from the ellipsodetic coordinates in body frame.
        
            Parameters:
                latitude (double): latitude coordinate
                longitude (double): longitude coordinate
                height (double): height coordinate (signed value)
        
            Returns:
                the position in body frame as :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`
        
        
        """
        ...
    def getARadius(self) -> float:
        """
            Getter for the semi axis A.
        
            Returns:
                the semi axis A
        
        
        """
        ...
    def getBRadius(self) -> float:
        """
            Getter for the semi axis B.
        
            Returns:
                the semi axis B
        
        
        """
        ...
    def getCRadius(self) -> float:
        """
            Getter for the semi axis C.
        
            Returns:
                the semi axis C
        
        
        """
        ...
    def getConjugateRadius(self) -> float: ...
    def getE2(self) -> float: ...
    def getEllipsoid(self) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid:
        """
            Getter for the :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid` object.
        
            Returns:
                the spheroid
        
        
        """
        ...
    def getEquatorialRadius(self) -> float: ...
    def getFlattening(self) -> float: ...
    def getG2(self) -> float: ...
    @typing.overload
    def getIntersectionPoint(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> 'EllipsoidPoint': ...
    @typing.overload
    def getIntersectionPoint(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, double: float) -> 'EllipsoidPoint': ...
    @typing.overload
    def getIntersectionPoint(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, string: str) -> 'EllipsoidPoint': ...
    def getIntersectionPoints(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> typing.MutableSequence['EllipsoidPoint']: ...
    def getTransverseRadius(self) -> float: ...
    def isSpherical(self) -> bool:
        """
            Indicate if the ellipsoid can be considered as a sphere.
        
            Returns:
                :code:`true` if the ellipsoid can be considered as a sphere, :code:`false` otherwise
        
        
        """
        ...

class EllipsoidPoint(AbstractBodyPoint):
    """
    public class EllipsoidPoint extends :class:`~fr.cnes.sirius.patrius.bodies.AbstractBodyPoint`
    
        Point location relative to a 2D body surface of type :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`.
    
        Instance of this class are guaranteed to be immutable.
    
        Since:
            4.12
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.bodies.AbstractBodyPoint`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, ellipsoidBodyShape: EllipsoidBodyShape, lLHCoordinates: LLHCoordinates, string: str): ...
    @typing.overload
    def __init__(self, ellipsoidBodyShape: EllipsoidBodyShape, lLHCoordinatesSystem: LLHCoordinatesSystem, double: float, double2: float, double3: float, string: str): ...
    @typing.overload
    def __init__(self, ellipsoidBodyShape: EllipsoidBodyShape, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, string: str): ...
    @typing.overload
    def __init__(self, ellipsoidBodyShape: EllipsoidBodyShape, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, string: str): ...
    def getBodyShape(self) -> EllipsoidBodyShape:
        """
            Get the :class:`~fr.cnes.sirius.patrius.bodies.BodyShape` associated to this body point.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyPoint.getBodyShape` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.bodies.AbstractBodyPoint.getBodyShape` in
                class :class:`~fr.cnes.sirius.patrius.bodies.AbstractBodyPoint`
        
            Returns:
                :class:`~fr.cnes.sirius.patrius.bodies.BodyShape` associated to this body point
        
        
        """
        ...
    def getClosestPointOnShape(self) -> 'EllipsoidPoint':
        """
            Returns the closest point to this on the shape surface.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyPoint.getClosestPointOnShape` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.bodies.AbstractBodyPoint.getClosestPointOnShape` in
                class :class:`~fr.cnes.sirius.patrius.bodies.AbstractBodyPoint`
        
            Returns:
                the closest point to this on the shape surface
        
        
        """
        ...
    def getRadialProjectionOnShape(self) -> 'EllipsoidPoint':
        """
            Returns the body point, on the associated shape surface, in the radial direction corresponding to the position of this:
            if several of them (may happen for not star-convex shapes), the method considers the one farthest to the body frame
            origin (having the largest norm).
        
        
            **Warnings**: the returned point is not necessary the closest point belonging to the shape in the radial direction.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyPoint.getRadialProjectionOnShape` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.bodies.AbstractBodyPoint.getRadialProjectionOnShape` in
                class :class:`~fr.cnes.sirius.patrius.bodies.AbstractBodyPoint`
        
            Returns:
                the projection of this on the associated shape surface along the radial direction
        
        
        """
        ...

class IAUCelestialBody(CelestialBody):
    """
    public interface IAUCelestialBody extends :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
    
        Interface for IAU celestial bodies like Sun, Moon or solar system planets.
    
        When body orientation is defined by an IAU model, you can choose inertial and rotating frame model precision through
        :meth:`~fr.cnes.sirius.patrius.bodies.IAUCelestialBody.getInertialFrame` and
        :meth:`~fr.cnes.sirius.patrius.bodies.IAUCelestialBody.getRotatingFrame` methods.
    
        By default in :meth:`~fr.cnes.sirius.patrius.bodies.IAUCelestialBody.getInertialFrame` and
        :meth:`~fr.cnes.sirius.patrius.bodies.IAUCelestialBody.getRotatingFrame` the complete model
        :meth:`~fr.cnes.sirius.patrius.bodies.IAUPoleModelType.TRUE` is used.
    
        Celestial Barycenters are handled by class :class:`~fr.cnes.sirius.patrius.bodies.BasicCelestialPoint`.
    
        Since:
            4.14
    """
    @typing.overload
    def getInertialFrame(self, iAUPoleModelType: IAUPoleModelType) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    @typing.overload
    def getInertialFrame(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    def getOrientation(self) -> CelestialBodyIAUOrientation:
        """
            Getter for the celestial body IAU orientation and primer meridians orientation.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.getOrientation` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
            Returns:
                the celestial body IAU orientation
        
        
        """
        ...
    @typing.overload
    def getRotatingFrame(self, iAUPoleModelType: IAUPoleModelType) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    @typing.overload
    def getRotatingFrame(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    def toString(self) -> str: ...

class JPLCelestialBodyLoader(AbstractJPLCelestialBodyLoader):
    """
    public class JPLCelestialBodyLoader extends :class:`~fr.cnes.sirius.patrius.bodies.AbstractJPLCelestialBodyLoader`
    
        Loader for JPL ephemerides binary files (DE 4xx and BSP) and similar formats (INPOP 06/08/10). It loads the whole
        :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`. For
        :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyEphemeris` loader only, see dedicated class.
    
        JPL ephemerides binary files contain ephemerides for all solar system planets.
    
        The JPL ephemerides binary files are recognized thanks to their base names, which must match the pattern
        :code:`[lu]nx[mp]####.ddd` (or :code:`[lu]nx[mp]####.ddd.gz` for gzip-compressed files) where # stands for a digit
        character and where ddd is an ephemeris type (typically 405 or 406).
    
        Currently accepted JPL formats are: DE200/DE 202/DE 403/DE 405/DE 406/DE 410/DE 413/DE 414/DE 418/DE 421/DE 422/DE
        423/DE 430 and BSP.
    
        The loader supports files encoded in big-endian as well as in little-endian notation. Usually, big-endian files are
        named :code:`unx[mp]####.ddd`, while little-endian files are named :code:`lnx[mp]####.ddd`.
    
        The IMCCE ephemerides binary files are recognized thanks to their base names, which must match the pattern
        :code:`inpop*.dat` (or :code:`inpop*.dat.gz` for gzip-compressed files) where * stands for any string.
    
        Currently accepted IMCCE formats are: INPOP 06b/06c/08a/10a/10b/10e/13c/17a/19a.
    
        The loader supports files encoded in big-endian as well as in little-endian notation. Usually, big-endian files contain
        :code:`bigendian` in their names, while little-endian files contain :code:`littleendian` in their names.
    
        The loader supports files in TDB or TCB time scales.
    
        Note: the time scale isn't serialized.
    
        Since:
            4.11.1
    
        Also see:
            :meth:`~serialized`
    """
    DEFAULT_DE_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` DEFAULT_DE_SUPPORTED_NAMES
    
        Default supported files name pattern for JPL DE files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_INPOP_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` DEFAULT_INPOP_SUPPORTED_NAMES
    
        Default supported files name pattern for IMCCE INPOP files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str, predefinedEphemerisType: PredefinedEphemerisType): ...
    @typing.overload
    def __init__(self, string: str, predefinedEphemerisType: PredefinedEphemerisType, gravityModel: fr.cnes.sirius.patrius.forces.gravity.GravityModel): ...
    def getName(self, string: str) -> str:
        """
            Returns name of body as known by the loader corresponding to PATRIUS body name.
        
            Parameters:
                patriusName (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): PATRIUS body name
        
            Returns:
                name of body as known by the loader corresponding to PATRIUS body name
        
        
        """
        ...
    def loadCelestialBody(self, string: str) -> CelestialBody: ...
    def loadCelestialPoint(self, string: str) -> CelestialPoint: ...

class JPLHistoricEphemerisLoader(JPLEphemerisLoader):
    """
    public class JPLHistoricEphemerisLoader extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.bodies.JPLEphemerisLoader`
    
        Loader for JPL ephemerides binary files (DE 4xx) and similar formats (INPOP 06/08/10). It loads only the
        :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyEphemeris`. For
        :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint` loader, see dedicated class.
    
        JPL ephemerides binary files contain ephemerides for all solar system planets.
    
        The JPL ephemerides binary files are recognized thanks to their base names, which must match the pattern
        :code:`[lu]nx[mp]####.ddd` (or :code:`[lu]nx[mp]####.ddd.gz` for gzip-compressed files) where # stands for a digit
        character and where ddd is an ephemeris type (typically 405 or 406).
    
        Currently accepted JPL formats are: DE200/DE 202/DE 403/DE 405/DE 406/DE 410/DE 413/DE 414/DE 418/DE 421/DE 422/DE 423
        and DE 430.
    
        The loader supports files encoded in big-endian as well as in little-endian notation. Usually, big-endian files are
        named :code:`unx[mp]####.ddd`, while little-endian files are named :code:`lnx[mp]####.ddd`.
    
        The IMCCE ephemerides binary files are recognized thanks to their base names, which must match the pattern
        :code:`inpop*.dat` (or :code:`inpop*.dat.gz` for gzip-compressed files) where * stands for any string.
    
        Currently accepted IMCCE formats are: INPOP 06b/06c/08a/10a/10b/10e/13c/17a/19a.
    
        The loader supports files encoded in big-endian as well as in little-endian notation. Usually, big-endian files contain
        :code:`bigendian` in their names, while little-endian files contain :code:`littleendian` in their names.
    
        The loader supports files in TDB or TCB time scales.
    
        Note: the time scale isn't serialized.
    
        Since:
            4.10
    
        Also see:
            :meth:`~serialized`
    """
    DEFAULT_DE_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` DEFAULT_DE_SUPPORTED_NAMES
    
        Default supported files name pattern for JPL DE files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_INPOP_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` DEFAULT_INPOP_SUPPORTED_NAMES
    
        Default supported files name pattern for IMCCE INPOP files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, string: str, predefinedEphemerisType: PredefinedEphemerisType): ...
    def getLoadedAstronomicalUnit(self) -> float: ...
    def getLoadedConstant(self, *string: str) -> float: ...
    def getLoadedEarthMoonMassRatio(self) -> float: ...
    def getLoadedGravitationalCoefficient(self, predefinedEphemerisType: PredefinedEphemerisType) -> float: ...
    def getMaxChunksDuration(self) -> float:
        """
            Get the maximal chunks duration.
        
            Returns:
                chunks maximal duration in seconds
        
        
        """
        ...
    def loadCelestialBodyEphemeris(self, string: str) -> CelestialBodyEphemeris: ...
    @staticmethod
    def setCacheSize(int: int) -> None:
        """
            Set ephemeris cache size in days. For best performances, cache size should be consistent with consideredd physical
            timespan. Default value is :meth:`~fr.cnes.sirius.patrius.bodies.JPLHistoricEphemerisLoader.FIFTY_DAYS`.
        
            Parameters:
                days (int): number of days
        
        
        """
        ...

class UserIAUPole(CelestialBodyIAUOrientation):
    """
    public class UserIAUPole extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyIAUOrientation`
    
        Generic IAU pole model for pole and prime meridian orientations.
    
        This class represents the model compliant with the report of the IAU/IAG Working Group on Cartographic Coordinates and
        Rotational Elements of the Planets and Satellites (WGCCRE). These definitions are common for all recent versions of this
        report published every three years.
    
        The precise values of pole direction and W angle coefficients may vary from publication year as models are adjusted. The
        latest value of constants for implementing this interface can be found in the `working group site
        <http://astrogeology.usgs.gov/Projects/WGCCRE/>`.
    
        Since:
            4.7
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, iAUPoleCoefficients: IAUPoleCoefficients): ...
    @typing.overload
    def getAngularCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, iAUPoleModelType: IAUPoleModelType) -> fr.cnes.sirius.patrius.utils.AngularCoordinates: ...
    @typing.overload
    def getAngularCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.utils.AngularCoordinates: ...
    @typing.overload
    def getAngularCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, orientationType: CelestialBodyOrientation.OrientationType) -> fr.cnes.sirius.patrius.utils.AngularCoordinates: ...
    @typing.overload
    def getAngularCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, orientationType: CelestialBodyOrientation.OrientationType, iAUPoleModelType: IAUPoleModelType) -> fr.cnes.sirius.patrius.utils.AngularCoordinates: ...
    @typing.overload
    def getPole(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D:
        """
            Getter for the body North pole direction with respect to a reference frame.
        
        
            It takes into account constant, secular and harmonics terms (conversion from ICRF to true equator).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation.getPole` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation`
        
            Parameters:
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): Current date
        
            Returns:
                the body North pole direction with respect to a reference frame
        
            Getter for the body North pole direction with respect to a reference frame.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyIAUOrientation.getPole` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyIAUOrientation`
        
            Parameters:
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): Current date
                iauPoleType (:class:`~fr.cnes.sirius.patrius.bodies.IAUPoleModelType`): IAUPole data to take into account for ICRF/inertial/mean equator/true equator transformation
        
            Returns:
                the body North pole direction with respect to a reference frame
        
        
        """
        ...
    @typing.overload
    def getPole(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, iAUPoleModelType: IAUPoleModelType) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getPoleDerivative(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D:
        """
            Getter for the body North pole direction derivative with respect to a reference frame.
        
        
            It takes into account constant, secular and harmonics terms (conversion from ICRF to true equator).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation.getPoleDerivative` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation`
        
            Parameters:
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): Current date
        
            Returns:
                the body North pole direction derivative with respect to a reference frame
        
            Getter for the body North pole direction derivative with respect to a reference frame.
        
        
            It takes into account constant, secular and harmonics terms (conversion from ICRF to true equator).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyIAUOrientation.getPoleDerivative` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyIAUOrientation`
        
            Parameters:
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): Current date
                iauPoleType (:class:`~fr.cnes.sirius.patrius.bodies.IAUPoleModelType`): IAUPole data to take into account for ICRF/inertial/mean equator/true equator transformation
        
            Returns:
                the body North pole direction derivative with respect to a reference frame
        
        
        """
        ...
    @typing.overload
    def getPoleDerivative(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, iAUPoleModelType: IAUPoleModelType) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getPrimeMeridianAngle(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> float:
        """
            Getter for the prime meridian angle.
        
        
            It takes into account constant, secular and harmonics terms (conversion from ICRF to true rotating).
        
            The prime meridian angle is the angle between the Q node and the prime meridian. Represents the body rotation.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation.getPrimeMeridianAngle` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation`
        
            Parameters:
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): Current date
        
            Returns:
                the prime meridian vector
        
            Getter for the prime meridian angle.
        
            The prime meridian angle is the angle between the Q node and the prime meridian. Represents the body rotation.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyIAUOrientation.getPrimeMeridianAngle` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyIAUOrientation`
        
            Parameters:
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): Current date
                iauPoleType (:class:`~fr.cnes.sirius.patrius.bodies.IAUPoleModelType`): IAUPole data to take into account for ICRF/inertial/mean rotating/true rotating transformation
        
            Returns:
                the prime meridian vector
        
        
        """
        ...
    @typing.overload
    def getPrimeMeridianAngle(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, iAUPoleModelType: IAUPoleModelType) -> float: ...
    @typing.overload
    def getPrimeMeridianAngleDerivative(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> float:
        """
            Getter for the prime meridian angle derivative.
        
        
            It takes into account constant, secular and harmonics terms (conversion from ICRF to true rotating).
        
            The prime meridian angle is the angle between the Q node and the prime meridian. Represents the body rotation.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation.getPrimeMeridianAngleDerivative` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation`
        
            Parameters:
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): Current date
        
            Returns:
                the prime meridian angle derivative
        
            Getter for the prime meridian angle derivative.
        
            The prime meridian angle is the angle between the Q node and the prime meridian. Represents the body rotation.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyIAUOrientation.getPrimeMeridianAngleDerivative` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyIAUOrientation`
        
            Parameters:
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): Current date
                iauPoleType (:class:`~fr.cnes.sirius.patrius.bodies.IAUPoleModelType`): IAUPole data to take into account for ICRF/inertial/mean rotating/true rotating transformation
        
            Returns:
                the prime meridian angle derivative
        
        
        """
        ...
    @typing.overload
    def getPrimeMeridianAngleDerivative(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, iAUPoleModelType: IAUPoleModelType) -> float: ...
    def toString(self) -> str:
        """
            Returns a string representation of the body orientation.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation.toString` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation`
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of the body orientation
        
        
        """
        ...

class AbstractEllipsoidBodyShape(AbstractBodyShape, EllipsoidBodyShape):
    """
    public abstract class AbstractEllipsoidBodyShape extends :class:`~fr.cnes.sirius.patrius.bodies.AbstractBodyShape` implements :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`
    
        Abstract class for an ellipsoid body shape to mutualize parameters and features.
    
        Since:
            4.13
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.bodies.AbstractBodyShape`, :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`,
            :meth:`~serialized`
    """
    DEFAULT_LLH_COORD_SYSTEM: typing.ClassVar[LLHCoordinatesSystem] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.bodies.LLHCoordinatesSystem` DEFAULT_LLH_COORD_SYSTEM
    
        Ellipsodetic used as default LLH coordinates system for the computed
        :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidPoint`.
    
    """
    CLOSE_APPROACH_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double CLOSE_APPROACH_THRESHOLD
    
        Close approach threshold.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, iEllipsoid: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame, boolean: bool, string: str): ...
    @typing.overload
    def __init__(self, iEllipsoid: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame, boolean: bool, string: str, lLHCoordinatesSystem: LLHCoordinatesSystem): ...
    @typing.overload
    def __init__(self, iEllipsoid: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame, string: str): ...
    @typing.overload
    def buildPoint(self, lLHCoordinatesSystem: LLHCoordinatesSystem, double: float, double2: float, double3: float, string: str) -> EllipsoidPoint:
        """
            Build a :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` from LLH coordinates. Type of returned body point depends on
            body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.buildPoint` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape.buildPoint` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`
        
            Parameters:
                coordSystem (:class:`~fr.cnes.sirius.patrius.bodies.LLHCoordinatesSystem`): LLH coordinates system in which are expressed the entered lat/long/height
                latitude (double): input latitude
                longitude (double): input longitude
                height (double): input height
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): name of the point
        
            Returns:
                a body point
        
        """
        ...
    @typing.overload
    def buildPoint(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, string: str) -> EllipsoidPoint: ...
    @typing.overload
    def buildPoint(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, string: str) -> EllipsoidPoint:
        """
            Build a :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` from position in body frame. Type of returned body point
            depends on body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.buildPoint` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape.buildPoint` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`
        
            Parameters:
                position (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): position in body frame
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): name of the point
        
            Returns:
                :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` from position in body frame
        
        public :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidPoint` buildPoint(:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` position, :class:`~fr.cnes.sirius.patrius.frames.Frame` frame, :class:`~fr.cnes.sirius.patrius.time.AbsoluteDate` date, `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` name) throws :class:`~fr.cnes.sirius.patrius.utils.exception.PatriusException`
        
            Build a :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` from position in provided frame at provided date. Type of
            returned body point depends on body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.buildPoint` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape.buildPoint` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`
        
            Parameters:
                position (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): position in provided frame at provided date
                frame (:class:`~fr.cnes.sirius.patrius.frames.Frame`): frame
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): date
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): name of the point
        
            Returns:
                :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` from position in provided frame at provided date
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.utils.exception.PatriusException`: if failed to build point
        
        
        """
        ...
    @typing.overload
    def closestPointTo(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D) -> EllipsoidPoint:
        """
            This method computes the two points, on the line and on the body, that are the closest to each other. The returned
            points are identical if the line intersects the shape: this point is the one with the lowest abscissa. The returned
            point with index 0 is the point on the Line, while the returned point with index 1 is the point on this.
        
            Note: calculations take the line's minimum abscissa into account.
        
            In this method we consider that the line's frame is the body frame, and the date is the
            :meth:`~fr.cnes.sirius.patrius.time.AbsoluteDate.J2000_EPOCH`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the original line for the shortest distance computation
        
            Returns:
                an array of length 2 containing the point of the line (slot [0]) and the point of the shape (slot [1]) expressed as
                :class:`~fr.cnes.sirius.patrius.bodies.BodyPoint` (depending on body shape)
        
        public :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidPoint` closestPointTo(:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` point, :class:`~fr.cnes.sirius.patrius.frames.Frame` frame, :class:`~fr.cnes.sirius.patrius.time.AbsoluteDate` date) throws :class:`~fr.cnes.sirius.patrius.utils.exception.PatriusException`
        
            Computes the point on body surface that is the closest to provided point.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): a point expressed in provided frame
                frame (:class:`~fr.cnes.sirius.patrius.frames.Frame`): frame
                date (:class:`~fr.cnes.sirius.patrius.time.AbsoluteDate`): date
        
            Returns:
                the closest point to the provided point on the body surface
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.utils.exception.PatriusException`: if computation failed
        
            Computes the point on body surface that is the closest to provided point.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): a point expressed in body frame
        
            Returns:
                the closest point to the provided point on the body surface
        
            Computes the point on body surface that is the closest to provided point.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): a point expressed in body frame
                name (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): name of the point
        
            Returns:
                the closest point to the provided point on the body surface
        
        
        """
        ...
    @typing.overload
    def closestPointTo(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> EllipsoidPoint: ...
    @typing.overload
    def closestPointTo(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, string: str) -> EllipsoidPoint: ...
    @typing.overload
    def closestPointTo(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line) -> typing.MutableSequence[EllipsoidPoint]: ...
    @typing.overload
    def closestPointTo(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> typing.MutableSequence[EllipsoidPoint]: ...
    def computePositionFromEllipsodeticCoordinates(self, double: float, double2: float, double3: float) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D:
        """
            Compute the position from the ellipsodetic coordinates in body frame.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape.computePositionFromEllipsodeticCoordinates` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`
        
            Parameters:
                latitude (double): latitude coordinate
                longitude (double): longitude coordinate
                height (double): height coordinate (signed value)
        
            Returns:
                the position in body frame as :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`
        
        
        """
        ...
    def distanceTo(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> float: ...
    def getARadius(self) -> float:
        """
            Getter for the semi axis A.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape.getARadius` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`
        
            Returns:
                the semi axis A
        
        
        """
        ...
    def getApparentRadius(self, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, pVCoordinatesProvider2: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, propagationDelayType: fr.cnes.sirius.patrius.events.detectors.AbstractSignalPropagationDetector.PropagationDelayType) -> float: ...
    def getBRadius(self) -> float:
        """
            Getter for the semi axis B.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape.getBRadius` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`
        
            Returns:
                the semi axis B
        
        
        """
        ...
    def getCRadius(self) -> float:
        """
            Getter for the semi axis C.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape.getCRadius` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`
        
            Returns:
                the semi axis C
        
        
        """
        ...
    def getEllipsoid(self) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid:
        """
            Getter for the :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid` object.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape.getEllipsoid` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`
        
            Returns:
                the spheroid
        
        
        """
        ...
    def getEncompassingSphereRadius(self) -> float:
        """
            Getter for the radius, in meters, of a sphere centered on the body frame origin and encompassing the shape.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.getEncompassingSphereRadius` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Returns:
                the encompassing radius
        
        
        """
        ...
    @typing.overload
    def getIntersectionPoint(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, double: float) -> EllipsoidPoint: ...
    @typing.overload
    def getIntersectionPoint(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> EllipsoidPoint: ...
    @typing.overload
    def getIntersectionPoint(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, string: str) -> EllipsoidPoint: ...
    def getIntersectionPoints(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> typing.MutableSequence[EllipsoidPoint]: ...
    def getMaxIterSignalPropagation(self) -> int:
        """
            Get the maximum number of iterations for signal propagation when signal propagation is taken into account.
        
            Returns:
                returns the maximum number of iterations for signal propagation when signal propagation is taken into account.
        
        
        """
        ...
    def isDefaultLLHCoordinatesSystem(self) -> bool:
        """
            Indicate if the current LLH coordinates system set for the body is the default one or not.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.isDefaultLLHCoordinatesSystem` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Returns:
                :code:`true` if the current LLH coordinates system is the default one, :code:`false` otherwise
        
        
        """
        ...
    def isSpherical(self) -> bool:
        """
            Indicate if the ellipsoid can be considered as a sphere.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape.isSpherical` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`
        
            Returns:
                :code:`true` if the ellipsoid can be considered as a sphere, :code:`false` otherwise
        
        
        """
        ...
    def setConvergenceThreshold(self, double: float) -> None:
        """
            Setter for the Newton algorithm threshold used to compute distance to the ellipsoid using method
            :meth:`~fr.cnes.sirius.patrius.bodies.AbstractEllipsoidBodyShape.distanceTo`. Method
            :meth:`~fr.cnes.sirius.patrius.bodies.AbstractEllipsoidBodyShape.distanceTo` is used in particular in SensorModel.
            Default value for this threshold is 1E-11.
        
            Parameters:
                newThreshold (double): new threshold to set
        
        
        """
        ...
    def setMaxIterSignalPropagation(self, int: int) -> None:
        """
            Set the maximum number of iterations for signal propagation when signal propagation is taken into account.
        
            Parameters:
                maxIterSignalPropagationIn (int): maximum number of iterations for signal propagation
        
        
        """
        ...

class AbstractIAUCelestialBody(AbstractCelestialBody, IAUCelestialBody):
    """
    public abstract class AbstractIAUCelestialBody extends :class:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialBody` implements :class:`~fr.cnes.sirius.patrius.bodies.IAUCelestialBody`
    
        Abstract implementation of the :class:`~fr.cnes.sirius.patrius.bodies.IAUCelestialBody` interface.
    
        This abstract implementation provides basic services that can be shared by most implementations of the
        :class:`~fr.cnes.sirius.patrius.bodies.IAUCelestialBody` interface. It holds the gravitational attraction coefficient
        and build the body-centered frames automatically using the definitions of pole and prime meridian specified by the
        IAU/IAG Working Group on Cartographic Coordinates and Rotational Elements of the Planets and Satellites (WGCCRE).
    
        Since:
            4.14
    
        Also see:
            :meth:`~serialized`
    """
    CONSTANT: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` CONSTANT
    
        Constant model string.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MEAN: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` MEAN
    
        Mean model string.
    
        Also see:
            :meth:`~constant`
    
    
    """
    TRUE: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` TRUE
    
        True model string.
    
        Also see:
            :meth:`~constant`
    
    
    """
    INERTIAL_FRAME_CONSTANT_MODEL: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` INERTIAL_FRAME_CONSTANT_MODEL
    
        Constant (equator) inertial, body-centered frame name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    INERTIAL_FRAME_MEAN_MODEL: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` INERTIAL_FRAME_MEAN_MODEL
    
        Mean (equator) inertial, body-centered frame name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    INERTIAL_FRAME_TRUE_MODEL: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` INERTIAL_FRAME_TRUE_MODEL
    
        True (equator) inertial, body-centered frame name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ROTATING_FRAME_CONSTANT_MODEL: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` ROTATING_FRAME_CONSTANT_MODEL
    
        Constant rotating, body-centered frame name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ROTATING_FRAME_MEAN_MODEL: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` ROTATING_FRAME_MEAN_MODEL
    
        Mean rotating, body-centered frame name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ROTATING_FRAME_TRUE_MODEL: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` ROTATING_FRAME_TRUE_MODEL
    
        True rotating, body-centered frame name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def getInertialFrame(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    @typing.overload
    def getInertialFrame(self, iAUPoleModelType: IAUPoleModelType) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    def getOrientation(self) -> CelestialBodyIAUOrientation:
        """
            Getter for the celestial body orientation and primer meridians orientation.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.getOrientation` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.IAUCelestialBody.getOrientation` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.IAUCelestialBody`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialBody.getOrientation` in
                class :class:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialBody`
        
            Returns:
                the celestial body orientation
        
        
        """
        ...
    @typing.overload
    def getRotatingFrame(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    @typing.overload
    def getRotatingFrame(self, iAUPoleModelType: IAUPoleModelType) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    def setOrientation(self, celestialBodyOrientation: CelestialBodyOrientation) -> None:
        """
            Set a celestial body IAU orientation to define the body frames.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.setOrientation` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialBody.setOrientation` in
                class :class:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialBody`
        
            Parameters:
                celestialBodyIAUOrientation (:class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation`): the celestial body IAU orientation
        
            Raises:
                : if the celestial body orientation isn't an instance of
                    :class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyIAUOrientation`
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns a string representation of the celestial point and its attributes.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.toString` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialBody.toString` in
                class :class:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialBody`
        
            Returns:
                a string representation of the celestial point and its attributes
        
        
        """
        ...

class Earth(IAUCelestialBody):
    """
    public class Earth extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.bodies.IAUCelestialBody`
    
        Earth body. Earth body is specific since it allows to match body frames with standard Earth boy frames (MOD, TOD, GCRF,
        etc.).
    
        Since:
            4.11.1
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, double: float): ...
    def getEME2000(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame:
        """
            Get an EME2000, celestial point centered frame.
        
            The frame is always bound to the celestial point center, and its axes are colinear to Earth EME2000 frame.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.getEME2000` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Returns:
                an EME2000, celestial point centered frame
        
        
        """
        ...
    def getEclipticJ2000(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    def getEphemeris(self) -> CelestialBodyEphemeris:
        """
            Get the ephemeris of the celestial point.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.getEphemeris` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Returns:
                the ephemeris
        
        
        """
        ...
    def getGM(self) -> float:
        """
            Get the central attraction coefficient of the celestial point.
        
            Warning: attraction model should not be null (it is not null by default).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.getGM` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Returns:
                central attraction coefficient of the celestial point (m :sup:`3` /s :sup:`2` )
        
        
        """
        ...
    def getGravityModel(self) -> fr.cnes.sirius.patrius.forces.gravity.GravityModel:
        """
            Getter for the gravitational attraction model of the body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.getGravityModel` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
            Returns:
                the gravitational attraction model
        
        
        """
        ...
    def getICRF(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame:
        """
            Get an ICRF, celestial point centered frame.
        
            The frame is always bound to the celestial point, and its axes have a fixed orientation with respect to other inertial
            frames.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.getICRF` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Returns:
                an inertially oriented, celestial point centered frame
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.getRotatingFrame`
        
        
        """
        ...
    @typing.overload
    def getInertialFrame(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    @typing.overload
    def getInertialFrame(self, iAUPoleModelType: IAUPoleModelType) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    def getName(self) -> str:
        """
            Getter for the name of the body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.getName` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.getName` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Returns:
                name of the body
        
        
        """
        ...
    def getNativeFrame(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> fr.cnes.sirius.patrius.frames.Frame: ...
    def getOrientation(self) -> CelestialBodyIAUOrientation:
        """
            Getter for the celestial body IAU orientation and primer meridians orientation.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.getOrientation` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.IAUCelestialBody.getOrientation` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.IAUCelestialBody`
        
            Returns:
                the celestial body IAU orientation
        
        
        """
        ...
    def getPVCoordinates(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, frame: fr.cnes.sirius.patrius.frames.Frame) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates: ...
    @typing.overload
    def getRotatingFrame(self) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    @typing.overload
    def getRotatingFrame(self, iAUPoleModelType: IAUPoleModelType) -> fr.cnes.sirius.patrius.frames.CelestialBodyFrame: ...
    def getShape(self) -> BodyShape:
        """
            Getter for the geometric shape of the body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.getShape` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
            Returns:
                geometric shape of the body
        
        
        """
        ...
    def setEphemeris(self, celestialBodyEphemeris: CelestialBodyEphemeris) -> None:
        """
            Set an ephemeris to the celestial point.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.setEphemeris` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Parameters:
                ephemerisIn (:class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyEphemeris`): the ephemeris
        
        
        """
        ...
    def setGM(self, double: float) -> None:
        """
            Set a central attraction coefficient to the celestial point.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.setGM` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Parameters:
                gmIn (double): the central attraction coefficient (m :sup:`3` /s :sup:`2` )
        
        
        """
        ...
    def setGravityModel(self, gravityModel: fr.cnes.sirius.patrius.forces.gravity.GravityModel) -> None:
        """
            Setter for a gravitational attraction model to the body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.setGravityModel` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
            Parameters:
                modelIn (:class:`~fr.cnes.sirius.patrius.forces.gravity.GravityModel`): the gravitational attraction model
        
        
        """
        ...
    def setOrientation(self, celestialBodyOrientation: CelestialBodyOrientation) -> None:
        """
            Setter for a celestial body orientation to define the body frames.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.setOrientation` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
            Parameters:
                celestialBodyOrientation (:class:`~fr.cnes.sirius.patrius.bodies.CelestialBodyOrientation`): the celestial body orientation
        
        
        """
        ...
    def setShape(self, bodyShape: BodyShape) -> None:
        """
            Setter for a geometric shape to the body.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialBody.setShape` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialBody`
        
            Parameters:
                shapeIn (:class:`~fr.cnes.sirius.patrius.bodies.BodyShape`): the shape of the body
        
        
        """
        ...

class UserCelestialBody(AbstractCelestialBody):
    """
    public class UserCelestialBody extends :class:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialBody`
    
        User-defined celestial body. It can be used to define any celestial body with:
    
          - Its name
          - A :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider` providing body position-velocity through
            time
          - Its gravitational constant
          - Its pole motion (if reference data are provided by IAU, prefer using
            :class:`~fr.cnes.sirius.patrius.bodies.UserIAUCelestialBody` )
    
    
        Since:
            3.4
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str, double: float, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider): ...
    @typing.overload
    def __init__(self, string: str, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, celestialBodyOrientation: CelestialBodyOrientation, frame: fr.cnes.sirius.patrius.frames.Frame, bodyShape: BodyShape): ...
    @typing.overload
    def __init__(self, string: str, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, celestialBodyOrientation: CelestialBodyOrientation, frame: fr.cnes.sirius.patrius.frames.Frame, bodyShape: BodyShape, spiceJ2000ConventionEnum: fr.cnes.sirius.patrius.bodies.bsp.BSPEphemerisLoader.SpiceJ2000ConventionEnum): ...
    @typing.overload
    def __init__(self, string: str, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, gravityModel: fr.cnes.sirius.patrius.forces.gravity.GravityModel, celestialBodyOrientation: CelestialBodyOrientation, frame: fr.cnes.sirius.patrius.frames.Frame, bodyShape: BodyShape): ...
    @typing.overload
    def __init__(self, string: str, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, gravityModel: fr.cnes.sirius.patrius.forces.gravity.GravityModel, celestialBodyOrientation: CelestialBodyOrientation, frame: fr.cnes.sirius.patrius.frames.Frame, bodyShape: BodyShape, spiceJ2000ConventionEnum: fr.cnes.sirius.patrius.bodies.bsp.BSPEphemerisLoader.SpiceJ2000ConventionEnum): ...
    def toString(self) -> str:
        """
            Returns a string representation of the celestial point and its attributes.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.toString` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialBody.toString` in
                class :class:`~fr.cnes.sirius.patrius.bodies.AbstractCelestialBody`
        
            Returns:
                a string representation of the celestial point and its attributes
        
        
        """
        ...

class MeeusMoon(AbstractIAUCelestialBody):
    """
    public class MeeusMoon extends :class:`~fr.cnes.sirius.patrius.bodies.AbstractIAUCelestialBody`
    
    
        This class implements the Moon ephemerides according to the algorithm of Meeus. It only provides the position. Note that
        it is not possible to build this Moon from the CelestialBodyFactory.
        See "Astronomical Algorithms", chapter 45 "Position of the Moon", Jean Meeus, 1991.
    
        Note that pole information allowing to define inertially-centered frame and rotating frame are defined in
        :class:`~fr.cnes.sirius.patrius.bodies.IAUPoleFactory` since Meeus model does not provide the information.
    
        Since:
            1.1
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int): ...
    def toString(self) -> str:
        """
            Returns a string representation of the celestial point and its attributes.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.toString` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.bodies.AbstractIAUCelestialBody.toString` in
                class :class:`~fr.cnes.sirius.patrius.bodies.AbstractIAUCelestialBody`
        
            Returns:
                a string representation of the celestial point and its attributes
        
        
        """
        ...

class MeeusSun(AbstractIAUCelestialBody):
    """
    public class MeeusSun extends :class:`~fr.cnes.sirius.patrius.bodies.AbstractIAUCelestialBody`
    
    
        This class implements the Sun ephemerides according to the algorithm of Meeus, it only provides the position. Note that
        it is not possible to build this Sun from the CelestialBodyFactory.
        See "Astronomical Algorithms", chapter 24 "Solar Coordinates", Jean Meeus, 1991. This class allows the use of three
        different Meeus model : the standard Meeus model, the STELA one and the on board model (used for CERES mission for
        instance).
    
        Note that pole information allowing to define inertially-centered frame and rotating frame are defined in
        :class:`~fr.cnes.sirius.patrius.bodies.IAUPoleFactory` since Meeus model does not provide the information.
    
        Since:
            1.1
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, mODEL: 'MeeusSun.MODEL'): ...
    def toString(self) -> str:
        """
            Returns a string representation of the celestial point and its attributes.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.toString` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.bodies.AbstractIAUCelestialBody.toString` in
                class :class:`~fr.cnes.sirius.patrius.bodies.AbstractIAUCelestialBody`
        
            Returns:
                a string representation of the celestial point and its attributes
        
        
        """
        ...
    class MODEL(java.lang.Enum['MeeusSun.MODEL']):
        STANDARD: typing.ClassVar['MeeusSun.MODEL'] = ...
        STELA: typing.ClassVar['MeeusSun.MODEL'] = ...
        BOARD: typing.ClassVar['MeeusSun.MODEL'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'MeeusSun.MODEL': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['MeeusSun.MODEL']: ...

class OneAxisEllipsoid(AbstractEllipsoidBodyShape):
    """
    public class OneAxisEllipsoid extends :class:`~fr.cnes.sirius.patrius.bodies.AbstractEllipsoidBodyShape`
    
        One axis ellipsoid representation.
    
        This ellipsoid is fully defined by its equatorial radius, its flattening and its associated body frame.
    
        Since:
            1.2
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.bodies.AbstractEllipsoidBodyShape`, :meth:`~serialized`
    """
    DEFAULT_ONE_AXIS_ELLIPSOID_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` DEFAULT_ONE_AXIS_ELLIPSOID_NAME
    
        Default ellipsoid name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame): ...
    @typing.overload
    def __init__(self, double: float, double2: float, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame, string: str): ...
    def computePositionFromEllipsodeticCoordinates(self, double: float, double2: float, double3: float) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D:
        """
            Compute the position from the ellipsodetic coordinates in body frame.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape.computePositionFromEllipsodeticCoordinates` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.EllipsoidBodyShape`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.bodies.AbstractEllipsoidBodyShape.computePositionFromEllipsodeticCoordinates` in
                class :class:`~fr.cnes.sirius.patrius.bodies.AbstractEllipsoidBodyShape`
        
            Parameters:
                latitude (double): latitude coordinate
                longitude (double): longitude coordinate
                height (double): height coordinate (signed value)
        
            Returns:
                the position in body frame as :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`
        
        
        """
        ...
    def getConjugateRadius(self) -> float: ...
    def getE2(self) -> float:
        """
            Getter for the e2 (eccentricity e squared with :code:`e = f * (2.0 - f)`).
        
            Returns:
                the e2
        
        
        """
        ...
    def getEncompassingSphereRadius(self) -> float:
        """
            Getter for the radius, in meters, of a sphere centered on the body frame origin and encompassing the shape.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.BodyShape.getEncompassingSphereRadius` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.BodyShape`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.bodies.AbstractEllipsoidBodyShape.getEncompassingSphereRadius` in
                class :class:`~fr.cnes.sirius.patrius.bodies.AbstractEllipsoidBodyShape`
        
            Returns:
                the encompassing radius
        
        
        """
        ...
    def getEquatorialRadius(self) -> float:
        """
            Getter for the equatorial radius of the body.
        
            Returns:
                the equatorial radius of the body (m)
        
        
        """
        ...
    def getFlattening(self) -> float:
        """
            Getter for the flattening.
        
            Returns:
                the flattening
        
        
        """
        ...
    def getG2(self) -> float:
        """
            Getter for the g2 (g squared with :code:`g = 1.0 - f`).
        
            Returns:
                the g2
        
        
        """
        ...
    @typing.overload
    def getIntersectionPoint(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> EllipsoidPoint: ...
    @typing.overload
    def getIntersectionPoint(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, string: str) -> EllipsoidPoint: ...
    @typing.overload
    def getIntersectionPoint(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, double: float) -> EllipsoidPoint: ...
    def getPolarRadius(self) -> float:
        """
            Getter for the polar radius of the body.
        
            Returns:
                the polar radius of the body (m)
        
        
        """
        ...
    def getTransverseRadius(self) -> float: ...
    def resize(self, marginType: BodyShape.MarginType, double: float) -> 'OneAxisEllipsoid':
        """
            Resize the geometric body shape by a margin.
        
            Parameters:
                marginType (:class:`~fr.cnes.sirius.patrius.bodies.BodyShape.MarginType`): margin type to be used
                marginValue (double): margin value to be used (in meters if the margin type is DISTANCE)
        
            Returns:
                resized geometric body shape with the margin
        
        
        """
        ...
    @typing.overload
    def transformAndComputeJacobian(self, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> EllipsoidPoint: ...
    @typing.overload
    def transformAndComputeJacobian(self, ellipsoidPoint: EllipsoidPoint, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D: ...

class ThreeAxisEllipsoid(AbstractEllipsoidBodyShape):
    """
    public class ThreeAxisEllipsoid extends :class:`~fr.cnes.sirius.patrius.bodies.AbstractEllipsoidBodyShape`
    
        Three axis ellipsoid representation.
    
        This ellipsoid is fully defined by its three axis radius (along the directions
        :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D.PLUS_I` /
        :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D.PLUS_J` /
        :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D.PLUS_K`) and its associated body frame.
    
        Since:
            4.13
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.bodies.AbstractEllipsoidBodyShape`, :meth:`~serialized`
    """
    DEFAULT_THREE_AXIS_ELLIPSOID_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` DEFAULT_THREE_AXIS_ELLIPSOID_NAME
    
        Default ellipsoid name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, celestialBodyFrame: fr.cnes.sirius.patrius.frames.CelestialBodyFrame, string: str): ...
    def getConjugateRadius(self) -> float: ...
    def getE2(self) -> float: ...
    def getEquatorialRadius(self) -> float: ...
    def getFlattening(self) -> float: ...
    def getG2(self) -> float: ...
    @typing.overload
    def getIntersectionPoint(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> EllipsoidPoint: ...
    @typing.overload
    def getIntersectionPoint(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, string: str) -> EllipsoidPoint: ...
    @typing.overload
    def getIntersectionPoint(self, line: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line, vector3D: fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D, frame: fr.cnes.sirius.patrius.frames.Frame, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, double: float) -> EllipsoidPoint: ...
    def getTransverseRadius(self) -> float: ...
    def resize(self, marginType: BodyShape.MarginType, double: float) -> 'ThreeAxisEllipsoid':
        """
            Resize the geometric body shape by a margin.
        
            Parameters:
                marginType (:class:`~fr.cnes.sirius.patrius.bodies.BodyShape.MarginType`): margin type to be used
                marginValue (double): margin value to be used (in meters if the margin type is DISTANCE)
        
            Returns:
                resized geometric body shape with the margin
        
        
        """
        ...

class UserIAUCelestialBody(AbstractIAUCelestialBody):
    """
    public class UserIAUCelestialBody extends :class:`~fr.cnes.sirius.patrius.bodies.AbstractIAUCelestialBody`
    
        User-defined IAU celestial body. It can be used to define any celestial body with:
    
          - Its name
          - A :class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider` providing body position-velocity through
            time
          - Its gravitational constant
          - Its pole motion (reference data are provided by IAU)
    
    
        Since:
            4.14
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, celestialBodyIAUOrientation: CelestialBodyIAUOrientation, frame: fr.cnes.sirius.patrius.frames.Frame, bodyShape: BodyShape): ...
    @typing.overload
    def __init__(self, string: str, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, double: float, celestialBodyIAUOrientation: CelestialBodyIAUOrientation, frame: fr.cnes.sirius.patrius.frames.Frame, bodyShape: BodyShape, spiceJ2000ConventionEnum: fr.cnes.sirius.patrius.bodies.bsp.BSPEphemerisLoader.SpiceJ2000ConventionEnum): ...
    @typing.overload
    def __init__(self, string: str, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, gravityModel: fr.cnes.sirius.patrius.forces.gravity.GravityModel, celestialBodyIAUOrientation: CelestialBodyIAUOrientation, frame: fr.cnes.sirius.patrius.frames.Frame, bodyShape: BodyShape): ...
    @typing.overload
    def __init__(self, string: str, pVCoordinatesProvider: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinatesProvider, gravityModel: fr.cnes.sirius.patrius.forces.gravity.GravityModel, celestialBodyIAUOrientation: CelestialBodyIAUOrientation, frame: fr.cnes.sirius.patrius.frames.Frame, bodyShape: BodyShape, spiceJ2000ConventionEnum: fr.cnes.sirius.patrius.bodies.bsp.BSPEphemerisLoader.SpiceJ2000ConventionEnum): ...
    def toString(self) -> str:
        """
            Returns a string representation of the celestial point and its attributes.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.bodies.CelestialPoint.toString` in
                interface :class:`~fr.cnes.sirius.patrius.bodies.CelestialPoint`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.bodies.AbstractIAUCelestialBody.toString` in
                class :class:`~fr.cnes.sirius.patrius.bodies.AbstractIAUCelestialBody`
        
            Returns:
                a string representation of the celestial point and its attributes
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("fr.cnes.sirius.patrius.bodies")``.

    AbstractBodyPoint: typing.Type[AbstractBodyPoint]
    AbstractBodyShape: typing.Type[AbstractBodyShape]
    AbstractCelestialBody: typing.Type[AbstractCelestialBody]
    AbstractCelestialPoint: typing.Type[AbstractCelestialPoint]
    AbstractEllipsoidBodyShape: typing.Type[AbstractEllipsoidBodyShape]
    AbstractIAUCelestialBody: typing.Type[AbstractIAUCelestialBody]
    AbstractJPLCelestialBodyLoader: typing.Type[AbstractJPLCelestialBodyLoader]
    ApparentRadiusProvider: typing.Type[ApparentRadiusProvider]
    BSPCelestialBodyLoader: typing.Type[BSPCelestialBodyLoader]
    BasicBoardSun: typing.Type[BasicBoardSun]
    BasicCelestialPoint: typing.Type[BasicCelestialPoint]
    BodyPoint: typing.Type[BodyPoint]
    BodyShape: typing.Type[BodyShape]
    CelestialBody: typing.Type[CelestialBody]
    CelestialBodyEphemeris: typing.Type[CelestialBodyEphemeris]
    CelestialBodyEphemerisLoader: typing.Type[CelestialBodyEphemerisLoader]
    CelestialBodyFactory: typing.Type[CelestialBodyFactory]
    CelestialBodyIAUOrientation: typing.Type[CelestialBodyIAUOrientation]
    CelestialBodyLoader: typing.Type[CelestialBodyLoader]
    CelestialBodyOrientation: typing.Type[CelestialBodyOrientation]
    CelestialBodyTabulatedOrientation: typing.Type[CelestialBodyTabulatedOrientation]
    CelestialPoint: typing.Type[CelestialPoint]
    ConstantRadiusProvider: typing.Type[ConstantRadiusProvider]
    Earth: typing.Type[Earth]
    EarthEphemeris: typing.Type[EarthEphemeris]
    EllipsoidBodyShape: typing.Type[EllipsoidBodyShape]
    EllipsoidPoint: typing.Type[EllipsoidPoint]
    IAUCelestialBody: typing.Type[IAUCelestialBody]
    IAUPoleCoefficients: typing.Type[IAUPoleCoefficients]
    IAUPoleCoefficients1D: typing.Type[IAUPoleCoefficients1D]
    IAUPoleFactory: typing.Type[IAUPoleFactory]
    IAUPoleFunction: typing.Type[IAUPoleFunction]
    IAUPoleFunctionType: typing.Type[IAUPoleFunctionType]
    IAUPoleModelType: typing.Type[IAUPoleModelType]
    JPLCelestialBodyLoader: typing.Type[JPLCelestialBodyLoader]
    JPLEphemerisLoader: typing.Type[JPLEphemerisLoader]
    JPLHistoricEphemerisLoader: typing.Type[JPLHistoricEphemerisLoader]
    LLHCoordinates: typing.Type[LLHCoordinates]
    LLHCoordinatesSystem: typing.Type[LLHCoordinatesSystem]
    MeeusMoon: typing.Type[MeeusMoon]
    MeeusSun: typing.Type[MeeusSun]
    OneAxisEllipsoid: typing.Type[OneAxisEllipsoid]
    PosVelChebyshev: typing.Type[PosVelChebyshev]
    PredefinedEphemerisType: typing.Type[PredefinedEphemerisType]
    StarConvexBodyShape: typing.Type[StarConvexBodyShape]
    ThreeAxisEllipsoid: typing.Type[ThreeAxisEllipsoid]
    UserCelestialBody: typing.Type[UserCelestialBody]
    UserCelestialBodyLoader: typing.Type[UserCelestialBodyLoader]
    UserIAUCelestialBody: typing.Type[UserIAUCelestialBody]
    UserIAUPole: typing.Type[UserIAUPole]
    VariableRadiusProvider: typing.Type[VariableRadiusProvider]
    bsp: fr.cnes.sirius.patrius.bodies.bsp.__module_protocol__
    mesh: fr.cnes.sirius.patrius.bodies.mesh.__module_protocol__
