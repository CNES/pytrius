
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import fr.cnes.sirius.patrius.math
import fr.cnes.sirius.patrius.math.analysis
import fr.cnes.sirius.patrius.math.analysis.differentiation
import fr.cnes.sirius.patrius.math.analysis.integration
import fr.cnes.sirius.patrius.math.complex
import fr.cnes.sirius.patrius.math.exception
import fr.cnes.sirius.patrius.math.exception.util
import fr.cnes.sirius.patrius.math.geometry
import fr.cnes.sirius.patrius.math.geometry.euclidean.oned
import fr.cnes.sirius.patrius.math.geometry.euclidean.twod
import fr.cnes.sirius.patrius.math.geometry.partitioning
import fr.cnes.sirius.patrius.math.linear
import fr.cnes.sirius.patrius.orbits.pvcoordinates
import fr.cnes.sirius.patrius.time
import java.io
import java.lang
import java.text
import java.util
import jpype
import typing



class AzimuthElevationCalculator:
    """
    public final class AzimuthElevationCalculator extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`
    
        Compute mathematical Azimuth and Elevation of a Point, defined by its Cartesian coordinates in a Frame whose x, y axis
        and "Reference Azimuth" axis are in the same Plane. Frame x axis is defined by its frameOrientation (counted trigowise,
        not clockwise !) from the "Reference Azimuth", z axis points to the zenith and y axis completes the right-handed
        trihedra. The Point Azimuth is the angle (counted clockwise) from the "Reference Azymuth" The Point Elevation is the
        angle (counted trigowise) from the x,y plane and the Point
    
        Since:
            4.6.1
    """
    @staticmethod
    def computeAzimuthRate(pVCoordinates: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates) -> float:
        """
            Compute the azimuth rate of a point defined by its Cartesian coordinates in a Frame whose x, y and "Reference Azimuth"
            axis are in the same Plane.
        
            Parameters:
                extPVTopo (:class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates`): point in Cartesian coordinates which shall be transformed
        
            Returns:
                azimuth rate
        
        
        """
        ...
    @staticmethod
    def computeCartesianUnitPV(double: float, double2: float, double3: float, double4: float, double5: float) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates:
        """
            Compute the cartesian unit vector corresponding to the provided azimuth/elevation angles and their derivatives.
        
            Parameters:
                azimuth (double): The azimuth
                azimuthDot (double): The azimuth derivative
                elevation (double): The elevation
                elevationDot (double): The elevation derivative
                frameOrientation (double): Oriented (trigowise) angle between the "Reference Azimuth" and the Frame's x axis
        
            Returns:
                the cartesian unit vector
        
        
        """
        ...
    @staticmethod
    def computeCartesianUnitPosition(double: float, double2: float, double3: float) -> 'Vector3D':
        """
            Compute the cartesian unit vector corresponding to the provided azimuth/elevation angles.
        
            Parameters:
                azimuth (double): The azimuth
                elevation (double): The elevation
                frameOrientation (double): Oriented (trigowise) angle between the "Reference Azimuth" and the Frame's x axis
        
            Returns:
                the cartesian unit vector
        
        
        """
        ...
    @staticmethod
    def computeDAzimuth(vector3D: 'Vector3D') -> 'Vector3D':
        """
            Compute the azimuth derivative of a point defined by its Cartesian coordinates in a Frame whose x, y and "Reference
            Azimuth" axis are in the same Plane.
        
            Parameters:
                extTopo (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): point in Cartesian coordinates which shall be transformed
        
            Returns:
                the azimuth derivative of a point given in Cartesian coordinates in the local topocentric frame
        
        
        """
        ...
    @staticmethod
    def computeDElevation(vector3D: 'Vector3D') -> 'Vector3D':
        """
            Compute the elevation derivative of a point defined by its Cartesian coordinates in a Frame whose x, y and "Reference
            Azimuth" axis are in the same Plane.
        
            Parameters:
                extTopo (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): point in Cartesian coordinates which shall be transformed
        
            Returns:
                the elevation derivative of a point given in Cartesian coordinates in the local topocentric frame
        
        
        """
        ...
    @staticmethod
    def computeElevationRate(pVCoordinates: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates) -> float:
        """
            Compute the elevation rate of a point defined by its Cartesian coordinates in a Frame whose x, y and "Reference Azimuth"
            axis are in the same Plane
        
            Parameters:
                extPVTopo (:class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates`): point in Cartesian coordinates which shall be transformed
        
            Returns:
                elevation rate
        
        
        """
        ...
    @staticmethod
    def getAzimuth(vector3D: 'Vector3D', double: float) -> float:
        """
            Compute the Azimuth of a point defined by its Cartesian coordinates in a Frame whose x, y and "Reference Azimuth" axis
            are in the same Plane
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): Point Cartesian coordinates / Frame
                frameOrientation (double): Oriented (trigowise) angle (radian) between the "Reference Azimuth" and the Frame's x axis
        
        
        Example : If "Reference Azimuth" is aligned with the local North of a local topocentric frame then a frameOrientation of
                    -0.785 (=> -45°) means that the x axis of the Frame points to North-East
        
            Returns:
                azimuth The angle (clockwise, radian) between the "Reference Azimuth" and the point projected in x,y plane
        
        
        """
        ...
    @staticmethod
    def getElevation(vector3D: 'Vector3D') -> float:
        """
            Compute the Elevation of a point defined by its Cartesian coordinates in a Frame whose x, y and "Reference Azimuth" axis
            are in the same Plane
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): Point Cartesian coordinates / Frame
        
            Returns:
                elevation The angle (trigowise, radian) between the x,y plane and the point
        
        
        """
        ...

class CardanCalculator:
    """
    public final class CardanCalculator extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`
    
        Compute X and Y Cardan angles of a point, defined by its Cartesian coordinates in a frame whose Y, Z axis, local
        vertical and west directions axis are in the same Plane. The X-angle is the angle from the "Local Vertical", in the
        (local vertical - west) plane. This angle is defined in [ :code:`-PI` ; :code:`PI`) and oriented trigowise.
    
    
        The Y-angle is the angle of rotation of the mounting around Y'. Y' is the image of West axis by the rotation of X-angle
        around North axis. This angle is defined in [:code:`-PI/2` ; :code:`PI/2`] and oriented by Y'.
    
        Since:
            4.13
    """
    @staticmethod
    def computeCartesianUnitPV(double: float, double2: float, double3: float, double4: float, double5: float) -> fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates:
        """
            Compute the cartesian unit vector corresponding to the provided cardan angles.
        
            Parameters:
                xAngle (double): The cardan x-angle
                xAngleDot (double): The cardan x-angle derivative
                yAngle (double): The cardan y-angle
                yAngleDot (double): The cardan y-angle derivative
                frameOrientation (double): Topocentric frame orientation around the local north and the x-axis (trigowise)
        
            Returns:
                the cartesian unit vector
        
        
        """
        ...
    @staticmethod
    def computeCartesianUnitPosition(double: float, double2: float, double3: float) -> 'Vector3D':
        """
            Compute the cartesian unit vector corresponding to the provided cardan angles.
        
            Parameters:
                xAngle (double): The cardan x-angle
                yAngle (double): The cardan y-angle
                frameOrientation (double): Topocentric frame orientation around the local north and the x-axis (trigowise)
        
            Returns:
                the cartesian unit vector
        
        
        """
        ...
    @staticmethod
    def computeDXangle(vector3D: 'Vector3D', double: float) -> 'Vector3D':
        """
            Get the X-angle derivative of a point wrt the local point (dX) expressed in the oriented topocentric frame.
        
        
            The angles are oriented trigowise.
        
            Parameters:
                vectInTopoFrame (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): Point in cartesian coordinates which shall be transformed
                frameOrientation (double): Topocentric frame orientation around the local north and the X-axis (trigowise)
        
            Returns:
                X-angle derivative
        
        
        """
        ...
    @staticmethod
    def computeDYangle(vector3D: 'Vector3D', double: float) -> 'Vector3D':
        """
            Get the Y-angle derivative of a point wrt the local point (dY) expressed in the oriented topocentric frame.
        
            Parameters:
                vectInTopoFrame (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): point in cartesian coordinates which shall be transformed
                frameOrientation (double): Topocentric frame orientation around the local north and the X-axis (trigowise)
        
            Returns:
                Y-angle derivative
        
        
        """
        ...
    @staticmethod
    def computeXangle(vector3D: 'Vector3D', double: float) -> float:
        """
            Compute the X-angle of a point given in cartesian coordinates in a local topocentric frame.
        
        
            The X-angle is defined in [:code:`-PI` ; :code:`PI`), and oriented trigowise.
        
            Parameters:
                extTopo (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): Point in cartesian coordinates which shall be transformed
                frameOrientation (double): Topocentric frame orientation around the local north and the X-axis (trigowise)
        
            Returns:
                X-angle
        
        
        """
        ...
    @staticmethod
    def computeXangleRate(pVCoordinates: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates, double: float) -> float:
        """
            Compute the X-angle rate of a point given in Cartesian coordinates in the local topocentric frame.
        
        
            The X-angle rate is oriented trigowise.
        
            Parameters:
                extPVTopoOld (:class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates`): Point in Cartesian coordinates which shall be transformed
                frameOrientation (double): Topocentric frame orientation around the local north and the X-axis (trigowise)
        
            Returns:
                X-angle rate
        
        
        """
        ...
    @staticmethod
    def computeYangle(vector3D: 'Vector3D', double: float) -> float:
        """
            Compute the Y-angle of a point given in Cartesian coordinates in the local topocentric frame.
        
        
            The Y-angle is defined in [:code:`-PI/2` ; :code:`PI/2`].
        
            Parameters:
                extTopo (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): Point in Cartesian coordinates which shall be transformed
                frameOrientation (double): Topocentric frame orientation around the local north and the X-axis (trigowise)
        
            Returns:
                Y-angle
        
        
        """
        ...
    @staticmethod
    def computeYangleRate(pVCoordinates: fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates, double: float) -> float:
        """
            Compute the Y-angle rate of a point given in Cartesian coordinates in the local topocentric frame.
        
            Parameters:
                extPVTopoOld (:class:`~fr.cnes.sirius.patrius.orbits.pvcoordinates.PVCoordinates`): Point in Cartesian coordinates which shall be transformed
                frameOrientation (double): Topocentric frame orientation around the local north and the x-axis (trigowise)
        
            Returns:
                Y-angle rate
        
        
        """
        ...

class CrossSectionProvider:
    """
    public interface CrossSectionProvider
    
    
        Interface for all geometric objects that can provide their cross section from a direction defined by a Vector3D.
    
        Since:
            1.0
    """
    def getCrossSection(self, vector3D: 'Vector3D') -> float:
        """
            Computes the cross section from the direction defined by a Vector3D.
        
            Parameters:
                direction (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): the direction vector
        
            Returns:
                the cross section
        
        
        """
        ...

class Euclidean3D(fr.cnes.sirius.patrius.math.geometry.Space):
    """
    public final class Euclidean3D extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.Space`
    
        This class implements a three-dimensional space.
    
        Since:
            3.0
    
        Also see:
            :meth:`~serialized`
    """
    def getDimension(self) -> int:
        """
            Get the dimension of the space.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Space.getDimension` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Space`
        
            Returns:
                dimension of the space
        
        
        """
        ...
    @staticmethod
    def getInstance() -> 'Euclidean3D':
        """
            Get the unique instance.
        
            Returns:
                the unique instance
        
        
        """
        ...
    def getSubSpace(self) -> fr.cnes.sirius.patrius.math.geometry.euclidean.twod.Euclidean2D:
        """
            Get the n-1 dimension subspace of this space.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Space.getSubSpace` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Space`
        
            Returns:
                n-1 dimension sub-space of this space
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Space.getDimension`
        
        
        """
        ...

_FieldRotation__T = typing.TypeVar('_FieldRotation__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
class FieldRotation(java.io.Serializable, typing.Generic[_FieldRotation__T]):
    """
    public class FieldRotation<T extends :class:`~fr.cnes.sirius.patrius.math.RealFieldElement`<T>> extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        This class is a re-implementation of :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation` using
        :class:`~fr.cnes.sirius.patrius.math.RealFieldElement`.
    
        Instance of this class are guaranteed to be immutable.
    
        Since:
            3.1
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`,
            :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, t: _FieldRotation__T, t2: _FieldRotation__T, t3: _FieldRotation__T, t4: _FieldRotation__T, boolean: bool): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[typing.MutableSequence[_FieldRotation__T]], jpype.JArray], double: float): ...
    @typing.overload
    def __init__(self, fieldVector3D: 'FieldVector3D'[_FieldRotation__T], t: _FieldRotation__T): ...
    @typing.overload
    def __init__(self, fieldVector3D: 'FieldVector3D'[_FieldRotation__T], fieldVector3D2: 'FieldVector3D'[_FieldRotation__T]): ...
    @typing.overload
    def __init__(self, fieldVector3D: 'FieldVector3D'[_FieldRotation__T], fieldVector3D2: 'FieldVector3D'[_FieldRotation__T], fieldVector3D3: 'FieldVector3D'[_FieldRotation__T], fieldVector3D4: 'FieldVector3D'[_FieldRotation__T]): ...
    @typing.overload
    def __init__(self, rotationOrder: 'RotationOrder', t: _FieldRotation__T, t2: _FieldRotation__T, t3: _FieldRotation__T): ...
    _applyInverseTo_4__T = typing.TypeVar('_applyInverseTo_4__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    _applyInverseTo_5__T = typing.TypeVar('_applyInverseTo_5__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    @typing.overload
    def applyInverseTo(self, fieldRotation: 'FieldRotation'[_FieldRotation__T]) -> 'FieldRotation'[_FieldRotation__T]: ...
    @typing.overload
    def applyInverseTo(self, rotation: 'Rotation') -> 'FieldRotation'[_FieldRotation__T]: ...
    @typing.overload
    def applyInverseTo(self, fieldVector3D: 'FieldVector3D'[_FieldRotation__T]) -> 'FieldVector3D'[_FieldRotation__T]: ...
    @typing.overload
    def applyInverseTo(self, vector3D: 'Vector3D') -> 'FieldVector3D'[_FieldRotation__T]: ...
    @typing.overload
    @staticmethod
    def applyInverseTo(rotation: 'Rotation', fieldRotation: 'FieldRotation'[_applyInverseTo_4__T]) -> 'FieldRotation'[_applyInverseTo_4__T]:
        """
            Apply the inverse of a rotation to a vector.
        
            Parameters:
                r (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation`): rotation to apply
                u (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> u): vector to apply the inverse of the rotation to
        
            Returns:
                a new vector which such that u is its image by the rotation
        
        public :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`> applyInverseTo(:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`> r)
        
            Apply the inverse of the instance to another rotation.
        
            Applying the inverse of the instance to a rotation is creating a composed rotation in the following order :
        
            R3 = R2.applyInverseTo(R1) is equivalent to R3 = R2 :sup:`-1` o R1
        
            Example :
        
            The vector u being transformed into v by R1 : v = R1(u)
        
            The vector v being transformed into w by R2 :sup:`-1` : w = R2 :sup:`-1` (v)
        
            w = R2 :sup:`-1` (v) = R2 :sup:`-1` (R1(u)) = R2 :sup:`-1` o R1(u) = R3(u)
        
            Parameters:
                r (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`> r): rotation to apply the rotation to
        
            Returns:
                a new rotation which is the composition of r by the inverse of the instance
        
        public :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`> applyInverseTo(:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation` r)
        
            Apply the inverse of the instance to another rotation.
        
            Applying the inverse of the instance to a rotation is creating a composed rotation in the following order :
        
            R3 = R2.applyInverseTo(R1) is equivalent to R3 = R2 :sup:`-1` o R1
        
            Example :
        
            The vector u being transformed into v by R1 : v = R1(u)
        
            The vector v being transformed into w by R2 :sup:`-1` : w = R2 :sup:`-1` (v)
        
            w = R2 :sup:`-1` (v) = R2 :sup:`-1` (R1(u)) = R2 :sup:`-1` o R1(u) = R3(u)
        
            Parameters:
                r (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation`): rotation to apply the rotation to
        
            Returns:
                a new rotation which is the composition of r by the inverse of the instance
        
            Apply the inverse of the a rotation to another rotation.
        
            Applying the inverse of the instance to a rotation is creating a composed rotation in the following order :
        
            R3 = R2.applyInverseTo(R1) is equivalent to R3 = R2 :sup:`-1` o R1
        
            Example :
        
            The vector u being transformed into v by R1 : v = R1(u)
        
            The vector v being transformed into w by R2 :sup:`-1` : w = R2 :sup:`-1` (v)
        
            w = R2 :sup:`-1` (v) = R2 :sup:`-1` (R1(u)) = R2 :sup:`-1` o R1(u) = R3(u)
        
            Parameters:
                rOuter (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation`): rotation to apply the rotation to
                rInner (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`<T> rInner): rotation to apply the rotation to
        
            Returns:
                a new rotation which is the composition of r by the inverse of the instance
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def applyInverseTo(rotation: 'Rotation', fieldVector3D: 'FieldVector3D'[_applyInverseTo_5__T]) -> 'FieldVector3D'[_applyInverseTo_5__T]: ...
    @typing.overload
    def applyInverseTo(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], tArray: typing.Union[typing.List[_FieldRotation__T], jpype.JArray]) -> None:
        """
            Apply the inverse of the rotation to a vector stored in an array. The image v' of a vector v applying the inverse of the
            rotation is v' = Q'.v.Q.
        
            Parameters:
                vIn (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`[]): an array with three items which stores vector to rotate
                vOut (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`[]): an array with three items to put result to (it can be the same array as in)
        
            Apply the inverse of the rotation to a vector stored in an array.
        
            Parameters:
                vIn (double[]): an array with three items which stores vector to rotate
                vOut (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`[]): an array with three items to put result to
        
        """
        ...
    @typing.overload
    def applyInverseTo(self, tArray: typing.Union[typing.List[_FieldRotation__T], jpype.JArray], tArray2: typing.Union[typing.List[_FieldRotation__T], jpype.JArray]) -> None: ...
    _applyTo_4__T = typing.TypeVar('_applyTo_4__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    _applyTo_5__T = typing.TypeVar('_applyTo_5__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    @typing.overload
    def applyTo(self, fieldRotation: 'FieldRotation'[_FieldRotation__T]) -> 'FieldRotation'[_FieldRotation__T]: ...
    @typing.overload
    def applyTo(self, rotation: 'Rotation') -> 'FieldRotation'[_FieldRotation__T]: ...
    @typing.overload
    def applyTo(self, fieldVector3D: 'FieldVector3D'[_FieldRotation__T]) -> 'FieldVector3D'[_FieldRotation__T]: ...
    @typing.overload
    def applyTo(self, vector3D: 'Vector3D') -> 'FieldVector3D'[_FieldRotation__T]: ...
    @typing.overload
    @staticmethod
    def applyTo(rotation: 'Rotation', fieldRotation: 'FieldRotation'[_applyTo_4__T]) -> 'FieldRotation'[_applyTo_4__T]:
        """
            Apply a rotation to a vector.
        
            Parameters:
                r (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation`): rotation to apply
                u (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> u): vector to apply the rotation to
        
            Returns:
                a new vector which is the image of u by the rotation
        
        public :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`> applyTo(:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`> r)
        
            Apply the instance to another rotation.
        
            Applying the instance to a rotation is creating a composed rotation in the following order :
        
            R3 = R2.applyTo(R1) is equivalent to R3 = R2 o R1
        
            Example :
        
            The vector u being transformed into v by R1 : v = R1(u)
        
            The vector v being transformed into w by R2 : w = R2(v)
        
            w = R2(v) = R2(R1(u)) = R2 o R1(u) = R3(u)
        
            Parameters:
                r (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`> r): rotation to apply the rotation to
        
            Returns:
                a new rotation which is the composition of r by the instance
        
        public :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`> applyTo(:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation` r)
        
            Apply the instance to another rotation.
        
            Applying the instance to a rotation is creating a composed rotation in the following order :
        
            R3 = R2.applyTo(R1) is equivalent to R3 = R2 o R1
        
            Example :
        
            The vector u being transformed into v by R1 : v = R1(u)
        
            The vector v being transformed into w by R2 : w = R2(v)
        
            w = R2(v) = R2(R1(u)) = R2 o R1(u) = R3(u)
        
            Parameters:
                r (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation`): rotation to apply the rotation to
        
            Returns:
                a new rotation which is the composition of r by the instance
        
            Apply a rotation to another rotation.
        
            Applying the instance to a rotation is creating a composed rotation in the following order :
        
            R3 = R2.applyTo(R1) is equivalent to R3 = R2 o R1
        
            Example :
        
            The vector u being transformed into v by R1 : v = R1(u)
        
            The vector v being transformed into w by R2 : w = R2(v)
        
            w = R2(v) = R2(R1(u)) = R2 o R1(u) = R3(u)
        
            Parameters:
                r1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation`): rotation to apply
                rInner (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`<T> rInner): rotation to apply the rotation to
        
            Returns:
                a new rotation which is the composition of r by the instance
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def applyTo(rotation: 'Rotation', fieldVector3D: 'FieldVector3D'[_applyTo_5__T]) -> 'FieldVector3D'[_applyTo_5__T]: ...
    @typing.overload
    def applyTo(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], tArray: typing.Union[typing.List[_FieldRotation__T], jpype.JArray]) -> None:
        """
            Apply the rotation to a vector stored in an array. The image v' of a vector v is v' = Q.v.Q'.
        
            Parameters:
                vIn (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`[]): an array with three items which stores vector to rotate
                vOut (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`[]): an array with three items to put result to (it can be the same array as in)
        
            Apply the rotation to a vector stored in an array. The image v' of a vector v is v' = Q.v.Q'.
        
            Parameters:
                vIn (double[]): an array with three items which stores vector to rotate
                vOut (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`[]): an array with three items to put result to
        
        """
        ...
    @typing.overload
    def applyTo(self, tArray: typing.Union[typing.List[_FieldRotation__T], jpype.JArray], tArray2: typing.Union[typing.List[_FieldRotation__T], jpype.JArray]) -> None: ...
    _distance__T = typing.TypeVar('_distance__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    @staticmethod
    def distance(fieldRotation: 'FieldRotation'[_distance__T], fieldRotation2: 'FieldRotation'[_distance__T]) -> _distance__T:
        """
            Compute the *distance* between two rotations.
        
            The *distance* is intended here as a way to check if two rotations are almost similar (i.e. they transform vectors the
            same way) or very different. It is mathematically defined as the angle of the rotation r that prepended to one of the
            rotations gives the other one:
        
            .. code-block: java
            
            
                    r :sub:`1` (r) = r :sub:`2` 
             
        
            This distance is an angle between 0 and π. Its value is the smallest possible upper bound of the angle in radians
            between r :sub:`1` (v) and r :sub:`2` (v) for all possible vectors v. This upper bound is reached for some v. The
            distance is equal to 0 if and only if the two rotations are identical.
        
            Comparing two rotations should always be done using this value rather than for example comparing the components of the
            quaternions. It is much more stable, and has a geometric meaning. Also comparing quaternions components is error prone
            since for example quaternions (0.36, 0.48, -0.48, -0.64) and (-0.36, -0.48, 0.48, 0.64) represent exactly the same
            rotation despite their components are different (they are exact opposites).
        
            Parameters:
                r1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`<T> r1): first rotation
                r2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation`<T> r2): second rotation
        
            Returns:
                *distance* between r1 and r2
        
        
        """
        ...
    def getAngle(self) -> _FieldRotation__T:
        """
            Get the angle of the rotation.
        
            Returns:
                angle of the rotation (between 0 and π)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldRotation.FieldRotation`
        
        
        """
        ...
    def getAngles(self, rotationOrder: 'RotationOrder') -> typing.MutableSequence[_FieldRotation__T]:
        """
            Get the Cardan or Euler angles corresponding to the instance.
        
            The equations show that each rotation can be defined by two different values of the Cardan or Euler angles set. For
            example if Cardan angles are used, the rotation defined by the angles a :sub:`1` , a :sub:`2` and a :sub:`3` is the same
            as the rotation defined by the angles π + a :sub:`1` , π - a :sub:`2` and π + a :sub:`3` . This method implements the
            following arbitrary choices:
        
              - for Cardan angles, the chosen set is the one for which the second angle is between -π/2 and π/2 (i.e its cosine is
                positive),
              - for Euler angles, the chosen set is the one for which the second angle is between 0 and π (i.e its sine is positive).
        
        
            Cardan and Euler angle have a very disappointing drawback: all of them have singularities. For Cardan angles, this is
            often called gimbal lock. There is *nothing* to do to prevent this, it is an intrinsic problem with Cardan and Euler
            representation (but not a problem with the rotation itself, which is perfectly well defined). For Cardan angles,
            singularities occur when the second angle is close to -π/2 or +π/2, for Euler angle singularities occur when the
            second angle is close to 0 or π, this implies that the identity rotation is always singular for Euler angles!
        
            Parameters:
                order (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder`): rotation order to use
        
            Returns:
                an array of three angles, in the order specified by the set
        
        
        """
        ...
    def getAxis(self) -> 'FieldVector3D'[_FieldRotation__T]: ...
    def getMatrix(self) -> typing.MutableSequence[typing.MutableSequence[_FieldRotation__T]]:
        """
            Get the 3X3 matrix corresponding to the instance
        
            Returns:
                the matrix corresponding to the instance
        
        
        """
        ...
    def getQ0(self) -> _FieldRotation__T:
        """
            Get the scalar coordinate of the quaternion.
        
            Returns:
                scalar coordinate of the quaternion
        
        
        """
        ...
    def getQ1(self) -> _FieldRotation__T:
        """
            Get the first coordinate of the vectorial part of the quaternion.
        
            Returns:
                first coordinate of the vectorial part of the quaternion
        
        
        """
        ...
    def getQ2(self) -> _FieldRotation__T:
        """
            Get the second coordinate of the vectorial part of the quaternion.
        
            Returns:
                second coordinate of the vectorial part of the quaternion
        
        
        """
        ...
    def getQ3(self) -> _FieldRotation__T:
        """
            Get the third coordinate of the vectorial part of the quaternion.
        
            Returns:
                third coordinate of the vectorial part of the quaternion
        
        
        """
        ...
    def revert(self) -> 'FieldRotation'[_FieldRotation__T]: ...
    def toRotation(self) -> 'Rotation':
        """
            Convert to a constant vector without derivatives.
        
            Returns:
                a constant vector
        
        
        """
        ...

_FieldVector3D__T = typing.TypeVar('_FieldVector3D__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
class FieldVector3D(java.io.Serializable, typing.Generic[_FieldVector3D__T]):
    """
    public class FieldVector3D<T extends :class:`~fr.cnes.sirius.patrius.math.RealFieldElement`<T>> extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        This class is a re-implementation of :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` using
        :class:`~fr.cnes.sirius.patrius.math.RealFieldElement`.
    
        Instance of this class are guaranteed to be immutable.
    
        Since:
            3.1
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T]): ...
    @typing.overload
    def __init__(self, double: float, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T], double2: float, fieldVector3D2: 'FieldVector3D'[_FieldVector3D__T]): ...
    @typing.overload
    def __init__(self, double: float, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T], double2: float, fieldVector3D2: 'FieldVector3D'[_FieldVector3D__T], double3: float, fieldVector3D3: 'FieldVector3D'[_FieldVector3D__T]): ...
    @typing.overload
    def __init__(self, double: float, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T], double2: float, fieldVector3D2: 'FieldVector3D'[_FieldVector3D__T], double3: float, fieldVector3D3: 'FieldVector3D'[_FieldVector3D__T], double4: float, fieldVector3D4: 'FieldVector3D'[_FieldVector3D__T]): ...
    @typing.overload
    def __init__(self, t: _FieldVector3D__T, t2: _FieldVector3D__T): ...
    @typing.overload
    def __init__(self, t: _FieldVector3D__T, t2: _FieldVector3D__T, t3: _FieldVector3D__T): ...
    @typing.overload
    def __init__(self, t: _FieldVector3D__T, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T]): ...
    @typing.overload
    def __init__(self, t: _FieldVector3D__T, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T], t2: _FieldVector3D__T, fieldVector3D2: 'FieldVector3D'[_FieldVector3D__T]): ...
    @typing.overload
    def __init__(self, t: _FieldVector3D__T, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T], t2: _FieldVector3D__T, fieldVector3D2: 'FieldVector3D'[_FieldVector3D__T], t3: _FieldVector3D__T, fieldVector3D3: 'FieldVector3D'[_FieldVector3D__T]): ...
    @typing.overload
    def __init__(self, t: _FieldVector3D__T, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T], t2: _FieldVector3D__T, fieldVector3D2: 'FieldVector3D'[_FieldVector3D__T], t3: _FieldVector3D__T, fieldVector3D3: 'FieldVector3D'[_FieldVector3D__T], t4: _FieldVector3D__T, fieldVector3D4: 'FieldVector3D'[_FieldVector3D__T]): ...
    @typing.overload
    def __init__(self, t: _FieldVector3D__T, vector3D: 'Vector3D'): ...
    @typing.overload
    def __init__(self, t: _FieldVector3D__T, vector3D: 'Vector3D', t2: _FieldVector3D__T, vector3D2: 'Vector3D'): ...
    @typing.overload
    def __init__(self, t: _FieldVector3D__T, vector3D: 'Vector3D', t2: _FieldVector3D__T, vector3D2: 'Vector3D', t3: _FieldVector3D__T, vector3D3: 'Vector3D'): ...
    @typing.overload
    def __init__(self, t: _FieldVector3D__T, vector3D: 'Vector3D', t2: _FieldVector3D__T, vector3D2: 'Vector3D', t3: _FieldVector3D__T, vector3D3: 'Vector3D', t4: _FieldVector3D__T, vector3D4: 'Vector3D'): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_FieldVector3D__T], jpype.JArray]): ...
    @typing.overload
    def add(self, double: float, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T]) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def add(self, double: float, vector3D: 'Vector3D') -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def add(self, t: _FieldVector3D__T, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T]) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def add(self, t: _FieldVector3D__T, vector3D: 'Vector3D') -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def add(self, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T]) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def add(self, vector3D: 'Vector3D') -> 'FieldVector3D'[_FieldVector3D__T]: ...
    _angle_0__T = typing.TypeVar('_angle_0__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    _angle_1__T = typing.TypeVar('_angle_1__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    _angle_2__T = typing.TypeVar('_angle_2__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def angle(fieldVector3D: 'FieldVector3D'[_angle_0__T], fieldVector3D2: 'FieldVector3D'[_angle_0__T]) -> _angle_0__T:
        """
            Compute the angular separation between two vectors.
        
            This method computes the angular separation between two vectors using the dot product for well separated vectors and the
            cross product for almost aligned vectors. This allows to have a good accuracy in all cases, even for vectors very close
            to each other.
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v1): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v2): second vector
        
            Returns:
                angular separation between v1 and v2
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathArithmeticException`: if either vector has a null norm
        
            Compute the angular separation between two vectors.
        
            This method computes the angular separation between two vectors using the dot product for well separated vectors and the
            cross product for almost aligned vectors. This allows to have a good accuracy in all cases, even for vectors very close
            to each other.
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v1): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                angular separation between v1 and v2
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathArithmeticException`: if either vector has a null norm
        
            Compute the angular separation between two vectors.
        
            This method computes the angular separation between two vectors using the dot product for well separated vectors and the
            cross product for almost aligned vectors. This allows to have a good accuracy in all cases, even for vectors very close
            to each other.
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v2): second vector
        
            Returns:
                angular separation between v1 and v2
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathArithmeticException`: if either vector has a null norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def angle(fieldVector3D: 'FieldVector3D'[_angle_1__T], vector3D: 'Vector3D') -> _angle_1__T: ...
    @typing.overload
    @staticmethod
    def angle(vector3D: 'Vector3D', fieldVector3D: 'FieldVector3D'[_angle_2__T]) -> _angle_2__T: ...
    _crossProduct_2__T = typing.TypeVar('_crossProduct_2__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    _crossProduct_3__T = typing.TypeVar('_crossProduct_3__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    _crossProduct_4__T = typing.TypeVar('_crossProduct_4__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    @typing.overload
    def crossProduct(self, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T]) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def crossProduct(self, vector3D: 'Vector3D') -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    @staticmethod
    def crossProduct(fieldVector3D: 'FieldVector3D'[_crossProduct_2__T], fieldVector3D2: 'FieldVector3D'[_crossProduct_2__T]) -> 'FieldVector3D'[_crossProduct_2__T]:
        """
            Compute the cross-product of two vectors.
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v1): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v2): second vector
        
            Returns:
                the cross product v1 ^ v2 as a new Vector
        
            Compute the cross-product of two vectors.
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v1): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the cross product v1 ^ v2 as a new Vector
        
            Compute the cross-product of two vectors.
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v2): second vector
        
            Returns:
                the cross product v1 ^ v2 as a new Vector
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def crossProduct(fieldVector3D: 'FieldVector3D'[_crossProduct_3__T], vector3D: 'Vector3D') -> 'FieldVector3D'[_crossProduct_3__T]: ...
    @typing.overload
    @staticmethod
    def crossProduct(vector3D: 'Vector3D', fieldVector3D: 'FieldVector3D'[_crossProduct_4__T]) -> 'FieldVector3D'[_crossProduct_4__T]: ...
    _distance_2__T = typing.TypeVar('_distance_2__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    _distance_3__T = typing.TypeVar('_distance_3__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    _distance_4__T = typing.TypeVar('_distance_4__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    @typing.overload
    def distance(self, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T]) -> _FieldVector3D__T:
        """
            Compute the distance between the instance and another vector according to the L :sub:`2` norm.
        
            Calling this method is equivalent to calling: :code:`q.subtract(p).getNorm()` except that no intermediate vector is
            built
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the distance between the instance and p according to the L :sub:`2` norm
        
        """
        ...
    @typing.overload
    def distance(self, vector3D: 'Vector3D') -> _FieldVector3D__T: ...
    @typing.overload
    @staticmethod
    def distance(fieldVector3D: 'FieldVector3D'[_distance_2__T], fieldVector3D2: 'FieldVector3D'[_distance_2__T]) -> _distance_2__T:
        """
            Compute the distance between two vectors according to the L :sub:`2` norm.
        
            Calling this method is equivalent to calling: :code:`v1.subtract(v2).getNorm()` except that no intermediate vector is
            built
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v1): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v2): second vector
        
            Returns:
                the distance between v1 and v2 according to the L :sub:`2` norm
        
            Compute the distance between two vectors according to the L :sub:`2` norm.
        
            Calling this method is equivalent to calling: :code:`v1.subtract(v2).getNorm()` except that no intermediate vector is
            built
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v1): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the distance between v1 and v2 according to the L :sub:`2` norm
        
            Compute the distance between two vectors according to the L :sub:`2` norm.
        
            Calling this method is equivalent to calling: :code:`v1.subtract(v2).getNorm()` except that no intermediate vector is
            built
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v2): second vector
        
            Returns:
                the distance between v1 and v2 according to the L :sub:`2` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance(fieldVector3D: 'FieldVector3D'[_distance_3__T], vector3D: 'Vector3D') -> _distance_3__T: ...
    @typing.overload
    @staticmethod
    def distance(vector3D: 'Vector3D', fieldVector3D: 'FieldVector3D'[_distance_4__T]) -> _distance_4__T: ...
    _distance1_2__T = typing.TypeVar('_distance1_2__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    _distance1_3__T = typing.TypeVar('_distance1_3__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    _distance1_4__T = typing.TypeVar('_distance1_4__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    @typing.overload
    def distance1(self, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T]) -> _FieldVector3D__T:
        """
            Compute the distance between the instance and another vector according to the L :sub:`1` norm.
        
            Calling this method is equivalent to calling: :code:`q.subtract(p).getNorm1()` except that no intermediate vector is
            built
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the distance between the instance and p according to the L :sub:`1` norm
        
        """
        ...
    @typing.overload
    def distance1(self, vector3D: 'Vector3D') -> _FieldVector3D__T: ...
    @typing.overload
    @staticmethod
    def distance1(fieldVector3D: 'FieldVector3D'[_distance1_2__T], fieldVector3D2: 'FieldVector3D'[_distance1_2__T]) -> _distance1_2__T:
        """
            Compute the distance between two vectors according to the L :sub:`1` norm.
        
            Calling this method is equivalent to calling: :code:`v1.subtract(v2).getNorm1()` except that no intermediate vector is
            built
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v1): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v2): second vector
        
            Returns:
                the distance between v1 and v2 according to the L :sub:`1` norm
        
            Compute the distance between two vectors according to the L :sub:`1` norm.
        
            Calling this method is equivalent to calling: :code:`v1.subtract(v2).getNorm1()` except that no intermediate vector is
            built
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v1): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the distance between v1 and v2 according to the L :sub:`1` norm
        
            Compute the distance between two vectors according to the L :sub:`1` norm.
        
            Calling this method is equivalent to calling: :code:`v1.subtract(v2).getNorm1()` except that no intermediate vector is
            built
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v2): second vector
        
            Returns:
                the distance between v1 and v2 according to the L :sub:`1` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance1(fieldVector3D: 'FieldVector3D'[_distance1_3__T], vector3D: 'Vector3D') -> _distance1_3__T: ...
    @typing.overload
    @staticmethod
    def distance1(vector3D: 'Vector3D', fieldVector3D: 'FieldVector3D'[_distance1_4__T]) -> _distance1_4__T: ...
    _distanceInf_2__T = typing.TypeVar('_distanceInf_2__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    _distanceInf_3__T = typing.TypeVar('_distanceInf_3__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    _distanceInf_4__T = typing.TypeVar('_distanceInf_4__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    @typing.overload
    def distanceInf(self, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T]) -> _FieldVector3D__T:
        """
            Compute the distance between the instance and another vector according to the L :sub:`∞` norm.
        
            Calling this method is equivalent to calling: :code:`q.subtract(p).getNormInf()` except that no intermediate vector is
            built
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the distance between the instance and p according to the L :sub:`∞` norm
        
        """
        ...
    @typing.overload
    def distanceInf(self, vector3D: 'Vector3D') -> _FieldVector3D__T: ...
    @typing.overload
    @staticmethod
    def distanceInf(fieldVector3D: 'FieldVector3D'[_distanceInf_2__T], fieldVector3D2: 'FieldVector3D'[_distanceInf_2__T]) -> _distanceInf_2__T:
        """
            Compute the distance between two vectors according to the L :sub:`∞` norm.
        
            Calling this method is equivalent to calling: :code:`v1.subtract(v2).getNormInf()` except that no intermediate vector is
            built
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v1): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v2): second vector
        
            Returns:
                the distance between v1 and v2 according to the L :sub:`∞` norm
        
            Compute the distance between two vectors according to the L :sub:`∞` norm.
        
            Calling this method is equivalent to calling: :code:`v1.subtract(v2).getNormInf()` except that no intermediate vector is
            built
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v1): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the distance between v1 and v2 according to the L :sub:`∞` norm
        
            Compute the distance between two vectors according to the L :sub:`∞` norm.
        
            Calling this method is equivalent to calling: :code:`v1.subtract(v2).getNormInf()` except that no intermediate vector is
            built
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v2): second vector
        
            Returns:
                the distance between v1 and v2 according to the L :sub:`∞` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceInf(fieldVector3D: 'FieldVector3D'[_distanceInf_3__T], vector3D: 'Vector3D') -> _distanceInf_3__T: ...
    @typing.overload
    @staticmethod
    def distanceInf(vector3D: 'Vector3D', fieldVector3D: 'FieldVector3D'[_distanceInf_4__T]) -> _distanceInf_4__T: ...
    _distanceSq_2__T = typing.TypeVar('_distanceSq_2__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    _distanceSq_3__T = typing.TypeVar('_distanceSq_3__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    _distanceSq_4__T = typing.TypeVar('_distanceSq_4__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    @typing.overload
    def distanceSq(self, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T]) -> _FieldVector3D__T:
        """
            Compute the square of the distance between the instance and another vector.
        
            Calling this method is equivalent to calling: :code:`q.subtract(p).getNormSq()` except that no intermediate vector is
            built
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the square of the distance between the instance and p
        
        """
        ...
    @typing.overload
    def distanceSq(self, vector3D: 'Vector3D') -> _FieldVector3D__T: ...
    @typing.overload
    @staticmethod
    def distanceSq(fieldVector3D: 'FieldVector3D'[_distanceSq_2__T], fieldVector3D2: 'FieldVector3D'[_distanceSq_2__T]) -> _distanceSq_2__T:
        """
            Compute the square of the distance between two vectors.
        
            Calling this method is equivalent to calling: :code:`v1.subtract(v2).getNormSq()` except that no intermediate vector is
            built
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v1): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v2): second vector
        
            Returns:
                the square of the distance between v1 and v2
        
            Compute the square of the distance between two vectors.
        
            Calling this method is equivalent to calling: :code:`v1.subtract(v2).getNormSq()` except that no intermediate vector is
            built
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v1): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the square of the distance between v1 and v2
        
            Compute the square of the distance between two vectors.
        
            Calling this method is equivalent to calling: :code:`v1.subtract(v2).getNormSq()` except that no intermediate vector is
            built
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v2): second vector
        
            Returns:
                the square of the distance between v1 and v2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceSq(fieldVector3D: 'FieldVector3D'[_distanceSq_3__T], vector3D: 'Vector3D') -> _distanceSq_3__T: ...
    @typing.overload
    @staticmethod
    def distanceSq(vector3D: 'Vector3D', fieldVector3D: 'FieldVector3D'[_distanceSq_4__T]) -> _distanceSq_4__T: ...
    _dotProduct_2__T = typing.TypeVar('_dotProduct_2__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    _dotProduct_3__T = typing.TypeVar('_dotProduct_3__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    _dotProduct_4__T = typing.TypeVar('_dotProduct_4__T', bound=fr.cnes.sirius.patrius.math.RealFieldElement)  # <T>
    @typing.overload
    def dotProduct(self, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T]) -> _FieldVector3D__T:
        """
            Compute the dot-product of the instance and another vector.
        
            The implementation uses specific multiplication and addition algorithms to preserve accuracy and reduce cancellation
            effects. It should be very accurate even for nearly orthogonal vectors.
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the dot product this.v
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.util.MathArrays.linearCombination`
        
        """
        ...
    @typing.overload
    def dotProduct(self, vector3D: 'Vector3D') -> _FieldVector3D__T: ...
    @typing.overload
    @staticmethod
    def dotProduct(fieldVector3D: 'FieldVector3D'[_dotProduct_2__T], fieldVector3D2: 'FieldVector3D'[_dotProduct_2__T]) -> _dotProduct_2__T:
        """
            Compute the dot-product of two vectors.
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v1): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v2): second vector
        
            Returns:
                the dot product v1.v2
        
            Compute the dot-product of two vectors.
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v1): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the dot product v1.v2
        
            Compute the dot-product of two vectors.
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D`<T> v2): second vector
        
            Returns:
                the dot product v1.v2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def dotProduct(fieldVector3D: 'FieldVector3D'[_dotProduct_3__T], vector3D: 'Vector3D') -> _dotProduct_3__T: ...
    @typing.overload
    @staticmethod
    def dotProduct(vector3D: 'Vector3D', fieldVector3D: 'FieldVector3D'[_dotProduct_4__T]) -> _dotProduct_4__T: ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two 3D vectors.
        
            If all coordinates of two 3D vectors are exactly the same, and none of their
            :meth:`~fr.cnes.sirius.patrius.math.RealFieldElement.getReal` are :code:`NaN`, the two 3D vectors are considered to be
            equal.
        
            :code:`NaN` coordinates are considered to affect globally the vector and be equals to each other - i.e, if either (or
            all) real part of the coordinates of the 3D vector are :code:`NaN`, the 3D vector is :code:`NaN`.
        
            Overrides:
                 in class 
        
            Parameters:
                other (`Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`): Object to test for equality to this
        
            Returns:
                true if two 3D vector objects are equal, false if object is null, not an instance of Vector3D, or not equal to this
                Vector3D instance
        
        
        """
        ...
    def getAlpha(self) -> _FieldVector3D__T:
        """
            Get the azimuth of the vector.
        
            Returns:
                azimuth (α) of the vector, between -π and +π
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D.FieldVector3D`
        
        
        """
        ...
    def getDelta(self) -> _FieldVector3D__T:
        """
            Get the elevation of the vector.
        
            Returns:
                elevation (δ) of the vector, between -π/2 and +π/2
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D.FieldVector3D`
        
        
        """
        ...
    def getNorm(self) -> _FieldVector3D__T:
        """
            Get the L :sub:`2` norm for the vector.
        
            Returns:
                Euclidean norm for the vector
        
        
        """
        ...
    def getNorm1(self) -> _FieldVector3D__T:
        """
            Get the L :sub:`1` norm for the vector.
        
            Returns:
                L :sub:`1` norm for the vector
        
        
        """
        ...
    def getNormInf(self) -> _FieldVector3D__T:
        """
            Get the L :sub:`∞` norm for the vector.
        
            Returns:
                L :sub:`∞` norm for the vector
        
        
        """
        ...
    def getNormSq(self) -> _FieldVector3D__T:
        """
            Get the square of the norm for the vector.
        
            Returns:
                square of the Euclidean norm for the vector
        
        
        """
        ...
    def getX(self) -> _FieldVector3D__T:
        """
            Get the abscissa of the vector.
        
            Returns:
                abscissa of the vector
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D.FieldVector3D`
        
        
        """
        ...
    def getY(self) -> _FieldVector3D__T:
        """
            Get the ordinate of the vector.
        
            Returns:
                ordinate of the vector
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D.FieldVector3D`
        
        
        """
        ...
    def getZ(self) -> _FieldVector3D__T:
        """
            Get the height of the vector.
        
            Returns:
                height of the vector
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.FieldVector3D.FieldVector3D`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Get a hashCode for the 3D vector.
        
            All NaN values have the same hash code.
        
            Overrides:
                 in class 
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
            Returns true if any coordinate of this vector is infinite and none are NaN; false otherwise
        
            Returns:
                true if any coordinate of this vector is infinite and none are NaN; false otherwise
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
            Returns true if any coordinate of this vector is NaN; false otherwise
        
            Returns:
                true if any coordinate of this vector is NaN; false otherwise
        
        
        """
        ...
    def negate(self) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    def normalize(self) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    def orthogonal(self) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def scalarMultiply(self, double: float) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def scalarMultiply(self, t: _FieldVector3D__T) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def subtract(self, double: float, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T]) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def subtract(self, double: float, vector3D: 'Vector3D') -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def subtract(self, t: _FieldVector3D__T, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T]) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def subtract(self, t: _FieldVector3D__T, vector3D: 'Vector3D') -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def subtract(self, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T]) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def subtract(self, vector3D: 'Vector3D') -> 'FieldVector3D'[_FieldVector3D__T]: ...
    def toArray(self) -> typing.MutableSequence[_FieldVector3D__T]:
        """
            Get the vector coordinates as a dimension 3 array.
        
            Returns:
                vector coordinates
        
            Also see:
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str:
        """
            Get a string representation of this vector.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of this vector
        
        """
        ...
    @typing.overload
    def toString(self, numberFormat: java.text.NumberFormat) -> str:
        """
            Get a string representation of this vector.
        
            Parameters:
                format (`NumberFormat <http://docs.oracle.com/javase/8/docs/api/java/text/NumberFormat.html?is-external=true>`): the custom format for components
        
            Returns:
                a string representation of this vector
        
        
        """
        ...
    def toVector3D(self) -> 'Vector3D':
        """
            Convert to a constant vector without derivatives.
        
            Returns:
                a constant vector
        
        
        """
        ...

class Line(fr.cnes.sirius.patrius.math.geometry.partitioning.Embedding[Euclidean3D, fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Euclidean1D], java.io.Serializable):
    """
    public class Line extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Embedding`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Euclidean3D`,:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Euclidean1D`>, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        The class represent lines in a three dimensional space.
    
        Each oriented line is intrinsically associated with an abscissa which is a coordinate on the line. The point at abscissa
        0 is the orthogonal projection of the origin on the line, another equivalent way to express this is to say that it is
        the point of the line which is closest to the origin. Abscissa increases in the line direction.
    
        This PATRIUS 4.9, the user can define a "min abscissa" in order to define a sub-line: only points after this abscissa
        are considered to be part of the sub-line.
    
        Since:
            3.0
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, line: 'Line'): ...
    @typing.overload
    def __init__(self, vector3D: 'Vector3D', vector3D2: 'Vector3D'): ...
    @typing.overload
    def __init__(self, vector3D: 'Vector3D', vector3D2: 'Vector3D', vector3D3: 'Vector3D'): ...
    def closestPoint(self, line: 'Line') -> 'Vector3D':
        """
            Compute the point of the instance closest to another line. Calculations take the minimum abscissa into account.
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): line to check against the instance
        
            Returns:
                point of the instance closest to another line
        
        
        """
        ...
    def closestPointTo(self, line: 'Line') -> typing.MutableSequence['Vector3D']:
        """
            Computes the points of this and another line realizing the shortest distance. If lines are parallel, the zero point of
            the other line is used. Calculations take the minimum abscissa into account.
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the closest point of the other line, and the closest point of this.
        
        
        """
        ...
    def contains(self, vector3D: 'Vector3D') -> bool:
        """
            Check if the instance contains a point. Calculations take the minimum abscissa into account.
        
            Parameters:
                p (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): point to check
        
            Returns:
                true if p belongs to the line and its abscissa is greater than the minimum abscissa
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createLine(vector3D: 'Vector3D', vector3D2: 'Vector3D') -> 'Line':
        """
            Creates a Line object from a point of space and a direction vector.
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): the origin point
                direction (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): the directing vector of the line
        
            Returns:
                the new Line
        
            Creates a Line object from a point of space, a direction vector and the point of minimum abscissa.
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): the origin point
                direction (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): the directing vector of the line
                pointMinAbscissa (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): point of minimum abscissa (only points after this abscissa are considered to be part of the sub-line)
        
            Returns:
                the new Line
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createLine(vector3D: 'Vector3D', vector3D2: 'Vector3D', vector3D3: 'Vector3D') -> 'Line': ...
    @typing.overload
    def distance(self, line: 'Line') -> float:
        """
            Compute the distance between the instance and a point. Calculations take the minimum abscissa into account.
        
            Parameters:
                p (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): to check
        
            Returns:
                distance between the instance and the point
        
            Compute the shortest distance between the instance and another line. Calculations take the minimum abscissa into
            account.
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): line to check against the instance
        
            Returns:
                shortest distance between the instance and the line
        
        
        """
        ...
    @typing.overload
    def distance(self, vector3D: 'Vector3D') -> float: ...
    def getAbscissa(self, vector3D: 'Vector3D') -> float:
        """
            Get the abscissa of a point with respect to the line.
        
            The abscissa is 0 if the projection of the point and the projection of the frame origin on the line are the same point.
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): point to check
        
            Returns:
                abscissa of the point
        
        
        """
        ...
    def getDirection(self) -> 'Vector3D':
        """
            Get the normalized direction vector.
        
            Returns:
                normalized direction vector
        
        
        """
        ...
    def getIntersectionPoints(self, line: 'Line') -> typing.MutableSequence['Vector3D']:
        """
            Compute the intersection points with another line if it exists. Calculations take the minimum abscissa into account.
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the second line
        
            Returns:
                a Vector3D array containing the intersection point if it exists, empty otherwise
        
        
        """
        ...
    def getMinAbscissa(self) -> float:
        """
            Get the line minimum abscissa.
        
            Returns:
                line minimum abscissa
        
        
        """
        ...
    def getOrigin(self) -> 'Vector3D':
        """
            Get the line point closest to the origin.
        
            Returns:
                line point closest to the origin
        
        
        """
        ...
    def intersection(self, line: 'Line') -> 'Vector3D':
        """
            Get the intersection point of the instance and another line. Calculations take the minimum abscissa into account.
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): other line
        
            Returns:
                intersection point of the instance and the other line or null if there are no intersection points
        
        
        """
        ...
    def isSimilarTo(self, line: 'Line') -> bool:
        """
            Check if the instance is similar to another line.
        
            Lines are considered similar if they contain the same points regardless abscissas and if they are both infinite or
            semi-finite. This does not mean they are equal since they can also have opposite directions.
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): line to which instance should be compared
        
            Returns:
                true if the lines are similar
        
        
        """
        ...
    def pointAt(self, double: float) -> 'Vector3D':
        """
            Get one point from the line.
        
            Parameters:
                abscissa (double): desired abscissa for the point
        
            Returns:
                one point belonging to the line, at specified abscissa
        
        
        """
        ...
    def pointOfMinAbscissa(self, vector3DArray: typing.Union[typing.List['Vector3D'], jpype.JArray]) -> 'Vector3D':
        """
            Get the point with the lowest abscissa from an array of points. Points are not filtered by the line's minAbscissa, ie.
            this method may return a point with an abscissa lower than this.minAbscissa.
        
        
            In case several points have the same lowest abscissa, only the first one of the array is returned.
        
        
            ***Warning: array must not be empty***
        
            Parameters:
                points (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`[]): array of points to assess, must not be empty
        
            Returns:
                the point of the array which has the lowest abscissa
        
        
        """
        ...
    def reset(self, vector3D: 'Vector3D', vector3D2: 'Vector3D') -> None:
        """
            Reset the instance as if built from two points.
        
            Parameters:
                p1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): first point belonging to the line (this can be any point)
                p2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second point belonging to the line (this can be any point, different from p1)
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException`: if the points are equal
        
        
        """
        ...
    def revert(self) -> 'Line':
        """
            Get a line with reversed direction.
        
        
            In the case of a semi-finite line, the min abscissa point is "frozen" so that the min abscissa point of the new line is
            the same. As a consequence, the minimum abscissa value is equal to the opposite of this.minAbscissa.
        
        
            Reverted infinite lines still have minAbscissa = Double.NEGATIVE_INFINITY
        
            Returns:
                a new instance, with reversed direction
        
        
        """
        ...
    def toSpace(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Euclidean1D]) -> 'Vector3D': ...
    def toSubSpace(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean3D]) -> fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Vector1D: ...
    def wholeLine(self) -> 'SubLine':
        """
            Build a sub-line covering the whole line.
        
            Returns:
                a sub-line covering the whole line
        
        
        """
        ...

class LineSegment(java.io.Serializable):
    """
    public final class LineSegment extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        This is a describing class for a line segment in 3D space, with a method to compute the shortest distance to a line.
    
        Since:
            1.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, vector3D: 'Vector3D', vector3D2: 'Vector3D', double: float): ...
    def closestPointTo(self, line: Line) -> typing.MutableSequence['Vector3D']:
        """
            Computation of the closest point to a line, and the associated point of the line;
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the point of the line and the point of the segment.
        
        
        """
        ...
    def distanceTo(self, line: Line) -> float:
        """
            Computes the shortest distance to a line of space.
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the distance
        
        
        """
        ...
    def getDirection(self) -> 'Vector3D':
        """
        
            Returns:
                the direction
        
        
        """
        ...
    def getEnd(self) -> 'Vector3D':
        """
        
            Returns:
                the end
        
        
        """
        ...
    def getLength(self) -> float:
        """
        
            Returns:
                the length
        
        
        """
        ...
    def getOrigin(self) -> 'Vector3D':
        """
        
            Returns:
                the origin
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a representation for this line segment. The given parameters are in the same order as in the constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a representation for this line segment
        
        
        """
        ...

class Matrix3D(java.io.Serializable):
    """
    public final class Matrix3D extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        This is a real 3x3 matrix designed to be used in geometric calculations. It is compatible with the Vector3D type.
    
        Since:
            1.0
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, vector3D: 'Vector3D'): ...
    @typing.overload
    def __init__(self, realMatrix: fr.cnes.sirius.patrius.math.linear.RealMatrix): ...
    def add(self, matrix3D: 'Matrix3D') -> 'Matrix3D':
        """
            Computes the addition of two Matrix3D
        
            Parameters:
                added (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Matrix3D`): the Matrix3D to be added
        
            Returns:
                the resulting Matrix3D
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
            Asserts two Matrix3D to be equal.
        
            Overrides:
                 in class 
        
            Parameters:
                other (`Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`): the Matrix3D to be compared to this
        
            Returns:
                true if the entries of both Matrix3D are equal
        
        
        """
        ...
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        
            Returns:
                the data
        
        
        """
        ...
    def getEntry(self, int: int, int2: int) -> float:
        """
            Returns the value of one entry of the matrix
        
            Parameters:
                row (int): the row of the wanted data
                column (int): the column of the wanted data
        
            Returns:
                the data value
        
        
        """
        ...
    def getRealMatrix(self) -> fr.cnes.sirius.patrius.math.linear.RealMatrix:
        """
        
            Returns:
                the Array2DRowRealMatrix with identical data
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Get a hashCode for the 3D matrix.
        
            All NaN values have the same hash code.
        
            Overrides:
                 in class 
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
            Returns true if any entry of this matrix is NaN; false otherwise
        
            Returns:
                true if any entry of this matrix is NaN; false otherwise
        
        
        """
        ...
    def isOrthogonal(self, double: float, double2: float) -> bool:
        """
            Given a threshold, is this an orthogonal matrix? The method indicates if the matrix is orthogonal. To do so the method
            checks if the column vectors of the matrix form an orthonomal set.
        
            Parameters:
                thresholdNorm (double): : allowed error with respect to the normality of the vectors
                thresholdOrthogonality (double): : allowed error with respect to the mutual orthogonality of the vectors
        
            Returns:
                true if the vectors form an orthonormal set taking into account an allowed error, false otherwise
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> 'Matrix3D':
        """
            Computes a matrix multiplication between two Matrix3D objects
        
            Parameters:
                mult (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Matrix3D`): the Matrix3D right term of the multiplication
        
            Returns:
                the resulting Matrix3D
        
            Computes the multiplication between a Matrix3D and a Vector3D
        
            Parameters:
                mult (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): the Vector3D right term of the multiplication
        
            Returns:
                the resulting Vector3D
        
            Computes a multiplication of this Matrix3D with a scalar
        
            Parameters:
                x (double): the Matrix3D right term of the multiplication
        
            Returns:
                the resulting Matrix3D
        
        
        """
        ...
    @typing.overload
    def multiply(self, matrix3D: 'Matrix3D') -> 'Matrix3D': ...
    @typing.overload
    def multiply(self, vector3D: 'Vector3D') -> 'Vector3D': ...
    def subtract(self, matrix3D: 'Matrix3D') -> 'Matrix3D':
        """
            Computes the subtraction of a Matrix3D to this one
        
            Parameters:
                sub (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Matrix3D`): the Matrix3D to be subtracted
        
            Returns:
                the resulting Matrix3D
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a string representation for this matrix.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation for this matrix
        
        
        """
        ...
    def transpose(self) -> 'Matrix3D':
        """
            Computes the transposition of this Matrix3D
        
            Returns:
                the resulting Matrix3D
        
        
        """
        ...
    def transposeAndMultiply(self, vector3D: 'Vector3D') -> 'Vector3D':
        """
            Computes the multiplication of the transposed matrix of this Matrix3D with a Vector3D
        
            Parameters:
                vector (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): the Vector3D right term of the multiplication
        
            Returns:
                the resulting Vector3D
        
        
        """
        ...

class NotARotationMatrixException(fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException):
    """
    public class NotARotationMatrixException extends :class:`~fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException`
    
        This class represents exceptions thrown while building rotations from matrices.
    
        Since:
            1.2
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, localizable: fr.cnes.sirius.patrius.math.exception.util.Localizable, *object: typing.Any): ...

class OutlineExtractor:
    """
    public class OutlineExtractor extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`
    
        Extractor for :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.twod.PolygonsSet` outlines.
    
        This class extracts the 2D outlines from {:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.twod.PolygonsSet` in a
        specified projection plane.
    
        Since:
            3.0
    """
    def __init__(self, vector3D: 'Vector3D', vector3D2: 'Vector3D'): ...
    def getOutline(self, polyhedronsSet: 'PolyhedronsSet') -> typing.MutableSequence[typing.MutableSequence[fr.cnes.sirius.patrius.math.geometry.euclidean.twod.Vector2D]]:
        """
            Extract the outline of a polyhedrons set.
        
            Parameters:
                polyhedronsSet (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.PolyhedronsSet`): polyhedrons set whose outline must be extracted
        
            Returns:
                an outline, as an array of loops.
        
        
        """
        ...

class PolyhedronsSet(fr.cnes.sirius.patrius.math.geometry.partitioning.AbstractRegion[Euclidean3D, fr.cnes.sirius.patrius.math.geometry.euclidean.twod.Euclidean2D]):
    """
    public class PolyhedronsSet extends :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.AbstractRegion`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Euclidean3D`,:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.twod.Euclidean2D`>
    
        This class represents a 3D region: a set of polyhedrons.
    
        Since:
            3.0
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    @typing.overload
    def __init__(self, bRep: 'PolyhedronsSet.BRep', double: float): ...
    @typing.overload
    def __init__(self, bSPTree: fr.cnes.sirius.patrius.math.geometry.partitioning.BSPTree[Euclidean3D]): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection[fr.cnes.sirius.patrius.math.geometry.partitioning.SubHyperplane[Euclidean3D]], typing.Sequence[fr.cnes.sirius.patrius.math.geometry.partitioning.SubHyperplane[Euclidean3D]], typing.Set[fr.cnes.sirius.patrius.math.geometry.partitioning.SubHyperplane[Euclidean3D]]]): ...
    @typing.overload
    def __init__(self, list: java.util.List['Vector3D'], list2: java.util.List[typing.Union[typing.List[int], jpype.JArray]], double: float): ...
    def buildNew(self, bSPTree: fr.cnes.sirius.patrius.math.geometry.partitioning.BSPTree[Euclidean3D]) -> 'PolyhedronsSet': ...
    def firstIntersection(self, vector3D: 'Vector3D', line: Line) -> fr.cnes.sirius.patrius.math.geometry.partitioning.SubHyperplane[Euclidean3D]: ...
    def getBRep(self) -> 'PolyhedronsSet.BRep': ...
    def rotate(self, vector3D: 'Vector3D', rotation: 'Rotation') -> 'PolyhedronsSet':
        """
            Rotate the region around the specified point.
        
            The instance is not modified, a new instance is created.
        
            Parameters:
                center (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): rotation center
                rotation (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation`): vectorial rotation operator
        
            Returns:
                a new instance representing the rotated region
        
        
        """
        ...
    def translate(self, vector3D: 'Vector3D') -> 'PolyhedronsSet':
        """
            Translate the region by the specified amount.
        
            The instance is not modified, a new instance is created.
        
            Parameters:
                translation (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): translation to apply
        
            Returns:
                a new instance representing the translated region
        
        
        """
        ...
    class BRep:
        def __init__(self, list: java.util.List['Vector3D'], list2: java.util.List[typing.Union[typing.List[int], jpype.JArray]]): ...
        def getFacets(self) -> java.util.List[typing.MutableSequence[int]]: ...
        def getVertices(self) -> java.util.List['Vector3D']: ...

class Rotation(java.io.Serializable):
    IDENTITY: typing.ClassVar['Rotation'] = ...
    @typing.overload
    def __init__(self, boolean: bool, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, boolean: bool, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, boolean: bool, quaternion: fr.cnes.sirius.patrius.math.complex.Quaternion): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], double2: float): ...
    @typing.overload
    def __init__(self, rotationOrder: 'RotationOrder', double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, vector3D: 'Vector3D', double: float): ...
    @typing.overload
    def __init__(self, vector3D: 'Vector3D', vector3D2: 'Vector3D'): ...
    @typing.overload
    def __init__(self, vector3D: 'Vector3D', vector3D2: 'Vector3D', vector3D3: 'Vector3D', vector3D4: 'Vector3D'): ...
    @typing.overload
    def applyInverseTo(self, rotation: 'Rotation') -> 'Rotation': ...
    @typing.overload
    def applyInverseTo(self, vector3D: 'Vector3D') -> 'Vector3D': ...
    @typing.overload
    def applyInverseTo(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    @typing.overload
    def applyTo(self, rotation: 'Rotation') -> 'Rotation': ...
    @typing.overload
    def applyTo(self, vector3D: 'Vector3D') -> 'Vector3D': ...
    @typing.overload
    def applyTo(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    @staticmethod
    def distance(rotation: 'Rotation', rotation2: 'Rotation') -> float: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAngle(self) -> float: ...
    def getAngles(self, rotationOrder: 'RotationOrder') -> typing.MutableSequence[float]: ...
    def getAxis(self) -> 'Vector3D': ...
    def getMatrix(self) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    def getQi(self) -> typing.MutableSequence[float]: ...
    def getQuaternion(self) -> fr.cnes.sirius.patrius.math.complex.Quaternion: ...
    def hashCode(self) -> int: ...
    @typing.overload
    def isEqualTo(self, rotation: 'Rotation') -> bool: ...
    @typing.overload
    def isEqualTo(self, rotation: 'Rotation', double: float, double2: float) -> bool: ...
    def isIdentity(self) -> bool: ...
    @staticmethod
    def lerp(rotation: 'Rotation', rotation2: 'Rotation', double: float) -> 'Rotation': ...
    def revert(self) -> 'Rotation': ...
    @staticmethod
    def slerp(rotation: 'Rotation', rotation2: 'Rotation', double: float) -> 'Rotation': ...
    def toString(self) -> str: ...

class RotationOrder(java.io.Serializable):
    """
    public final class RotationOrder extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        This class is a utility representing a rotation order specification for Cardan or Euler angles specification. This class
        cannot be instanciated by the user. He can only use one of the twelve predefined supported orders as an argument to
        either the :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation.Rotation` constructor or the
        :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation.getAngles` method.
    
        Since:
            1.2
    
        Also see:
            :meth:`~serialized`
    """
    XYZ: typing.ClassVar['RotationOrder'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder` XYZ
    
        Set of Cardan angles. this ordered set of rotations is around X, then around Y, then around Z
    
    """
    XZY: typing.ClassVar['RotationOrder'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder` XZY
    
        Set of Cardan angles. this ordered set of rotations is around X, then around Z, then around Y
    
    """
    YXZ: typing.ClassVar['RotationOrder'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder` YXZ
    
        Set of Cardan angles. this ordered set of rotations is around Y, then around X, then around Z
    
    """
    YZX: typing.ClassVar['RotationOrder'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder` YZX
    
        Set of Cardan angles. this ordered set of rotations is around Y, then around Z, then around X
    
    """
    ZXY: typing.ClassVar['RotationOrder'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder` ZXY
    
        Set of Cardan angles. this ordered set of rotations is around Z, then around X, then around Y
    
    """
    ZYX: typing.ClassVar['RotationOrder'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder` ZYX
    
        Set of Cardan angles. this ordered set of rotations is around Z, then around Y, then around X
    
    """
    XYX: typing.ClassVar['RotationOrder'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder` XYX
    
        Set of Euler angles. this ordered set of rotations is around X, then around Y, then around X
    
    """
    XZX: typing.ClassVar['RotationOrder'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder` XZX
    
        Set of Euler angles. this ordered set of rotations is around X, then around Z, then around X
    
    """
    YXY: typing.ClassVar['RotationOrder'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder` YXY
    
        Set of Euler angles. this ordered set of rotations is around Y, then around X, then around Y
    
    """
    YZY: typing.ClassVar['RotationOrder'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder` YZY
    
        Set of Euler angles. this ordered set of rotations is around Y, then around Z, then around Y
    
    """
    ZXZ: typing.ClassVar['RotationOrder'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder` ZXZ
    
        Set of Euler angles. this ordered set of rotations is around Z, then around X, then around Z
    
    """
    ZYZ: typing.ClassVar['RotationOrder'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder` ZYZ
    
        Set of Euler angles. this ordered set of rotations is around Z, then around Y, then around Z
    
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getA1(self) -> 'Vector3D':
        """
            Get the axis of the first rotation.
        
            Returns:
                axis of the first rotation
        
        
        """
        ...
    def getA2(self) -> 'Vector3D':
        """
            Get the axis of the second rotation.
        
            Returns:
                axis of the second rotation
        
        
        """
        ...
    def getA3(self) -> 'Vector3D':
        """
            Get the axis of the second rotation.
        
            Returns:
                axis of the second rotation
        
        
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
            Get a string representation of the instance.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of the instance (in fact, its name)
        
        
        """
        ...

class Screw:
    """
    public class Screw extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`
    
        This class represents a screw
    
        Since:
            3.1.2
    """
    @typing.overload
    def __init__(self, screw: 'Screw'): ...
    @typing.overload
    def __init__(self, vector3D: 'Vector3D', vector3D2: 'Vector3D', vector3D3: 'Vector3D'): ...
    @typing.overload
    def displace(self, vector3D: 'Vector3D') -> 'Screw':
        """
            Displace this screw, using Chasles
        
            Parameters:
                s (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Screw`): screw
                newOrigin (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): new origin for s
        
            Returns:
                screw expressed in new origin
        
            Displace this screw, using Chasles
        
            Parameters:
                newOrigin (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): new origin for current object
        
            Returns:
                screw expressed in new origin
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def displace(screw: 'Screw', vector3D: 'Vector3D') -> 'Screw': ...
    def getOrigin(self) -> 'Vector3D':
        """
        
            Returns:
                the origin
        
        
        """
        ...
    def getRotation(self) -> 'Vector3D':
        """
        
            Returns:
                the rotation
        
        
        """
        ...
    def getTranslation(self) -> 'Vector3D':
        """
        
            Returns:
                the translation
        
        
        """
        ...
    @typing.overload
    def sum(self, screw: 'Screw') -> 'Screw':
        """
            Calculate the sum of this and screw, expressed in this objects origin.
        
            Parameters:
                s1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Screw`): screw.
                s2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Screw`): screw.
        
            Returns:
                sum of screws
        
            Calculate the sum of this and screw, expressed in this objects origin.
        
            Parameters:
                screw (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Screw`): screw to add to this.
        
            Returns:
                sum of screws
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def sum(screw: 'Screw', screw2: 'Screw') -> 'Screw': ...
    def toString(self) -> str:
        """
            Get a String representation of this screw.
        
            Overrides:
                 in class 
        
            Returns:
                a representation for this screw
        
        
        """
        ...

class Segment:
    """
    public class Segment extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`
    
        Simple container for a two-points segment.
    
        Since:
            3.0
    """
    @typing.overload
    def __init__(self, vector3D: 'Vector3D', vector3D2: 'Vector3D'): ...
    @typing.overload
    def __init__(self, vector3D: 'Vector3D', vector3D2: 'Vector3D', line: Line): ...
    def getEnd(self) -> 'Vector3D':
        """
            Get the end point of the segment.
        
            Returns:
                end point of the segment
        
        
        """
        ...
    def getLine(self) -> Line:
        """
            Get the line containing the segment.
        
            Returns:
                line containing the segment
        
        
        """
        ...
    def getStart(self) -> 'Vector3D':
        """
            Get the start point of the segment.
        
            Returns:
                start point of the segment
        
        
        """
        ...
    @staticmethod
    def isIntersectingSegments(segmentArray: typing.Union[typing.List['Segment'], jpype.JArray]) -> bool:
        """
            Indicates whether or not the given segments intersect each other.
        
            Parameters:
                segments (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Segment`[]): array of segments
        
            Returns:
                :code:`true` if the given segments intersect each other
        
        
        """
        ...

class Shape:
    """
    public interface Shape
    
        Interface for all shapes.
    
        It includes infinite and solid shapes. All of them must be able to compute their intersection and distance to a line.
    """
    def closestPointTo(self, line: Line) -> typing.MutableSequence['Vector3D']:
        """
            Computes the points of the shape and the line realizing the shortest distance. If the line intersects the shape, the
            returned points are identical : this point is the one with the lowest abscissa on the line.
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the two points : first the one from the line, and the one from the shape.
        
        
        """
        ...
    def distanceTo(self, line: Line) -> float:
        """
            Computes the distance to a line.
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the shortest distance between the the line and the shape
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence['Vector3D']:
        """
            Compute the intersection points with a line.
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the intersection points if they exist. If no intersection is found, the dimension is zero
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            Tests the intersection with a line.
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                true if the line intersects the shape
        
        
        """
        ...

class SphericalCoordinates(java.io.Serializable):
    """
    public class SphericalCoordinates extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        This class provides spherical coordinates (elevation, azimuth, norm) from a Vector3D.
    
        Instance of this class are guaranteed to be immutable.
    
        Since:
            4.7
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, boolean: bool): ...
    @typing.overload
    def __init__(self, vector3D: 'Vector3D'): ...
    def getAlpha(self) -> float:
        """
            Get the azimuth α.
        
            Returns:
                azimuth (α), between -π and +π
        
        
        """
        ...
    def getCartesianCoordinates(self) -> 'Vector3D':
        """
            Returns the cartesian coordinates.
        
            Returns:
                the cartesian coordinates
        
        
        """
        ...
    def getDelta(self) -> float:
        """
            Get the elevation δ.
        
            Returns:
                elevation (δ), between -π/2 and +π/2
        
        
        """
        ...
    def getNorm(self) -> float:
        """
            Get the norm.
        
            Returns:
                the norm
        
        
        """
        ...

class SubLine:
    """
    public class SubLine extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`
    
        This class represents a subset of a :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`.
    
        Since:
            3.0
    """
    @typing.overload
    def __init__(self, line: Line, intervalsSet: fr.cnes.sirius.patrius.math.geometry.euclidean.oned.IntervalsSet): ...
    @typing.overload
    def __init__(self, segment: Segment): ...
    @typing.overload
    def __init__(self, vector3D: 'Vector3D', vector3D2: 'Vector3D'): ...
    def getSegments(self) -> java.util.List[Segment]: ...
    def intersection(self, subLine: 'SubLine', boolean: bool) -> 'Vector3D':
        """
            Get the intersection of the instance and another sub-line.
        
            This method is related to the :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line.intersection` method in
            the :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line` class, but in addition to compute the point
            along infinite lines, it also checks the point lies on both sub-line ranges.
        
            Parameters:
                subLine (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.SubLine`): other sub-line which may intersect instance
                includeEndPoints (boolean): if true, endpoints are considered to belong to instance (i.e. they are closed sets) and may be returned, otherwise
                    endpoints are considered to not belong to instance (i.e. they are open sets) and intersection occurring on endpoints
                    lead to null being returned
        
            Returns:
                the intersection point if there is one, null if the sub-lines don't intersect
        
        
        """
        ...

class SubPlane(fr.cnes.sirius.patrius.math.geometry.partitioning.AbstractSubHyperplane[Euclidean3D, fr.cnes.sirius.patrius.math.geometry.euclidean.twod.Euclidean2D]):
    """
    public class SubPlane extends :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.AbstractSubHyperplane`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Euclidean3D`,:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.twod.Euclidean2D`>
    
        This class represents a sub-hyperplane for :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane`.
    
        Since:
            3.0
    """
    def __init__(self, hyperplane: fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane[Euclidean3D], region: fr.cnes.sirius.patrius.math.geometry.partitioning.Region[fr.cnes.sirius.patrius.math.geometry.euclidean.twod.Euclidean2D]): ...
    def side(self, hyperplane: fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane[Euclidean3D]) -> fr.cnes.sirius.patrius.math.geometry.partitioning.Side: ...
    def split(self, hyperplane: fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane[Euclidean3D]) -> fr.cnes.sirius.patrius.math.geometry.partitioning.SubHyperplane.SplitSubHyperplane[Euclidean3D]: ...

class Vector3D(fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean3D]):
    """
    public class Vector3D extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Euclidean3D`>
    
        This class implements vectors in a three-dimensional space.
    
        Instance of this class are guaranteed to be immutable.
    
        Since:
            1.2
    
        Also see:
            :meth:`~serialized`
    """
    ZERO: typing.ClassVar['Vector3D'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` ZERO
    
        Null vector (coordinates: 0, 0, 0).
    
    """
    PLUS_I: typing.ClassVar['Vector3D'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` PLUS_I
    
        First canonical vector (coordinates: 1, 0, 0).
    
    """
    MINUS_I: typing.ClassVar['Vector3D'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` MINUS_I
    
        Opposite of the first canonical vector (coordinates: -1, 0, 0).
    
    """
    PLUS_J: typing.ClassVar['Vector3D'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` PLUS_J
    
        Second canonical vector (coordinates: 0, 1, 0).
    
    """
    MINUS_J: typing.ClassVar['Vector3D'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` MINUS_J
    
        Opposite of the second canonical vector (coordinates: 0, -1, 0).
    
    """
    PLUS_K: typing.ClassVar['Vector3D'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` PLUS_K
    
        Third canonical vector (coordinates: 0, 0, 1).
    
    """
    MINUS_K: typing.ClassVar['Vector3D'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` MINUS_K
    
        Opposite of the third canonical vector (coordinates: 0, 0, -1).
    
    """
    NaN: typing.ClassVar['Vector3D'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` NaN
    
        A vector with all coordinates set to NaN.
    
    """
    POSITIVE_INFINITY: typing.ClassVar['Vector3D'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` POSITIVE_INFINITY
    
        A vector with all coordinates set to positive infinity.
    
    """
    NEGATIVE_INFINITY: typing.ClassVar['Vector3D'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` NEGATIVE_INFINITY
    
        A vector with all coordinates set to negative infinity.
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, vector3D: 'Vector3D'): ...
    @typing.overload
    def __init__(self, double: float, vector3D: 'Vector3D', double2: float, vector3D2: 'Vector3D'): ...
    @typing.overload
    def __init__(self, double: float, vector3D: 'Vector3D', double2: float, vector3D2: 'Vector3D', double3: float, vector3D3: 'Vector3D'): ...
    @typing.overload
    def __init__(self, double: float, vector3D: 'Vector3D', double2: float, vector3D2: 'Vector3D', double3: float, vector3D3: 'Vector3D', double4: float, vector3D4: 'Vector3D'): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, sphericalCoordinates: SphericalCoordinates): ...
    @typing.overload
    def __init__(self, realVector: fr.cnes.sirius.patrius.math.linear.RealVector): ...
    @typing.overload
    def add(self, double: float, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean3D]) -> 'Vector3D': ...
    @typing.overload
    def add(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean3D]) -> 'Vector3D': ...
    @staticmethod
    def angle(vector3D: 'Vector3D', vector3D2: 'Vector3D') -> float:
        """
            Compute the angular separation between two vectors.
        
            This method computes the angular separation between two vectors using the dot product for well separated vectors and the
            cross product for almost aligned vectors. This allows to have a good accuracy in all cases, even for vectors very close
            to each other.
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                angular separation between v1 and v2
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathArithmeticException`: if either vector has a null norm
        
        
        """
        ...
    @typing.overload
    def crossProduct(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean3D]) -> 'Vector3D':
        """
            Compute the cross-product of two vectors.
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the cross product v1 ^ v2 as a new Vector
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def crossProduct(vector3D: 'Vector3D', vector3D2: 'Vector3D') -> 'Vector3D': ...
    @typing.overload
    def distance(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean3D]) -> float:
        """
            Compute the distance between two vectors according to the L :sub:`2` norm.
        
            Calling this method is equivalent to calling: :code:`v1.subtract(v2).getNorm()` except that no intermediate vector is
            built
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the distance between v1 and v2 according to the L :sub:`2` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance(vector3D: 'Vector3D', vector3D2: 'Vector3D') -> float: ...
    @typing.overload
    def distance1(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean3D]) -> float:
        """
            Compute the distance between two vectors according to the L :sub:`1` norm.
        
            Calling this method is equivalent to calling: :code:`v1.subtract(v2).getNorm1()` except that no intermediate vector is
            built
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the distance between v1 and v2 according to the L :sub:`1` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance1(vector3D: 'Vector3D', vector3D2: 'Vector3D') -> float: ...
    @typing.overload
    def distanceInf(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean3D]) -> float:
        """
            Compute the distance between two vectors according to the L :sub:`∞` norm.
        
            Calling this method is equivalent to calling: :code:`v1.subtract(v2).getNormInf()` except that no intermediate vector is
            built
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the distance between v1 and v2 according to the L :sub:`∞` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceInf(vector3D: 'Vector3D', vector3D2: 'Vector3D') -> float: ...
    @typing.overload
    def distanceSq(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean3D]) -> float:
        """
            Compute the square of the distance between two vectors.
        
            Calling this method is equivalent to calling: :code:`v1.subtract(v2).getNormSq()` except that no intermediate vector is
            built
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the square of the distance between v1 and v2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceSq(vector3D: 'Vector3D', vector3D2: 'Vector3D') -> float: ...
    @typing.overload
    def dotProduct(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean3D]) -> float:
        """
            Compute the dot-product of two vectors.
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): first vector
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): second vector
        
            Returns:
                the dot product v1.v2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def dotProduct(vector3D: 'Vector3D', vector3D2: 'Vector3D') -> float: ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two 3D vectors.
        
            If all coordinates of two 3D vectors are exactly the same, and none are :code:`Double.NaN`, the two 3D vectors are
            considered to be equal.
        
            Overrides:
                 in class 
        
            Parameters:
                other (`Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`): Object to test for equality to this
        
            Returns:
                true if two 3D vector objects are equal, false if object is null, not an instance of Vector3D, or not equal to this
                Vector3D instance
        
        
        """
        ...
    def getAlpha(self) -> float:
        """
            For a given vector, get the angle between projection on XY-plane and X-axis counted in counter-clockwise direction: 0
            corresponds to Vector3D(1, 0, ...), and increasing values are counter-clockwise.
        
            Returns:
                the angle between projection on XY-plane and X-axis counted in counter-clockwise direction (α) of the vector, between
                -π and +π
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D.Vector3D`
        
        
        """
        ...
    def getDelta(self) -> float:
        """
            Get the elevation of the vector.
        
            Returns:
                elevation (δ) of the vector, between -π/2 and +π/2
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D.Vector3D`
        
        
        """
        ...
    def getNorm(self) -> float:
        """
            Get the L :sub:`2` norm for the vector.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Vector.getNorm` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`
        
            Returns:
                Euclidean norm for the vector
        
        
        """
        ...
    def getNorm1(self) -> float:
        """
            Get the L :sub:`1` norm for the vector.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Vector.getNorm1` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`
        
            Returns:
                L :sub:`1` norm for the vector
        
        
        """
        ...
    def getNormInf(self) -> float:
        """
            Get the L :sub:`∞` norm for the vector.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Vector.getNormInf` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`
        
            Returns:
                L :sub:`∞` norm for the vector
        
        
        """
        ...
    def getNormSq(self) -> float:
        """
            Get the square of the norm for the vector.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Vector.getNormSq` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`
        
            Returns:
                square of the Euclidean norm for the vector
        
        
        """
        ...
    def getRealVector(self) -> fr.cnes.sirius.patrius.math.linear.RealVector:
        """
            Get a RealVector with identical data.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Vector.getRealVector` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`
        
            Returns:
                the RealVector
        
            Also see:
                :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
        
        """
        ...
    def getSpace(self) -> fr.cnes.sirius.patrius.math.geometry.Space:
        """
            Get the space to which the vector belongs.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Vector.getSpace` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`
        
            Returns:
                containing space
        
        
        """
        ...
    def getSphericalCoordinates(self) -> SphericalCoordinates:
        """
            Returns the spherical coordinates.
        
            Returns:
                the spherical coordinates (δ, α, norm) / (latitude, longitude, altitude)
        
        
        """
        ...
    def getX(self) -> float:
        """
            Get the abscissa of the vector.
        
            Returns:
                abscissa of the vector
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D.Vector3D`
        
        
        """
        ...
    def getY(self) -> float:
        """
            Get the ordinate of the vector.
        
            Returns:
                ordinate of the vector
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D.Vector3D`
        
        
        """
        ...
    def getZ(self) -> float:
        """
            Get the height of the vector.
        
            Returns:
                height of the vector
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D.Vector3D`
        
        
        """
        ...
    def getZero(self) -> 'Vector3D':
        """
            Get the null vector of the vectorial space or origin point of the affine space.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Vector.getZero` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`
        
            Returns:
                null vector of the vectorial space or origin point of the affine space
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Get a hashCode for the 3D vector.
        
            Overrides:
                 in class 
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    @staticmethod
    def inverseCrossProducts(vector3D: 'Vector3D', vector3D2: 'Vector3D', vector3D3: 'Vector3D', vector3D4: 'Vector3D', double: float) -> 'Vector3D':
        """
            Find a vector from two known cross products.
        
            We want to find Ω such that: Ω ⨯ v₁ = c₁ and Ω ⨯ v₂ = c₂
        
            The first equation (Ω ⨯ v₁ = c₁) will always be fulfilled exactly, and the second one will be fulfilled if possible.
        
            Parameters:
                v1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): vector forming the first known cross product
                c1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): know vector for cross product Ω ⨯ v₁
                v2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): vector forming the second known cross product
                c2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): know vector for cross product Ω ⨯ v₂
                tolerance (double): relative tolerance factor used to check singularities
        
            Returns:
                vector Ω such that: Ω ⨯ v₁ = c₁ and Ω ⨯ v₂ = c₂
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException`: if vectors are inconsistent and no solution can be found
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
            Returns true if any coordinate of this vector is infinite and none are NaN; false otherwise
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Vector.isInfinite` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`
        
            Returns:
                true if any coordinate of this vector is infinite and none are NaN; false otherwise
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
            Returns true if any coordinate of this vector is NaN; false otherwise
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Vector.isNaN` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`
        
            Returns:
                true if any coordinate of this vector is NaN; false otherwise
        
        
        """
        ...
    def isZero(self) -> bool:
        """
            Indicates if this vector has all its components to 0.
        
            Returns:
                true if all the components are 0.
        
        
        """
        ...
    def negate(self) -> 'Vector3D':
        """
            Get the opposite of the instance.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Vector.negate` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`
        
            Returns:
                a new vector which is opposite to the instance
        
        
        """
        ...
    def normalize(self) -> 'Vector3D':
        """
            Get a normalized vector aligned with the instance.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Vector.normalize` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`
        
            Returns:
                a new normalized vector
        
        
        """
        ...
    def orthogonal(self) -> 'Vector3D':
        """
            Get a vector orthogonal to the instance.
        
            There are an infinite number of normalized vectors orthogonal to the instance. This method picks up one of them almost
            arbitrarily. It is useful when one needs to compute a reference frame with one of the axes in a predefined direction.
            The following example shows how to build a frame having the k axis aligned with the known vector u :
        
            .. code-block: java
            
            
             
               Vector3D k = u.normalize();
               Vector3D i = k.orthogonal();
               Vector3D j = Vector3D.crossProduct(k, i);
             
             
        
            Returns:
                a new normalized vector orthogonal to the instance
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathArithmeticException`: if the norm of the instance is null
        
        
        """
        ...
    def scalarMultiply(self, double: float) -> 'Vector3D':
        """
            Multiply the instance by a scalar.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Vector.scalarMultiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`
        
            Parameters:
                a (double): scalar
        
            Returns:
                a new vector
        
        
        """
        ...
    @typing.overload
    def subtract(self, double: float, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean3D]) -> 'Vector3D': ...
    @typing.overload
    def subtract(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean3D]) -> 'Vector3D': ...
    def toArray(self) -> typing.MutableSequence[float]:
        """
            Get the vector coordinates as a dimension 3 array.
        
            Returns:
                vector coordinates
        
            Also see:
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str:
        """
            Get a string representation of this vector.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of this vector
        
        """
        ...
    @typing.overload
    def toString(self, numberFormat: java.text.NumberFormat) -> str:
        """
            Get a string representation of this vector.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Vector.toString` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`
        
            Parameters:
                format (`NumberFormat <http://docs.oracle.com/javase/8/docs/api/java/text/NumberFormat.html?is-external=true>`): the custom format for components
        
            Returns:
                a string representation of this vector
        
        
        """
        ...

class Vector3DFormat(fr.cnes.sirius.patrius.math.geometry.VectorFormat[Euclidean3D]):
    """
    public class Vector3DFormat extends :class:`~fr.cnes.sirius.patrius.math.geometry.VectorFormat`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Euclidean3D`>
    
        Formats a 3D vector in components list format "{x; y; z}".
    
        The prefix and suffix "{" and "}" and the separator "; " can be replaced by any user-defined strings. The number format
        for components can be configured.
    
        White space is ignored at parse time, even if it is in the prefix, suffix or separator specifications. So even if the
        default separator does include a space character that is used at format time, both input string "{1;1;1}" and " { 1 ; 1
        ; 1 } " will be parsed without error and the same vector will be returned. In the second case, however, the parse
        position after parsing will be just after the closing curly brace, i.e. just before the trailing space.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def format(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[fr.cnes.sirius.patrius.math.geometry.Space]) -> str: ...
    @typing.overload
    def format(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean3D], stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    @staticmethod
    def getInstance() -> 'Vector3DFormat':
        """
            Returns the default 3D vector format for the current locale.
        
            Returns:
                the default 3D vector format.
        
        """
        ...
    @typing.overload
    @staticmethod
    def getInstance(locale: java.util.Locale) -> 'Vector3DFormat':
        """
            Returns the default 3D vector format for the given locale.
        
            Parameters:
                locale (`Locale <http://docs.oracle.com/javase/8/docs/api/java/util/Locale.html?is-external=true>`): the specific locale used by the format.
        
            Returns:
                the 3D vector format specific to the given locale.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str) -> Vector3D:
        """
            Parses a string to produce a :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` object.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.VectorFormat.parse` in
                class :class:`~fr.cnes.sirius.patrius.math.geometry.VectorFormat`
        
            Parameters:
                source (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): the string to parse
        
            Returns:
                the parsed :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` object.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathParseException`: if the beginning of the specified string cannot be parsed.
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> Vector3D:
        """
            Parses a string to produce a :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` object.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.VectorFormat.parse` in
                class :class:`~fr.cnes.sirius.patrius.math.geometry.VectorFormat`
        
            Parameters:
                source (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): the string to parse
                pos (`ParsePosition <http://docs.oracle.com/javase/8/docs/api/java/text/ParsePosition.html?is-external=true>`): input/ouput parsing parameter.
        
            Returns:
                the parsed :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D` object.
        
        
        """
        ...

class Vector3DFunction(fr.cnes.sirius.patrius.math.analysis.UnivariateVectorFunction):
    """
    public interface Vector3DFunction extends :class:`~fr.cnes.sirius.patrius.math.analysis.UnivariateVectorFunction`
    
        This interface is a time-dependent function representing a generic vector 3D.
    
        Since:
            1.3
    """
    def getSize(self) -> int:
        """
            Compute the size of the list of values of the function as created by the
            :meth:`~fr.cnes.sirius.patrius.math.analysis.UnivariateVectorFunction.value` method
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.analysis.UnivariateVectorFunction.getSize` in
                interface :class:`~fr.cnes.sirius.patrius.math.analysis.UnivariateVectorFunction`
        
            Returns:
                the size of the values array
        
        
        """
        ...
    def getVector3D(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> Vector3D: ...
    def integral(self, double: float, double2: float) -> Vector3D:
        """
            Returns the integral of the vector function in the given interval. The integration can be analytical or numerical,
            depending on the current vector function.
        
            Parameters:
                x0 (double): the lower bound of the interval.
                xf (double): the upper bound of the interval.
        
            Returns:
                the value of the integral
        
        
        """
        ...
    def nthDerivative(self, int: int) -> 'Vector3DFunction':
        """
            Compute the :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3DFunction` representing the n-th
            derivative of the current vector function. The derivation can be analytical or numerical, depending on the current
            vector function.
        
            Parameters:
                order (int): the order n
        
            Returns:
                the n-th derivative of the current vector function.
        
        
        """
        ...

class AbstractVector3DFunction(Vector3DFunction):
    """
    public abstract class AbstractVector3DFunction extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3DFunction`
    
        This abstract class is a time-dependent function representing a vector 3D.
    
        Since:
            1.3
    """
    DEFAULT_STEP: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_STEP
    
        Default finite difference step.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate): ...
    @typing.overload
    def __init__(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, univariateVectorFunctionDifferentiator: typing.Union[fr.cnes.sirius.patrius.math.analysis.differentiation.UnivariateVectorFunctionDifferentiator, typing.Callable]): ...
    @typing.overload
    def __init__(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate, univariateVectorFunctionDifferentiator: typing.Union[fr.cnes.sirius.patrius.math.analysis.differentiation.UnivariateVectorFunctionDifferentiator, typing.Callable], univariateIntegrator: fr.cnes.sirius.patrius.math.analysis.integration.UnivariateIntegrator): ...
    def getDifferentiator(self) -> fr.cnes.sirius.patrius.math.analysis.differentiation.UnivariateVectorFunctionDifferentiator:
        """
            Get the differentiator.
        
            Returns:
                the differentiator.
        
        
        """
        ...
    def getIntegrator(self) -> fr.cnes.sirius.patrius.math.analysis.integration.UnivariateIntegrator:
        """
            Get the integrator.
        
            Returns:
                the integrator.
        
        
        """
        ...
    def getSize(self) -> int:
        """
            Compute the size of the list of values of the function as created by the
            :meth:`~fr.cnes.sirius.patrius.math.analysis.UnivariateVectorFunction.value` method
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.analysis.UnivariateVectorFunction.getSize` in
                interface :class:`~fr.cnes.sirius.patrius.math.analysis.UnivariateVectorFunction`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3DFunction.getSize` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3DFunction`
        
            Returns:
                the size of the values array
        
        
        """
        ...
    def getVector3D(self, absoluteDate: fr.cnes.sirius.patrius.time.AbsoluteDate) -> Vector3D: ...
    def getZeroDate(self) -> fr.cnes.sirius.patrius.time.AbsoluteDate:
        """
            Get the date at x = 0.
        
            Returns:
                the date at x = 0.
        
        
        """
        ...
    def integral(self, double: float, double2: float) -> Vector3D:
        """
            Returns the integral of the vector function in the given interval. The integration is performed using a numerical
            integration method. This method can be overridden if an analytical integration should be performed instead.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3DFunction.integral` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3DFunction`
        
            Parameters:
                x0 (double): the lower bound of the interval.
                xf (double): the upper bound of the interval.
        
            Returns:
                the value of the integral
        
        
        """
        ...
    def nthDerivative(self, int: int) -> Vector3DFunction:
        """
            Compute the :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3DFunction` representing the n-th
            derivative of the current vector function.
        
        
            The differentiation is performed using a numerical differentiation method. This method can be overridden if an
            analytical differentiation should be performed instead.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3DFunction.nthDerivative` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3DFunction`
        
            Parameters:
                order (int): the order n
        
            Returns:
                the n-th derivative of the current vector function.
        
        
        """
        ...
    def value(self, double: float) -> typing.MutableSequence[float]:
        """
            Compute the components of the vector at the (zero + x) date.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.analysis.UnivariateVectorFunction.value` in
                interface :class:`~fr.cnes.sirius.patrius.math.analysis.UnivariateVectorFunction`
        
            Parameters:
                x (double): the time from the date zero for which the function value should be computed
        
            Returns:
                the three components of the vector at the given date.
        
            Raises:
        
        """
        ...

class EulerRotation(Rotation):
    """
    public class EulerRotation extends :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation`
    
        Rotation focusing on Euler angles. This is a specific class extending
        :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation`. It does not contain algorithmic code but allow
        to store an Euler rotation order.
    
        Since:
            4.1
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, rotationOrder: RotationOrder, double: float, double2: float, double3: float): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation.equals` in
                class :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation`
        
        
        """
        ...
    @typing.overload
    def getAngles(self) -> typing.MutableSequence[float]:
        """
            Get the Cardan or Euler angles corresponding to the instance in the initial rotation order.
        
            Returns:
                an array of three angles, in the order specified by the set
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation.getAngles`
        
        
        """
        ...
    @typing.overload
    def getAngles(self, rotationOrder: RotationOrder) -> typing.MutableSequence[float]:
        """
            Get the Cardan or Euler angles corresponding to the instance.
        
            The equations show that each rotation can be defined by two different values of the Cardan or Euler angles set. For
            example if Cardan angles are used, the rotation defined by the angles a :sub:`1` , a :sub:`2` and a :sub:`3` is the same
            as the rotation defined by the angles π + a :sub:`1` , π - a :sub:`2` and π + a :sub:`3` . This method implements the
            following arbitrary choices:
        
              - for Cardan angles, the chosen set is the one for which the second angle is between -π/2 and π/2 (i.e its cosine is
                positive),
              - for Euler angles, the chosen set is the one for which the second angle is between 0 and π (i.e its sine is positive).
        
        
            Cardan and Euler angle have a very disappointing drawback: all of them have singularities. For Cardan angles, this is
            often called gimbal lock. There is *nothing* to do to prevent this, it is an intrinsic problem with Cardan and Euler
            representation (but not a problem with the rotation itself, which is perfectly well defined). For Cardan angles,
            singularities occur when the second angle is close to -π/2 or +π/2, for Euler angle singularities occur when the
            second angle is close to 0 or π, this implies that the identity rotation is always singular for Euler angles!
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation.getAngles` in
                class :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation`
        
            Parameters:
                order (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.RotationOrder`): rotation order to use
        
            Returns:
                an array of three angles, in the order specified by the set
        
        """
        ...
    def getRotationOrder(self) -> RotationOrder:
        """
            Getter for the order of rotations to use for (alpha1, alpha2, alpha3) composition.
        
            Returns:
                the order of rotations to use for (alpha1, alpha2, alpha3) composition
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation.hashCode` in
                class :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation`
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a string representation for the rotation.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation.toString` in
                class :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation`
        
            Returns:
                a string representation for this rotation
        
        
        """
        ...

class InfiniteShape(Shape):
    """
    public interface InfiniteShape extends :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
    
        Interface for all infinite shapes.
    """
    ...

class RightCircularSurfaceCylinder(CrossSectionProvider):
    """
    public class RightCircularSurfaceCylinder extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.CrossSectionProvider`
    
        Cylinder shape class.
    """
    def __init__(self, double: float, double2: float): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getCrossSection(self, vector3D: Vector3D) -> float: ...
    def getEquivalentTransversalSurf(self) -> float:
        """
            Get equivalent transversal surface. This surface is used in order to modelize the cylinder as a parallelepiped (m2).
        
            Returns:
                the transveral surface of the equivalent parallelepiped
        
        
        """
        ...
    def getLength(self) -> float: ...
    @staticmethod
    def getLengthFromTSurfaceAndRadius(double: float, double2: float) -> float: ...
    def getRadius(self) -> float:
        """
            Get radius corresponding to perpendicular x axis surface (m).
        
            Returns:
                the radius
        
        
        """
        ...
    def getSurfX(self) -> float:
        """
            Get surface perpendicular to X axis (m2).
        
            Returns:
                the surface perpendicular to X axis
        
        
        """
        ...
    @staticmethod
    def getTSurfaceFromRadiusAndLength(double: float, double2: float) -> float:
        """
            Get transversal surface from radius and length.
        
            Parameters:
                radius (double): cylinder radius
                length (double): cylinder length
        
            Returns:
                the surface
        
        
        """
        ...
    def getTransversalSurf(self) -> float:
        """
            Get transversal surface (m2).
        
            Returns:
                the transversal surface
        
        
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

class RightParallelepiped(CrossSectionProvider, java.io.Serializable):
    """
    public class RightParallelepiped extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.CrossSectionProvider`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Right parallelepiped shape.
    
        Since:
            4.1
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getCrossSection(self, vector3D: Vector3D) -> float: ...
    def getHeight(self) -> float: ...
    @staticmethod
    def getHeightFromSurfs(double: float, double2: float, double3: float) -> float: ...
    def getLength(self) -> float: ...
    @staticmethod
    def getLengthFromSurfs(double: float, double2: float, double3: float) -> float: ...
    def getSurfX(self) -> float:
        """
            Get surface perpendicular to X axis.
        
            Returns:
                the surface perpendicular to X axis
        
        
        """
        ...
    def getSurfY(self) -> float:
        """
            Get surface perpendicular to Y axis.
        
            Returns:
                the surface perpendicular to Y axis
        
        
        """
        ...
    def getSurfZ(self) -> float:
        """
            Get surface perpendicular to Z axis.
        
            Returns:
                the surface perpendicular to Z axis
        
        
        """
        ...
    def getWidth(self) -> float: ...
    @staticmethod
    def getWidthFromSurfs(double: float, double2: float, double3: float) -> float: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class SolidShape(Shape):
    """
    public interface SolidShape extends :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
    
        Interface for all solids. The rectangles are considered to be solid shapes as they are not infinite.
    """
    ...

class AbstractEllipse(SolidShape, java.io.Serializable):
    """
    public abstract class AbstractEllipse extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.SolidShape`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        This is an abstract describing class for an ellipse in 3D space, with some algorithm to compute intersections and
        distances to some other objects.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`, :meth:`~serialized`
    """
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, vector3D3: Vector3D, double: float, double2: float): ...
    @typing.overload
    def closestPointTo(self, vector3D: Vector3D) -> Vector3D:
        """
            Computes the point on the ellipse closest to a point.
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): the point
        
            Returns:
                the closest point on the ellipse
        
            Computes the points of the shape and the line realizing the shortest distance. If the line intersects the shape, the
            returned points are identical : this point is the one with the lowest abscissa on the line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the two points : first the one from the line, and the one from the shape.
        
        
        """
        ...
    @typing.overload
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]: ...
    @typing.overload
    def distanceTo(self, line: Line) -> float:
        """
            Computes the distance to a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the shortest distance between the the line and the shape
        
            Computes the shortest distance from a point to the ellipse.
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): the point
        
            Returns:
                the shortest distance from the point to the ellipse
        
        
        """
        ...
    @typing.overload
    def distanceTo(self, vector3D: Vector3D) -> float: ...
    def getCenter(self) -> Vector3D:
        """
        
            Returns:
                the center
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Compute the intersection points with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the intersection points if they exist. If no intersection is found, the dimension is zero
        
        
        """
        ...
    def getNormal(self) -> Vector3D:
        """
        
            Returns:
                the normal
        
        
        """
        ...
    def getRadiusA(self) -> float:
        """
        
            Returns:
                the radius A
        
        
        """
        ...
    def getRadiusB(self) -> float:
        """
        
            Returns:
                the radius B
        
        
        """
        ...
    def getU(self) -> Vector3D:
        """
        
            Returns:
                the u vector for the local frame
        
        
        """
        ...
    def getV(self) -> Vector3D:
        """
        
            Returns:
                the v vector for the local frame
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            Tests the intersection with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                true if the line intersects the shape
        
        
        """
        ...

class Cone(SolidShape):
    """
    public interface Cone extends :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.SolidShape`
    
    
        This interface extends the solid shape for the particular case of cones.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`
    """
    ...

class Cylinder(SolidShape):
    """
    public interface Cylinder extends :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.SolidShape`
    
    
        This interface extends the solid shape for the particular case of cylinders.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`
    """
    ...

class IEllipsoid(SolidShape):
    @typing.overload
    def closestPointTo(self, vector3D: Vector3D) -> Vector3D: ...
    @typing.overload
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]: ...
    def getCenter(self) -> Vector3D: ...
    def getNormal(self, vector3D: Vector3D) -> Vector3D: ...
    def getSemiA(self) -> float: ...
    def getSemiB(self) -> float: ...
    def getSemiC(self) -> float: ...

class InfiniteCone(InfiniteShape):
    """
    public interface InfiniteCone extends :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteShape`
    
    
        This interface extends the infinite shape for the particular cases of infinite cones.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`
    """
    def getOrigin(self) -> Vector3D:
        """
        
            Returns:
                the origin
        
        
        """
        ...

class InfiniteCylinder(InfiniteShape):
    """
    public interface InfiniteCylinder extends :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteShape`
    
    
        This interface extends the infinite shape for the particular cases of infinite cylinders.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`
    """
    ...

class Parallelepiped(SolidShape, CrossSectionProvider, java.io.Serializable):
    """
    public class Parallelepiped extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.SolidShape`, :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.CrossSectionProvider`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        This is a describing class for a rectangle parallelepiped shape, with some algorithm to compute intersections and
        distances to some other objects.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`, :meth:`~serialized`
    """
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, vector3D3: Vector3D, double: float, double2: float, double3: float): ...
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Computes the points of the shape and the line realizing the shortest distance. If the line intersects the shape, the
            returned points are identical : this point is the one with the lowest abscissa on the line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the two points : first the one from the line, and the one from the shape.
        
        
        """
        ...
    def distanceTo(self, line: Line) -> float:
        """
            Computes the distance to a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the shortest distance between the the line and the shape
        
        
        """
        ...
    def getCenter(self) -> Vector3D:
        """
        
            Returns:
                the center
        
        
        """
        ...
    def getCorners(self) -> typing.MutableSequence[Vector3D]:
        """
        
            Returns:
                the corners
        
        
        """
        ...
    def getCrossSection(self, vector3D: Vector3D) -> float:
        """
            Computes the cross section from the direction defined by a Vector3D.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.CrossSectionProvider.getCrossSection` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.CrossSectionProvider`
        
            Parameters:
                direction (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): the direction vector
        
            Returns:
                the cross section
        
        
        """
        ...
    def getFaces(self) -> typing.MutableSequence['Plate']:
        """
        
            Returns:
                the faces
        
        
        """
        ...
    def getHeight(self) -> float:
        """
        
            Returns:
                the height
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Compute the intersection points with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the intersection points if they exist. If no intersection is found, the dimension is zero
        
        
        """
        ...
    def getLength(self) -> float:
        """
        
            Returns:
                the length
        
        
        """
        ...
    def getU(self) -> Vector3D:
        """
        
            Returns:
                the u
        
        
        """
        ...
    def getV(self) -> Vector3D:
        """
        
            Returns:
                the v
        
        
        """
        ...
    def getW(self) -> Vector3D:
        """
        
            Returns:
                the w
        
        
        """
        ...
    def getWidth(self) -> float:
        """
        
            Returns:
                the width
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            Tests the intersection with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                true if the line intersects the shape
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a representation for this parallelepiped. The given parameters are in the same order as in the constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a representation for this parallelepiped
        
        
        """
        ...

class Plane(fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane[Euclidean3D], fr.cnes.sirius.patrius.math.geometry.partitioning.Embedding[Euclidean3D, fr.cnes.sirius.patrius.math.geometry.euclidean.twod.Euclidean2D], InfiniteShape, java.io.Serializable):
    """
    public class Plane extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Euclidean3D`>, :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Embedding`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Euclidean3D`,:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.twod.Euclidean2D`>, :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteShape`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        The class represent planes in a three dimensional space.
    
        Since:
            3.0
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, line: Line, vector3D: Vector3D): ...
    @typing.overload
    def __init__(self, plane: 'Plane'): ...
    @typing.overload
    def __init__(self, vector3D: Vector3D): ...
    @typing.overload
    def __init__(self, vector3D: Vector3D, line: Line): ...
    @typing.overload
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D): ...
    @typing.overload
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, vector3D3: Vector3D): ...
    @typing.overload
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, vector3D3: Vector3D, boolean: bool): ...
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Computes the points of the shape and the line realizing the shortest distance. If the line intersects the shape, the
            returned points are identical : this point is the one with the lowest abscissa on the line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the two points : first the one from the line, and the one from the shape.
        
        
        """
        ...
    def contains(self, vector3D: Vector3D) -> bool:
        """
            Check if the instance contains a point.
        
            Parameters:
                p (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): point to check
        
            Returns:
                true if p belongs to the plane
        
        
        """
        ...
    def copySelf(self) -> 'Plane':
        """
            Copy the instance.
        
            The instance created is completely independant of the original one. A deep copy is used, none of the underlying objects
            are shared (except for immutable objects).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane.copySelf` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane`
        
            Returns:
                a new hyperplane, copy of the instance
        
        
        """
        ...
    @typing.overload
    def distanceTo(self, line: Line) -> float:
        """
            Computes the distance between this plane and a point of space.
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): any point of space
        
            Returns:
                the distance between this and the given point
        
            Computes the distance between this plane and a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): a line of space
        
            Returns:
                the distance between this plane and the line : zero if the line intersects this plane
        
        
        """
        ...
    @typing.overload
    def distanceTo(self, vector3D: Vector3D) -> float: ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Compute the intersection points with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the intersection points if they exist. If no intersection is found, the dimension is zero
        
        
        """
        ...
    def getNormal(self) -> Vector3D:
        """
            Get the normalized normal vector.
        
            The frame defined by (:meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getU`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getV`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getNormal`) is a rigth-handed orthonormalized
            frame).
        
            Returns:
                normalized normal vector
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getU`,
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getV`
        
        
        """
        ...
    @typing.overload
    def getOffset(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean3D]) -> float:
        """
            Get the offset (oriented distance) of a parallel plane.
        
            This method should be called only for parallel planes otherwise the result is not meaningful.
        
            The offset is 0 if both planes are the same, it is positive if the plane is on the plus side of the instance and
            negative if it is on the minus side, according to its natural orientation.
        
            Parameters:
                plane (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane`): plane to check
        
            Returns:
                offset of the plane
        
        public double getOffset(:class:`~fr.cnes.sirius.patrius.math.geometry.Vector`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Euclidean3D`> point)
        
            Get the offset (oriented distance) of a point.
        
            The offset is 0 if the point is on the underlying hyperplane, it is positive if the point is on one particular side of
            the hyperplane, and it is negative if the point is on the other side, according to the hyperplane natural orientation.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane.getOffset` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane`
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.Vector`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Euclidean3D`> point): point to check
        
            Returns:
                offset of the point
        
        
        """
        ...
    @typing.overload
    def getOffset(self, plane: 'Plane') -> float: ...
    def getOrigin(self) -> Vector3D:
        """
            Get the origin point of the plane frame.
        
            The point returned is the orthogonal projection of the 3D-space origin in the plane.
        
            Returns:
                the origin point of the plane frame (point closest to the 3D-space origin)
        
        
        """
        ...
    def getPointAt(self, vector2D: fr.cnes.sirius.patrius.math.geometry.euclidean.twod.Vector2D, double: float) -> Vector3D:
        """
            Get one point from the 3D-space.
        
            Parameters:
                plane (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.twod.Vector2D`): desired in-plane coordinates for the point in the plane
                offset (double): desired offset for the point
        
            Returns:
                one point in the 3D-space, with given coordinates and offset relative to the plane
        
        
        """
        ...
    def getU(self) -> Vector3D:
        """
            Get the plane first canonical vector.
        
            The frame defined by (:meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getU`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getV`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getNormal`) is a rigth-handed orthonormalized
            frame).
        
            Returns:
                normalized first canonical vector
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getV`,
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getNormal`
        
        
        """
        ...
    def getV(self) -> Vector3D:
        """
            Get the plane second canonical vector.
        
            The frame defined by (:meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getU`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getV`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getNormal`) is a rigth-handed orthonormalized
            frame).
        
            Returns:
                normalized second canonical vector
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getU`,
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getNormal`
        
        
        """
        ...
    @typing.overload
    def intersection(self, plane: 'Plane') -> Line:
        """
            Get the intersection of a line with the instance.
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): line intersecting the instance
        
            Returns:
                intersection point between between the line and the instance (null if the line is parallel to the instance)
        
            Build the line shared by the instance and another plane.
        
            Parameters:
                other (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane`): other plane
        
            Returns:
                line at the intersection of the instance and the other plane (really a
                :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line` instance)
        
            Get the intersection point of three planes.
        
            Parameters:
                plane1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane`): first plane1
                plane2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane`): second plane2
                plane3 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane`): third plane2
        
            Returns:
                intersection point of three planes, null if some planes are parallel
        
        
        """
        ...
    @typing.overload
    def intersection(self, line: Line) -> Vector3D: ...
    @typing.overload
    @staticmethod
    def intersection(plane: 'Plane', plane2: 'Plane', plane3: 'Plane') -> Vector3D: ...
    def intersects(self, line: Line) -> bool:
        """
            Tests the intersection with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                true if the line intersects the shape
        
        
        """
        ...
    def isSimilarTo(self, plane: 'Plane') -> bool:
        """
            Check if the instance is similar to another plane.
        
            Planes are considered similar if they contain the same points. This does not mean they are equal since they can have
            opposite normals.
        
            Parameters:
                plane (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane`): plane to which the instance is compared
        
            Returns:
                true if the planes are similar
        
        
        """
        ...
    @typing.overload
    def reset(self, plane: 'Plane') -> None:
        """
            Reset the instance as if built from a point and a normal.
        
            Parameters:
                p (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): point belonging to the plane
                normal (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): normal direction to the plane
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathArithmeticException`: if the normal norm is too small
        
            Reset the instance from another one.
        
            The updated instance is completely independant of the original one. A deep reset is used none of the underlying object
            is shared.
        
            Parameters:
                original (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane`): plane to reset from
        
        
        """
        ...
    @typing.overload
    def reset(self, vector3D: Vector3D, vector3D2: Vector3D) -> None: ...
    def revertSelf(self) -> None:
        """
            Revert the plane.
        
            Replace the instance by a similar plane with opposite orientation.
        
            The new plane frame is chosen in such a way that a 3D point that had :code:`(x, y)` in-plane coordinates and :code:`z`
            offset with respect to the plane and is unaffected by the change will have :code:`(y, x)` in-plane coordinates and
            :code:`-z` offset with respect to the new plane. This means that the :code:`u` and :code:`v` vectors returned by the
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getU` and
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getV` methods are exchanged, and the :code:`w`
            vector returned by the :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Plane.getNormal` method is
            reversed.
        
        """
        ...
    def rotate(self, vector3D: Vector3D, rotation: Rotation) -> 'Plane':
        """
            Rotate the plane around the specified point.
        
            The instance is not modified, a new instance is created.
        
            Parameters:
                center (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): rotation center
                rotation (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Rotation`): vectorial rotation operator
        
            Returns:
                a new plane
        
        
        """
        ...
    def sameOrientationAs(self, hyperplane: fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane[Euclidean3D]) -> bool: ...
    def toSpace(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[fr.cnes.sirius.patrius.math.geometry.euclidean.twod.Euclidean2D]) -> Vector3D: ...
    def toSubSpace(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean3D]) -> fr.cnes.sirius.patrius.math.geometry.euclidean.twod.Vector2D: ...
    def translate(self, vector3D: Vector3D) -> 'Plane':
        """
            Translate the plane by the specified amount.
        
            The instance is not modified, a new instance is created.
        
            Parameters:
                translation (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): translation to apply
        
            Returns:
                a new plane
        
        
        """
        ...
    def wholeHyperplane(self) -> SubPlane:
        """
            Build a region covering the whole hyperplane.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane.wholeHyperplane` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane`
        
            Returns:
                a region covering the whole hyperplane
        
        
        """
        ...
    def wholeSpace(self) -> PolyhedronsSet:
        """
            Build a region covering the whole space.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane.wholeSpace` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane`
        
            Returns:
                a region containing the instance (really a
                :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.PolyhedronsSet` instance)
        
        
        """
        ...

class Plate(SolidShape, CrossSectionProvider, java.io.Serializable):
    """
    public final class Plate extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.SolidShape`, :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.CrossSectionProvider`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        This is a describing class for a 3D rectangle plate shape, with some algorithm to compute intersections and distances to
        some other objects.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`, :meth:`~serialized`
    """
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, vector3D3: Vector3D, double: float, double2: float): ...
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Computes the points of the shape and the line realizing the shortest distance. If the line intersects the shape, the
            returned points are identical : this point is the one with the lowest abscissa on the line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the two points : first the one from the line, and the one from the shape.
        
        
        """
        ...
    def distanceTo(self, line: Line) -> float:
        """
            Computes the distance to a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the shortest distance between the the line and the shape
        
        
        """
        ...
    def getC1(self) -> Vector3D:
        """
        
            Returns:
                the first corner
        
        
        """
        ...
    def getC2(self) -> Vector3D:
        """
        
            Returns:
                the second corner
        
        
        """
        ...
    def getC3(self) -> Vector3D:
        """
        
            Returns:
                the third corner
        
        
        """
        ...
    def getC4(self) -> Vector3D:
        """
        
            Returns:
                the fourth corner
        
        
        """
        ...
    def getCenter(self) -> Vector3D:
        """
        
            Returns:
                the center point
        
        
        """
        ...
    def getCrossSection(self, vector3D: Vector3D) -> float:
        """
            Computes the cross section from the direction defined by a Vector3D.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.CrossSectionProvider.getCrossSection` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.CrossSectionProvider`
        
            Parameters:
                direction (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): the direction vector
        
            Returns:
                the cross section
        
        
        """
        ...
    def getEdges(self) -> typing.MutableSequence[LineSegment]:
        """
        
            Returns:
                the edges of the plate
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Compute the intersection points with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the intersection points if they exist. If no intersection is found, the dimension is zero
        
        
        """
        ...
    def getLength(self) -> float:
        """
        
            Returns:
                the length
        
        
        """
        ...
    def getU(self) -> Vector3D:
        """
        
            Returns:
                the U vector of the local frame
        
        
        """
        ...
    def getV(self) -> Vector3D:
        """
        
            Returns:
                the V vector of the local frame
        
        
        """
        ...
    def getWidth(self) -> float:
        """
        
            Returns:
                the width
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            Tests the intersection with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                true if the line intersects the shape
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a representation for this plate. The given parameters are in the same order as in the constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a representation for this plate
        
        
        """
        ...

class SphericalCap(SolidShape):
    """
    public final class SphericalCap extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.SolidShape`
    
        Implements a representation of a spherical cap solid.
    
        This class implements the SolidShape interface, so it provides the expected : intersection with a line, distance from
        the surface of the shape, intersection points...
    
        Since:
            1.0
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.SolidShape`
    """
    def __init__(self, sphere: 'Sphere', plane: Plane): ...
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Computes the points of the shape and the line realizing the shortest distance. If the line intersects the shape, the
            returned points are identical : this point is the one with the lowest abscissa on the line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the two points : first the one from the line, and the one from the shape.
        
        
        """
        ...
    def distanceTo(self, line: Line) -> float:
        """
            Gives the distance from the line to the spherical cap.
        
        
            When the line intersects the spherical cap, the distance is 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): to get the distance from
        
            Returns:
                the distance (>=0)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Returns a list of intersection points between the line and the spherical cap.
        
        
            Only the border points are given. Since the spherical cap is convex, there will always be at most two points returned by
            this method.
        
        
            When there are none, an empty array is returned.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): to intersect
        
            Returns:
                an array of intersection points.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints`
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            Returns true when the line intersects the spherical cap.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): to intersect
        
            Returns:
                true when the line intersects the spherical cap
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a representation for this sphere. The given parameters are in the same order as in the constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a representation for this sphere
        
        
        """
        ...

class Disk(AbstractEllipse):
    """
    public final class Disk extends :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.AbstractEllipse`
    
        Implements a representation of a disk.
    
        The disk is defined by a center, a normal to the plane containing the disk, and a radius.
    
    
        This class implements the SolidShape interface.
    
        Since:
            1.0
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.SolidShape`, :meth:`~serialized`
    """
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, double: float): ...
    def toString(self) -> str:
        """
            Get a string representation for this disk. The given parameters are in the same order as in the constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation for this disk
        
        
        """
        ...

class Ellipse(AbstractEllipse):
    """
    public final class Ellipse extends :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.AbstractEllipse`
    
    
        This is a describing class for an ellipse in 3D space, with some algorithm to compute intersections and distances to
        some other objects.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`, :meth:`~serialized`
    """
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, vector3D3: Vector3D, double: float, double2: float): ...
    def toString(self) -> str:
        """
            Get a string representation for this ellipse. The given parameters are in the same order as in the constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation for this ellipse
        
        
        """
        ...

class Ellipsoid(IEllipsoid, java.io.Serializable):
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, vector3D3: Vector3D, double: float, double2: float, double3: float): ...
    @typing.overload
    def closestPointTo(self, vector3D: Vector3D) -> Vector3D: ...
    @typing.overload
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]: ...
    @typing.overload
    def distanceTo(self, line: Line) -> float: ...
    @typing.overload
    def distanceTo(self, vector3D: Vector3D) -> float: ...
    def getAffineLocalExpression(self, vector3D: Vector3D) -> Vector3D: ...
    def getAffineStandardExpression(self, vector3D: Vector3D) -> Vector3D: ...
    def getCartesianCoordinates(self, double: float, double2: float) -> typing.MutableSequence[float]: ...
    def getCenter(self) -> Vector3D: ...
    def getEllipsoidicCoordinates(self, vector3D: Vector3D) -> typing.MutableSequence[float]: ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]: ...
    def getLocalBasisTransform(self) -> Matrix3D: ...
    def getNormal(self, vector3D: Vector3D) -> Vector3D: ...
    def getSemiA(self) -> float: ...
    def getSemiB(self) -> float: ...
    def getSemiC(self) -> float: ...
    def getSemiPrincipalX(self) -> Vector3D: ...
    def getSemiPrincipalY(self) -> Vector3D: ...
    def getSemiPrincipalZ(self) -> Vector3D: ...
    def getStandardBasisTransform(self) -> Matrix3D: ...
    def getVectorialLocalExpression(self, vector3D: Vector3D) -> Vector3D: ...
    def getVectorialStandardExpression(self, vector3D: Vector3D) -> Vector3D: ...
    def intersects(self, line: Line) -> bool: ...
    def setNewtonThreshold(self, double: float) -> None: ...
    def toString(self) -> str: ...

class EllipticCone(Cone, java.io.Serializable):
    """
    public final class EllipticCone extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Cone`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        This is a describing class for a 3D oblique circular cone ended by a plane normal to its axis, with some algorithm to
        compute intersections and distances to some other objects.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`, :meth:`~serialized`
    """
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, vector3D3: Vector3D, double: float, double2: float, double3: float): ...
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Computes the points of the shape and the line realizing the shortest distance. If the line intersects the shape, the
            returned points are identical : this point is the one with the lowest abscissa on the line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the two points : first the one from the line, and the one from the shape.
        
        
        """
        ...
    def distanceTo(self, line: Line) -> float:
        """
            Computes the distance to a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the shortest distance between the the line and the shape
        
        
        """
        ...
    def getAngleU(self) -> float:
        """
        
            Returns:
                the angle in U/W plane
        
        
        """
        ...
    def getAngleV(self) -> float:
        """
        
            Returns:
                the angle in U/W plane
        
        
        """
        ...
    def getDirection(self) -> Vector3D:
        """
        
            Returns:
                the direction
        
        
        """
        ...
    def getHeight(self) -> float:
        """
        
            Returns:
                the height
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Compute the intersection points with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the intersection points if they exist. If no intersection is found, the dimension is zero
        
        
        """
        ...
    def getOrigin(self) -> Vector3D:
        """
        
            Returns:
                the origin
        
        
        """
        ...
    def getU(self) -> Vector3D:
        """
        
            Returns:
                the u vector for the local frame
        
        
        """
        ...
    def getV(self) -> Vector3D:
        """
        
            Returns:
                the v vector for the local frame
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            Tests the intersection with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                true if the line intersects the shape
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a representation for this oblique circular cone. The given parameters are in the same order as in the constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a representation for this oblique circular cone
        
        
        """
        ...

class EllipticCylinder(Cylinder, java.io.Serializable):
    """
    public final class EllipticCylinder extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Cylinder`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        This is a describing class for a 3D oblique circular cylinder ended by two planes normal to its axis, with some
        algorithm to compute intersections and distances to some other objects.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`, :meth:`~serialized`
    """
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, vector3D3: Vector3D, double: float, double2: float, double3: float): ...
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Computes the points of the shape and the line realizing the shortest distance. If the line intersects the shape, the
            returned points are identical : this point is the one with the lowest abscissa on the line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the two points : first the one from the line, and the one from the shape.
        
        
        """
        ...
    def distanceTo(self, line: Line) -> float:
        """
            Computes the distance to a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the shortest distance between the the line and the shape
        
        
        """
        ...
    def getDirection(self) -> Vector3D:
        """
        
            Returns:
                the direction of the axis
        
        
        """
        ...
    def getHeight(self) -> float:
        """
        
            Returns:
                the height
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Compute the intersection points with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the intersection points if they exist. If no intersection is found, the dimension is zero
        
        
        """
        ...
    def getOrigin(self) -> Vector3D:
        """
        
            Returns:
                the origin
        
        
        """
        ...
    def getRadiusA(self) -> float:
        """
        
            Returns:
                the radiusA, on U axis of the local frame
        
        
        """
        ...
    def getRadiusB(self) -> float:
        """
        
            Returns:
                the radiusB, on V axis of the local frame
        
        
        """
        ...
    def getU(self) -> Vector3D:
        """
        
            Returns:
                the u vector of the local frame
        
        
        """
        ...
    def getV(self) -> Vector3D:
        """
        
            Returns:
                the v vector of the local frame
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            Tests the intersection with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                true if the line intersects the shape
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a string representation for this elliptic cylinder. The given parameters are in the same order as in the
            constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation for this elliptic cylinder
        
        
        """
        ...

class InfiniteEllipticCone(InfiniteCone, java.io.Serializable):
    """
    public final class InfiniteEllipticCone extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteCone`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        This class is the Infinite Oblique Circular Cone class.
    
        It represents the mathematical object by the same name.
    
        Since:
            1.0
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteCone`,
            :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`, :meth:`~serialized`
    """
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, vector3D3: Vector3D, double: float, double2: float): ...
    @typing.overload
    def closestPointTo(self, vector3D: Vector3D) -> Vector3D:
        """
            Computes the closest point on the cone to a user specified point
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): specified by user in standard basis
        
            Returns:
                A vector3D representing the coordinates of the closest point
        
            Calculate the closest point to a line
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): specified by user
        
            Returns:
                closest point as a Vector3D to line
        
        
        """
        ...
    @typing.overload
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]: ...
    @typing.overload
    def distanceTo(self, line: Line) -> float:
        """
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): specified by user in standard basis
        
            Returns:
                distance to point. Negative if point is inside cone
        
            Get the smallest distance from the line to the cone
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the computed distance
        
        
        """
        ...
    @typing.overload
    def distanceTo(self, vector3D: Vector3D) -> float: ...
    def getAffineLocalExpression(self, vector3D: Vector3D) -> Vector3D:
        """
            Express a Vector3D in spheroid local frame. Warning : Affine transformation
        
            Parameters:
                myVector (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): Vector expressed in standard basis
        
            Returns:
                vectorRef Same vector expressed in spheroid local frame
        
        
        """
        ...
    def getAffineStandardExpression(self, vector3D: Vector3D) -> Vector3D:
        """
            Express a Vector3D in standard basis. Warning : Affine transformation
        
            Parameters:
                vector (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): Vector expressed in spheroid local frame
        
            Returns:
                vectorRef Same vector expressed in standard basis
        
        
        """
        ...
    def getAngleX(self) -> float:
        """
            This method returns the angle of the cone along X axis
        
            Returns:
                A double representing the angle along X axis
        
        
        """
        ...
    def getAngleY(self) -> float:
        """
            This method returns the angle of the cone along Y axis
        
            Returns:
                A double representing the angle along Y axis
        
        
        """
        ...
    def getApertureX(self) -> float:
        """
            This method returns the aperture of the cone along X axis
        
            Returns:
                A double representing the aperture along X axis
        
        
        """
        ...
    def getApertureY(self) -> float:
        """
            This method returns the aperture of the cone along Y axis
        
            Returns:
                A double representing the aperture along Y axis
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            This methods computes and returns the intersection points between a line and the cone.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): The line with which the intersections are to be computed
        
            Returns:
                A Vector3D array containing the intersections coordinates. If no intersections have been found, the array is empty.
        
        
        """
        ...
    def getLocalBasisTransform(self) -> Matrix3D:
        """
            This method returns the matrix of the transformation to the local basis
        
            Returns:
                the matrix
        
        
        """
        ...
    def getOrigin(self) -> Vector3D:
        """
            This method returns the origin of the cone
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteCone.getOrigin` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteCone`
        
            Returns:
                A vector containing the coordinates of the cones origin
        
        
        """
        ...
    def getSemiAxisX(self) -> float:
        """
            This method returns the semi axis of the cone along X axis
        
            Returns:
                A double representing the semi axis along X axis (at height :code:`h=1`)
        
        
        """
        ...
    def getSemiAxisY(self) -> float:
        """
            This method returns the semi axis of the cone along Y axis
        
            Returns:
                A double representing the semi axis along Y axis (at height :code:`h=1`)
        
        
        """
        ...
    def getStandardBasisTransform(self) -> Matrix3D:
        """
            This method returns the matrix of the transformation to the standard basis
        
            Returns:
                A vector containing the coordinates of the cones origin
        
        
        """
        ...
    def getVectorialLocalExpression(self, vector3D: Vector3D) -> Vector3D:
        """
            Express a Vector3D in spheroid local frame. Warning : Vectorial transformation
        
            Parameters:
                myVector (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): Vector expressed in standard basis
        
            Returns:
                vectorRef Same vector expressed in spheroid local frame
        
        
        """
        ...
    def getVectorialStandardExpression(self, vector3D: Vector3D) -> Vector3D:
        """
            Express a Vector3D in standard basis. Warning : Vectorial transformation
        
            Parameters:
                vector (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): Vector expressed in spheroid local frame
        
            Returns:
                vectorRef Same vector expressed in standard basis
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            This method returns true if the user specified line intersects the cone.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): User specified line
        
            Returns:
                a boolean set to true if the line intersects, false otherwise
        
        
        """
        ...
    def isInside(self, vector3D: Vector3D) -> bool:
        """
            Return true if point is inside cone
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): in standard basis
        
            Returns:
                boolean if is inside
        
            Since:
                1.0
        
        
        """
        ...
    def isStrictlyInside(self, vector3D: Vector3D) -> bool:
        """
            Return true if point is inside cone
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): in standard basis
        
            Returns:
                boolean if is inside
        
            Since:
                1.0
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a representation for this infinite oblique circular cone. The given parameters are in the same order as in the
            constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a representation for this infinite oblique circular cone
        
        
        """
        ...

class InfiniteEllipticCylinder(InfiniteCylinder, java.io.Serializable):
    """
    public final class InfiniteEllipticCylinder extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteCylinder`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        This class is the Infinite Elliptic Cylinder class.
    
        It represents the mathematical object by he same name
    
        Since:
            1.0
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteCylinder`,
            :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`, :meth:`~serialized`
    """
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, vector3D3: Vector3D, double: float, double2: float): ...
    @typing.overload
    def closestPointTo(self, vector3D: Vector3D) -> Vector3D:
        """
            Computes the closest point on the cone to a user specified point
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): specified by user in standard basis
        
            Returns:
                A vector3D representing the coordinates of the closest point
        
            Calculate closest point to a line
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): user line
        
            Returns:
                points in a Vector3D array.
        
            Since:
                1.0
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteEllipticCylinder.closestPointTo`
        
        
        """
        ...
    @typing.overload
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]: ...
    @typing.overload
    def distanceTo(self, line: Line) -> float:
        """
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): specified by user in standard basis
        
            Returns:
                distance to point. Negative if point is inside cone
        
            Get the smallest distance from the line to the cone
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the computed distance
        
        
        """
        ...
    @typing.overload
    def distanceTo(self, vector3D: Vector3D) -> float: ...
    def getAffineLocalExpression(self, vector3D: Vector3D) -> Vector3D:
        """
            Express a Vector3D in spheroid local frame. Warning : Affine transformation
        
            Parameters:
                myVector (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): Vector expressed in standard basis
        
            Returns:
                vectorRef Same vector expressed in spheroid local frame
        
        
        """
        ...
    def getAffineStandardExpression(self, vector3D: Vector3D) -> Vector3D:
        """
            Express a Vector3D in standard basis. Warning : Affine transformation
        
            Parameters:
                myVector (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): Vector expressed in spheroid local frame
        
            Returns:
                vectorRef Same vector expressed in standard basis
        
        
        """
        ...
    def getDirection(self) -> Vector3D:
        """
            This method returns the main axis of the cylinder
        
            Returns:
                A vector containing the cylinders' axis
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            This methods computes and returns the intersection points between a line and the cylinder.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): The line with which the intersections are to be computed
        
            Returns:
                A Vector3D array containing the intersections coordinates. If no intersections have been found, the array is empty.
        
        
        """
        ...
    def getLocalBasisTransform(self) -> Matrix3D:
        """
            This method returns the matrix of the transformation to the local basis
        
            Returns:
                the matrix
        
        
        """
        ...
    def getOrigin(self) -> Vector3D:
        """
            This method returns the position of the cylinder on the Oxy plane
        
            Returns:
                A vector containing the position
        
        
        """
        ...
    def getSemiAxisA(self) -> float:
        """
            This method returns the semi axis a
        
            Returns:
                A double representing the semi axis along X axis
        
        
        """
        ...
    def getSemiAxisB(self) -> float:
        """
            This method returns the semi axis b
        
            Returns:
                A double representing the semi axis along b axis
        
        
        """
        ...
    def getStandardBasisTransform(self) -> Matrix3D:
        """
            This method returns the matrix of the transformation to the standard basis
        
            Returns:
                A vector containing the coordinates of the cylinder origin
        
        
        """
        ...
    def getVectorialLocalExpression(self, vector3D: Vector3D) -> Vector3D:
        """
            Express a Vector3D in spheroid local frame. Warning : Vectorial transformation
        
            Parameters:
                myVector (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): Vector expressed in standard basis
        
            Returns:
                vectorRef Same vector expressed in spheroid local frame
        
        
        """
        ...
    def getVectorialStandardExpression(self, vector3D: Vector3D) -> Vector3D:
        """
            Express a Vector3D in standard basis. Warning : Vectorial transformation
        
            Parameters:
                myVector (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): Vector expressed in spheroid local frame
        
            Returns:
                vectorRef Same vector expressed in standard basis
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            This method returns true if the user specified line intersects the cylinder.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): User specified line
        
            Returns:
                a boolean set to true if the line intersects, false otherwise
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a representation for this infinite elliptic cylinder. The given parameters are in the same order as in the
            constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a representation for this infinite elliptic cylinder
        
        
        """
        ...

class InfiniteRectangleCone(InfiniteCone, java.io.Serializable):
    """
    public final class InfiniteRectangleCone extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteCone`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        This is a describing class for a 3D infinite cone, with some algorithm to compute intersections and distances to some
        other objects.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`, :meth:`~serialized`
    """
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, vector3D3: Vector3D, double: float, double2: float): ...
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Computes the points of the shape and the line realizing the shortest distance. If the line intersects the shape, the
            returned points are identical : this point is the one with the lowest abscissa on the line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the two points : first the one from the line, and the one from the shape.
        
        
        """
        ...
    def distanceTo(self, line: Line) -> float:
        """
            Computes the distance to a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the shortest distance between the the line and the shape
        
        
        """
        ...
    def getAngleU(self) -> float:
        """
        
            Returns:
                the angle on the U axis
        
        
        """
        ...
    def getAngleV(self) -> float:
        """
        
            Returns:
                the angle on the V axis
        
        
        """
        ...
    def getAxis(self) -> Vector3D:
        """
        
            Returns:
                the axis
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Compute the intersection points with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the intersection points if they exist. If no intersection is found, the dimension is zero
        
        
        """
        ...
    def getOrigin(self) -> Vector3D:
        """
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteCone.getOrigin` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteCone`
        
            Returns:
                the origin
        
        
        """
        ...
    def getU(self) -> Vector3D:
        """
        
            Returns:
                the U local frame vector
        
        
        """
        ...
    def getV(self) -> Vector3D:
        """
        
            Returns:
                the V local frame vector
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            Tests the intersection with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                true if the line intersects the shape
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a representation for this infinite rectangle cone. The given parameters are in the same order as in the constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a representation for this infinite rectangle cone
        
        
        """
        ...

class InfiniteRectangleCylinder(InfiniteCylinder):
    """
    public final class InfiniteRectangleCylinder extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteCylinder`
    
    
        This is a describing class for a 3D infinite rectangle cylinder, with some algorithm to compute intersections and
        distances to some other objects.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`
    """
    @typing.overload
    def __init__(self, line: Line, vector3D: Vector3D, double: float, double2: float): ...
    @typing.overload
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, vector3D3: Vector3D, double: float, double2: float): ...
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Computes the points of the shape and the line realizing the shortest distance. If the line intersects the shape, the
            returned points are identical : this point is the one with the lowest abscissa on the line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the two points : first the one from the line, and the one from the shape.
        
        
        """
        ...
    def distanceTo(self, line: Line) -> float:
        """
            Computes the distance to a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the shortest distance between the the line and the shape
        
        
        """
        ...
    def getDirection(self) -> Vector3D:
        """
        
            Returns:
                the direction
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Compute the intersection points with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the intersection points if they exist. If no intersection is found, the dimension is zero
        
        
        """
        ...
    def getLength(self) -> float:
        """
        
            Returns:
                the length
        
        
        """
        ...
    def getOrigin(self) -> Vector3D:
        """
        
            Returns:
                the origin
        
        
        """
        ...
    def getU(self) -> Vector3D:
        """
        
            Returns:
                the u vector of the frame
        
        
        """
        ...
    def getV(self) -> Vector3D:
        """
        
            Returns:
                the v vector of the frame
        
        
        """
        ...
    def getWidth(self) -> float:
        """
        
            Returns:
                the width
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            Tests the intersection with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                true if the line intersects the shape
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a representation for this infinite rectangle cylinder. The given parameters are in the same order as in the
            constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a representation for this infinite rectangle cylinder
        
        
        """
        ...

class InfiniteRightCircularCone(InfiniteCone, java.io.Serializable):
    """
    public final class InfiniteRightCircularCone extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteCone`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        This is a describing class for a 3D infinite cone, with some algorithm to compute intersections and distances to some
        other objects.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`, :meth:`~serialized`
    """
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, double: float): ...
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Computes the points of the shape and the line realizing the shortest distance. If the line intersects the shape, the
            returned points are identical : this point is the one with the lowest abscissa on the line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the two points : first the one from the line, and the one from the shape.
        
        
        """
        ...
    def distanceTo(self, line: Line) -> float:
        """
            Computes the distance to a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the shortest distance between the the line and the shape
        
        
        """
        ...
    def getAngle(self) -> float:
        """
        
            Returns:
                the angle
        
        
        """
        ...
    def getAxis(self) -> Vector3D:
        """
        
            Returns:
                the axis
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Compute the intersection points with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the intersection points if they exist. If no intersection is found, the dimension is zero
        
        
        """
        ...
    def getOrigin(self) -> Vector3D:
        """
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteCone.getOrigin` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteCone`
        
            Returns:
                the origin
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            Tests the intersection with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                true if the line intersects the shape
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a representation for this infinite elliptic cone. The given parameters are in the same order as in the constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a representation for this infinite elliptic cone
        
        
        """
        ...

class InfiniteRightCircularCylinder(InfiniteCylinder, java.io.Serializable):
    """
    public final class InfiniteRightCircularCylinder extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.InfiniteCylinder`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        This is a describing class for a 3D infinite right circular cylinder, with some algorithm to compute intersections and
        distances to some other objects.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, line: Line, double: float): ...
    @typing.overload
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, double: float): ...
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Computes the points of the shape and the line realizing the shortest distance. If the line intersects the shape, the
            returned points are identical : this point is the one with the lowest abscissa on the line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the two points : first the one from the line, and the one from the shape.
        
        
        """
        ...
    def distanceTo(self, line: Line) -> float:
        """
            Computes the distance to a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the shortest distance between the the line and the shape
        
        
        """
        ...
    def getDirection(self) -> Vector3D:
        """
        
            Returns:
                the direction
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Compute the intersection points with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the intersection points if they exist. If no intersection is found, the dimension is zero
        
        
        """
        ...
    def getOrigin(self) -> Vector3D:
        """
        
            Returns:
                the origin
        
        
        """
        ...
    def getRadius(self) -> float:
        """
        
            Returns:
                the radius
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            Tests the intersection with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                true if the line intersects the shape
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a representation for this infinite right circular cylinder. The given parameters are in the same order as in the
            constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a representation for this infinite right circular cylinder
        
        
        """
        ...

class RectangleCone(Cone, java.io.Serializable):
    """
    public final class RectangleCone extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Cone`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        This is a describing class for a 3D rectangle cone ended by a plane normal to its axis (pyramid), with some algorithm to
        compute intersections and distances to some other objects.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`, :meth:`~serialized`
    """
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, vector3D3: Vector3D, double: float, double2: float, double3: float): ...
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Computes the points of the shape and the line realizing the shortest distance. If the line intersects the shape, the
            returned points are identical : this point is the one with the lowest abscissa on the line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the two points : first the one from the line, and the one from the shape.
        
        
        """
        ...
    def distanceTo(self, line: Line) -> float:
        """
            Computes the distance to a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the shortest distance between the the line and the shape
        
        
        """
        ...
    def getDirection(self) -> Vector3D:
        """
        
            Returns:
                the direction
        
        
        """
        ...
    def getHeight(self) -> float:
        """
        
            Returns:
                the height
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Compute the intersection points with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the intersection points if they exist. If no intersection is found, the dimension is zero
        
        
        """
        ...
    def getLength(self) -> float:
        """
        
            Returns:
                the length
        
        
        """
        ...
    def getOrigin(self) -> Vector3D:
        """
        
            Returns:
                the origin
        
        
        """
        ...
    def getU(self) -> Vector3D:
        """
        
            Returns:
                the u vector of the local frame
        
        
        """
        ...
    def getV(self) -> Vector3D:
        """
        
            Returns:
                the v vector of the local frame
        
        
        """
        ...
    def getWidth(self) -> float:
        """
        
            Returns:
                the width
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            Tests the intersection with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                true if the line intersects the shape
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a representation for this rectangle cone. The given parameters are in the same order as in the constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a representation for this rectangle cone
        
        
        """
        ...

class RightCircularCone(Cone, java.io.Serializable):
    """
    public final class RightCircularCone extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Cone`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        This is a describing class for a 3D right circular cone ended by a plane normal to its axis, with some algorithm to
        compute intersections and distances to some other objects.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`, :meth:`~serialized`
    """
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, double: float, double2: float): ...
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Computes the points of the shape and the line realizing the shortest distance. If the line intersects the shape, the
            returned points are identical : this point is the one with the lowest abscissa on the line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the two points : first the one from the line, and the one from the shape.
        
        
        """
        ...
    def distanceTo(self, line: Line) -> float:
        """
            Computes the distance to a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the shortest distance between the the line and the shape
        
        
        """
        ...
    def getAngle(self) -> float:
        """
        
            Returns:
                the angle
        
        
        """
        ...
    def getDirection(self) -> Vector3D:
        """
        
            Returns:
                the direction
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Compute the intersection points with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the intersection points if they exist. If no intersection is found, the dimension is zero
        
        
        """
        ...
    def getLength(self) -> float:
        """
        
            Returns:
                the height
        
        
        """
        ...
    def getOrigin(self) -> Vector3D:
        """
        
            Returns:
                the origin
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            Tests the intersection with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                true if the line intersects the shape
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a representation for this elliptic cone. The given parameters are in the same order as in the constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a representation for this elliptic cone
        
        
        """
        ...

class RightCircularCylinder(CrossSectionProvider, Cylinder, java.io.Serializable):
    """
    public final class RightCircularCylinder extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.CrossSectionProvider`, :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Cylinder`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        This is a describing class for a 3D right circular cylinder ended by two planes normal to its axis, with some algorithm
        to compute intersections and distances to some other objects.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, line: Line, double: float, double2: float): ...
    @typing.overload
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, double: float, double2: float): ...
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Computes the points of the shape and the line realizing the shortest distance. If the line intersects the shape, the
            returned points are identical : this point is the one with the lowest abscissa on the line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the two points : first the one from the line, and the one from the shape.
        
        
        """
        ...
    def distanceTo(self, line: Line) -> float:
        """
            Computes the distance to a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the shortest distance between the the line and the shape
        
        
        """
        ...
    def getBaseSurface(self) -> float:
        """
            Returns the surface of the cylinder base.
        
            Returns:
                the surface of the cylinder base
        
        
        """
        ...
    def getCrossSection(self, vector3D: Vector3D) -> float:
        """
            Computes the cross section from the direction defined by a Vector3D.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.CrossSectionProvider.getCrossSection` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.CrossSectionProvider`
        
            Parameters:
                crossDirection (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): the direction vector
        
            Returns:
                the cross section
        
        
        """
        ...
    def getDirection(self) -> Vector3D:
        """
        
            Returns:
                the direction
        
        
        """
        ...
    def getEquivalentTransversalSurf(self) -> float:
        """
            Get equivalent transversal surface. This surface is used in order to modelize the cylinder as a parallelepiped.
        
            Returns:
                the transveral surface of the equivalent parallelepiped
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Compute the intersection points with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the intersection points if they exist. If no intersection is found, the dimension is zero
        
        
        """
        ...
    def getLength(self) -> float:
        """
        
            Returns:
                the height
        
        
        """
        ...
    def getOrigin(self) -> Vector3D:
        """
        
            Returns:
                the origin
        
        
        """
        ...
    def getRadius(self) -> float:
        """
        
            Returns:
                the radius
        
        
        """
        ...
    def getTransversalSurf(self) -> float:
        """
            Get transversal surface.
        
            Returns:
                the transversal surface
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            Tests the intersection with a line.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                true if the line intersects the shape
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a representation for this right circular cylinder. The given parameters are in the same order as in the constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a representation for this right circular cylinder
        
        
        """
        ...

class Sphere(IEllipsoid, CrossSectionProvider, java.io.Serializable):
    """
    public final class Sphere extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid`, :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.CrossSectionProvider`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        This is a describing class for a 3D spherical shape, with some algorithm to compute intersections and distances to some
        other objects.
    
        Since:
            1.0
    
        Also see:
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo`,
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, vector3D: Vector3D, double: float): ...
    @typing.overload
    def closestPointTo(self, vector3D: Vector3D) -> Vector3D:
        """
            Computes the points of the shape and the line realizing the shortest distance. If the line intersects the shape, the
            returned points are identical : this point is the one with the lowest abscissa on the line.
        
            Note: calculations take the line's minimum abscissa into account.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the two points : first the one from the line, and the one from the shape.
        
            Computes the point, on the ellipsoid surface, that is the closest to a point of space.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid.closestPointTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid`
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): the point expressed in standard basis
        
            Returns:
                the closest point to the user point on the ellipsoid surface
        
        
        """
        ...
    @typing.overload
    def closestPointTo(self, line: Line) -> typing.MutableSequence[Vector3D]: ...
    @typing.overload
    def distanceTo(self, line: Line) -> float:
        """
            Computes the distance to a line.
        
            Note: calculations take the line's minimum abscissa into account.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.distanceTo` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the shortest distance between the the line and the shape
        
            Computes the distance to a point of space.
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): the point
        
            Returns:
                the shortest distance between the surface of the sphere and the point
        
        
        """
        ...
    @typing.overload
    def distanceTo(self, vector3D: Vector3D) -> float: ...
    def getCenter(self) -> Vector3D:
        """
            Description copied from interface: :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid.getCenter`
            Get ellipsoids' center
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid.getCenter` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid`
        
            Returns:
                the center
        
        
        """
        ...
    def getCrossSection(self, vector3D: Vector3D) -> float:
        """
            Computes the cross section from the direction defined by a Vector3D.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.CrossSectionProvider.getCrossSection` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.CrossSectionProvider`
        
            Parameters:
                direction (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): the direction vector
        
            Returns:
                the cross section
        
        
        """
        ...
    def getIntersectionPoints(self, line: Line) -> typing.MutableSequence[Vector3D]:
        """
            Compute the intersection points with a line.
        
            Note: calculations take the line's minimum abscissa into account.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.getIntersectionPoints` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                the intersection points if they exist. If no intersection is found, the dimension is zero
        
        
        """
        ...
    def getNormal(self, vector3D: Vector3D) -> Vector3D:
        """
            Computes the normal vector to the surface
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid.getNormal` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid`
        
            Parameters:
                point (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Vector3D`): Point as a Vector3D
        
            Returns:
                the normal vector in local basis
        
        
        """
        ...
    def getRadius(self) -> float:
        """
        
            Returns:
                the radius
        
        
        """
        ...
    @staticmethod
    def getRadiusFromSurface(double: float) -> float:
        """
            Get radius from surface value.
        
            Parameters:
                surface (double): surface
        
            Returns:
                radius
        
        
        """
        ...
    def getSemiA(self) -> float:
        """
            Get semi axis A
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid.getSemiA` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid`
        
            Returns:
                semi axis a
        
        
        """
        ...
    def getSemiB(self) -> float:
        """
            Get semi axis B
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid.getSemiB` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid`
        
            Returns:
                semi axis b
        
        
        """
        ...
    def getSemiC(self) -> float:
        """
            Get semi axis C
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid.getSemiC` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.IEllipsoid`
        
            Returns:
                semi axis c
        
        
        """
        ...
    def getSurface(self) -> float:
        """
            Get surface
        
            Returns:
                the sphere surface
        
        
        """
        ...
    @staticmethod
    def getSurfaceFromRadius(double: float) -> float:
        """
            Get surface from radius value.
        
            Parameters:
                radius (double): radius
        
            Returns:
                surface
        
        
        """
        ...
    def intersects(self, line: Line) -> bool:
        """
            Tests the intersection with a line.
        
            Note: calculations take the line's minimum abscissa into account.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape.intersects` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Shape`
        
            Parameters:
                line (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.threed.Line`): the line
        
            Returns:
                true if the line intersects the shape
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a representation for this sphere. The given parameters are in the same order as in the constructor.
        
            Overrides:
                 in class 
        
            Returns:
                a representation for this sphere
        
        
        """
        ...

class Spheroid(Ellipsoid):
    def __init__(self, vector3D: Vector3D, vector3D2: Vector3D, double: float, double2: float): ...
    def getEquatorialRadius(self) -> float: ...
    def getPolarRadius(self) -> float: ...
    def toString(self) -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("fr.cnes.sirius.patrius.math.geometry.euclidean.threed")``.

    AbstractEllipse: typing.Type[AbstractEllipse]
    AbstractVector3DFunction: typing.Type[AbstractVector3DFunction]
    AzimuthElevationCalculator: typing.Type[AzimuthElevationCalculator]
    CardanCalculator: typing.Type[CardanCalculator]
    Cone: typing.Type[Cone]
    CrossSectionProvider: typing.Type[CrossSectionProvider]
    Cylinder: typing.Type[Cylinder]
    Disk: typing.Type[Disk]
    Ellipse: typing.Type[Ellipse]
    Ellipsoid: typing.Type[Ellipsoid]
    EllipticCone: typing.Type[EllipticCone]
    EllipticCylinder: typing.Type[EllipticCylinder]
    Euclidean3D: typing.Type[Euclidean3D]
    EulerRotation: typing.Type[EulerRotation]
    FieldRotation: typing.Type[FieldRotation]
    FieldVector3D: typing.Type[FieldVector3D]
    IEllipsoid: typing.Type[IEllipsoid]
    InfiniteCone: typing.Type[InfiniteCone]
    InfiniteCylinder: typing.Type[InfiniteCylinder]
    InfiniteEllipticCone: typing.Type[InfiniteEllipticCone]
    InfiniteEllipticCylinder: typing.Type[InfiniteEllipticCylinder]
    InfiniteRectangleCone: typing.Type[InfiniteRectangleCone]
    InfiniteRectangleCylinder: typing.Type[InfiniteRectangleCylinder]
    InfiniteRightCircularCone: typing.Type[InfiniteRightCircularCone]
    InfiniteRightCircularCylinder: typing.Type[InfiniteRightCircularCylinder]
    InfiniteShape: typing.Type[InfiniteShape]
    Line: typing.Type[Line]
    LineSegment: typing.Type[LineSegment]
    Matrix3D: typing.Type[Matrix3D]
    NotARotationMatrixException: typing.Type[NotARotationMatrixException]
    OutlineExtractor: typing.Type[OutlineExtractor]
    Parallelepiped: typing.Type[Parallelepiped]
    Plane: typing.Type[Plane]
    Plate: typing.Type[Plate]
    PolyhedronsSet: typing.Type[PolyhedronsSet]
    RectangleCone: typing.Type[RectangleCone]
    RightCircularCone: typing.Type[RightCircularCone]
    RightCircularCylinder: typing.Type[RightCircularCylinder]
    RightCircularSurfaceCylinder: typing.Type[RightCircularSurfaceCylinder]
    RightParallelepiped: typing.Type[RightParallelepiped]
    Rotation: typing.Type[Rotation]
    RotationOrder: typing.Type[RotationOrder]
    Screw: typing.Type[Screw]
    Segment: typing.Type[Segment]
    Shape: typing.Type[Shape]
    SolidShape: typing.Type[SolidShape]
    Sphere: typing.Type[Sphere]
    SphericalCap: typing.Type[SphericalCap]
    SphericalCoordinates: typing.Type[SphericalCoordinates]
    Spheroid: typing.Type[Spheroid]
    SubLine: typing.Type[SubLine]
    SubPlane: typing.Type[SubPlane]
    Vector3D: typing.Type[Vector3D]
    Vector3DFormat: typing.Type[Vector3DFormat]
    Vector3DFunction: typing.Type[Vector3DFunction]
