
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import fr.cnes.sirius.patrius.math.geometry
import fr.cnes.sirius.patrius.math.geometry.partitioning
import fr.cnes.sirius.patrius.math.linear
import java.lang
import java.text
import java.util
import typing



class Euclidean1D(fr.cnes.sirius.patrius.math.geometry.Space):
    """
    public final class Euclidean1D extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.Space`
    
        This class implements a one-dimensional space.
    
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
    def getInstance() -> 'Euclidean1D':
        """
            Get the unique instance.
        
            Returns:
                the unique instance
        
        
        """
        ...
    def getSubSpace(self) -> fr.cnes.sirius.patrius.math.geometry.Space:
        """
            Get the n-1 dimension subspace of this space.
        
            As the 1-dimension Euclidean space does not have proper sub-spaces, this method always throws a
            :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Space.getSubSpace` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Space`
        
            Returns:
                nothing
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: in all cases
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Space.getDimension`
        
        
        """
        ...

class Interval:
    """
    public class Interval extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`
    
        This class represents a 1D interval.
    
        Since:
            3.0
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.IntervalsSet`
    """
    def __init__(self, double: float, double2: float): ...
    def checkPoint(self, double: float, double2: float) -> fr.cnes.sirius.patrius.math.geometry.partitioning.Region.Location:
        """
            Check a point with respect to the interval.
        
            Parameters:
                point (double): point to check
                tolerance (double): tolerance below which points are considered to belong to the boundary
        
            Returns:
                a code representing the point status: either
                :meth:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Region.Location.INSIDE`,
                :meth:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Region.Location.OUTSIDE` or
                :meth:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Region.Location.BOUNDARY`
        
            Since:
                3.1
        
        
        """
        ...
    def getBarycenter(self) -> float:
        """
            Get the barycenter of the interval.
        
            Returns:
                barycenter of the interval
        
            Since:
                3.1
        
        
        """
        ...
    def getInf(self) -> float:
        """
            Get the lower bound of the interval.
        
            Returns:
                lower bound of the interval
        
            Since:
                3.1
        
        
        """
        ...
    def getSize(self) -> float:
        """
            Get the size of the interval.
        
            Returns:
                size of the interval
        
            Since:
                3.1
        
        
        """
        ...
    def getSup(self) -> float:
        """
            Get the upper bound of the interval.
        
            Returns:
                upper bound of the interval
        
            Since:
                3.1
        
        
        """
        ...

class IntervalsSet(fr.cnes.sirius.patrius.math.geometry.partitioning.AbstractRegion[Euclidean1D, Euclidean1D]):
    """
    public class IntervalsSet extends :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.AbstractRegion`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Euclidean1D`,:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Euclidean1D`>
    
        This class represents a 1D region: a set of intervals.
    
        Since:
            3.0
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, bSPTree: fr.cnes.sirius.patrius.math.geometry.partitioning.BSPTree[Euclidean1D]): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection[fr.cnes.sirius.patrius.math.geometry.partitioning.SubHyperplane[Euclidean1D]], typing.Sequence[fr.cnes.sirius.patrius.math.geometry.partitioning.SubHyperplane[Euclidean1D]], typing.Set[fr.cnes.sirius.patrius.math.geometry.partitioning.SubHyperplane[Euclidean1D]]]): ...
    def asList(self) -> java.util.List[Interval]: ...
    def buildNew(self, bSPTree: fr.cnes.sirius.patrius.math.geometry.partitioning.BSPTree[Euclidean1D]) -> 'IntervalsSet': ...
    def getInf(self) -> float:
        """
            Get the lowest value belonging to the instance.
        
            Returns:
                lowest value belonging to the instance (:code:`Double.NEGATIVE_INFINITY` if the instance doesn't have any low bound,
                :code:`Double.POSITIVE_INFINITY` if the instance is empty)
        
        
        """
        ...
    def getSup(self) -> float:
        """
            Get the highest value belonging to the instance.
        
            Returns:
                highest value belonging to the instance (:code:`Double.POSITIVE_INFINITY` if the instance doesn't have any high bound,
                :code:`Double.NEGATIVE_INFINITY` if the instance is empty)
        
        
        """
        ...

class OrientedPoint(fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane[Euclidean1D]):
    """
    public class OrientedPoint extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Euclidean1D`>
    
        This class represents a 1D oriented hyperplane.
    
        An hyperplane in 1D is a simple point, its orientation being a boolean.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            3.0
    """
    def __init__(self, vector1D: 'Vector1D', boolean: bool): ...
    def copySelf(self) -> 'OrientedPoint':
        """
            Copy the instance.
        
            Since instances are immutable, this method directly returns the instance.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane.copySelf` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane`
        
            Returns:
                the instance itself
        
        
        """
        ...
    def getLocation(self) -> 'Vector1D':
        """
            Get the hyperplane location on the real line.
        
            Returns:
                the hyperplane location
        
        
        """
        ...
    def getOffset(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean1D]) -> float: ...
    def isDirect(self) -> bool:
        """
            Check if the hyperplane orientation is direct.
        
            Returns:
                true if the plus side of the hyperplane is towards abscissae greater than hyperplane location
        
        
        """
        ...
    def revertSelf(self) -> None:
        """
            Revert the instance.
        
        """
        ...
    def sameOrientationAs(self, hyperplane: fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane[Euclidean1D]) -> bool: ...
    def wholeHyperplane(self) -> 'SubOrientedPoint':
        """
            Build a region covering the whole hyperplane.
        
            Since this class represent zero dimension spaces which does not have lower dimension sub-spaces, this method returns a
            dummy implementation of a :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.SubHyperplane`. This implementation
            is only used to allow the :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.SubHyperplane` class implementation
            to work properly, it should *not* be used otherwise.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane.wholeHyperplane` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane`
        
            Returns:
                a dummy sub hyperplane
        
        
        """
        ...
    def wholeSpace(self) -> IntervalsSet:
        """
            Build a region covering the whole space.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane.wholeSpace` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane`
        
            Returns:
                a region containing the instance (really an :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.IntervalsSet`
                instance)
        
        
        """
        ...

class SubOrientedPoint(fr.cnes.sirius.patrius.math.geometry.partitioning.AbstractSubHyperplane[Euclidean1D, Euclidean1D]):
    """
    public class SubOrientedPoint extends :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.AbstractSubHyperplane`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Euclidean1D`,:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Euclidean1D`>
    
        This class represents sub-hyperplane for :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.OrientedPoint`.
    
        An hyperplane in 1D is a simple point, its orientation being a boolean.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            3.0
    """
    def __init__(self, hyperplane: fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane[Euclidean1D], region: fr.cnes.sirius.patrius.math.geometry.partitioning.Region[Euclidean1D]): ...
    def getSize(self) -> float:
        """
            Get the size of the instance.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.partitioning.SubHyperplane.getSize` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.SubHyperplane`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.partitioning.AbstractSubHyperplane.getSize` in
                class :class:`~fr.cnes.sirius.patrius.math.geometry.partitioning.AbstractSubHyperplane`
        
            Returns:
                the size of the instance (this is a length in 1D, an area in 2D, a volume in 3D ...)
        
        
        """
        ...
    def side(self, hyperplane: fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane[Euclidean1D]) -> fr.cnes.sirius.patrius.math.geometry.partitioning.Side: ...
    def split(self, hyperplane: fr.cnes.sirius.patrius.math.geometry.partitioning.Hyperplane[Euclidean1D]) -> fr.cnes.sirius.patrius.math.geometry.partitioning.SubHyperplane.SplitSubHyperplane[Euclidean1D]: ...

class Vector1D(fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean1D]):
    """
    public class Vector1D extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Euclidean1D`>
    
        This class represents a 1D vector.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            3.0
    
        Also see:
            :meth:`~serialized`
    """
    ZERO: typing.ClassVar['Vector1D'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Vector1D` ZERO
    
        Origin (coordinates: 0).
    
    """
    ONE: typing.ClassVar['Vector1D'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Vector1D` ONE
    
        Unit (coordinates: 1).
    
    """
    NaN: typing.ClassVar['Vector1D'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Vector1D` NaN
    
        A vector with all coordinates set to NaN.
    
    """
    POSITIVE_INFINITY: typing.ClassVar['Vector1D'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Vector1D` POSITIVE_INFINITY
    
        A vector with all coordinates set to positive infinity.
    
    """
    NEGATIVE_INFINITY: typing.ClassVar['Vector1D'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Vector1D` NEGATIVE_INFINITY
    
        A vector with all coordinates set to negative infinity.
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, vector1D: 'Vector1D'): ...
    @typing.overload
    def __init__(self, double: float, vector1D: 'Vector1D', double2: float, vector1D2: 'Vector1D'): ...
    @typing.overload
    def __init__(self, double: float, vector1D: 'Vector1D', double2: float, vector1D2: 'Vector1D', double3: float, vector1D3: 'Vector1D'): ...
    @typing.overload
    def __init__(self, double: float, vector1D: 'Vector1D', double2: float, vector1D2: 'Vector1D', double3: float, vector1D3: 'Vector1D', double4: float, vector1D4: 'Vector1D'): ...
    @typing.overload
    def add(self, double: float, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean1D]) -> 'Vector1D': ...
    @typing.overload
    def add(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean1D]) -> 'Vector1D': ...
    @typing.overload
    def distance(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean1D]) -> float:
        """
            Compute the distance between two vectors according to the L :sub:`2` norm.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNorm()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Vector1D`): first vector
                p2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Vector1D`): second vector
        
            Returns:
                the distance between p1 and p2 according to the L :sub:`2` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance(vector1D: 'Vector1D', vector1D2: 'Vector1D') -> float: ...
    def distance1(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean1D]) -> float: ...
    @typing.overload
    def distanceInf(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean1D]) -> float:
        """
            Compute the distance between two vectors according to the L :sub:`∞` norm.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNormInf()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Vector1D`): first vector
                p2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Vector1D`): second vector
        
            Returns:
                the distance between p1 and p2 according to the L :sub:`∞` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceInf(vector1D: 'Vector1D', vector1D2: 'Vector1D') -> float: ...
    @typing.overload
    def distanceSq(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean1D]) -> float:
        """
            Compute the square of the distance between two vectors.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNormSq()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Vector1D`): first vector
                p2 (:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Vector1D`): second vector
        
            Returns:
                the square of the distance between p1 and p2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceSq(vector1D: 'Vector1D', vector1D2: 'Vector1D') -> float: ...
    def dotProduct(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean1D]) -> float: ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two 1D vectors.
        
            If all coordinates of two 1D vectors are exactly the same, and none are :code:`Double.NaN`, the two 1D vectors are
            considered to be equal.
        
            :code:`NaN` coordinates are considered to affect globally the vector and be equals to each other - i.e, if either (or
            all) coordinates of the 1D vector are equal to :code:`Double.NaN`, the 1D vector is equal to
            :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Vector1D.NaN`.
        
            Overrides:
                 in class 
        
            Parameters:
                other (`Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`): Object to test for equality to this
        
            Returns:
                true if two 1D vector objects are equal, false if object is null, not an instance of Vector1D, or not equal to this
                Vector1D instance
        
        
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
    def getX(self) -> float:
        """
            Get the abscissa of the vector.
        
            Returns:
                abscissa of the vector
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Vector1D.Vector1D`
        
        
        """
        ...
    def getZero(self) -> 'Vector1D':
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
            Get a hashCode for the 1D vector.
        
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
    def negate(self) -> 'Vector1D':
        """
            Get the opposite of the instance.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Vector.negate` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`
        
            Returns:
                a new vector which is opposite to the instance
        
        
        """
        ...
    def normalize(self) -> 'Vector1D':
        """
            Get a normalized vector aligned with the instance.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.Vector.normalize` in
                interface :class:`~fr.cnes.sirius.patrius.math.geometry.Vector`
        
            Returns:
                a new normalized vector
        
        
        """
        ...
    def scalarMultiply(self, double: float) -> 'Vector1D':
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
    def subtract(self, double: float, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean1D]) -> 'Vector1D': ...
    @typing.overload
    def subtract(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean1D]) -> 'Vector1D': ...
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

class Vector1DFormat(fr.cnes.sirius.patrius.math.geometry.VectorFormat[Euclidean1D]):
    """
    public class Vector1DFormat extends :class:`~fr.cnes.sirius.patrius.math.geometry.VectorFormat`<:class:`~fr.cnes.sirius.patrius.math.geometry.euclidean.oned.Euclidean1D`>
    
        Formats a 1D vector in components list format "{x}".
    
        The prefix and suffix "{" and "}" can be replaced by any user-defined strings. The number format for components can be
        configured.
    
        White space is ignored at parse time, even if it is in the prefix, suffix or separator specifications. So even if the
        default separator does include a space character that is used at format time, both input string "{1}" and " { 1 } " will
        be parsed without error and the same vector will be returned. In the second case, however, the parse position after
        parsing will be just after the closing curly brace, i.e. just before the trailing space.
    
        Since:
            3.0
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def format(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[fr.cnes.sirius.patrius.math.geometry.Space]) -> str: ...
    @typing.overload
    def format(self, vector: fr.cnes.sirius.patrius.math.geometry.Vector[Euclidean1D], stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    @staticmethod
    def getInstance() -> 'Vector1DFormat':
        """
            Returns the default 1D vector format for the current locale.
        
            Returns:
                the default 1D vector format.
        
        """
        ...
    @typing.overload
    @staticmethod
    def getInstance(locale: java.util.Locale) -> 'Vector1DFormat':
        """
            Returns the default 1D vector format for the given locale.
        
            Parameters:
                locale (`Locale <http://docs.oracle.com/javase/8/docs/api/java/util/Locale.html?is-external=true>`): the specific locale used by the format.
        
            Returns:
                the 1D vector format specific to the given locale.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str) -> Vector1D:
        """
            Parses a string to produce a :class:`~fr.cnes.sirius.patrius.math.geometry.Vector` object.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.VectorFormat.parse` in
                class :class:`~fr.cnes.sirius.patrius.math.geometry.VectorFormat`
        
            Parameters:
                source (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): the string to parse
        
            Returns:
                the parsed :class:`~fr.cnes.sirius.patrius.math.geometry.Vector` object.
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> Vector1D:
        """
            Parses a string to produce a :class:`~fr.cnes.sirius.patrius.math.geometry.Vector` object.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.geometry.VectorFormat.parse` in
                class :class:`~fr.cnes.sirius.patrius.math.geometry.VectorFormat`
        
            Parameters:
                source (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): the string to parse
                pos (`ParsePosition <http://docs.oracle.com/javase/8/docs/api/java/text/ParsePosition.html?is-external=true>`): input/output parsing parameter.
        
            Returns:
                the parsed :class:`~fr.cnes.sirius.patrius.math.geometry.Vector` object.
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("fr.cnes.sirius.patrius.math.geometry.euclidean.oned")``.

    Euclidean1D: typing.Type[Euclidean1D]
    Interval: typing.Type[Interval]
    IntervalsSet: typing.Type[IntervalsSet]
    OrientedPoint: typing.Type[OrientedPoint]
    SubOrientedPoint: typing.Type[SubOrientedPoint]
    Vector1D: typing.Type[Vector1D]
    Vector1DFormat: typing.Type[Vector1DFormat]
