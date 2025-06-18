
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import fr.cnes.sirius.patrius.math
import fr.cnes.sirius.patrius.math.analysis
import fr.cnes.sirius.patrius.math.exception
import fr.cnes.sirius.patrius.math.fraction
import fr.cnes.sirius.patrius.math.util
import java.io
import java.lang
import java.text
import java.util
import java.util.function
import jpype
import typing



class AnyMatrix:
    """
    public interface AnyMatrix
    
        Interface defining very basic matrix operations.
    
        Since:
            2.0
    """
    def getColumnDimension(self) -> int:
        """
            Returns the number of columns in the matrix.
        
            Returns:
                columnDimension
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
            Returns the number of rows in the matrix.
        
            Returns:
                rowDimension
        
        
        """
        ...
    def isSquare(self) -> bool:
        """
            Is this a square matrix?
        
            Returns:
                true if the matrix is square (rowDimension = columnDimension)
        
        
        """
        ...

class Decomposition:
    """
    public interface Decomposition
    
        Define the decomposition of a real matrix.
    """
    def getSolver(self) -> 'DecompositionSolver':
        """
            Gets a solver for finding the A × X = B solution in exact linear sense.
        
            Returns:
                the decomposition solver.
        
        
        """
        ...

class DecompositionSolver:
    """
    public interface DecompositionSolver
    
        Interface handling decomposition algorithms that can solve A × X = B.
    
        Decomposition algorithms decompose an A matrix has a product of several specific matrices from which they can solve A ×
        X = B in least squares sense: they find X such that ||A × X - B|| is minimal.
    
        Some solvers like :class:`~fr.cnes.sirius.patrius.math.linear.LUDecomposition` can only find the solution for square
        matrices and when the solution is an exact linear solution, i.e. when ||A × X - B|| is exactly 0. Other solvers can
        also find solutions with non-square matrix A and with non-null minimal norm. If an exact linear solution exists it is
        also the minimal norm solution.
    
        Since:
            2.0
    """
    def getInverse(self) -> 'RealMatrix':
        """
            Get the inverse (or pseudo-inverse) of the decomposed matrix.
        
            Returns:
                inverse matrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.SingularMatrixException`: if the decomposed matrix is singular.
        
        
        """
        ...
    def isNonSingular(self) -> bool:
        """
            Check if the decomposed matrix is non-singular.
        
            Returns:
                true if the decomposed matrix is non-singular.
        
        
        """
        ...
    @typing.overload
    def solve(self, realMatrix: 'RealMatrix') -> 'RealMatrix':
        """
            Solve the linear equation A × X = B for matrices A.
        
            The A matrix is implicit, it is provided by the underlying decomposition algorithm.
        
            Parameters:
                b (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): right-hand side of the equation A × X = B
        
            Returns:
                a vector X that minimizes the two norm of A × X - B
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the matrices dimensions do not match.
                :class:`~fr.cnes.sirius.patrius.math.linear.SingularMatrixException`: if the decomposed matrix is singular.
        
            Solve the linear equation A × X = B for matrices A.
        
            The A matrix is implicit, it is provided by the underlying decomposition algorithm.
        
            Parameters:
                b (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): right-hand side of the equation A × X = B
        
            Returns:
                a matrix X that minimizes the two norm of A × X - B
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the matrices dimensions do not match.
                :class:`~fr.cnes.sirius.patrius.math.linear.SingularMatrixException`: if the decomposed matrix is singular.
        
        
        """
        ...
    @typing.overload
    def solve(self, realVector: 'RealVector') -> 'RealVector': ...

_FieldDecompositionSolver__T = typing.TypeVar('_FieldDecompositionSolver__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
class FieldDecompositionSolver(typing.Generic[_FieldDecompositionSolver__T]):
    """
    public interface FieldDecompositionSolver<T extends :class:`~fr.cnes.sirius.patrius.math.FieldElement`<T>>
    
        Interface handling decomposition algorithms that can solve A × X = B.
    
        Decomposition algorithms decompose an A matrix has a product of several specific matrices from which they can solve A ×
        X = B in least squares sense: they find X such that ||A × X - B|| is minimal.
    
        Some solvers like :class:`~fr.cnes.sirius.patrius.math.linear.FieldLUDecomposition` can only find the solution for
        square matrices and when the solution is an exact linear solution, i.e. when ||A × X - B|| is exactly 0. Other solvers
        can also find solutions with non-square matrix A and with non-null minimal norm. If an exact linear solution exists it
        is also the minimal norm solution.
    
        Since:
            2.0
    """
    def getInverse(self) -> 'FieldMatrix'[_FieldDecompositionSolver__T]: ...
    def isNonSingular(self) -> bool:
        """
            Check if the decomposed matrix is non-singular.
        
            Returns:
                true if the decomposed matrix is non-singular
        
        
        """
        ...
    @typing.overload
    def solve(self, fieldMatrix: 'FieldMatrix'[_FieldDecompositionSolver__T]) -> 'FieldMatrix'[_FieldDecompositionSolver__T]: ...
    @typing.overload
    def solve(self, fieldVector: 'FieldVector'[_FieldDecompositionSolver__T]) -> 'FieldVector'[_FieldDecompositionSolver__T]: ...

_FieldLUDecomposition__T = typing.TypeVar('_FieldLUDecomposition__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
class FieldLUDecomposition(typing.Generic[_FieldLUDecomposition__T]):
    """
    public class FieldLUDecomposition<T extends :class:`~fr.cnes.sirius.patrius.math.FieldElement`<T>> extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`
    
        Calculates the LUP-decomposition of a square matrix.
    
        The LUP-decomposition of a matrix A consists of three matrices L, U and P that satisfy: PA = LU, L is lower triangular,
        and U is upper triangular and P is a permutation matrix. All matrices are m×m.
    
        Since :class:`~fr.cnes.sirius.patrius.math.FieldElement` do not provide an ordering operator, the permutation matrix is
        computed here only in order to avoid a zero pivot element, no attempt is done to get the largest pivot element.
    
        This class is based on the class with similar name from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library.
    
          - a :meth:`~fr.cnes.sirius.patrius.math.linear.FieldLUDecomposition.getP` method has been added,
          - the :code:`det` method has been renamed as
            :meth:`~fr.cnes.sirius.patrius.math.linear.FieldLUDecomposition.getDeterminant`,
          - the :code:`getDoublePivot` method has been removed (but the int based
            :meth:`~fr.cnes.sirius.patrius.math.linear.FieldLUDecomposition.getPivot` method has been kept),
          - the :code:`solve` and :code:`isNonSingular` methods have been replaced by a
            :meth:`~fr.cnes.sirius.patrius.math.linear.FieldLUDecomposition.getSolver` method and the equivalent methods provided by
            the returned :class:`~fr.cnes.sirius.patrius.math.linear.DecompositionSolver`.
    
    
        Since:
            2.0 (changed to concrete class in 3.0)
    
        Also see:
            `MathWorld <http://mathworld.wolfram.com/LUDecomposition.html>`, `Wikipedia
            <http://en.wikipedia.org/wiki/LU_decomposition>`
    """
    def __init__(self, fieldMatrix: 'FieldMatrix'[_FieldLUDecomposition__T]): ...
    def getDeterminant(self) -> _FieldLUDecomposition__T:
        """
            Return the determinant of the matrix.
        
            Returns:
                determinant of the matrix
        
        
        """
        ...
    def getL(self) -> 'FieldMatrix'[_FieldLUDecomposition__T]: ...
    def getP(self) -> 'FieldMatrix'[_FieldLUDecomposition__T]: ...
    def getPivot(self) -> typing.MutableSequence[int]:
        """
            Returns the pivot permutation vector.
        
            Returns:
                the pivot permutation vector
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.FieldLUDecomposition.getP`
        
        
        """
        ...
    def getSolver(self) -> FieldDecompositionSolver[_FieldLUDecomposition__T]: ...
    def getU(self) -> 'FieldMatrix'[_FieldLUDecomposition__T]: ...

_FieldMatrixChangingVisitor__T = typing.TypeVar('_FieldMatrixChangingVisitor__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
class FieldMatrixChangingVisitor(typing.Generic[_FieldMatrixChangingVisitor__T]):
    """
    public interface FieldMatrixChangingVisitor<T extends :class:`~fr.cnes.sirius.patrius.math.FieldElement`<?>>
    
        Interface defining a visitor for matrix entries.
    
        Since:
            2.0
    """
    def end(self) -> _FieldMatrixChangingVisitor__T:
        """
            End visiting a matrix.
        
            This method is called once after all entries of the matrix have been visited.
        
            Returns:
                the value that the :code:`walkInXxxOrder` must return
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int) -> None:
        """
            Start visiting a matrix.
        
            This method is called once before any entry of the matrix is visited.
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, int: int, int2: int, t: _FieldMatrixChangingVisitor__T) -> _FieldMatrixChangingVisitor__T:
        """
            Visit one matrix entry.
        
            Parameters:
                row (int): row index of the entry
                column (int): column index of the entry
                value (:class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixChangingVisitor`): current value of the entry
        
            Returns:
                the new value to be set for the entry
        
        
        """
        ...

_FieldMatrixPreservingVisitor__T = typing.TypeVar('_FieldMatrixPreservingVisitor__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
class FieldMatrixPreservingVisitor(typing.Generic[_FieldMatrixPreservingVisitor__T]):
    """
    public interface FieldMatrixPreservingVisitor<T extends :class:`~fr.cnes.sirius.patrius.math.FieldElement`<?>>
    
        Interface defining a visitor for matrix entries.
    
        Since:
            2.0
    """
    def end(self) -> _FieldMatrixPreservingVisitor__T:
        """
            End visiting a matrix.
        
            This method is called once after all entries of the matrix have been visited.
        
            Returns:
                the value that the :code:`walkInXxxOrder` must return
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int) -> None:
        """
            Start visiting a matrix.
        
            This method is called once before any entry of the matrix is visited.
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, int: int, int2: int, t: _FieldMatrixPreservingVisitor__T) -> None:
        """
            Visit one matrix entry.
        
            Parameters:
                row (int): row index of the entry
                column (int): column index of the entry
                value (:class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixPreservingVisitor`): current value of the entry
        
        
        """
        ...

_FieldVector__T = typing.TypeVar('_FieldVector__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
class FieldVector(typing.Generic[_FieldVector__T]):
    """
    public interface FieldVector<T extends :class:`~fr.cnes.sirius.patrius.math.FieldElement`<T>>
    
        Interface defining a field-valued vector with basic algebraic operations.
    
        vector element indexing is 0-based -- e.g., :code:`getEntry(0)` returns the first element of the vector.
    
        The various :code:`mapXxx` and :code:`mapXxxToSelf` methods operate on vectors element-wise, i.e. they perform the same
        operation (adding a scalar, applying a function ...) on each element in turn. The :code:`mapXxx` versions create a new
        vector to hold the result and do not change the instance. The :code:`mapXxxToSelf` versions use the instance itself to
        store the results, so the instance is changed by these methods. In both cases, the result vector is returned by the
        methods, this allows to use the *fluent API* style, like this:
    
        .. code-block: java
        
        
         RealVector result = v.mapAddToSelf(3.0).mapTanToSelf().mapSquareToSelf();
         
    
        Since:
            2.0
    """
    def add(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]: ...
    @typing.overload
    def append(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    @typing.overload
    def append(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]: ...
    def copy(self) -> 'FieldVector'[_FieldVector__T]: ...
    def dotProduct(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> _FieldVector__T: ...
    def ebeDivide(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]: ...
    def ebeMultiply(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]: ...
    def getDimension(self) -> int:
        """
            Returns the size of the vector.
        
            Returns:
                size
        
        
        """
        ...
    def getEntry(self, int: int) -> _FieldVector__T:
        """
            Returns the entry in the specified index.
        
            Parameters:
                index (int): Index location of entry to be fetched.
        
            Returns:
                the vector entry at :code:`index`.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the index is not valid.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.FieldVector.setEntry`
        
        
        """
        ...
    def getField(self) -> fr.cnes.sirius.patrius.math.Field[_FieldVector__T]: ...
    def getSubVector(self, int: int, int2: int) -> 'FieldVector'[_FieldVector__T]: ...
    def mapAdd(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    def mapAddToSelf(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    def mapDivide(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    def mapDivideToSelf(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    def mapInv(self) -> 'FieldVector'[_FieldVector__T]: ...
    def mapInvToSelf(self) -> 'FieldVector'[_FieldVector__T]: ...
    def mapMultiply(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    def mapMultiplyToSelf(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    def mapSubtract(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    def mapSubtractToSelf(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    def outerProduct(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> 'FieldMatrix'[_FieldVector__T]: ...
    def projection(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]: ...
    def set(self, t: _FieldVector__T) -> None:
        """
            Set all elements to a single value.
        
            Parameters:
                value (:class:`~fr.cnes.sirius.patrius.math.linear.FieldVector`): single value to set for all elements
        
        
        """
        ...
    def setEntry(self, int: int, t: _FieldVector__T) -> None:
        """
            Set a single element.
        
            Parameters:
                index (int): element index.
                value (:class:`~fr.cnes.sirius.patrius.math.linear.FieldVector`): new value for the element.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the index is not valid.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.FieldVector.getEntry`
        
        
        """
        ...
    def setSubVector(self, int: int, fieldVector: 'FieldVector'[_FieldVector__T]) -> None: ...
    def subtract(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]: ...
    def toArray(self) -> typing.MutableSequence[_FieldVector__T]:
        """
            Convert the vector to a T array.
        
            The array is independent from vector data, it's elements are copied.
        
            Returns:
                array containing a copy of vector elements
        
        
        """
        ...

class IllConditionedOperatorException(fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException):
    """
    public class IllConditionedOperatorException extends :class:`~fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException`
    
        An exception to be thrown when the condition number of a :class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`
        is too high.
    
        Since:
            3.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, double: float): ...

class IterativeLinearSolver:
    """
    public abstract class IterativeLinearSolver extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`
    
        This abstract class defines an iterative solver for the linear system A · x = b. In what follows, the *residual* r is
        defined as r = b - A · x, where A is the linear operator of the linear system, b is the right-hand side vector, and x
        the current estimate of the solution.
    
        Since:
            3.0
    """
    @typing.overload
    def __init__(self, iterationManager: fr.cnes.sirius.patrius.math.util.IterationManager): ...
    @typing.overload
    def __init__(self, int: int): ...
    def getIterationManager(self) -> fr.cnes.sirius.patrius.math.util.IterationManager:
        """
            Returns the iteration manager attached to this solver.
        
            Returns:
                the manager
        
        
        """
        ...
    @typing.overload
    def solve(self, realLinearOperator: 'RealLinearOperator', realVector: 'RealVector') -> 'RealVector':
        """
            Returns an estimate of the solution to the linear system A · x = b.
        
            Parameters:
                a (:class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`): the linear operator A of the system
                b (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the right-hand side vector
        
            Returns:
                a new vector containing the solution
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if one of the parameters is :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.linear.NonSquareOperatorException`: if :code:`a` is not square
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`b` has dimensions inconsistent with :code:`a`
                :class:`~fr.cnes.sirius.patrius.math.exception.MaxCountExceededException`: at exhaustion of the iteration count, unless a custom
                    :class:`~fr.cnes.sirius.patrius.math.util.Incrementor.MaxCountExceededCallback` has been set at construction of the
                    :class:`~fr.cnes.sirius.patrius.math.util.IterationManager`
        
            Returns an estimate of the solution to the linear system A · x = b.
        
            Parameters:
                a (:class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`): the linear operator A of the system
                b (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the right-hand side vector
                x0 (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the initial guess of the solution
        
            Returns:
                a new vector containing the solution
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if one of the parameters is :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.linear.NonSquareOperatorException`: if :code:`a` is not square
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`b` or :code:`x0` have dimensions inconsistent with :code:`a`
                :class:`~fr.cnes.sirius.patrius.math.exception.MaxCountExceededException`: at exhaustion of the iteration count, unless a custom
                    :class:`~fr.cnes.sirius.patrius.math.util.Incrementor.MaxCountExceededCallback` has been set at construction of the
                    :class:`~fr.cnes.sirius.patrius.math.util.IterationManager`
        
        
        """
        ...
    @typing.overload
    def solve(self, realLinearOperator: 'RealLinearOperator', realVector: 'RealVector', realVector2: 'RealVector') -> 'RealVector': ...
    def solveInPlace(self, realLinearOperator: 'RealLinearOperator', realVector: 'RealVector', realVector2: 'RealVector') -> 'RealVector':
        """
            Returns an estimate of the solution to the linear system A · x = b. The solution is computed in-place (initial guess is
            modified).
        
            Parameters:
                a (:class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`): the linear operator A of the system
                b (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the right-hand side vector
                x0 (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): initial guess of the solution
        
            Returns:
                a reference to :code:`x0` (shallow copy) updated with the solution
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if one of the parameters is :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.linear.NonSquareOperatorException`: if :code:`a` is not square
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`b` or :code:`x0` have dimensions inconsistent with :code:`a`
                :class:`~fr.cnes.sirius.patrius.math.exception.MaxCountExceededException`: at exhaustion of the iteration count, unless a custom
                    :class:`~fr.cnes.sirius.patrius.math.util.Incrementor.MaxCountExceededCallback` has been set at construction of the
                    :class:`~fr.cnes.sirius.patrius.math.util.IterationManager`
        
        
        """
        ...

class IterativeLinearSolverEvent(fr.cnes.sirius.patrius.math.util.IterationEvent):
    """
    public abstract class IterativeLinearSolverEvent extends :class:`~fr.cnes.sirius.patrius.math.util.IterationEvent`
    
        This is the base class for all events occuring during the iterations of a
        :class:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolver`.
    
        Since:
            3.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, object: typing.Any, int: int): ...
    def getNormOfResidual(self) -> float:
        """
            Returns the norm of the residual. The returned value is not required to be *exact*. Instead, the norm of the so-called
            *updated* residual (if available) should be returned. For example, the
            :class:`~fr.cnes.sirius.patrius.math.linear.ConjugateGradient` method computes a sequence of residuals, the norm of
            which is cheap to compute. However, due to accumulation of round-off errors, this residual might differ from the true
            residual after some iterations. See e.g. A. Greenbaum and Z. Strakos, *Predicting the Behavior of Finite Precision
            Lanzos and Conjugate Gradient Computations*, Technical Report 538, Department of Computer Science, New York University,
            1991 (available `here <http://www.archive.org/details/predictingbehavi00gree>`).
        
            Returns:
                the norm of the residual, ||r||
        
        
        """
        ...
    def getResidual(self) -> 'RealVector':
        """
        
            Returns the residual. This is an optional operation, as all iterative linear solvers do not provide cheap estimate of
            the updated residual vector, in which case
        
              - this method should throw a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`,
              - :meth:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent.providesResidual` returns :code:`false`.
        
        
            The default implementation throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`.
            If this method is overriden, then
            :meth:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent.providesResidual` should be overriden as well.
        
            Returns:
                the updated residual, r
        
        
        """
        ...
    def getRightHandSideVector(self) -> 'RealVector':
        """
            Returns the current right-hand side of the linear system to be solved. This method should return an unmodifiable view,
            or a deep copy of the actual right-hand side vector, in order not to compromise subsequent iterations of the source
            :class:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolver`.
        
            Returns:
                the right-hand side vector, b
        
        
        """
        ...
    def getSolution(self) -> 'RealVector':
        """
            Returns the current estimate of the solution to the linear system to be solved. This method should return an
            unmodifiable view, or a deep copy of the actual current solution, in order not to compromise subsequent iterations of
            the source :class:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolver`.
        
            Returns:
                the solution, x
        
        
        """
        ...
    def providesResidual(self) -> bool:
        """
            Returns :code:`true` if :meth:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent.getResidual` is supported.
            The default implementation returns :code:`false`.
        
            Returns:
                :code:`false` if :meth:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent.getResidual` throws a
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
        
        
        """
        ...

class MatrixDimensionMismatchException(fr.cnes.sirius.patrius.math.exception.MultiDimensionMismatchException):
    """
    public class MatrixDimensionMismatchException extends :class:`~fr.cnes.sirius.patrius.math.exception.MultiDimensionMismatchException`
    
        Exception to be thrown when either the number of rows or the number of columns of a matrix do not match the expected
        values.
    
        Since:
            3.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, int: int, int2: int, int3: int, int4: int): ...
    def getExpectedColumnDimension(self) -> int:
        """
        
            Returns:
                the expected column dimension.
        
        
        """
        ...
    def getExpectedRowDimension(self) -> int:
        """
        
            Returns:
                the expected row dimension.
        
        
        """
        ...
    def getWrongColumnDimension(self) -> int:
        """
        
            Returns:
                the wrong column dimension.
        
        
        """
        ...
    def getWrongRowDimension(self) -> int:
        """
        
            Returns:
                the expected row dimension.
        
        
        """
        ...

class MatrixUtils:
    """
    public final class MatrixUtils extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`
    
        A collection of static methods that operate on or return matrices.
    
        This class is up-to-date with commons-math 3.6.1.
    """
    NUMBER_FORMAT: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` NUMBER_FORMAT
    
        Format number.
    
        Also see:
            :meth:`~constant`
    
    
    """
    OPENING_CURLY_BRACKET: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` OPENING_CURLY_BRACKET
    
        Opening curly bracket character ('{').
    
        Also see:
            :meth:`~constant`
    
    
    """
    CLOSING_CURLY_BRACKET: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` CLOSING_CURLY_BRACKET
    
        Closing curly bracket character ('}').
    
        Also see:
            :meth:`~constant`
    
    
    """
    OPENING_BRACKET: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` OPENING_BRACKET
    
        Opening bracket character ('[').
    
        Also see:
            :meth:`~constant`
    
    
    """
    CLOSING_BRACKET: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` CLOSING_BRACKET
    
        Closing bracket character (']').
    
        Also see:
            :meth:`~constant`
    
    
    """
    SPACE: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` SPACE
    
        Space character (' ').
    
        Also see:
            :meth:`~constant`
    
    
    """
    COMMA: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` COMMA
    
        Comma character (',').
    
        Also see:
            :meth:`~constant`
    
    
    """
    SEMICOLON: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` SEMICOLON
    
        Semicolon character (';') .
    
        Also see:
            :meth:`~constant`
    
    
    """
    CARRIER_RETURN: typing.ClassVar[str] = ...
    """
    public static final `String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>` CARRIER_RETURN
    
        Carrier return ('\n').
    
        Also see:
            :meth:`~constant`
    
    
    """
    MAX_DIGITS: typing.ClassVar[int] = ...
    """
    public static final int MAX_DIGITS
    
        Maximum number of fraction digits for no numerical approximation.
    
    
        Set to integer maximum value so that the formatter uses the upper value adapted to the numeric type being formatted (see
        `null
        <http://docs.oracle.com/javase/8/docs/api/java/text/NumberFormat.html?is-external=true#setMaximumFractionDigits-int->`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_FORMAT: typing.ClassVar['RealMatrixFormat'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixFormat` DEFAULT_FORMAT
    
        The default :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixFormat`.
    
        Since:
            3.1
    
    
    """
    JAVA_FORMAT: typing.ClassVar['RealMatrixFormat'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixFormat` JAVA_FORMAT
    
        The JAVA format for :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` objects.
    
        This format guarantee no numerical approximation.
    
        Since:
            4.5
    
    
    """
    OCTAVE_FORMAT: typing.ClassVar['RealMatrixFormat'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixFormat` OCTAVE_FORMAT
    
        A format for :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` objects compatible with octave.
    
        This format guarantee no numerical approximation.
    
        Since:
            3.1
    
    
    """
    NUMPY_FORMAT: typing.ClassVar['RealMatrixFormat'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixFormat` NUMPY_FORMAT
    
        The NUMPY format for :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` objects.
    
        This format guarantee no numerical approximation.
    
        Since:
            4.13
    
    
    """
    SCILAB_FORMAT: typing.ClassVar['RealMatrixFormat'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixFormat` SCILAB_FORMAT
    
        The SCILAB format for :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` objects.
    
        This format guarantee no numerical approximation.
    
        Since:
            4.5
    
    
    """
    VISUAL_FORMAT: typing.ClassVar['RealMatrixFormat'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixFormat` VISUAL_FORMAT
    
        Visual format for :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` objects displayed on several rows.
    
        The pattern ""% 11.5g"" by default set the significant digit accuracy at 5, the width equal to 11, the format is
        automatically set to digital or scientific and the space between % and 11 allows to display the sign for scientific
        values.
    
        Since:
            4.5
    
    
    """
    SUMMARY_FORMAT: typing.ClassVar['RealMatrixFormat'] = ...
    """
    public static final :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixFormat` SUMMARY_FORMAT
    
        Summary visual format for :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` objects displayed on several rows.
    
        The pattern ""% 11.5g"" by default set the significant digit accuracy at 5, the width equal to 11, the format is
        automatically set to digital or scientific and the space between % and 11 allows to display the sign for scientific
        values. The summary mode, with an index set to 3, will display the 3x3 sub-matrix in each corner and the rows and
        columns total number.
    
        Since:
            4.5
    
    
    """
    @staticmethod
    def bigFractionMatrixToRealMatrix(fieldMatrix: 'FieldMatrix'[fr.cnes.sirius.patrius.math.fraction.BigFraction]) -> 'Array2DRowRealMatrix': ...
    @staticmethod
    def blockInverse(realMatrix: 'RealMatrix', int: int) -> 'RealMatrix':
        """
            Computes the inverse of the given matrix by splitting it into 4 sub-matrices.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): Matrix whose inverse must be computed.
                splitIndex (int): Index that determines the "split" line and column. The element corresponding to this index will part of the upper-left
                    sub-matrix.
        
            Returns:
                the inverse of :code:`m`.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.NonSquareMatrixException`: if :code:`m` is not square.
        
        
        """
        ...
    @staticmethod
    def buildSummaryMatrixFormat(int: int) -> 'RealMatrixFormat':
        """
            Build a summary matrix format with different specific size for sub-corners blocs square dimensions of the summary view.
        
            The pattern ""% 11.5g"" by default set the significant digit accuracy at 5, the width equal to 11, the format is
            automatically set to digital or scientific and the space between % and 11 allows to display the sign for scientific
            values.
        
            Parameters:
                summarySize (int): Sub-corners blocs square dimensions for summary view
        
            Returns:
                the real matrix format
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils.SUMMARY_FORMAT`
        
        
        """
        ...
    @staticmethod
    def checkAdditionCompatible(anyMatrix: AnyMatrix, anyMatrix2: AnyMatrix) -> None:
        """
            Check if matrices are addition compatible.
        
            Parameters:
                left (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): Left hand side matrix.
                right (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): Right hand side matrix.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the matrices are not addition compatible.
        
        
        """
        ...
    @staticmethod
    def checkArrayIndex(doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int: int, int2: int) -> None:
        """
            Checks if the provided indices are valid row and column indices for a given 2D-array.
        
            Parameters:
                array (double[][]): the array
                row (int): the row index to be checked
                column (int): the column index to be checked
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the provided indices are not valid row or column indices
        
        
        """
        ...
    @staticmethod
    def checkColumnDimension(int: int) -> None:
        """
            Checks the validity of the provided column dimension (must be strictly positive).
        
            Parameters:
                columnDimension (int): the column dimension to be checked
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NotStrictlyPositiveException`: if the column dimension is not strictly positive
        
        
        """
        ...
    @staticmethod
    def checkColumnIndex(anyMatrix: AnyMatrix, int: int) -> None:
        """
            Checks if an index is a valid column index for a given matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): the matrix
                column (int): the column index to be checked
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the provided index is not a valid column index
        
        
        """
        ...
    @staticmethod
    def checkColumnIndices(anyMatrix: AnyMatrix, intArray: typing.Union[typing.List[int], jpype.JArray]) -> None:
        """
            Checks if the provided indices are valid column indices for a given matrix.
        
            This method throws an exception if the provided array is not a valid row index array. An index array is considered to be
            valid if it is not :code:`null` or empty, and if each of its indices are between 0 to n-1, with n the column dimension
            of the matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): the matrix
                indices (int[]): the array of column indices
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if the provided index array is :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if the provided index array is empty (zero length)
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if one of the provided indices is not a valid column index
        
        
        """
        ...
    @staticmethod
    def checkDimension(int: int, int2: int) -> None:
        """
            Check if the provided dimension is the one expected.
        
            Parameters:
                expected (int): the expected dimension
                actual (int): the actual dimension
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the provided dimension is not the one expected
        
        
        """
        ...
    @staticmethod
    def checkDuplicates(intArray: typing.Union[typing.List[int], jpype.JArray]) -> None:
        """
            Checks if the provided array contains duplicates.
        
            Parameters:
                array (int[]): the array to be checked
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException`: if the provided array contains any duplicates
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkMatrixArray(doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None:
        """
            Checks the validity of a matrix data array.
        
            To be valid, the provided data array must not be :code:`null` or empty, its first row must also not be :code:`null` or
            empty, and the rows must all have the same length.
        
            Parameters:
                data (double[][]): the matrix data array to be checked
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if the data array is :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if the data array is empty
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the rows of the data array do not have a constant number of columns
        
            Checks the validity of a matrix data array.
        
            To be valid, the provided data array must not be :code:`null` or empty, its first row must also not be :code:`null` or
            empty, and the rows must all have the same length.
        
            Parameters:
                data (`Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`[][]): the matrix data array to be checked
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if the data array is :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if the data array is empty
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the rows of the data array do not have a constant number of columns
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkMatrixArray(doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], boolean: bool) -> None:
        """
            Checks the validity of a matrix data array.
        
            To be valid, the provided data array must not be :code:`null` or empty, and its first row must also not be :code:`null`
            or empty. Setting :code:`checkColumnDimensions` to :code:`true` , enables an additional check which verifies that the
            rows all have the same length.
        
            Parameters:
                data (double[][]): the matrix data array to be checked
                checkColumnDimensions (boolean): whether or not to check if the rows all have the same dimension
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if the data array is :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if the data array is empty
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the rows of the data array do not have a constant number of columns (optional check)
        
            Checks the validity of a matrix data array.
        
            To be valid, the provided data array must not be :code:`null` or empty, and its first row must also not be :code:`null`
            or empty. Setting :code:`checkColumnDimensions` to :code:`true` , enables an additional check which verifies that the
            rows all have the same length.
        
            Parameters:
                data (`Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`[][]): the matrix data array to be checked
                checkColumnDimensions (boolean): whether or not to check if the rows all have the same dimension
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if the data array is :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if the data array is empty
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the rows of the data array do not have a constant number of columns (optional check)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkMatrixArray(objectArray: typing.Union[typing.List[typing.MutableSequence[typing.Any]], jpype.JArray]) -> None: ...
    @typing.overload
    @staticmethod
    def checkMatrixArray(objectArray: typing.Union[typing.List[typing.MutableSequence[typing.Any]], jpype.JArray], boolean: bool) -> None: ...
    @staticmethod
    def checkMatrixIndex(anyMatrix: AnyMatrix, int: int, int2: int) -> None:
        """
            Checks if the provided indices are valid row and column indices are for a given matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): the matrix
                row (int): the row index to be checked
                column (int): the column index to be checked
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the provided indices are not valid row or column indices
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkMultiplicationCompatible(anyMatrix: AnyMatrix, anyMatrix2: AnyMatrix) -> None:
        """
            Check if matrices are multiplication compatible
        
            Parameters:
                left (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): Left hand side matrix.
                right (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): Right hand side matrix.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`getColumnDimension(left) != getRowDimension(right)`
        
            Check if matrices are multiplication compatible
        
            Parameters:
                left (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): Left hand side matrix.
                right (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): Right hand side matrix.
                rightToTransposed (boolean): indicate if the right matrix will be transposed before the operation
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`getColumnDimension(left) != getRowDimension(right)`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkMultiplicationCompatible(anyMatrix: AnyMatrix, anyMatrix2: AnyMatrix, boolean: bool) -> None: ...
    @staticmethod
    def checkRowDimension(int: int) -> None:
        """
            Checks the validity of the provided row dimension (must be strictly positive).
        
            Parameters:
                rowDimension (int): the row dimension to be checked
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NotStrictlyPositiveException`: if the row dimension is not strictly positive
        
        
        """
        ...
    @staticmethod
    def checkRowIndex(anyMatrix: AnyMatrix, int: int) -> None:
        """
            Checks if an index is a valid row index for a given matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): the matrix
                row (int): the row index to be checked
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the provided index is not a valid row index
        
        
        """
        ...
    @staticmethod
    def checkRowIndices(anyMatrix: AnyMatrix, intArray: typing.Union[typing.List[int], jpype.JArray]) -> None:
        """
            Checks if the provided indices are valid row indices for a given matrix.
        
            This method throws an exception if the provided array is not a valid row index array. An index array is considered to be
            valid if it is not :code:`null` or empty, and if each of its indices are between 0 to n-1, with n the row dimension of
            the matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): the matrix
                indices (int[]): the array of row indices
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if the provided index array is :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if the provided index array is empty (zero length)
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if one of the provided indices is not a valid row index
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkSubMatrixIndex(anyMatrix: AnyMatrix, int: int, int2: int, int3: int, int4: int) -> None:
        """
            Checks if the provided sub-matrix ranges are valid for a given matrix.
        
            Rows and columns are indicated counting from 0 to :code:`n - 1`.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): the matrix
                startRow (int): the initial row index
                endRow (int): the final row index
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if one of the provided indices is not a valid row or column index
                :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooSmallException`: if :code:`endRow < startRow` or :code:`endColumn < startColumn`.
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkSubMatrixIndex(anyMatrix: AnyMatrix, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> None:
        """
            Checks if the provided sub-matrix indices are valid for a given matrix.
        
            Rows and columns are indicated counting from 0 to n-1.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): the matrix
                selectedRows (int[]): the array of row indices
                selectedColumns (int[]): the array of column indices
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if any of the provided index arrays is :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if any of the provided index arrays is empty (zero length)
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if any of the provided indices is not a valid row or column index
        
        
        """
        ...
    @staticmethod
    def checkSubtractionCompatible(anyMatrix: AnyMatrix, anyMatrix2: AnyMatrix) -> None:
        """
            Check if matrices are subtraction compatible
        
            Parameters:
                left (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): Left hand side matrix.
                right (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): Right hand side matrix.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the matrices are not subtraction compatible.
        
        
        """
        ...
    @staticmethod
    def checkSymmetric(realMatrix: 'RealMatrix', double: float) -> None:
        """
            Checks whether a matrix is symmetric.
        
            Parameters:
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): Matrix to check.
                eps (double): Relative tolerance.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.NonSquareMatrixException`: if the matrix is not square.
                :class:`~fr.cnes.sirius.patrius.math.linear.NonSymmetricMatrixException`: if the matrix is not symmetric.
        
            Since:
                3.1
        
        
        """
        ...
    @staticmethod
    def checkSymmetry(realMatrix: 'RealMatrix', double: float, double2: float) -> None:
        """
            Checks if the matrix is symmetric and throws an exception if that's not the case.
        
            Parameters:
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be checked
                absTol (double): the absolute threshold above which two off-diagonal elements are considered to be different
                relTol (double): the relative threshold above which two off-diagonal elements are considered to be different
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.NonSymmetricMatrixException`: if the provided matrix is not symmetric
        
        
        """
        ...
    @staticmethod
    def concatenateHorizontally(realMatrix: 'RealMatrix', realMatrix2: 'RealMatrix') -> 'RealMatrix':
        """
            Concatenates two matrices horizontally.
        
            Parameters:
                left (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the left matrix [NxM]
                right (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the right matrix [NxL]
        
            Returns:
                the concatenated matrix [Nx(M+L)]
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the two matrices don't have the same number of rows
        
        
        """
        ...
    @staticmethod
    def concatenateVertically(realMatrix: 'RealMatrix', realMatrix2: 'RealMatrix') -> 'RealMatrix':
        """
            Concatenates two matrices vertically.
        
            Parameters:
                upper (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the upper matrix [MxN]
                lower (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the upper matrix [LxN]
        
            Returns:
                the concatenated matrix [(M+L)xN]
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the two matrices don't have the same number of columns
        
        
        """
        ...
    @staticmethod
    def copyArray(doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Returns a deep copy of a 2D :code:`double` array.
        
            Parameters:
                array (double[][]): the array to be copied
        
            Returns:
                a deep copy of the provided array, or :code:`null` if the supplied array is :code:`null`
        
        
        """
        ...
    _createColumnFieldMatrix__T = typing.TypeVar('_createColumnFieldMatrix__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
    @staticmethod
    def createColumnFieldMatrix(tArray: typing.Union[typing.List[_createColumnFieldMatrix__T], jpype.JArray]) -> 'FieldMatrix'[_createColumnFieldMatrix__T]:
        """
            Creates a column :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrix` using the data from the input array.
        
            Parameters:
                columnData (T[]): the input column data
        
            Returns:
                a columnData x 1 FieldMatrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if :code:`data` is empty.
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if :code:`columnData` is :code:`null`.
        
        
        """
        ...
    @staticmethod
    def createColumnRealMatrix(doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> 'RealMatrix':
        """
            Creates a column :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` using the data from the input array.
        
            Parameters:
                columnData (double[]): the input column data
        
            Returns:
                a columnData x 1 RealMatrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if :code:`columnData` is empty.
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if :code:`columnData` is :code:`null`.
        
        
        """
        ...
    _createFieldDiagonalMatrix__T = typing.TypeVar('_createFieldDiagonalMatrix__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
    @staticmethod
    def createFieldDiagonalMatrix(tArray: typing.Union[typing.List[_createFieldDiagonalMatrix__T], jpype.JArray]) -> 'FieldMatrix'[_createFieldDiagonalMatrix__T]:
        """
            Returns a diagonal matrix with specified elements.
        
            Parameters:
                diagonal (T[]): diagonal elements of the matrix (the array elements will be copied)
        
            Returns:
                diagonal matrix
        
            Since:
                2.0
        
        
        """
        ...
    _createFieldIdentityMatrix__T = typing.TypeVar('_createFieldIdentityMatrix__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
    @staticmethod
    def createFieldIdentityMatrix(field: fr.cnes.sirius.patrius.math.Field[_createFieldIdentityMatrix__T], int: int) -> 'FieldMatrix'[_createFieldIdentityMatrix__T]:
        """
            Returns :code:`dimension x dimension` identity matrix.
        
            Parameters:
                field (:class:`~fr.cnes.sirius.patrius.math.Field`<T> field): field to which the elements belong
                dimension (int): dimension of identity matrix to generate
        
            Returns:
                identity matrix
        
            Raises:
                : if dimension is not positive
        
            Since:
                2.0
        
        
        """
        ...
    _createFieldMatrix_0__T = typing.TypeVar('_createFieldMatrix_0__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
    _createFieldMatrix_1__T = typing.TypeVar('_createFieldMatrix_1__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
    @typing.overload
    @staticmethod
    def createFieldMatrix(field: fr.cnes.sirius.patrius.math.Field[_createFieldMatrix_0__T], int: int, int2: int) -> 'FieldMatrix'[_createFieldMatrix_0__T]:
        """
            Returns a :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrix` with specified dimensions.
        
            The type of matrix returned depends on the dimension. Below 2 :sup:`12` elements (i.e. 4096 elements or 64×64 for a
            square matrix), a :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrix` instance is built. Above this threshold a
            :class:`~fr.cnes.sirius.patrius.math.linear.BlockFieldMatrix` instance is built.
        
            The matrix elements are all set to field.getZero().
        
            Parameters:
                field (:class:`~fr.cnes.sirius.patrius.math.Field`<T> field): the field to which the matrix elements belong
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
        
            Returns:
                a new :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrix` with specified dimensions
        
            Since:
                2.0
        
            Also see:
        
        """
        ...
    @typing.overload
    @staticmethod
    def createFieldMatrix(tArray: typing.Union[typing.List[typing.MutableSequence[_createFieldMatrix_1__T]], jpype.JArray]) -> 'FieldMatrix'[_createFieldMatrix_1__T]:
        """
            Returns a :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrix` whose entries are the the values in the the input
            array.
        
            The type of matrix returned depends on the dimension. Below 2 :sup:`12` elements (i.e. 4096 elements or 64×64 for a
            square matrix), a :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrix` instance is built. Above this threshold a
            :class:`~fr.cnes.sirius.patrius.math.linear.BlockFieldMatrix` instance is built.
        
            The input array is copied, not referenced.
        
            Parameters:
                data (T[][]): the input array
        
            Returns:
                a matrix containing the values of the array.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if either :code:`data` or :code:`data[0]` is :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if a row or column is empty.
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`data` is not rectangular (not all rows have the same length)
        
            Since:
                2.0
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils.createFieldMatrix`
        
        
        """
        ...
    _createFieldVector__T = typing.TypeVar('_createFieldVector__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
    @staticmethod
    def createFieldVector(tArray: typing.Union[typing.List[_createFieldVector__T], jpype.JArray]) -> FieldVector[_createFieldVector__T]:
        """
            Creates a :class:`~fr.cnes.sirius.patrius.math.linear.FieldVector` using the data from the input array.
        
            Parameters:
                data (T[]): the input data
        
            Returns:
                a data.length FieldVector
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if :code:`data` is empty.
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if :code:`data` is :code:`null`.
                :class:`~fr.cnes.sirius.patrius.math.exception.ZeroException`: if :code:`data` has 0 elements
        
        
        """
        ...
    @staticmethod
    def createRealDiagonalMatrix(doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> 'RealMatrix':
        """
            Returns a diagonal matrix with specified elements.
        
            Parameters:
                diagonal (double[]): diagonal elements of the matrix (the array elements will be copied)
        
            Returns:
                diagonal matrix
        
            Since:
                2.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createRealIdentityMatrix(int: int) -> 'RealMatrix':
        """
            Returns :code:`dimension x dimension` identity matrix.
        
            The type of matrix returned depends on the dimension. Below 2 :sup:`12` elements (i.e. 4096 elements or 64×64 for a
            square matrix) which can be stored in a 32kB array, a :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix`
            instance is built. Above this threshold a :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` instance is
            built.
        
            Parameters:
                dimension (int): the dimension of identity matrix to be generated
        
            Returns:
                the generated identity matrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NotStrictlyPositiveException`: if the specified dimension is not strictly positive
        
            Since:
                1.1
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils.createRealMatrix`
        
            Returns :code:`dimension x dimension` identity matrix.
        
            If :code:`diagonalMatrixInstance` is set to :code:`true`, the generated identity matrix is a
            :class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix` instance. Otherwise, the type of matrix returned depends on
            the dimension. Below 2 :sup:`12` elements (i.e. 4096 elements or 64×64 for a square matrix) which can be stored in a
            32kB array, a :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix` instance is built. Above this threshold
            a :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` instance is built.
        
            Although :class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix` instances are optimized for storing diagonal
            matrices, they do have some limitations. Setting off-diagonal elements to non-zero values is forbidden, which means any
            attempt to modify the matrix will most likely result in an exception.
        
            Parameters:
                dimension (int): the dimension of identity matrix to be generated
                diagonalMatrixInstance (boolean): if :code:`true`, the generated identity matrix is a :class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix`
                    instance, otherwise it is either an :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix` or a
                    :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` instance
        
            Returns:
                the generated identity matrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NotStrictlyPositiveException`: if the specified dimension is not strictly positive
        
            Since:
                4.5
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils.createRealMatrix`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createRealIdentityMatrix(int: int, boolean: bool) -> 'RealMatrix': ...
    @typing.overload
    @staticmethod
    def createRealMatrix(doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> 'RealMatrix':
        """
            Returns a :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` with specified dimensions.
        
            The type of matrix returned depends on the dimension. Below 2 :sup:`12` elements (i.e. 4096 elements or 64×64 for a
            square matrix) which can be stored in a 32kB array, a :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix`
            instance is built. Above this threshold a :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` instance is
            built.
        
            The matrix elements are all set to 0.0.
        
            Parameters:
                rows (int): the number of rows of the matrix
                columns (int): the number of columns of the matrix
        
            Returns:
                a new :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` with specified dimensions
        
            Also see:
        
            Returns a :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` whose entries are the the values in the the input
            array.
        
            The type of matrix returned depends on the dimension. Below 2 :sup:`12` elements (i.e. 4096 elements or 64×64 for a
            square matrix) which can be stored in a 32kB array, a :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix`
            instance is built. Above this threshold a :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` instance is
            built.
        
            The input array is copied, not referenced.
        
            Parameters:
                data (double[][]): the input array
        
            Returns:
                a new :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` containing the values of the input array
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if either :code:`data` or :code:`data[0]` is :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if a row or column is empty
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`data` is not rectangular (not all rows have the same length)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils.createRealMatrix`
        
        """
        ...
    @typing.overload
    @staticmethod
    def createRealMatrix(doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], boolean: bool) -> 'RealMatrix':
        """
            Returns a :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` whose entries are the the values in the the input
            array.
        
            The type of matrix returned depends on the dimension. Below 2 :sup:`12` elements (i.e. 4096 elements or 64×64 for a
            square matrix) which can be stored in a 32kB array, a :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix`
            instance is built. Above this threshold a :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` instance is
            built.
        
            The input array is either copied or referenced, depending on the :code:`forceCopyArray` argument.
        
            Parameters:
                data (double[][]): the input array
                forceCopyArray (boolean): if :code:`true` or if the matrix has more than 4096 elements, the input array is copied, otherwise it is referenced
        
            Returns:
                a new :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` containing the values of the input array
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if either :code:`data` or :code:`data[0]` is :code:`null`.
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if a row or column is empty.
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`data` is not rectangular (not all rows have the same length)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils.createRealMatrix`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createRealMatrix(int: int, int2: int) -> 'RealMatrix': ...
    @staticmethod
    def createRealVector(doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> 'RealVector':
        """
            Creates a :class:`~fr.cnes.sirius.patrius.math.linear.RealVector` using the data from the input array.
        
            Parameters:
                data (double[]): the input data
        
            Returns:
                a data.length RealVector
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if :code:`data` is empty.
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if :code:`data` is :code:`null`.
        
        
        """
        ...
    _createRowFieldMatrix__T = typing.TypeVar('_createRowFieldMatrix__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
    @staticmethod
    def createRowFieldMatrix(tArray: typing.Union[typing.List[_createRowFieldMatrix__T], jpype.JArray]) -> 'FieldMatrix'[_createRowFieldMatrix__T]:
        """
            Create a row :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrix` using the data from the input array.
        
            Parameters:
                rowData (T[]): the input row data
        
            Returns:
                a 1 x rowData.length FieldMatrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if :code:`rowData` is empty.
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if :code:`rowData` is :code:`null`.
        
        
        """
        ...
    @staticmethod
    def createRowRealMatrix(doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> 'RealMatrix':
        """
            Create a row :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` using the data from the input array.
        
            Parameters:
                rowData (double[]): the input row data
        
            Returns:
                a 1 x rowData.length RealMatrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if :code:`rowData` is empty.
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if :code:`rowData` is :code:`null`.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def deserializeRealMatrix(objectInputStream: java.io.ObjectInputStream) -> 'RealMatrix': ...
    @typing.overload
    @staticmethod
    def deserializeRealMatrix(string: str) -> 'RealMatrix': ...
    @staticmethod
    def deserializeRealVector(objectInputStream: java.io.ObjectInputStream) -> 'RealVector': ...
    @staticmethod
    def fractionMatrixToRealMatrix(fieldMatrix: 'FieldMatrix'[fr.cnes.sirius.patrius.math.fraction.Fraction]) -> 'Array2DRowRealMatrix': ...
    @staticmethod
    def getColumnPermutationIndexArray(anyMatrix: AnyMatrix, intArray: typing.Union[typing.List[int], jpype.JArray]) -> typing.MutableSequence[int]:
        """
            Builds a column permutation index array for a given matrix, starting with the preselected columns.
        
            This methods creates a permutation index array by completing the supplied index array with the missing column indices
            (in increasing order). The preselected indices must be valid column indices for the supplied matrix. Any duplicate found
            in the supplied index array is simply ignored.
        
            **Usage examples, for a 4x5 matrix:**
        
            .. code-block: java
            
            
             getColumnPermutation(m, {2, 3}) => {2, 3, 0, 1, 4}
             getColumnPermutation(m, {0, 4, 1, 0}) => {0, 4, 1, 2, 3}
             
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): the matrix
                preSelectedColumns (int[]): the preselected column indices
        
            Returns:
                the column permutation index array built
        
        
        """
        ...
    @staticmethod
    def getRowPermutationIndexArray(anyMatrix: AnyMatrix, intArray: typing.Union[typing.List[int], jpype.JArray]) -> typing.MutableSequence[int]:
        """
            Builds a row permutation index array for a given matrix, starting with the preselected rows.
        
            This methods creates a permutation index array by completing the supplied index array with the missing row indices (in
            increasing order). The preselected indices must be valid row indices for the supplied matrix. Any duplicate found in the
            supplied index array is simply ignored.
        
            **Usage examples, for a 5x4 matrix:**
        
            .. code-block: java
            
            
             getRowPermutation(m, {2, 3}) => {2, 3, 0, 1, 4}
             getRowPermutation(m, {0, 4, 1, 0}) => {0, 4, 1, 2, 3}
             
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`): the matrix
                preSelectedRows (int[]): the preselected row indices
        
            Returns:
                the row permutation index array built
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def multiplyByTranspose(double: float, realMatrix: 'RealMatrix', realMatrix2: 'RealMatrix') -> 'RealMatrix':
        """
            Multiplies the matrix L by R :sup:`T` and by a scalar factor α.
        
            This methods allows to combine scalar multiplication, matrix multiplication and matrix transposition for optimization
            purposes.
        
            Parameters:
                alpha (double): the scalar factor α
                matrixL (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the left-side matrix L
                matrixR (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the right-side matrix R (not its transpose)
        
            Returns:
                the result of the multiplication
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def multiplyByTranspose(realMatrix: 'RealMatrix', realMatrix2: 'RealMatrix') -> 'RealMatrix':
        """
            Multiplies the matrix L by R :sup:`T` .
        
            This methods allows to combine matrix multiplication and matrix transposition for optimization purposes.
        
            Parameters:
                matrixL (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the left-side matrix L
                matrixR (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the right-side matrix R (not its transpose)
        
            Returns:
                the result of the multiplication
        
        """
        ...
    @staticmethod
    def resize(realMatrix: 'RealMatrix', int: int, int2: int) -> 'RealMatrix':
        """
            Resizes the provided matrix to a NxM matrix.
        
            The provided matrix is truncated or extended, depending on whether its dimensions are bigger or smaller than the
            requested dimensions. If extended, the terms added are set to zero.
        
            Parameters:
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be truncated
                rowDim (int): the row dimension N of the matrix returned
                colDim (int): the column dimension M of the matrix returned
        
            Returns:
                the resized matrix (NxM)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def serializeRealMatrix(realMatrix: 'RealMatrix', objectOutputStream: java.io.ObjectOutputStream) -> None: ...
    @typing.overload
    @staticmethod
    def serializeRealMatrix(realMatrix: 'RealMatrix', string: str) -> None: ...
    @staticmethod
    def serializeRealVector(realVector: 'RealVector', objectOutputStream: java.io.ObjectOutputStream) -> None: ...
    @staticmethod
    def solveLowerTriangularSystem(realMatrix: 'RealMatrix', realVector: 'RealVector') -> None:
        """
            Solve a system of composed of a Lower Triangular Matrix :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`.
        
            This method is called to solve systems of equations which are of the lower triangular form. The matrix
            :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` is assumed, though not checked, to be in lower triangular form.
            The vector :class:`~fr.cnes.sirius.patrius.math.linear.RealVector` is overwritten with the solution. The matrix is
            checked that it is square and its dimensions match the length of the vector.
        
            Parameters:
                rm (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): RealMatrix which is lower triangular
                b (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): RealVector this is overwritten
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the matrix and vector are not compatible
                :class:`~fr.cnes.sirius.patrius.math.linear.NonSquareMatrixException`: if the matrix :code:`rm` is not square
                :class:`~fr.cnes.sirius.patrius.math.exception.MathArithmeticException`: if the absolute value of one of the diagonal coefficient of :code:`rm` is lower than
                    :meth:`~fr.cnes.sirius.patrius.math.util.Precision.SAFE_MIN`
        
        
        """
        ...
    @staticmethod
    def solveUpperTriangularSystem(realMatrix: 'RealMatrix', realVector: 'RealVector') -> None:
        """
            Solver a system composed of an Upper Triangular Matrix :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`.
        
            This method is called to solve systems of equations which are of the lower triangular form. The matrix
            :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` is assumed, though not checked, to be in upper triangular form.
            The vector :class:`~fr.cnes.sirius.patrius.math.linear.RealVector` is overwritten with the solution. The matrix is
            checked that it is square and its dimensions match the length of the vector.
        
            Parameters:
                rm (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): RealMatrix which is upper triangular
                b (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): RealVector this is overwritten
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the matrix and vector are not compatible
                :class:`~fr.cnes.sirius.patrius.math.linear.NonSquareMatrixException`: if the matrix :code:`rm` is not square
                :class:`~fr.cnes.sirius.patrius.math.exception.MathArithmeticException`: if the absolute value of one of the diagonal coefficient of :code:`rm` is lower than
                    :meth:`~fr.cnes.sirius.patrius.math.util.Precision.SAFE_MIN`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def writeMatrix(realMatrix: 'RealMatrix', string: str) -> None: ...
    @typing.overload
    @staticmethod
    def writeMatrix(realMatrix: 'RealMatrix', string: str, string2: str) -> None: ...
    @staticmethod
    def writeMatrixStructure(realMatrix: 'RealMatrix', string: str) -> None: ...

class NonPositiveDefiniteMatrixException(fr.cnes.sirius.patrius.math.exception.NumberIsTooSmallException):
    """
    public class NonPositiveDefiniteMatrixException extends :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooSmallException`
    
        Exception to be thrown when a positive definite matrix is expected.
    
        Since:
            3.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, double: float, int: int, double2: float): ...
    def getColumn(self) -> int:
        """
        
            Returns:
                the column index.
        
        
        """
        ...
    def getRow(self) -> int:
        """
        
            Returns:
                the row index.
        
        
        """
        ...
    def getThreshold(self) -> float:
        """
        
            Returns:
                the absolute positivity threshold.
        
        
        """
        ...

class NonPositiveDefiniteOperatorException(fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException):
    """
    public class NonPositiveDefiniteOperatorException extends :class:`~fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException`
    
        Exception to be thrown when a symmetric, definite positive
        :class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator` is expected. Since the coefficients of the matrix are
        not accessible, the most general definition is used to check that :code:`A` is not positive definite, i.e. there exists
        :code:`x` such that :code:`x' A x <= 0`. In the terminology of this exception, :code:`A` is the "offending" linear
        operator and :code:`x` the "offending" vector.
    
        Since:
            3.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...

class NonSelfAdjointOperatorException(fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException):
    """
    public class NonSelfAdjointOperatorException extends :class:`~fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException`
    
        Exception to be thrown when a self-adjoint :class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator` is expected.
        Since the coefficients of the matrix are not accessible, the most general definition is used to check that A is not
        self-adjoint, i.e. there exist x and y such as :code:`| x' A y - y' A x | >= eps`, where :code:`eps` is a user-specified
        tolerance, and :code:`x'` denotes the transpose of :code:`x`. In the terminology of this exception, :code:`A` is the
        "offending" linear operator, :code:`x` and :code:`y` are the first and second "offending" vectors, respectively.
    
        Since:
            3.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...

class NonSquareMatrixException(fr.cnes.sirius.patrius.math.exception.DimensionMismatchException):
    """
    public class NonSquareMatrixException extends :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`
    
        Exception to be thrown when a square matrix is expected.
    
        Since:
            3.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, int: int, int2: int): ...

class NonSquareOperatorException(fr.cnes.sirius.patrius.math.exception.DimensionMismatchException):
    """
    public class NonSquareOperatorException extends :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`
    
        Exception to be thrown when a square linear operator is expected.
    
        Since:
            3.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, int: int, int2: int): ...

class NonSymmetricMatrixException(fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException):
    """
    public class NonSymmetricMatrixException extends :class:`~fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException`
    
        Exception to be thrown when a symmetric matrix is expected.
    
        Since:
            3.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, int: int, int2: int, double: float): ...
    def getColumn(self) -> int:
        """
        
            Returns:
                the column index of the entry.
        
        
        """
        ...
    def getRow(self) -> int:
        """
        
            Returns:
                the row index of the entry.
        
        
        """
        ...
    def getThreshold(self) -> float:
        """
        
            Returns:
                the relative symmetry threshold.
        
        
        """
        ...

class RealLinearOperator:
    def __init__(self): ...
    def getColumnDimension(self) -> int: ...
    def getRowDimension(self) -> int: ...
    def isTransposable(self) -> bool: ...
    def operate(self, realVector: 'RealVector') -> 'RealVector': ...
    def operateTranspose(self, realVector: 'RealVector') -> 'RealVector': ...

class RealMatrixChangingVisitor:
    """
    public interface RealMatrixChangingVisitor
    
        Interface defining a visitor for matrix entries.
    
        Since:
            2.0
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.math.linear.DefaultRealMatrixChangingVisitor`
    """
    def end(self) -> float:
        """
            End visiting a matrix.
        
            This method is called once after all entries of the matrix have been visited.
        
            Returns:
                the value that the :code:`walkInXxxOrder` must return
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int) -> None:
        """
            Start visiting a matrix.
        
            This method is called once before any entry of the matrix is visited.
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, int: int, int2: int, double: float) -> float:
        """
            Visit one matrix entry.
        
            Parameters:
                row (int): row index of the entry
                column (int): column index of the entry
                value (double): current value of the entry
        
            Returns:
                the new value to be set for the entry
        
        
        """
        ...

class RealMatrixFormat:
    """
    public class RealMatrixFormat extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`
    
        Formats a :code:`nxm` matrix in components list format "{{a :sub:`0` :sub:`0` ,a :sub:`0` :sub:`1` , ..., a :sub:`0`
        :sub:`m-1` },{a :sub:`1` :sub:`0` , a :sub:`1` :sub:`1` , ..., a :sub:`1` :sub:`m-1` },{...},{ a :sub:`n-1` :sub:`0` , a
        :sub:`n-1` :sub:`1` , ..., a :sub:`n-1` :sub:`m-1` }}".
    
        The prefix and suffix "{" and "}", the row prefix and suffix "{" and "}", the row separator "," and the column separator
        "," can be replaced by any user-defined strings. The number format for components can be configured.
    
        White space is ignored at parse time, even if it is in the prefix, suffix or separator specifications. So even if the
        default separator does include a space character that is used at format time, both input string "{{1,1,1}}" and " { { 1
        , 1 , 1 } } " will be parsed without error and the same matrix will be returned. In the second case, however, the parse
        position after parsing will be just after the closing curly brace, i.e. just before the trailing space.
    
        **Note:** the grouping functionality of the used `null
        <http://docs.oracle.com/javase/8/docs/api/java/text/NumberFormat.html?is-external=true>` is disabled to prevent problems
        when parsing (e.g. 1,345.34 would be a valid number but conflicts with the default column separator).
    
        Since:
            3.1
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, string4: str, string5: str, string6: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, string4: str, string5: str, string6: str, string7: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, string4: str, string5: str, string6: str, string7: str, int: int): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, string4: str, string5: str, string6: str, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def format(self, realMatrix: 'RealMatrix') -> str:
        """
            This method calls :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixFormat.format`.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): RealMatrix object to format.
        
            Returns:
                a formatted matrix.
        
        """
        ...
    @typing.overload
    def format(self, realMatrix: 'RealMatrix', stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer:
        """
            Formats a :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` object to produce a string.
        
            Parameters:
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the object to format.
                toAppendTo (`StringBuffer <http://docs.oracle.com/javase/8/docs/api/java/lang/StringBuffer.html?is-external=true>`): where the text is to be appended
                pos (`FieldPosition <http://docs.oracle.com/javase/8/docs/api/java/text/FieldPosition.html?is-external=true>`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                the value passed in as toAppendTo.
        
        
        """
        ...
    @staticmethod
    def getAvailableLocales() -> typing.MutableSequence[java.util.Locale]:
        """
            Get the set of locales for which real vectors formats are available.
        
            This is the same set as the `null
            <http://docs.oracle.com/javase/8/docs/api/java/text/NumberFormat.html?is-external=true>` set.
        
            Returns:
                available real vector format locales.
        
        
        """
        ...
    def getColumnSeparator(self) -> str:
        """
            Get the format separator between components.
        
            Returns:
                format separator between components.
        
        
        """
        ...
    def getFormat(self) -> java.text.NumberFormat:
        """
            Get the components format.
        
            Returns:
                components format.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getInstance() -> 'RealMatrixFormat':
        """
            Returns the default real vector format for the current locale.
        
            Returns:
                the default real vector format.
        
        """
        ...
    @typing.overload
    @staticmethod
    def getInstance(locale: java.util.Locale) -> 'RealMatrixFormat':
        """
            Returns the default real vector format for the given locale.
        
            Parameters:
                locale (`Locale <http://docs.oracle.com/javase/8/docs/api/java/util/Locale.html?is-external=true>`): the specific locale used by the format.
        
            Returns:
                the real vector format specific to the given locale.
        
        
        """
        ...
    def getPrefix(self) -> str:
        """
            Get the format prefix.
        
            Returns:
                format prefix.
        
        
        """
        ...
    def getRowPrefix(self) -> str:
        """
            Get the format prefix.
        
            Returns:
                format prefix.
        
        
        """
        ...
    def getRowSeparator(self) -> str:
        """
            Get the format separator between rows of the matrix.
        
            Returns:
                format separator for rows.
        
        
        """
        ...
    def getRowSuffix(self) -> str:
        """
            Get the format suffix.
        
            Returns:
                format suffix.
        
        
        """
        ...
    def getSuffix(self) -> str:
        """
            Get the format suffix.
        
            Returns:
                format suffix.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str) -> 'RealMatrix':
        """
            Parse a string to produce a :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` object.
        
            Parameters:
                source (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): String to parse.
        
            Returns:
                the parsed :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` object.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathParseException`: if the beginning of the specified string cannot be parsed.
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> 'RealMatrix':
        """
            Parse a string to produce a :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` object.
        
            Parameters:
                source (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): String to parse.
                pos (`ParsePosition <http://docs.oracle.com/javase/8/docs/api/java/text/ParsePosition.html?is-external=true>`): input/ouput parsing parameter.
        
            Returns:
                the parsed :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` object.
        
        
        """
        ...

class RealMatrixPreservingVisitor:
    """
    public interface RealMatrixPreservingVisitor
    
        Interface defining a visitor for matrix entries.
    
        Since:
            2.0
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.math.linear.DefaultRealMatrixPreservingVisitor`
    """
    def end(self) -> float:
        """
            End visiting a matrix.
        
            This method is called once after all entries of the matrix have been visited.
        
            Returns:
                the value that the :code:`walkInXxxOrder` must return
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int) -> None:
        """
            Start visiting a matrix.
        
            This method is called once before any entry of the matrix is visited.
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, int: int, int2: int, double: float) -> None:
        """
            Visit one matrix entry.
        
            Parameters:
                row (int): row index of the entry
                column (int): column index of the entry
                value (double): current value of the entry
        
        
        """
        ...

class RealVector:
    """
    public abstract class RealVector extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`
    
        Class defining a real-valued vector with basic algebraic operations.
    
        vector element indexing is 0-based -- e.g., :code:`getEntry(0)` returns the first element of the vector.
    
        The :code:`code map` and :code:`mapToSelf` methods operate on vectors element-wise, i.e. they perform the same operation
        (adding a scalar, applying a function ...) on each element in turn. The :code:`map` versions create a new vector to hold
        the result and do not change the instance. The :code:`mapToSelf` version uses the instance itself to store the results,
        so the instance is changed by this method. In all cases, the result vector is returned by the methods, allowing the
        *fluent API* style, like this:
    
        .. code-block: java
        
        
         RealVector result = v.mapAddToSelf(3.4).mapToSelf(new Tan()).mapToSelf(new Power(2.3));
         
    
        Since:
            2.1
    """
    def __init__(self): ...
    def add(self, realVector: 'RealVector') -> 'RealVector':
        """
            Compute the sum of this vector and :code:`v`. Returns a new vector. Does not change instance data.
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector to be added.
        
            Returns:
                :code:`this` + :code:`v`.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`v` is not the same size as :code:`this` vector.
        
        
        """
        ...
    def addToEntry(self, int: int, double: float) -> None:
        """
            Change an entry at the specified index.
        
            Parameters:
                index (int): Index location of entry to be set.
                increment (double): Value to add to the vector entry.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the index is not valid.
        
            Since:
                3.0
        
        
        """
        ...
    @typing.overload
    def append(self, double: float) -> 'RealVector':
        """
            Construct a new vector by appending a vector to this vector.
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): vector to append to this one.
        
            Returns:
                a new vector.
        
            Construct a new vector by appending a double to this vector.
        
            Parameters:
                d (double): double to append.
        
            Returns:
                a new vector.
        
        
        """
        ...
    @typing.overload
    def append(self, realVector: 'RealVector') -> 'RealVector': ...
    def combine(self, double: float, double2: float, realVector: 'RealVector') -> 'RealVector':
        """
            Returns a new vector representing :code:`a * this + b * y`, the linear combination of :code:`this` and :code:`y`.
            Returns a new vector. Does not change instance data.
        
            Parameters:
                a (double): Coefficient of :code:`this`.
                b (double): Coefficient of :code:`y`.
                y (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector with which :code:`this` is linearly combined.
        
            Returns:
                a vector containing :code:`a * this[i] + b * y[i]` for all :code:`i`.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`y` is not the same size as :code:`this` vector.
        
        
        """
        ...
    def combineToSelf(self, double: float, double2: float, realVector: 'RealVector') -> 'RealVector':
        """
            Updates :code:`this` with the linear combination of :code:`this` and :code:`y`.
        
            Parameters:
                a (double): Weight of :code:`this`.
                b (double): Weight of :code:`y`.
                y (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector with which :code:`this` is linearly combined.
        
            Returns:
                :code:`this`, with components equal to :code:`a * this[i] + b * y[i]` for all :code:`i`.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`y` is not the same size as :code:`this` vector.
        
        
        """
        ...
    def copy(self) -> 'RealVector':
        """
            Returns a (deep) copy of this vector.
        
            Returns:
                a vector copy.
        
        
        """
        ...
    def cosine(self, realVector: 'RealVector') -> float:
        """
            Computes the cosine of the angle between this vector and the argument.
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector.
        
            Returns:
                the cosine of the angle between this vector and :code:`v`.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathArithmeticException`: if :code:`this` or :code:`v` is the null vector
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the dimensions of :code:`this` and :code:`v` do not match
        
        
        """
        ...
    def dotProduct(self, realVector: 'RealVector') -> float:
        """
            Compute the dot product of this vector with :code:`v`.
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector with which dot product should be computed
        
            Returns:
                the scalar dot product between this instance and :code:`v`.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`v` is not the same size as :code:`this` vector.
        
        
        """
        ...
    def ebeDivide(self, realVector: 'RealVector') -> 'RealVector': ...
    def ebeMultiply(self, realVector: 'RealVector') -> 'RealVector': ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Test for the equality of two real vectors. If all coordinates of two real vectors are exactly the same, and none are
            :code:`NaN`, the two real vectors are considered to be equal. :code:`NaN` coordinates are considered to affect globally
            the vector and be equals to each other - i.e, if either (or all) coordinates of the real vector are equal to
            :code:`NaN`, the real vector is equal to a vector with all :code:`NaN` coordinates.
        
            This method *must* be overriden by concrete subclasses of :class:`~fr.cnes.sirius.patrius.math.linear.RealVector` (the
            current implementation throws an exception).
        
            Overrides:
                 in class 
        
            Parameters:
                other (`Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`): Object to test for equality.
        
            Returns:
                :code:`true` if two vector objects are equal, :code:`false` if :code:`other` is null, not an instance of
                :code:`RealVector`, or not equal to this :code:`RealVector` instance.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: if this method is not overridden.
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Returns the size of the vector.
        
            Returns:
                the size of this vector.
        
        
        """
        ...
    def getDistance(self, realVector: 'RealVector') -> float:
        """
            Distance between two vectors.
        
            This method computes the distance consistent with the L :sub:`2` norm, i.e. the square root of the sum of element
            differences, or Euclidean distance.
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector to which distance is requested.
        
            Returns:
                the distance between two vectors.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`v` is not the same size as :code:`this` vector.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getL1Distance`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getLInfDistance`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getNorm`
        
        
        """
        ...
    def getEntry(self, int: int) -> float:
        """
            Return the entry at the specified index.
        
            Parameters:
                index (int): Index location of entry to be fetched.
        
            Returns:
                the vector entry at :code:`index`.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the index is not valid.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.setEntry`
        
        
        """
        ...
    def getL1Distance(self, realVector: 'RealVector') -> float:
        """
            Distance between two vectors.
        
            This method computes the distance consistent with L :sub:`1` norm, i.e. the sum of the absolute values of the elements
            differences.
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector to which distance is requested.
        
            Returns:
                the distance between two vectors.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`v` is not the same size as :code:`this` vector.
        
        
        """
        ...
    def getL1Norm(self) -> float:
        """
            Returns the L :sub:`1` norm of the vector.
        
            The L :sub:`1` norm is the sum of the absolute values of the elements.
        
            Returns:
                the norm.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getNorm`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getLInfNorm`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getL1Distance`
        
        
        """
        ...
    def getLInfDistance(self, realVector: 'RealVector') -> float:
        """
            Distance between two vectors.
        
            This method computes the distance consistent with L :sub:`∞` norm, i.e. the max of the absolute values of element
            differences.
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector to which distance is requested.
        
            Returns:
                the distance between two vectors.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`v` is not the same size as :code:`this` vector.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getDistance`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getL1Distance`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getLInfNorm`
        
        
        """
        ...
    def getLInfNorm(self) -> float:
        """
            Returns the L :sub:`∞` norm of the vector.
        
            The L :sub:`∞` norm is the max of the absolute values of the elements.
        
            Returns:
                the norm.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getNorm`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getL1Norm`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getLInfDistance`
        
        
        """
        ...
    def getMaxIndex(self) -> int:
        """
            Get the index of the maximum entry.
        
            Returns:
                the index of the maximum entry or -1 if vector length is 0 or all entries are :code:`NaN`
        
        
        """
        ...
    def getMaxValue(self) -> float:
        """
            Get the value of the maximum entry.
        
            Returns:
                the value of the maximum entry or :code:`NaN` if all entries are :code:`NaN`.
        
        
        """
        ...
    def getMinIndex(self) -> int:
        """
            Get the index of the minimum entry.
        
            Returns:
                the index of the minimum entry or -1 if vector length is 0 or all entries are :code:`NaN`.
        
        
        """
        ...
    def getMinValue(self) -> float:
        """
            Get the value of the minimum entry.
        
            Returns:
                the value of the minimum entry or :code:`NaN` if all entries are :code:`NaN`.
        
        
        """
        ...
    def getNorm(self) -> float:
        """
            Returns the L :sub:`2` norm of the vector.
        
            The L :sub:`2` norm is the root of the sum of the squared elements.
        
            Returns:
                the norm.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getL1Norm`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getLInfNorm`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getDistance`
        
        
        """
        ...
    def getSubVector(self, int: int, int2: int) -> 'RealVector':
        """
            Get a subvector from consecutive elements.
        
            Parameters:
                index (int): index of first element.
                n (int): number of elements to be retrieved.
        
            Returns:
                a vector containing n elements.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the index is not valid.
                :class:`~fr.cnes.sirius.patrius.math.exception.NotPositiveException`: if the number of elements is not positive.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            . This method *must* be overriden by concrete subclasses of :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
            (current implementation throws an exception).
        
            Overrides:
                 in class 
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: if this method is not overridden.
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
            Check whether any coordinate of this vector is infinite and none are :code:`NaN`.
        
            Returns:
                :code:`true` if any coordinate of this vector is infinite and none are :code:`NaN`, :code:`false` otherwise.
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
            Check whether any coordinate of this vector is :code:`NaN`.
        
            Returns:
                :code:`true` if any coordinate of this vector is :code:`NaN`, :code:`false` otherwise.
        
        
        """
        ...
    def iterator(self) -> java.util.Iterator['RealVector.Entry']: ...
    def map(self, univariateFunction: typing.Union[fr.cnes.sirius.patrius.math.analysis.UnivariateFunction, typing.Callable]) -> 'RealVector':
        """
            Acts as if implemented as:
        
            .. code-block: java
            
            
             return copy().mapToSelf(function);
             
            Returns a new vector. Does not change instance data.
        
            Parameters:
                function (:class:`~fr.cnes.sirius.patrius.math.analysis.UnivariateFunction`): Function to apply to each entry.
        
            Returns:
                a new vector.
        
        
        """
        ...
    def mapAdd(self, double: float) -> 'RealVector':
        """
            Add a value to each entry. Returns a new vector. Does not change instance data.
        
            Parameters:
                d (double): Value to be added to each entry.
        
            Returns:
                :code:`this` + :code:`d`.
        
        
        """
        ...
    def mapAddToSelf(self, double: float) -> 'RealVector':
        """
            Add a value to each entry. The instance is changed in-place.
        
            Parameters:
                d (double): Value to be added to each entry.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def mapDivide(self, double: float) -> 'RealVector':
        """
            Divide each entry by the argument. Returns a new vector. Does not change instance data.
        
            Parameters:
                d (double): Value to divide by.
        
            Returns:
                :code:`this` / :code:`d`.
        
        
        """
        ...
    def mapDivideToSelf(self, double: float) -> 'RealVector':
        """
            Divide each entry by the argument. The instance is changed in-place.
        
            Parameters:
                d (double): Value to divide by.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def mapMultiply(self, double: float) -> 'RealVector':
        """
            Multiply each entry by the argument. Returns a new vector. Does not change instance data.
        
            Parameters:
                d (double): Multiplication factor.
        
            Returns:
                :code:`this` * :code:`d`.
        
        
        """
        ...
    def mapMultiplyToSelf(self, double: float) -> 'RealVector':
        """
            Multiply each entry. The instance is changed in-place.
        
            Parameters:
                d (double): Multiplication factor.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def mapSubtract(self, double: float) -> 'RealVector':
        """
            Subtract a value from each entry. Returns a new vector. Does not change instance data.
        
            Parameters:
                d (double): Value to be subtracted.
        
            Returns:
                :code:`this` - :code:`d`.
        
        
        """
        ...
    def mapSubtractToSelf(self, double: float) -> 'RealVector':
        """
            Subtract a value from each entry. The instance is changed in-place.
        
            Parameters:
                d (double): Value to be subtracted.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def mapToSelf(self, univariateFunction: typing.Union[fr.cnes.sirius.patrius.math.analysis.UnivariateFunction, typing.Callable]) -> 'RealVector':
        """
            Acts as if it is implemented as:
        
            .. code-block: java
            
            
             Entry e = null;
             for (Iterator<Entry> it = iterator(); it.hasNext(); e = it.next()) {
                 e.setValue(function.value(e.getValue()));
             }
             
            Entries of this vector are modified in-place by this method.
        
            Parameters:
                function (:class:`~fr.cnes.sirius.patrius.math.analysis.UnivariateFunction`): Function to apply to each entry.
        
            Returns:
                a reference to this vector.
        
        
        """
        ...
    def outerProduct(self, realVector: 'RealVector') -> 'RealMatrix':
        """
            Compute the outer product.
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector with which outer product should be computed.
        
            Returns:
                the matrix outer product between this instance and :code:`v`.
        
        
        """
        ...
    def projection(self, realVector: 'RealVector') -> 'RealVector':
        """
            Find the orthogonal projection of this vector onto another vector.
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): vector onto which instance must be projected.
        
            Returns:
                projection of the instance onto :code:`v`.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`v` is not the same size as :code:`this` vector.
                :class:`~fr.cnes.sirius.patrius.math.exception.MathArithmeticException`: if :code:`this` or :code:`v` is the null vector
        
        
        """
        ...
    def set(self, double: float) -> None:
        """
            Set all elements to a single value.
        
            Parameters:
                value (double): Single value to set for all elements.
        
        
        """
        ...
    def setEntry(self, int: int, double: float) -> None:
        """
            Set a single element.
        
            Parameters:
                index (int): element index.
                value (double): new value for the element.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the index is not valid.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getEntry`
        
        
        """
        ...
    def setSubVector(self, int: int, realVector: 'RealVector') -> None:
        """
            Set a sequence of consecutive elements.
        
            Parameters:
                index (int): index of first element to be set.
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): vector containing the values to set.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the index is not valid.
        
        
        """
        ...
    def subtract(self, realVector: 'RealVector') -> 'RealVector':
        """
            Subtract :code:`v` from this vector. Returns a new vector. Does not change instance data.
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector to be subtracted.
        
            Returns:
                :code:`this` - :code:`v`.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`v` is not the same size as :code:`this` vector.
        
        
        """
        ...
    def toArray(self) -> typing.MutableSequence[float]:
        """
            Convert the vector to an array of :code:`double`s. The array is independent from this vector data: the elements are
            copied.
        
            Returns:
                an array containing a copy of the vector elements.
        
        
        """
        ...
    def unitVector(self) -> 'RealVector':
        """
            Creates a unit vector pointing in the direction of this vector. The instance is not changed by this method.
        
            Returns:
                a unit vector pointing in direction of this vector.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathArithmeticException`: if the norm is zero.
        
        
        """
        ...
    def unitize(self) -> None:
        """
            Converts this vector into a unit vector. The instance itself is changed by this method.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathArithmeticException`: if the norm is zero.
        
        
        """
        ...
    @staticmethod
    def unmodifiableRealVector(realVector: 'RealVector') -> 'RealVector':
        """
            Returns an unmodifiable view of the specified vector. The returned vector has read-only access. An attempt to modify it
            will result in a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`. However, the
            returned vector is *not* immutable, since any modification of :code:`v` will also change the returned view. For example,
            in the following piece of code
        
            .. code-block: java
            
            
             RealVector v = new ArrayRealVector(2);
             RealVector w = RealVector.unmodifiableRealVector(v);
             v.setEntry(0, 1.2);
             v.setEntry(1, -3.4);
             
            the changes will be seen in the :code:`w` view of :code:`v`.
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector for which an unmodifiable view is to be returned.
        
            Returns:
                an unmodifiable view of :code:`v`.
        
        
        """
        ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorChangingVisitor: 'RealVectorChangingVisitor') -> float:
        """
            Visits (but does not alter) all entries of this vector in default order (increasing index).
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealVectorPreservingVisitor`): the visitor to be used to process the entries of this vector
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorPreservingVisitor.end` at the end of the walk
        
            Since:
                3.1
        
            Visits (but does not alter) some entries of this vector in default order (increasing index).
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealVectorPreservingVisitor`): visitor to be used to process the entries of this vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooSmallException`: if :code:`end < start`.
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the indices are not valid.
        
            Since:
                3.1
        
            Visits (and possibly alters) all entries of this vector in default order (increasing index).
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealVectorChangingVisitor`): the visitor to be used to process and modify the entries of this vector
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorChangingVisitor.end` at the end of the walk
        
            Since:
                3.1
        
            Visits (and possibly alters) some entries of this vector in default order (increasing index).
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealVectorChangingVisitor`): visitor to be used to process the entries of this vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooSmallException`: if :code:`end < start`.
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the indices are not valid.
        
            Since:
                3.1
        
        
        """
        ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorChangingVisitor: 'RealVectorChangingVisitor', int: int, int2: int) -> float: ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorPreservingVisitor: 'RealVectorPreservingVisitor') -> float: ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorPreservingVisitor: 'RealVectorPreservingVisitor', int: int, int2: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realVectorChangingVisitor: 'RealVectorChangingVisitor') -> float:
        """
            Visits (but does not alter) all entries of this vector in optimized order. The order in which the entries are visited is
            selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this
            abstract class.
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealVectorPreservingVisitor`): the visitor to be used to process the entries of this vector
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorPreservingVisitor.end` at the end of the walk
        
            Since:
                3.1
        
            Visits (but does not alter) some entries of this vector in optimized order. The order in which the entries are visited
            is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this
            abstract class.
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealVectorPreservingVisitor`): visitor to be used to process the entries of this vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooSmallException`: if :code:`end < start`.
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the indices are not valid.
        
            Since:
                3.1
        
            Visits (and possibly alters) all entries of this vector in optimized order. The order in which the entries are visited
            is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this
            abstract class.
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealVectorChangingVisitor`): the visitor to be used to process the entries of this vector
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorChangingVisitor.end` at the end of the walk
        
            Since:
                3.1
        
            Visits (and possibly change) some entries of this vector in optimized order. The order in which the entries are visited
            is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this
            abstract class.
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealVectorChangingVisitor`): visitor to be used to process the entries of this vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooSmallException`: if :code:`end < start`.
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the indices are not valid.
        
            Since:
                3.1
        
        
        """
        ...
    @typing.overload
    def walkInOptimizedOrder(self, realVectorChangingVisitor: 'RealVectorChangingVisitor', int: int, int2: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realVectorPreservingVisitor: 'RealVectorPreservingVisitor') -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realVectorPreservingVisitor: 'RealVectorPreservingVisitor', int: int, int2: int) -> float: ...
    class Entry: ...

class RealVectorChangingVisitor:
    """
    public interface RealVectorChangingVisitor
    
        This interface defines a visitor for the entries of a vector. Visitors implementing this interface may alter the entries
        of the vector being visited.
    
        Since:
            3.1
    """
    def end(self) -> float:
        """
            End visiting a vector. This method is called once, after all entries of the vector have been visited.
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.walkInDefaultOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.walkInDefaultOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.walkInOptimizedOrder` or
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.walkInOptimizedOrder`
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int) -> None:
        """
            Start visiting a vector. This method is called once, before any entry of the vector is visited.
        
            Parameters:
                dimension (int): the size of the vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
        
        """
        ...
    def visit(self, int: int, double: float) -> float:
        """
            Visit one entry of the vector.
        
            Parameters:
                index (int): the index of the entry being visited
                value (double): the value of the entry being visited
        
            Returns:
                the new value of the entry being visited
        
        
        """
        ...

class RealVectorFormat:
    """
    public class RealVectorFormat extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`
    
        Formats a vector in components list format "{v0; v1; ...; vk-1}".
    
        The prefix and suffix "{" and "}" and the separator "; " can be replaced by any user-defined strings. The number format
        for components can be configured.
    
        White space is ignored at parse time, even if it is in the prefix, suffix or separator specifications. So even if the
        default separator does include a space character that is used at format time, both input string "{1;1;1}" and " { 1 ; 1
        ; 1 } " will be parsed without error and the same vector will be returned. In the second case, however, the parse
        position after parsing will be just after the closing curly brace, i.e. just before the trailing space.
    
        Since:
            2.0
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
    def format(self, realVector: RealVector) -> str:
        """
            This method calls :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorFormat.format`.
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): RealVector object to format.
        
            Returns:
                a formatted vector.
        
        """
        ...
    @typing.overload
    def format(self, realVector: RealVector, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer:
        """
            Formats a :class:`~fr.cnes.sirius.patrius.math.linear.RealVector` object to produce a string.
        
            Parameters:
                vector (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the object to format.
                toAppendTo (`StringBuffer <http://docs.oracle.com/javase/8/docs/api/java/lang/StringBuffer.html?is-external=true>`): where the text is to be appended
                pos (`FieldPosition <http://docs.oracle.com/javase/8/docs/api/java/text/FieldPosition.html?is-external=true>`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                the value passed in as toAppendTo.
        
        
        """
        ...
    @staticmethod
    def getAvailableLocales() -> typing.MutableSequence[java.util.Locale]:
        """
            Get the set of locales for which real vectors formats are available.
        
            This is the same set as the `null
            <http://docs.oracle.com/javase/8/docs/api/java/text/NumberFormat.html?is-external=true>` set.
        
            Returns:
                available real vector format locales.
        
        
        """
        ...
    def getFormat(self) -> java.text.NumberFormat:
        """
            Get the components format.
        
            Returns:
                components format.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getInstance() -> 'RealVectorFormat':
        """
            Returns the default real vector format for the current locale.
        
            Returns:
                the default real vector format.
        
        """
        ...
    @typing.overload
    @staticmethod
    def getInstance(locale: java.util.Locale) -> 'RealVectorFormat':
        """
            Returns the default real vector format for the given locale.
        
            Parameters:
                locale (`Locale <http://docs.oracle.com/javase/8/docs/api/java/util/Locale.html?is-external=true>`): the specific locale used by the format.
        
            Returns:
                the real vector format specific to the given locale.
        
        
        """
        ...
    def getPrefix(self) -> str:
        """
            Get the format prefix.
        
            Returns:
                format prefix.
        
        
        """
        ...
    def getSeparator(self) -> str:
        """
            Get the format separator between components.
        
            Returns:
                format separator.
        
        
        """
        ...
    def getSuffix(self) -> str:
        """
            Get the format suffix.
        
            Returns:
                format suffix.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str) -> 'ArrayRealVector':
        """
            Parse a string to produce a :class:`~fr.cnes.sirius.patrius.math.linear.RealVector` object.
        
            Parameters:
                source (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): String to parse.
        
            Returns:
                the parsed :class:`~fr.cnes.sirius.patrius.math.linear.RealVector` object.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathParseException`: if the beginning of the specified string cannot be parsed.
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> 'ArrayRealVector':
        """
            Parse a string to produce a :class:`~fr.cnes.sirius.patrius.math.linear.RealVector` object.
        
            Parameters:
                source (`String <http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true>`): String to parse.
                pos (`ParsePosition <http://docs.oracle.com/javase/8/docs/api/java/text/ParsePosition.html?is-external=true>`): input/ouput parsing parameter.
        
            Returns:
                the parsed :class:`~fr.cnes.sirius.patrius.math.linear.RealVector` object.
        
        
        """
        ...

class RealVectorPreservingVisitor:
    """
    public interface RealVectorPreservingVisitor
    
        This interface defines a visitor for the entries of a vector. Visitors implementing this interface do not alter the
        entries of the vector being visited.
    
        Since:
            3.1
    """
    def end(self) -> float:
        """
            End visiting a vector. This method is called once, after all entries of the vector have been visited.
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.walkInDefaultOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.walkInDefaultOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.walkInOptimizedOrder` or
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.walkInOptimizedOrder`
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int) -> None:
        """
            Start visiting a vector. This method is called once, before any entry of the vector is visited.
        
            Parameters:
                dimension (int): the size of the vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
        
        """
        ...
    def visit(self, int: int, double: float) -> None:
        """
            Visit one entry of the vector.
        
            Parameters:
                index (int): the index of the entry being visited
                value (double): the value of the entry being visited
        
        
        """
        ...

class RectangularCholeskyDecomposition:
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float): ...
    def getRank(self) -> int: ...
    def getRootMatrix(self) -> 'RealMatrix': ...

class SingularMatrixException(fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException):
    """
    public class SingularMatrixException extends :class:`~fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException`
    
        Exception to be thrown when a non-singular matrix is expected.
    
        Since:
            3.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...

class SingularOperatorException(fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException):
    """
    public class SingularOperatorException extends :class:`~fr.cnes.sirius.patrius.math.exception.MathIllegalArgumentException`
    
        Exception to be thrown when trying to invert a singular operator.
    
        Since:
            3.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...

class UDDecomposition:
    """
    public interface UDDecomposition
    
        An interface to classes that implement an algorithm to calculate the UD-decomposition of a real matrix.
    
        The UD-decomposition of matrix A is a set of three matrices: U, D and U :sup:`t` such that A = U×D×U :sup:`t` . U is a
        upper triangular matrix and D is an diagonal matrix.
    
        - The matrix A must be a symmetric matrix and positive definite
        See DV_MATHS_270.
    
        Since:
            1.0
    """
    def getD(self) -> 'RealMatrix':
        """
            Returns the matrix D of the decomposition.
        
            D is an diagonal matrix
        
            Returns:
                the D matrix
        
        
        """
        ...
    def getDeterminant(self) -> float:
        """
            Return the determinant of the matrix
        
            Returns:
                determinant of the matrix
        
        
        """
        ...
    def getSolver(self) -> DecompositionSolver:
        """
            Get a solver of the linear equation A × X = B for matrices A.
        
            Returns:
                a solver
        
        
        """
        ...
    def getU(self) -> 'RealMatrix':
        """
            Returns the matrix U of the decomposition.
        
            U is an upper-triangular matrix
        
            Returns:
                the U matrix
        
        
        """
        ...
    def getUT(self) -> 'RealMatrix':
        """
            Returns the transpose of the matrix U of the decomposition.
        
            U :sup:`T` is an lower-triangular matrix
        
            Returns:
                the transpose of the matrix U of the decomposition
        
        
        """
        ...

_ArrayFieldVector__T = typing.TypeVar('_ArrayFieldVector__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
class ArrayFieldVector(FieldVector[_ArrayFieldVector__T], java.io.Serializable, typing.Generic[_ArrayFieldVector__T]):
    """
    public class ArrayFieldVector<T extends :class:`~fr.cnes.sirius.patrius.math.FieldElement`<T>> extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.linear.FieldVector`<T>, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        This class implements the :class:`~fr.cnes.sirius.patrius.math.linear.FieldVector` interface with a
        :class:`~fr.cnes.sirius.patrius.math.FieldElement` array.
    
        This class is up-to-date with commons-math 3.6.1.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, field: fr.cnes.sirius.patrius.math.Field[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, field: fr.cnes.sirius.patrius.math.Field[_ArrayFieldVector__T], tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, field: fr.cnes.sirius.patrius.math.Field[_ArrayFieldVector__T], tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray], boolean: bool): ...
    @typing.overload
    def __init__(self, field: fr.cnes.sirius.patrius.math.Field[_ArrayFieldVector__T], tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray], tArray2: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, field: fr.cnes.sirius.patrius.math.Field[_ArrayFieldVector__T], tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray], int: int, int2: int): ...
    @typing.overload
    def __init__(self, field: fr.cnes.sirius.patrius.math.Field[_ArrayFieldVector__T], int: int): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray], boolean: bool): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray], tArray2: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray], fieldVector: FieldVector[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray], int: int, int2: int): ...
    @typing.overload
    def __init__(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T], boolean: bool): ...
    @typing.overload
    def __init__(self, fieldVector: FieldVector[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, fieldVector: FieldVector[_ArrayFieldVector__T], tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, fieldVector: FieldVector[_ArrayFieldVector__T], fieldVector2: FieldVector[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, int: int, t: _ArrayFieldVector__T): ...
    @typing.overload
    def add(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> 'ArrayFieldVector'[_ArrayFieldVector__T]: ...
    @typing.overload
    def add(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> FieldVector[_ArrayFieldVector__T]: ...
    @typing.overload
    def append(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> 'ArrayFieldVector'[_ArrayFieldVector__T]: ...
    @typing.overload
    def append(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    @typing.overload
    def append(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> FieldVector[_ArrayFieldVector__T]: ...
    def copy(self) -> FieldVector[_ArrayFieldVector__T]: ...
    @typing.overload
    def dotProduct(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> _ArrayFieldVector__T: ...
    @typing.overload
    def dotProduct(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> _ArrayFieldVector__T: ...
    @typing.overload
    def ebeDivide(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> 'ArrayFieldVector'[_ArrayFieldVector__T]: ...
    @typing.overload
    def ebeDivide(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> FieldVector[_ArrayFieldVector__T]: ...
    @typing.overload
    def ebeMultiply(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> 'ArrayFieldVector'[_ArrayFieldVector__T]: ...
    @typing.overload
    def ebeMultiply(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> FieldVector[_ArrayFieldVector__T]: ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two vectors.
        
            Overrides:
                 in class 
        
            Parameters:
                other (`Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`): Object to test for equality.
        
            Returns:
                :code:`true` if two vector objects are equal, :code:`false` otherwise.
        
        
        """
        ...
    def getData(self) -> typing.MutableSequence[_ArrayFieldVector__T]:
        """
            Returns the vector data (copy).
        
            Returns:
                the vector data
        
        
        """
        ...
    def getDataRef(self) -> typing.MutableSequence[_ArrayFieldVector__T]:
        """
            Returns a reference to the underlying data array.
        
            Does not make a fresh copy of the underlying data.
        
            Returns:
                array of entries
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Returns the size of the vector.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.FieldVector.getDimension` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.FieldVector`
        
            Returns:
                size
        
        
        """
        ...
    def getEntry(self, int: int) -> _ArrayFieldVector__T:
        """
            Returns the entry in the specified index.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.FieldVector.getEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.FieldVector`
        
            Parameters:
                index (int): Index location of entry to be fetched.
        
            Returns:
                the vector entry at :code:`index`.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.FieldVector.setEntry`
        
        
        """
        ...
    def getField(self) -> fr.cnes.sirius.patrius.math.Field[_ArrayFieldVector__T]: ...
    def getSubVector(self, int: int, int2: int) -> FieldVector[_ArrayFieldVector__T]: ...
    def hashCode(self) -> int:
        """
            Get a hashCode for the real vector.
        
            All NaN values have the same hash code.
        
            Overrides:
                 in class 
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    def mapAdd(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapAddToSelf(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapDivide(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapDivideToSelf(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapInv(self) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapInvToSelf(self) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapMultiply(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapMultiplyToSelf(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapSubtract(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapSubtractToSelf(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    @typing.overload
    def outerProduct(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> 'FieldMatrix'[_ArrayFieldVector__T]: ...
    @typing.overload
    def outerProduct(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> 'FieldMatrix'[_ArrayFieldVector__T]: ...
    @typing.overload
    def projection(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> 'ArrayFieldVector'[_ArrayFieldVector__T]: ...
    @typing.overload
    def projection(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> FieldVector[_ArrayFieldVector__T]: ...
    @typing.overload
    def set(self, t: _ArrayFieldVector__T) -> None:
        """
            Set all elements to a single value.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.FieldVector.set` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.FieldVector`
        
            Parameters:
                value (:class:`~fr.cnes.sirius.patrius.math.linear.ArrayFieldVector`): single value to set for all elements
        
        
        """
        ...
    @typing.overload
    def set(self, int: int, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> None: ...
    def setEntry(self, int: int, t: _ArrayFieldVector__T) -> None:
        """
            Set a single element.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.FieldVector.setEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.FieldVector`
        
            Parameters:
                index (int): element index.
                value (:class:`~fr.cnes.sirius.patrius.math.linear.ArrayFieldVector`): new value for the element.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.FieldVector.getEntry`
        
        
        """
        ...
    def setSubVector(self, int: int, fieldVector: FieldVector[_ArrayFieldVector__T]) -> None: ...
    @typing.overload
    def subtract(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> 'ArrayFieldVector'[_ArrayFieldVector__T]: ...
    @typing.overload
    def subtract(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> FieldVector[_ArrayFieldVector__T]: ...
    def toArray(self) -> typing.MutableSequence[_ArrayFieldVector__T]:
        """
            Convert the vector to a T array.
        
            The array is independent from vector data, it's elements are copied.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.FieldVector.toArray` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.FieldVector`
        
            Returns:
                array containing a copy of vector elements
        
        
        """
        ...

class ArrayRealVector(RealVector, java.io.Serializable):
    """
    public class ArrayRealVector extends :class:`~fr.cnes.sirius.patrius.math.linear.RealVector` implements `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        This class implements the :class:`~fr.cnes.sirius.patrius.math.linear.RealVector` interface with a double array.
    
        This class is up-to-date with commons-math 3.6.1.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], boolean: bool): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], arrayRealVector: 'ArrayRealVector'): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int): ...
    @typing.overload
    def __init__(self, arrayRealVector: 'ArrayRealVector'): ...
    @typing.overload
    def __init__(self, arrayRealVector: 'ArrayRealVector', boolean: bool): ...
    @typing.overload
    def __init__(self, arrayRealVector: 'ArrayRealVector', doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, arrayRealVector: 'ArrayRealVector', arrayRealVector2: 'ArrayRealVector'): ...
    @typing.overload
    def __init__(self, arrayRealVector: 'ArrayRealVector', realVector: RealVector): ...
    @typing.overload
    def __init__(self, realVector: RealVector): ...
    @typing.overload
    def __init__(self, realVector: RealVector, arrayRealVector: 'ArrayRealVector'): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int): ...
    def add(self, realVector: RealVector) -> 'ArrayRealVector':
        """
            Compute the sum of this vector and :code:`v`. Returns a new vector. Does not change instance data.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.add` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector to be added.
        
            Returns:
                :code:`this` + :code:`v`.
        
        
        """
        ...
    def addToEntry(self, int: int, double: float) -> None:
        """
            Change an entry at the specified index.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.addToEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                index (int): Index location of entry to be set.
                increment (double): Value to add to the vector entry.
        
        
        """
        ...
    @typing.overload
    def append(self, arrayRealVector: 'ArrayRealVector') -> 'ArrayRealVector':
        """
            Construct a new vector by appending a vector to this vector.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.append` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): vector to append to this one.
        
            Returns:
                a new vector.
        
            Construct a vector by appending a vector to this vector.
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.ArrayRealVector`): Vector to append to this one.
        
            Returns:
                a new vector.
        
            Construct a new vector by appending a double to this vector.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.append` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                v (double): double to append.
        
            Returns:
                a new vector.
        
        
        """
        ...
    @typing.overload
    def append(self, double: float) -> RealVector: ...
    @typing.overload
    def append(self, realVector: RealVector) -> RealVector: ...
    def combine(self, double: float, double2: float, realVector: RealVector) -> 'ArrayRealVector':
        """
            Returns a new vector representing :code:`a * this + b * y`, the linear combination of :code:`this` and :code:`y`.
            Returns a new vector. Does not change instance data.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.combine` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                a (double): Coefficient of :code:`this`.
                b (double): Coefficient of :code:`y`.
                y (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector with which :code:`this` is linearly combined.
        
            Returns:
                a vector containing :code:`a * this[i] + b * y[i]` for all :code:`i`.
        
        
        """
        ...
    def combineToSelf(self, double: float, double2: float, realVector: RealVector) -> 'ArrayRealVector':
        """
            Updates :code:`this` with the linear combination of :code:`this` and :code:`y`.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.combineToSelf` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                a (double): Weight of :code:`this`.
                b (double): Weight of :code:`y`.
                y (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector with which :code:`this` is linearly combined.
        
            Returns:
                :code:`this`, with components equal to :code:`a * this[i] + b * y[i]` for all :code:`i`.
        
        
        """
        ...
    def copy(self) -> 'ArrayRealVector':
        """
            Returns a (deep) copy of this vector.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.copy` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Returns:
                a vector copy.
        
        
        """
        ...
    def dotProduct(self, realVector: RealVector) -> float:
        """
            Compute the dot product of this vector with :code:`v`.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.dotProduct` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector with which dot product should be computed
        
            Returns:
                the scalar dot product between this instance and :code:`v`.
        
        
        """
        ...
    def ebeDivide(self, realVector: RealVector) -> 'ArrayRealVector':
        """
            Element-by-element division.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.ebeDivide` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector by which instance elements must be divided.
        
            Returns:
                a vector containing this[i] / v[i] for all i.
        
        
        """
        ...
    def ebeMultiply(self, realVector: RealVector) -> 'ArrayRealVector':
        """
            Element-by-element multiplication.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.ebeMultiply` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector by which instance elements must be multiplied
        
            Returns:
                a vector containing this[i] * v[i] for all i.
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Test for the equality of two real vectors. If all coordinates of two real vectors are exactly the same, and none are
            :code:`NaN`, the two real vectors are considered to be equal. :code:`NaN` coordinates are considered to affect globally
            the vector and be equals to each other - i.e, if either (or all) coordinates of the real vector are equal to
            :code:`NaN`, the real vector is equal to a vector with all :code:`NaN` coordinates.
        
            This method *must* be overriden by concrete subclasses of :class:`~fr.cnes.sirius.patrius.math.linear.RealVector` (the
            current implementation throws an exception).
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.equals` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                other (`Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`): Object to test for equality.
        
            Returns:
                :code:`true` if two vector objects are equal, :code:`false` if :code:`other` is null, not an instance of
                :code:`RealVector`, or not equal to this :code:`RealVector` instance.
        
        
        """
        ...
    def getDataRef(self) -> typing.MutableSequence[float]:
        """
            Get a reference to the underlying data array. This method does not make a fresh copy of the underlying data.
        
            Returns:
                the array of entries.
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Returns the size of the vector.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getDimension` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Returns:
                the size of this vector.
        
        
        """
        ...
    def getDistance(self, realVector: RealVector) -> float:
        """
            Distance between two vectors.
        
            This method computes the distance consistent with the L :sub:`2` norm, i.e. the square root of the sum of element
            differences, or Euclidean distance.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getDistance` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector to which distance is requested.
        
            Returns:
                the distance between two vectors.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getL1Distance`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getLInfDistance`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getNorm`
        
        
        """
        ...
    def getEntry(self, int: int) -> float:
        """
            Return the entry at the specified index.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                index (int): Index location of entry to be fetched.
        
            Returns:
                the vector entry at :code:`index`.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.setEntry`
        
        
        """
        ...
    def getL1Distance(self, realVector: RealVector) -> float:
        """
            Distance between two vectors.
        
            This method computes the distance consistent with L :sub:`1` norm, i.e. the sum of the absolute values of the elements
            differences.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getL1Distance` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector to which distance is requested.
        
            Returns:
                the distance between two vectors.
        
        
        """
        ...
    def getL1Norm(self) -> float:
        """
            Returns the L :sub:`1` norm of the vector.
        
            The L :sub:`1` norm is the sum of the absolute values of the elements.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getL1Norm` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Returns:
                the norm.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getNorm`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getLInfNorm`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getL1Distance`
        
        
        """
        ...
    def getLInfDistance(self, realVector: RealVector) -> float:
        """
            Distance between two vectors.
        
            This method computes the distance consistent with L :sub:`∞` norm, i.e. the max of the absolute values of element
            differences.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getLInfDistance` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector to which distance is requested.
        
            Returns:
                the distance between two vectors.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getDistance`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getL1Distance`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getLInfNorm`
        
        
        """
        ...
    def getLInfNorm(self) -> float:
        """
            Returns the L :sub:`∞` norm of the vector.
        
            The L :sub:`∞` norm is the max of the absolute values of the elements.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getLInfNorm` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Returns:
                the norm.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getNorm`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getL1Norm`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getLInfDistance`
        
        
        """
        ...
    def getNorm(self) -> float:
        """
            Returns the L :sub:`2` norm of the vector.
        
            The L :sub:`2` norm is the root of the sum of the squared elements.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getNorm` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Returns:
                the norm.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getL1Norm`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getLInfNorm`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getDistance`
        
        
        """
        ...
    def getSubVector(self, int: int, int2: int) -> RealVector:
        """
            Get a subvector from consecutive elements.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getSubVector` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                index (int): index of first element.
                n (int): number of elements to be retrieved.
        
            Returns:
                a vector containing n elements.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            . This method *must* be overriden by concrete subclasses of :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
            (current implementation throws an exception). All :code:`NaN` values have the same hash code.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.hashCode` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
            Check whether any coordinate of this vector is infinite and none are :code:`NaN`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.isInfinite` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Returns:
                :code:`true` if any coordinate of this vector is infinite and none are :code:`NaN`, :code:`false` otherwise.
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
            Check if any coordinate of this vector is :code:`NaN`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.isNaN` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Returns:
                :code:`true` if any coordinate of this vector is :code:`NaN`, :code:`false` otherwise.
        
        
        """
        ...
    def map(self, univariateFunction: typing.Union[fr.cnes.sirius.patrius.math.analysis.UnivariateFunction, typing.Callable]) -> 'ArrayRealVector':
        """
            Acts as if implemented as:
        
            .. code-block: java
            
            
             return copy().mapToSelf(function);
             
            Returns a new vector. Does not change instance data.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.map` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                function (:class:`~fr.cnes.sirius.patrius.math.analysis.UnivariateFunction`): Function to apply to each entry.
        
            Returns:
                a new vector.
        
        
        """
        ...
    def mapAddToSelf(self, double: float) -> RealVector:
        """
            Add a value to each entry. The instance is changed in-place.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.mapAddToSelf` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                d (double): Value to be added to each entry.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def mapDivideToSelf(self, double: float) -> RealVector:
        """
            Divide each entry by the argument. The instance is changed in-place.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.mapDivideToSelf` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                d (double): Value to divide by.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def mapMultiplyToSelf(self, double: float) -> RealVector:
        """
            Multiply each entry. The instance is changed in-place.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.mapMultiplyToSelf` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                d (double): Multiplication factor.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def mapSubtractToSelf(self, double: float) -> RealVector:
        """
            Subtract a value from each entry. The instance is changed in-place.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.mapSubtractToSelf` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                d (double): Value to be subtracted.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def mapToSelf(self, univariateFunction: typing.Union[fr.cnes.sirius.patrius.math.analysis.UnivariateFunction, typing.Callable]) -> 'ArrayRealVector':
        """
            Acts as if it is implemented as:
        
            .. code-block: java
            
            
             Entry e = null;
             for (Iterator<Entry> it = iterator(); it.hasNext(); e = it.next()) {
                 e.setValue(function.value(e.getValue()));
             }
             
            Entries of this vector are modified in-place by this method.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.mapToSelf` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                function (:class:`~fr.cnes.sirius.patrius.math.analysis.UnivariateFunction`): Function to apply to each entry.
        
            Returns:
                a reference to this vector.
        
        
        """
        ...
    def outerProduct(self, realVector: RealVector) -> 'RealMatrix':
        """
            Compute the outer product.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.outerProduct` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector with which outer product should be computed.
        
            Returns:
                the matrix outer product between this instance and :code:`v`.
        
        
        """
        ...
    def set(self, double: float) -> None:
        """
            Set all elements to a single value.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.set` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                value (double): Single value to set for all elements.
        
        
        """
        ...
    def setEntry(self, int: int, double: float) -> None:
        """
            Set a single element.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.setEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                index (int): element index.
                value (double): new value for the element.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.getEntry`
        
        
        """
        ...
    @typing.overload
    def setSubVector(self, int: int, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Set a sequence of consecutive elements.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.setSubVector` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                index (int): index of first element to be set.
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): vector containing the values to set.
        
            Set a set of consecutive elements.
        
            Parameters:
                index (int): Index of first element to be set.
                v (double[]): Vector containing the values to set.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the index is inconsistent with the vector size.
        
        
        """
        ...
    @typing.overload
    def setSubVector(self, int: int, realVector: RealVector) -> None: ...
    def subtract(self, realVector: RealVector) -> 'ArrayRealVector':
        """
            Subtract :code:`v` from this vector. Returns a new vector. Does not change instance data.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.subtract` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): Vector to be subtracted.
        
            Returns:
                :code:`this` - :code:`v`.
        
        
        """
        ...
    def toArray(self) -> typing.MutableSequence[float]:
        """
            Convert the vector to an array of :code:`double`s. The array is independent from this vector data: the elements are
            copied.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.toArray` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Returns:
                an array containing a copy of the vector elements.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorChangingVisitor: RealVectorChangingVisitor) -> float:
        """
            Visits (but does not alter) all entries of this vector in default order (increasing index).
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.walkInDefaultOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealVectorPreservingVisitor`): the visitor to be used to process the entries of this vector
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorPreservingVisitor.end` at the end of the walk
        
            Visits (but does not alter) some entries of this vector in default order (increasing index).
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.walkInDefaultOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealVectorPreservingVisitor`): visitor to be used to process the entries of this vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorPreservingVisitor.end` at the end of the walk
        
            Visits (and possibly alters) all entries of this vector in default order (increasing index).
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.walkInDefaultOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealVectorChangingVisitor`): the visitor to be used to process and modify the entries of this vector
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorChangingVisitor.end` at the end of the walk
        
            Visits (and possibly alters) some entries of this vector in default order (increasing index).
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.walkInDefaultOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealVectorChangingVisitor`): visitor to be used to process the entries of this vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorChangingVisitor.end` at the end of the walk
        
        
        """
        ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorChangingVisitor: RealVectorChangingVisitor, int: int, int2: int) -> float: ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorPreservingVisitor: RealVectorPreservingVisitor) -> float: ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorPreservingVisitor: RealVectorPreservingVisitor, int: int, int2: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realVectorChangingVisitor: RealVectorChangingVisitor) -> float:
        """
            Visits (but does not alter) all entries of this vector in optimized order. The order in which the entries are visited is
            selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this
            abstract class. In this implementation, the optimized order is the default order.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.walkInOptimizedOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealVectorPreservingVisitor`): the visitor to be used to process the entries of this vector
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorPreservingVisitor.end` at the end of the walk
        
            Visits (but does not alter) some entries of this vector in optimized order. The order in which the entries are visited
            is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this
            abstract class. In this implementation, the optimized order is the default order.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.walkInOptimizedOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealVectorPreservingVisitor`): visitor to be used to process the entries of this vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorPreservingVisitor.end` at the end of the walk
        
            Visits (and possibly alters) all entries of this vector in optimized order. The order in which the entries are visited
            is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this
            abstract class. In this implementation, the optimized order is the default order.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.walkInOptimizedOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealVectorChangingVisitor`): the visitor to be used to process the entries of this vector
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorChangingVisitor.end` at the end of the walk
        
            Visits (and possibly change) some entries of this vector in optimized order. The order in which the entries are visited
            is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this
            abstract class. In this implementation, the optimized order is the default order.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealVector.walkInOptimizedOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealVector`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealVectorChangingVisitor`): visitor to be used to process the entries of this vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealVectorChangingVisitor.end` at the end of the walk
        
        
        """
        ...
    @typing.overload
    def walkInOptimizedOrder(self, realVectorChangingVisitor: RealVectorChangingVisitor, int: int, int2: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realVectorPreservingVisitor: RealVectorPreservingVisitor) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realVectorPreservingVisitor: RealVectorPreservingVisitor, int: int, int2: int) -> float: ...

class CholeskyDecomposition(Decomposition):
    DEFAULT_RELATIVE_SYMMETRY_THRESHOLD: typing.ClassVar[float] = ...
    DEFAULT_ABSOLUTE_POSITIVITY_THRESHOLD: typing.ClassVar[float] = ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float, double2: float): ...
    @staticmethod
    def decompositionBuilder(double: float, double2: float) -> java.util.function.Function['RealMatrix', Decomposition]: ...
    def getDeterminant(self) -> float: ...
    def getL(self) -> 'RealMatrix': ...
    def getLT(self) -> 'RealMatrix': ...
    def getSolver(self) -> DecompositionSolver: ...

_DefaultFieldMatrixChangingVisitor__T = typing.TypeVar('_DefaultFieldMatrixChangingVisitor__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
class DefaultFieldMatrixChangingVisitor(FieldMatrixChangingVisitor[_DefaultFieldMatrixChangingVisitor__T], typing.Generic[_DefaultFieldMatrixChangingVisitor__T]):
    """
    public class DefaultFieldMatrixChangingVisitor<T extends :class:`~fr.cnes.sirius.patrius.math.FieldElement`<T>> extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixChangingVisitor`<T>
    
        Default implementation of the :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixChangingVisitor` interface.
    
        This class is a convenience to create custom visitors without defining all methods. This class provides default
        implementations that do nothing.
    
        Since:
            2.0
    """
    def __init__(self, t: _DefaultFieldMatrixChangingVisitor__T): ...
    def end(self) -> _DefaultFieldMatrixChangingVisitor__T:
        """
            End visiting a matrix.
        
            This method is called once after all entries of the matrix have been visited.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixChangingVisitor.end` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixChangingVisitor`
        
            Returns:
                the value that the :code:`walkInXxxOrder` must return
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int) -> None:
        """
            Start visiting a matrix.
        
            This method is called once before any entry of the matrix is visited.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixChangingVisitor.start` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixChangingVisitor`
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, int: int, int2: int, t: _DefaultFieldMatrixChangingVisitor__T) -> _DefaultFieldMatrixChangingVisitor__T:
        """
            Visit one matrix entry.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixChangingVisitor.visit` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixChangingVisitor`
        
            Parameters:
                row (int): row index of the entry
                column (int): column index of the entry
                value (:class:`~fr.cnes.sirius.patrius.math.linear.DefaultFieldMatrixChangingVisitor`): current value of the entry
        
            Returns:
                the new value to be set for the entry
        
        
        """
        ...

_DefaultFieldMatrixPreservingVisitor__T = typing.TypeVar('_DefaultFieldMatrixPreservingVisitor__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
class DefaultFieldMatrixPreservingVisitor(FieldMatrixPreservingVisitor[_DefaultFieldMatrixPreservingVisitor__T], typing.Generic[_DefaultFieldMatrixPreservingVisitor__T]):
    """
    public class DefaultFieldMatrixPreservingVisitor<T extends :class:`~fr.cnes.sirius.patrius.math.FieldElement`<T>> extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixPreservingVisitor`<T>
    
        Default implementation of the :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixPreservingVisitor` interface.
    
        This class is a convenience to create custom visitors without defining all methods. This class provides default
        implementations that do nothing.
    
        Since:
            2.0
    """
    def __init__(self, t: _DefaultFieldMatrixPreservingVisitor__T): ...
    def end(self) -> _DefaultFieldMatrixPreservingVisitor__T:
        """
            End visiting a matrix.
        
            This method is called once after all entries of the matrix have been visited.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixPreservingVisitor.end` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixPreservingVisitor`
        
            Returns:
                the value that the :code:`walkInXxxOrder` must return
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int) -> None:
        """
            Start visiting a matrix.
        
            This method is called once before any entry of the matrix is visited.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixPreservingVisitor.start` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixPreservingVisitor`
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, int: int, int2: int, t: _DefaultFieldMatrixPreservingVisitor__T) -> None:
        """
            Visit one matrix entry.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixPreservingVisitor.visit` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.FieldMatrixPreservingVisitor`
        
            Parameters:
                row (int): row index of the entry
                column (int): column index of the entry
                value (:class:`~fr.cnes.sirius.patrius.math.linear.DefaultFieldMatrixPreservingVisitor`): current value of the entry
        
        
        """
        ...

class DefaultIterativeLinearSolverEvent(IterativeLinearSolverEvent):
    """
    public class DefaultIterativeLinearSolverEvent extends :class:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent`
    
        A default concrete implementation of the abstract class
        :class:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, object: typing.Any, int: int, realVector: RealVector, realVector2: RealVector, double: float): ...
    @typing.overload
    def __init__(self, object: typing.Any, int: int, realVector: RealVector, realVector2: RealVector, realVector3: RealVector, double: float): ...
    def getNormOfResidual(self) -> float:
        """
            Returns the norm of the residual. The returned value is not required to be *exact*. Instead, the norm of the so-called
            *updated* residual (if available) should be returned. For example, the
            :class:`~fr.cnes.sirius.patrius.math.linear.ConjugateGradient` method computes a sequence of residuals, the norm of
            which is cheap to compute. However, due to accumulation of round-off errors, this residual might differ from the true
            residual after some iterations. See e.g. A. Greenbaum and Z. Strakos, *Predicting the Behavior of Finite Precision
            Lanzos and Conjugate Gradient Computations*, Technical Report 538, Department of Computer Science, New York University,
            1991 (available `here <http://www.archive.org/details/predictingbehavi00gree>`).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent.getNormOfResidual` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent`
        
            Returns:
                the norm of the residual, ||r||
        
        
        """
        ...
    def getResidual(self) -> RealVector:
        """
        
            Returns the residual. This is an optional operation, as all iterative linear solvers do not provide cheap estimate of
            the updated residual vector, in which case
        
              - this method should throw a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`,
              - :meth:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent.providesResidual` returns :code:`false`.
        
        
            The default implementation throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`.
            If this method is overriden, then
            :meth:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent.providesResidual` should be overriden as well.
            This implementation throws an :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException` if no
            residual vector :code:`r` was provided at construction time.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent.getResidual` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent`
        
            Returns:
                the updated residual, r
        
        
        """
        ...
    def getRightHandSideVector(self) -> RealVector:
        """
            Returns the current right-hand side of the linear system to be solved. This method should return an unmodifiable view,
            or a deep copy of the actual right-hand side vector, in order not to compromise subsequent iterations of the source
            :class:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolver`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent.getRightHandSideVector` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent`
        
            Returns:
                the right-hand side vector, b
        
        
        """
        ...
    def getSolution(self) -> RealVector:
        """
            Returns the current estimate of the solution to the linear system to be solved. This method should return an
            unmodifiable view, or a deep copy of the actual current solution, in order not to compromise subsequent iterations of
            the source :class:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolver`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent.getSolution` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent`
        
            Returns:
                the solution, x
        
        
        """
        ...
    def providesResidual(self) -> bool:
        """
            Returns :code:`true` if :meth:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent.getResidual` is supported.
            The default implementation returns :code:`false`. This implementation returns :code:`true` if a non-:code:`null` value
            was specified for the residual vector :code:`r` at construction time.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent.providesResidual` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolverEvent`
        
            Returns:
                :code:`true` if :code:`r != null`
        
        
        """
        ...

class DefaultRealMatrixChangingVisitor(RealMatrixChangingVisitor):
    """
    public class DefaultRealMatrixChangingVisitor extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`
    
        Default implementation of the :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor` interface.
    
        This class is a convenience to create custom visitors without defining all methods. This class provides default
        implementations that do nothing.
    
        Since:
            2.0
    """
    def __init__(self): ...
    def end(self) -> float:
        """
            End visiting a matrix.
        
            This method is called once after all entries of the matrix have been visited.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`
        
            Returns:
                the value that the :code:`walkInXxxOrder` must return
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int) -> None:
        """
            Start visiting a matrix.
        
            This method is called once before any entry of the matrix is visited.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.start` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, int: int, int2: int, double: float) -> float:
        """
            Visit one matrix entry.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.visit` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`
        
            Parameters:
                row (int): row index of the entry
                column (int): column index of the entry
                value (double): current value of the entry
        
            Returns:
                the new value to be set for the entry
        
        
        """
        ...

class DefaultRealMatrixPreservingVisitor(RealMatrixPreservingVisitor):
    """
    public class DefaultRealMatrixPreservingVisitor extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`
    
        Default implementation of the :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor` interface.
    
        This class is a convenience to create custom visitors without defining all methods. This class provides default
        implementations that do nothing.
    
        Since:
            2.0
    """
    def __init__(self): ...
    def end(self) -> float:
        """
            End visiting a matrix.
        
            This method is called once after all entries of the matrix have been visited.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`
        
            Returns:
                the value that the :code:`walkInXxxOrder` must return
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int) -> None:
        """
            Start visiting a matrix.
        
            This method is called once before any entry of the matrix is visited.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.start` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, int: int, int2: int, double: float) -> None:
        """
            Visit one matrix entry.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.visit` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`
        
            Parameters:
                row (int): row index of the entry
                column (int): column index of the entry
                value (double): current value of the entry
        
        
        """
        ...

class EigenDecomposition(Decomposition):
    """
    public class EigenDecomposition extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`
    
        Calculates the eigen decomposition of a real matrix.
    
        The eigen decomposition of matrix A is a set of two matrices: V and D such that A = V × D × V :sup:`-1` . Where A, V
        and D are all m × m matrices.
    
        This class is similar in spirit to the :code:`EigenvalueDecomposition` class from the `JAMA
        <http://math.nist.gov/javanumerics/jama/>` library, with the following changes:
    
          - a :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getVT` method has been added,
          - two :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getRealEigenvalue` and
            :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getImagEigenvalue` methods to pick up a single eigenvalue
            have been added,
          - a :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getEigenvector` method to pick up a single eigenvector
            has been added,
          - a :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getDeterminant` method has been added.
          - a :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getSolver` method has been added.
    
    
        As of 3.1, this class supports general real matrices (both symmetric and non-symmetric):
    
        If A is symmetric, then A = V × D × V :sup:`T` where the eigenvalue matrix D is a diagonal of real values and the
        eigenvector matrix V is orthogonal (i.e. V × V :sup:`T` = V :sup:`T` × V = Id).
    
        If A is not symmetric, then the eigenvalue matrix D is block diagonal with the real eigenvalues in 1-by-1 blocks and any
        complex eigenvalues, lambda + i*mu, in 2-by-2 blocks:
    
        .. code-block: java
        
        
            [lambda, mu    ]
            [   -mu, lambda]
         
        The columns of V represent the eigenvectors in the sense that A*V = V*D. The matrix V may be badly conditioned, or even
        singular, so the validity of the equation A = V × D × V :sup:`-1` depends upon the condition of V.
    
        This implementation is based on the paper by A. Drubrulle, R.S. Martin and J.H. Wilkinson "The Implicit QL Algorithm" in
        Wilksinson and Reinsch (1971) Handbook for automatic computation, vol. 2, Linear algebra, Springer-Verlag, New-York
    
        Since:
            2.0 (changed to concrete class in 3.0)
    
        Also see:
            `MathWorld <http://mathworld.wolfram.com/EigenDecomposition.html>`, `Wikipedia
            <http://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix>`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float): ...
    @staticmethod
    def decompositionBuilder(double: float) -> java.util.function.Function['RealMatrix', Decomposition]: ...
    def getD(self) -> 'RealMatrix':
        """
            Gets the block diagonal matrix D of the decomposition. D is a block diagonal matrix. Real eigenvalues are on the
            diagonal while complex values are on 2x2 blocks { {real +imaginary}, {-imaginary, real} }.
        
            Returns:
                the D matrix.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getRealEigenvalues`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getImagEigenvalues`
        
        
        """
        ...
    def getDeterminant(self) -> float:
        """
            Computes the determinant of the matrix.
        
            Returns:
                the determinant of the matrix.
        
        
        """
        ...
    def getEigenvector(self, int: int) -> RealVector:
        """
            Gets a copy of the i :sup:`th` eigenvector of the original matrix.
        
            Parameters:
                i (int): Index of the eigenvector (counting from 0).
        
            Returns:
                a copy of the i :sup:`th` eigenvector of the original matrix.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getD`
        
        
        """
        ...
    def getImagEigenvalue(self, int: int) -> float:
        """
            Gets the imaginary part of the i :sup:`th` eigenvalue of the original matrix.
        
            Parameters:
                i (int): Index of the eigenvalue (counting from 0).
        
            Returns:
                the imaginary part of the i :sup:`th` eigenvalue of the original matrix.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getD`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getImagEigenvalues`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getRealEigenvalue`
        
        
        """
        ...
    def getImagEigenvalues(self) -> typing.MutableSequence[float]:
        """
            Gets a copy of the imaginary parts of the eigenvalues of the original matrix.
        
            Returns:
                a copy of the imaginary parts of the eigenvalues of the original matrix.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getD`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getImagEigenvalue`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getRealEigenvalues`
        
        
        """
        ...
    def getRealEigenvalue(self, int: int) -> float:
        """
            Returns the real part of the i :sup:`th` eigenvalue of the original matrix.
        
            Parameters:
                i (int): index of the eigenvalue (counting from 0)
        
            Returns:
                real part of the i :sup:`th` eigenvalue of the original matrix.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getD`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getRealEigenvalues`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getImagEigenvalue`
        
        
        """
        ...
    def getRealEigenvalues(self) -> typing.MutableSequence[float]:
        """
            Gets a copy of the real parts of the eigenvalues of the original matrix.
        
            Returns:
                a copy of the real parts of the eigenvalues of the original matrix.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getD`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getRealEigenvalue`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getImagEigenvalues`
        
        
        """
        ...
    def getSolver(self) -> DecompositionSolver:
        """
            Gets a solver for finding the A × X = B solution in exact linear sense.
        
            Since 3.1, eigen decomposition of a general matrix is supported, but the
            :class:`~fr.cnes.sirius.patrius.math.linear.DecompositionSolver` only supports real eigenvalues.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.Decomposition.getSolver` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`
        
            Returns:
                a solver
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: if the matrix is not symmetric
        
        
        """
        ...
    def getSquareRoot(self) -> 'RealMatrix':
        """
            Computes the square-root of the matrix. This implementation assumes that the matrix is symmetric and positive definite.
        
            Returns:
                the square-root of the matrix.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: if the matrix is not symmetric or not positive definite.
        
            Since:
                3.1
        
        
        """
        ...
    def getV(self) -> 'RealMatrix':
        """
            Gets the matrix V of the decomposition. The columns of V are the eigenvectors of the original matrix. No assumption is
            made about the orientation of the system axes formed by the columns of V (e.g. in a 3-dimension space, V can form a
            left- or right-handed system).
        
            Returns:
                the V matrix.
        
        
        """
        ...
    def getVT(self) -> 'RealMatrix':
        """
            Gets the transpose of the matrix V of the decomposition. The columns of V are the eigenvectors of the original matrix.
            No assumption is made about the orientation of the system axes formed by the columns of V (e.g. in a 3-dimension space,
            V can form a left- or right-handed system).
        
            Returns:
                the transpose of the V matrix.
        
        
        """
        ...
    def hasComplexEigenvalues(self) -> bool:
        """
            Returns whether the calculated eigen values are complex or real.
        
            The method performs a zero check for each element of the
            :meth:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition.getImagEigenvalues` array and returns :code:`true` if any
            element is not equal to zero.
        
            Returns:
                :code:`true` if the eigen values are complex, :code:`false` otherwise
        
            Since:
                3.1
        
        
        """
        ...
    def isSymmetric(self) -> bool:
        """
            Method returning the value of the private global parameter isSymmetric. If the methods returns true, it means that the
            decomposition method used is Dubrulle et al.(1971)'s. If the methods returns false, it means that the decomposition
            method used is the matrix transformation to a Shur form.
        
            Returns:
                the value of the boolean private global parameter isSymmetric.
        
            Since:
                4.5
        
        
        """
        ...

_FieldMatrix__T = typing.TypeVar('_FieldMatrix__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
class FieldMatrix(AnyMatrix, typing.Generic[_FieldMatrix__T]):
    def add(self, fieldMatrix: 'FieldMatrix'[_FieldMatrix__T]) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def addToEntry(self, int: int, int2: int, t: _FieldMatrix__T) -> None: ...
    def copy(self) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    @typing.overload
    def copySubMatrix(self, int: int, int2: int, int3: int, int4: int, tArray: typing.Union[typing.List[typing.MutableSequence[_FieldMatrix__T]], jpype.JArray]) -> None: ...
    @typing.overload
    def copySubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray], tArray: typing.Union[typing.List[typing.MutableSequence[_FieldMatrix__T]], jpype.JArray]) -> None: ...
    def createMatrix(self, int: int, int2: int) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def getColumn(self, int: int) -> typing.MutableSequence[_FieldMatrix__T]: ...
    def getColumnMatrix(self, int: int) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def getColumnVector(self, int: int) -> FieldVector[_FieldMatrix__T]: ...
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[_FieldMatrix__T]]: ...
    def getEntry(self, int: int, int2: int) -> _FieldMatrix__T: ...
    def getField(self) -> fr.cnes.sirius.patrius.math.Field[_FieldMatrix__T]: ...
    def getRow(self, int: int) -> typing.MutableSequence[_FieldMatrix__T]: ...
    def getRowMatrix(self, int: int) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def getRowVector(self, int: int) -> FieldVector[_FieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def getTrace(self) -> _FieldMatrix__T: ...
    def multiply(self, fieldMatrix: 'FieldMatrix'[_FieldMatrix__T]) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def multiplyEntry(self, int: int, int2: int, t: _FieldMatrix__T) -> None: ...
    @typing.overload
    def operate(self, tArray: typing.Union[typing.List[_FieldMatrix__T], jpype.JArray]) -> typing.MutableSequence[_FieldMatrix__T]: ...
    @typing.overload
    def operate(self, fieldVector: FieldVector[_FieldMatrix__T]) -> FieldVector[_FieldMatrix__T]: ...
    def power(self, int: int) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, tArray: typing.Union[typing.List[_FieldMatrix__T], jpype.JArray]) -> typing.MutableSequence[_FieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldMatrix: 'FieldMatrix'[_FieldMatrix__T]) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldVector: FieldVector[_FieldMatrix__T]) -> FieldVector[_FieldMatrix__T]: ...
    def scalarAdd(self, t: _FieldMatrix__T) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def scalarMultiply(self, t: _FieldMatrix__T) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def setColumn(self, int: int, tArray: typing.Union[typing.List[_FieldMatrix__T], jpype.JArray]) -> None: ...
    def setColumnMatrix(self, int: int, fieldMatrix: 'FieldMatrix'[_FieldMatrix__T]) -> None: ...
    def setColumnVector(self, int: int, fieldVector: FieldVector[_FieldMatrix__T]) -> None: ...
    def setEntry(self, int: int, int2: int, t: _FieldMatrix__T) -> None: ...
    def setRow(self, int: int, tArray: typing.Union[typing.List[_FieldMatrix__T], jpype.JArray]) -> None: ...
    def setRowMatrix(self, int: int, fieldMatrix: 'FieldMatrix'[_FieldMatrix__T]) -> None: ...
    def setRowVector(self, int: int, fieldVector: FieldVector[_FieldMatrix__T]) -> None: ...
    def setSubMatrix(self, tArray: typing.Union[typing.List[typing.MutableSequence[_FieldMatrix__T]], jpype.JArray], int: int, int2: int) -> None: ...
    def subtract(self, fieldMatrix: 'FieldMatrix'[_FieldMatrix__T]) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def transpose(self) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_FieldMatrix__T]) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_FieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_FieldMatrix__T]) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_FieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_FieldMatrix__T]) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_FieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_FieldMatrix__T]) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_FieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_FieldMatrix__T]) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_FieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_FieldMatrix__T]) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_FieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _FieldMatrix__T: ...

class JacobiPreconditioner(RealLinearOperator):
    """
    public class JacobiPreconditioner extends :class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`
    
        This class implements the standard Jacobi (diagonal) preconditioner. For a matrix A :sub:`ij` , this preconditioner is M
        = diag(1 / A :sub:`11` , 1 / A :sub:`22` , …).
    
        Since:
            3.0
    """
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], boolean: bool): ...
    @staticmethod
    def create(realLinearOperator: RealLinearOperator) -> 'JacobiPreconditioner':
        """
            Creates a new instance of this class. This method extracts the diagonal coefficients of the specified linear operator.
            If :code:`a` does not extend :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`, then the coefficients of
            the underlying matrix are not accessible, coefficient extraction is made by matrix-vector products with the basis
            vectors (and might therefore take some time). With matrices, direct entry access is carried out.
        
            Parameters:
                a (:class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`): the linear operator for which the preconditioner should be built
        
            Returns:
                the diagonal preconditioner made of the inverse of the diagonal coefficients of the specified linear operator
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.NonSquareOperatorException`: if :code:`a` is not square
        
        
        """
        ...
    def getColumnDimension(self) -> int:
        """
            Returns the dimension of the domain of this operator.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator.getColumnDimension` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`
        
            Returns:
                the number of columns of the underlying matrix
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
            Returns the dimension of the codomain of this operator.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator.getRowDimension` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`
        
            Returns:
                the number of rows of the underlying matrix
        
        
        """
        ...
    def operate(self, realVector: RealVector) -> RealVector:
        """
            Returns the result of multiplying :code:`this` by the vector :code:`x`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator.operate` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`
        
            Parameters:
                x (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the vector to operate on
        
            Returns:
                the product of :code:`this` instance with :code:`x`
        
        
        """
        ...
    def sqrt(self) -> RealLinearOperator:
        """
            Returns the square root of :code:`this` diagonal operator. More precisely, this method returns P = diag(1 / √A
            :sub:`11` , 1 / √A :sub:`22` , …).
        
            Returns:
                the square root of :code:`this` preconditioner
        
            Since:
                3.1
        
        
        """
        ...

class LUDecomposition(Decomposition):
    """
    public class LUDecomposition extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`
    
        Calculates the LUP-decomposition of a square matrix.
    
        The LUP-decomposition of a matrix A consists of three matrices L, U and P that satisfy: P×A = L×U. L is lower
        triangular (with unit diagonal terms), U is upper triangular and P is a permutation matrix. All matrices are m×m.
    
        As shown by the presence of the P matrix, this decomposition is implemented using partial pivoting.
    
        This class is based on the class with similar name from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library.
    
          - a :meth:`~fr.cnes.sirius.patrius.math.linear.LUDecomposition.getP` method has been added,
          - the :code:`det` method has been renamed as :meth:`~fr.cnes.sirius.patrius.math.linear.LUDecomposition.getDeterminant`,
          - the :code:`getDoublePivot` method has been removed (but the int based
            :meth:`~fr.cnes.sirius.patrius.math.linear.LUDecomposition.getPivot` method has been kept),
          - the :code:`solve` and :code:`isNonSingular` methods have been replaced by a
            :meth:`~fr.cnes.sirius.patrius.math.linear.LUDecomposition.getSolver` method and the equivalent methods provided by the
            returned :class:`~fr.cnes.sirius.patrius.math.linear.DecompositionSolver`.
    
    
        Since:
            2.0 (changed to concrete class in 3.0)
    
        Also see:
            `MathWorld <http://mathworld.wolfram.com/LUDecomposition.html>`, `Wikipedia
            <http://en.wikipedia.org/wiki/LU_decomposition>`
    """
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float): ...
    @staticmethod
    def decompositionBuilder(double: float) -> java.util.function.Function['RealMatrix', Decomposition]: ...
    def getDeterminant(self) -> float:
        """
            Return the determinant of the matrix
        
            Returns:
                determinant of the matrix
        
        
        """
        ...
    def getL(self) -> 'RealMatrix':
        """
            Returns the matrix L of the decomposition.
        
            L is a lower-triangular matrix
        
            Returns:
                the L matrix (or null if decomposed matrix is singular)
        
        
        """
        ...
    def getP(self) -> 'RealMatrix':
        """
            Returns the P rows permutation matrix.
        
            P is a sparse matrix with exactly one element set to 1.0 in each row and each column, all other elements being set to
            0.0.
        
            The positions of the 1 elements are given by the :meth:`~fr.cnes.sirius.patrius.math.linear.LUDecomposition.getPivot`.
        
            Returns:
                the P rows permutation matrix (or null if decomposed matrix is singular)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.LUDecomposition.getPivot`
        
        
        """
        ...
    def getPivot(self) -> typing.MutableSequence[int]:
        """
            Returns the pivot permutation vector.
        
            Returns:
                the pivot permutation vector
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.LUDecomposition.getP`
        
        
        """
        ...
    def getSolver(self) -> DecompositionSolver:
        """
            Gets a solver for finding the A × X = B solution in exact linear sense.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.Decomposition.getSolver` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`
        
            Returns:
                the decomposition solver.
        
        
        """
        ...
    def getU(self) -> 'RealMatrix':
        """
            Returns the matrix U of the decomposition.
        
            U is an upper-triangular matrix
        
            Returns:
                the U matrix (or null if decomposed matrix is singular)
        
        
        """
        ...

class PreconditionedIterativeLinearSolver(IterativeLinearSolver):
    """
    public abstract class PreconditionedIterativeLinearSolver extends :class:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolver`
    
    
        This abstract class defines preconditioned iterative solvers. When A is ill-conditioned, instead of solving system A ·
        x = b directly, it is preferable to solve either
        (M · A) · x = M · b
        (left preconditioning), or
        (A · M) · y = b,     followed by M · y = x
        (right preconditioning), where M approximates in some way A :sup:`-1` , while matrix-vector products of the type M · y
        remain comparatively easy to compute. In this library, M (not M :sup:`-1` !) is called the *preconditionner*.
    
        Concrete implementations of this abstract class must be provided with the preconditioner M, as a
        :class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`.
    
        Since:
            3.0
    """
    @typing.overload
    def __init__(self, iterationManager: fr.cnes.sirius.patrius.math.util.IterationManager): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector) -> RealVector:
        """
            Returns an estimate of the solution to the linear system A · x = b.
        
            Parameters:
                a (:class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`): the linear operator A of the system
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`): the preconditioner, M (can be :code:`null`)
                b (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the right-hand side vector
                x0 (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the initial guess of the solution
        
            Returns:
                a new vector containing the solution
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if one of the parameters is :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.linear.NonSquareOperatorException`: if :code:`a` or :code:`m` is not square
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`m`, :code:`b` or :code:`x0` have dimensions inconsistent with :code:`a`
                :class:`~fr.cnes.sirius.patrius.math.exception.MaxCountExceededException`: at exhaustion of the iteration count, unless a custom
                    :class:`~fr.cnes.sirius.patrius.math.util.Incrementor.MaxCountExceededCallback` has been set at construction of the
                    :class:`~fr.cnes.sirius.patrius.math.util.IterationManager`
        
            Returns an estimate of the solution to the linear system A · x = b.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolver.solve` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolver`
        
            Parameters:
                a (:class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`): the linear operator A of the system
                b (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the right-hand side vector
                x0 (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the initial guess of the solution
        
            Returns:
                a new vector containing the solution
        
            Returns an estimate of the solution to the linear system A · x = b.
        
            Parameters:
                a (:class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`): the linear operator A of the system
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`): the preconditioner, M (can be :code:`null`)
                b (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the right-hand side vector
        
            Returns:
                a new vector containing the solution
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if one of the parameters is :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.linear.NonSquareOperatorException`: if :code:`a` or :code:`m` is not square
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`m` or :code:`b` have dimensions inconsistent with :code:`a`
                :class:`~fr.cnes.sirius.patrius.math.exception.MaxCountExceededException`: at exhaustion of the iteration count, unless a custom
                    :class:`~fr.cnes.sirius.patrius.math.util.Incrementor.MaxCountExceededCallback` has been set at construction of the
                    :class:`~fr.cnes.sirius.patrius.math.util.IterationManager`
        
        
        """
        ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realVector: RealVector) -> RealVector:
        """
            Returns an estimate of the solution to the linear system A · x = b.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolver.solve` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolver`
        
            Parameters:
                a (:class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`): the linear operator A of the system
                b (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the right-hand side vector
        
            Returns:
                a new vector containing the solution
        
        """
        ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...
    @typing.overload
    def solveInPlace(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector:
        """
            Returns an estimate of the solution to the linear system A · x = b. The solution is computed in-place (initial guess is
            modified).
        
            Parameters:
                a (:class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`): the linear operator A of the system
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`): the preconditioner, M (can be :code:`null`)
                b (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the right-hand side vector
                x0 (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the initial guess of the solution
        
            Returns:
                a reference to :code:`x0` (shallow copy) updated with the solution
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if one of the parameters is :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.linear.NonSquareOperatorException`: if :code:`a` or :code:`m` is not square
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`m`, :code:`b` or :code:`x0` have dimensions inconsistent with :code:`a`
                :class:`~fr.cnes.sirius.patrius.math.exception.MaxCountExceededException`: at exhaustion of the iteration count, unless a custom
                    :class:`~fr.cnes.sirius.patrius.math.util.Incrementor.MaxCountExceededCallback` has been set at construction of the
                    :class:`~fr.cnes.sirius.patrius.math.util.IterationManager`
        
        """
        ...
    @typing.overload
    def solveInPlace(self, realLinearOperator: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector:
        """
            Returns an estimate of the solution to the linear system A · x = b. The solution is computed in-place (initial guess is
            modified).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolver.solveInPlace` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.IterativeLinearSolver`
        
            Parameters:
                a (:class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`): the linear operator A of the system
                b (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the right-hand side vector
                x0 (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): initial guess of the solution
        
            Returns:
                a reference to :code:`x0` (shallow copy) updated with the solution
        
        
        """
        ...

class QRDecomposition(Decomposition):
    """
    public class QRDecomposition extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`
    
        Calculates the QR-decomposition of a matrix.
    
        The QR-decomposition of a matrix A consists of two matrices Q and R that satisfy: A = QR, Q is orthogonal (Q :sup:`T` Q
        = I), and R is upper triangular. If A is m×n, Q is m×m and R m×n.
    
        This class compute the decomposition using Householder reflectors.
    
        For efficiency purposes, the decomposition in packed form is transposed. This allows inner loop to iterate inside rows,
        which is much more cache-efficient in Java.
    
        This class is based on the class with similar name from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library,
        with the following changes:
    
          - a :meth:`~fr.cnes.sirius.patrius.math.linear.QRDecomposition.getQT` method has been added,
          - the :code:`solve` and :code:`isFullRank` methods have been replaced by a
            :meth:`~fr.cnes.sirius.patrius.math.linear.QRDecomposition.getSolver` method and the equivalent methods provided by the
            returned :class:`~fr.cnes.sirius.patrius.math.linear.DecompositionSolver`.
    
    
        This class is up-to-date with commons-math 3.6.1.
    
        Since:
            1.2 (changed to concrete class in 3.0)
    
        Also see:
            `MathWorld <http://mathworld.wolfram.com/QRDecomposition.html>`, `Wikipedia
            <http://en.wikipedia.org/wiki/QR_decomposition>`
    """
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float, boolean: bool): ...
    @typing.overload
    @staticmethod
    def decompositionBuilder(double: float) -> java.util.function.Function['RealMatrix', Decomposition]: ...
    @typing.overload
    @staticmethod
    def decompositionBuilder(double: float, boolean: bool) -> java.util.function.Function['RealMatrix', Decomposition]: ...
    def getH(self) -> 'RealMatrix':
        """
            Returns the Householder reflector vectors.
        
            H is a lower trapezoidal matrix whose columns represent each successive Householder reflector vector. This matrix is
            used to compute Q.
        
            Returns:
                a matrix containing the Householder reflector vectors
        
        
        """
        ...
    def getQ(self) -> 'RealMatrix':
        """
            Returns the matrix Q of the decomposition.
        
            Q is an orthogonal matrix
        
            Returns:
                the Q matrix
        
        
        """
        ...
    def getQT(self) -> 'RealMatrix':
        """
            Returns the transpose of the matrix Q of the decomposition.
        
            Q is an orthogonal matrix
        
            Returns:
                the transpose of the Q matrix, Q :sup:`T`
        
        
        """
        ...
    @typing.overload
    def getR(self) -> 'RealMatrix':
        """
            Returns the matrix R of the decomposition. By default, this method returns the full form (n &times; m) of the matrix R.
        
            R is an upper-triangular matrix
        
            Returns:
                the R matrix
        
        """
        ...
    @typing.overload
    def getR(self, boolean: bool) -> 'RealMatrix':
        """
            Returns the matrix R of the decomposition in its compact form (n &times; n) or in its full form (m &times; n).
        
            R is an upper-triangular matrix
        
            Parameters:
                compactForm (boolean): if :code:`true` R dimensions will be n &times; n, else R dimensions will be m &times; n
        
            Returns:
                the R matrix
        
        
        """
        ...
    def getSolver(self) -> DecompositionSolver:
        """
            Gets a solver for finding the A × X = B solution in exact linear sense. Get a solver for finding the A × X = B
            solution in least square sense.
        
            Least Square sense means a solver can be computed for an overdetermined system, (i.e. a system with more equations than
            unknowns, which corresponds to a tall A matrix with more rows than columns). In any case, if the matrix is singular
            within the tolerance set at :meth:`~fr.cnes.sirius.patrius.math.linear.QRDecomposition.QRDecomposition`, an error will
            be triggered when the :meth:`~fr.cnes.sirius.patrius.math.linear.DecompositionSolver.solve` method will be called.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.Decomposition.getSolver` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`
        
            Returns:
                a solver
        
        
        """
        ...

class RealMatrix(AnyMatrix, java.io.Serializable):
    """
    public interface RealMatrix extends :class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`, `Serializable <http://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Interface defining a real-valued matrix with basic algebraic operations.
    
        Matrix element indexing is 0-based -- e.g., :code:`getEntry(0, 0)` returns the element in the first row, first column of
        the matrix.
    """
    def add(self, realMatrix: 'RealMatrix') -> 'RealMatrix':
        """
            Returns the result of adding the matrix :code:`m` to this matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be added
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`m`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the matrix M is not the same size as this matrix
        
        
        """
        ...
    def addToEntry(self, int: int, int2: int, double: float) -> None:
        """
            Adds (in place) a given value to the specified entry of this matrix.
        
            Row and column indices start at 0.
        
            Parameters:
                row (int): the row index of the entry to be modified
                column (int): the column index of the entry to be modified
                increment (double): the value to add to the matrix entry
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the row or column index is not valid
        
            Since:
                2.0
        
        
        """
        ...
    @typing.overload
    def concatenateDiagonally(self, realMatrix: 'RealMatrix') -> 'RealMatrix':
        """
            Diagonally concatenates this matrix and another matrix :code:`m`, placing it in the lower right part of the concatenated
            matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
        
            Returns:
                the concatenated matrix
        
            Diagonally concatenates this matrix and another matrix :code:`m`, placing it in the lower right or upper left part of
            the concatenated matrix.
        
            The way the two matrices are concatenated depends on the provided argument:
        
        
            The matrix :code:`m` is placed in the lower right part of the concatenated matrix if :code:`lowerRightConcatenation` is
            set to :code:`true`, and in its upper left part if it is set to :code:`false`.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             this.concatenateDiagonally(m, true)  => [this, 0] 
                                                     [   0, m]
                
             this.concatenateDiagonally(m, false) => [m,    0]
                                                     [0, this]
             
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
                lowerRightConcatenation (boolean): whether the matrix :code:`m` is to be placed in the lower right (:code:`true`) or upper left (:code:`false`) part of the
                    concatenated matrix
        
            Returns:
                the concatenated matrix
        
            Diagonally or anti-diagonally concatenates this matrix and another matrix :code:`m`.
        
            The way the two matrices are concatenated depends on the provided arguments:
        
        
            The matrix :code:`m` is placed in the right part of the concatenated matrix if :code:`rightConcatenation` is set to
            :code:`true`, and in its left part if it is set to :code:`false`. Similarly, the matrix :code:`m` is placed in the lower
            part of the concatenated matrix if :code:`lowerConcatenation` is set to :code:`true`, and in its upper part if it is set
            to :code:`false`. This matrix is then placed in the opposite part of the concatenated matrix (as an example, if the
            provided matrix is placed in the upper left part, this matrix will be placed in the lower right part, the remaining
            parts being filled with zeros).
        
            **Usage examples:**
        
            .. code-block: java
            
            
             // Diagonal concatenation
             this.concatenateDiagonally(m, true, true)   => [this, 0] 
                                                            [   0, m]
                                                          
             this.concatenateDiagonally(m, false, false) => [m,    0]
                                                            [0, this]
                                      
             // Anti-diagonal concatenation
             this.concatenateDiagonally(m, false, true)  => [0, this]
                                                            [m,    0]
                                                           
             this.concatenateDiagonally(m, true, false)  => [   0, m]
                                                            [this, 0]
             
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
                rightConcatenation (boolean): whether the matrix :code:`m` is to be placed in the right (:code:`true`) or left ( :code:`false`) part of the
                    concatenated matrix
                lowerConcatenation (boolean): whether the matrix :code:`m` is to be placed in the lower (:code:`true`) or upper ( :code:`false`) part of the
                    concatenated matrix
        
            Returns:
                the concatenated matrix
        
        
        """
        ...
    @typing.overload
    def concatenateDiagonally(self, realMatrix: 'RealMatrix', boolean: bool) -> 'RealMatrix': ...
    @typing.overload
    def concatenateDiagonally(self, realMatrix: 'RealMatrix', boolean: bool, boolean2: bool) -> 'RealMatrix': ...
    @typing.overload
    def concatenateHorizontally(self, realMatrix: 'RealMatrix') -> 'RealMatrix':
        """
            Horizontally concatenates this matrix and another matrix :code:`m`, placing it in the right part of the concatenated
            matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
        
            Returns:
                the concatenated matrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the matrices have different row dimensions
        
            Horizontally concatenates this matrix and another matrix :code:`m`, , placing it in the left or right part of the
            concatenated matrix.
        
            The way the two matrices are concatenated depends on the provided argument:
        
        
            The matrix :code:`m` is placed in the right part of the concatenated matrix if :code:`rightConcatenation` is set to
            :code:`true`, and in its left part if it is set to :code:`false`.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             this.concatenateHorizontally(m, true)  => [this, m] 
             
             this.concatenateHorizontally(m, false) => [m, this]
             
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
                rightConcatenation (boolean): whether the matrix :code:`m` is to be placed in the right (:code:`true`) or left ( :code:`false`) part of the
                    concatenated matrix
        
            Returns:
                the concatenated matrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the matrices have different row dimensions
        
        
        """
        ...
    @typing.overload
    def concatenateHorizontally(self, realMatrix: 'RealMatrix', boolean: bool) -> 'RealMatrix': ...
    @typing.overload
    def concatenateVertically(self, realMatrix: 'RealMatrix') -> 'RealMatrix':
        """
            Vertically concatenates this matrix and another matrix :code:`m`, placing it in the lower part of the concatenated
            matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
        
            Returns:
                the concatenated matrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the matrices have different column dimensions
        
            Vertically concatenates this matrix and another matrix :code:`m`, placing it in the lower or upper part of the
            concatenated matrix.
        
            The way the two matrices are concatenated depends on the provided argument:
        
        
            The matrix :code:`m` is placed in the lower part of the concatenated matrix if :code:`lowerConcatenation` is set to
            :code:`true`, and in its upper part if it is set to :code:`false`.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             this.concatenateVertically(m, true)  => [this] 
                                                     [   m]
                                                          
             this.concatenateVertically(m, false) => [   m]
                                                     [this]
             
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
                lowerConcatenation (boolean): whether the matrix :code:`m` is to be placed in the lower (:code:`true`) or upper ( :code:`false`) part of the
                    concatenated matrix
        
            Returns:
                the concatenated matrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the matrices have different row dimensions
        
        
        """
        ...
    @typing.overload
    def concatenateVertically(self, realMatrix: 'RealMatrix', boolean: bool) -> 'RealMatrix': ...
    def copy(self) -> 'RealMatrix':
        """
            Returns a deep copy of this matrix.
        
            Returns:
                a deep copy of this matrix
        
        
        """
        ...
    @typing.overload
    def copySubMatrix(self, int: int, int2: int, int3: int, int4: int, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None:
        """
            Copies a submatrix into a given 2D array.
        
            Rows and columns are indicated counting from 0 to n-1. The submatrix data is copied in the upper-left part of the
            destination array. Elements which are not overwritten by the submatrix data are left unchanged (for example, if the
            destination array is larger than the size of the extracted submatrix).
        
            Parameters:
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
                destination (double[][]): the 2D array where the submatrix data should be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the row/column indices are not valid
                :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooSmallException`: if :code:`endRow < startRow` or :code:`endColumn < startColumn`
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the destination array is too small
        
            Copies a submatrix into a given 2D array.
        
            Rows and columns are indicated counting from 0 to n-1. The submatrix data is copied in the upper-left part of the
            destination array, starting at the specified row/column indices. Elements which are not overwritten by the submatrix
            data are left unchanged (for example, if the destination array is larger than the size of the extracted submatrix).
        
            Parameters:
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
                destination (double[][]): the 2D array where the submatrix data should be copied
                startRowDest (int): the initial row index of the destination array
                startColumnDest (int): the initial column index of the destination array
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the row/column indices are not valid
                :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooSmallException`: if :code:`endRow < startRow` or :code:`endColumn < startColumn`.
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the destination array is too small
        
            Copies a submatrix into a given 2D array.
        
            Rows and columns are indicated counting from 0 to n-1. The submatrix data is copied in the upper-left part of the
            destination array, starting at the specified row/column indices. Elements which are not overwritten by the submatrix
            data are left unchanged (for example, if the destination array is larger than the size of the extracted submatrix).
        
            Parameters:
                selectedRows (int[]): the selected row indices
                selectedColumns (int[]): the selected column indices
                destination (double[][]): the 2D array where the submatrix data should be copied
                startRowDest (int): the initial row index of the destination array
                startColumnDest (int): the initial column index of the destination array
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if the row or column selections are :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if the row or column selections are empty (zero length)
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the selected indices are not valid
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the destination array is too small
        
        
        """
        ...
    @typing.overload
    def copySubMatrix(self, int: int, int2: int, int3: int, int4: int, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int5: int, int6: int) -> None: ...
    @typing.overload
    def copySubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray], doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None:
        """
            Copies a submatrix into a given 2D array.
        
            Rows and columns are indicated counting from 0 to n-1. The submatrix data is copied in the upper-left part of the
            destination array. Elements which are not overwritten by the submatrix data are left unchanged (for example, if the
            destination array is larger than the size of the extracted submatrix).
        
            Parameters:
                selectedRows (int[]): the selected row indices
                selectedColumns (int[]): the selected column indices
                destination (double[][]): the 2D array where the submatrix data should be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if the row or column selections are :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if the row or column selections are empty (zero length)
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the selected indices are not valid
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the destination array is too small
        
        """
        ...
    @typing.overload
    def copySubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray], doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int3: int, int4: int) -> None: ...
    def createMatrix(self, int: int, int2: int) -> 'RealMatrix':
        """
            Creates a new matrix of the same type as this matrix.
        
            The returned matrix is filled with zeros. Its size is determined by the specified row and column dimensions, which must
            both be strictly positive. Additional constraints on the dimensions may apply depending on the implementation (for
            example, symmetric matrices must be square, which implies that the row and column dimensions must be equal).
        
            Parameters:
                rowDimension (int): the number of rows in the new matrix
                columnDimension (int): the number of columns in the new matrix
        
            Returns:
                a new matrix of the same type as this matrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NotStrictlyPositiveException`: if row or column dimension is not positive.
        
            Since:
                2.0
        
        
        """
        ...
    def equals(self, realMatrix: 'RealMatrix', double: float, double2: float) -> bool:
        """
            Is this matrix numerically equivalent to another matrix?
        
            This method indicates if this matrix is equal to another matrix.
        
        
            To do so, the method checks that the two matrices have the same row/column dimensions, and that all entries are
            numerically equal. Two elements are considered to have different values if their absolute and relative differences are
            both above the specified tolerances.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be tested for equality
                relativeTolerance (double): the relative tolerance to take into account when comparing the entries of the matrices
                absoluteTolerance (double): the absolute tolerance to take into account when comparing the entries of the matrices
        
            Returns:
                :code:`true` if the tested matrix is numerically equivalent to this matrix, :code:`false` otherwise
        
        
        """
        ...
    def getAbs(self) -> 'RealMatrix':
        """
            Returns the corresponding absolute values matrix.
        
            Returns:
                the corresponding absolute values matrix
        
        
        """
        ...
    def getColumn(self, int: int) -> typing.MutableSequence[float]:
        """
            Gets the entries of a given column.
        
            Column indices start at 0.
        
            Parameters:
                column (int): the index of the column to be fetched
        
            Returns:
                the extracted column data
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified column index is invalid
        
        
        """
        ...
    def getColumnMatrix(self, int: int) -> 'RealMatrix':
        """
            Gets the entries of a given column as a column matrix.
        
            Column indices start at 0.
        
            Parameters:
                column (int): the index of the column to be fetched
        
            Returns:
                the extracted column matrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified column index is invalid
        
        
        """
        ...
    def getColumnVector(self, int: int) -> RealVector:
        """
            Gets the entries of a given column as a vector.
        
            Column indices start at 0.
        
            Parameters:
                column (int): the index of the column to be fetched
        
            Returns:
                the extracted column vector
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified column index is invalid
        
        
        """
        ...
    @typing.overload
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Returns a 2D array containing the entries of the matrix.
        
            Returns:
                a 2D array containing the entries of the matrix
        
        """
        ...
    @typing.overload
    def getData(self, boolean: bool) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Returns a 2D array containing the entries of the matrix.
        
            If :code:`forceCopy` is :code:`true`, the returned array is guaranteed to be free of references to any internal data
            array (thus, can be safely modified). Otherwise, the returned array may contain references to internal data arrays (for
            optimization purposes). Note that setting :code:`forceCopy` to :code:`false` does not guarantee the returned array
            references an internal data array. For instance, implementations that do not store the entries of the matrix in a 2D
            array have to rebuild a new array each time this method is called, regardless of this parameter.
        
            Parameters:
                forceCopy (boolean): if :code:`true`, the entries of the matrix are systematically stored in a new array; otherwise the returned array may
                    reference internal data arrays
        
            Returns:
                a 2D array containing entries of the matrix
        
        
        """
        ...
    def getDefaultDecomposition(self) -> java.util.function.Function['RealMatrix', Decomposition]: ...
    def getDiagonal(self) -> typing.MutableSequence[float]:
        """
            Gets the diagonal vector from this matrix.
        
            **Note:** The matrix needs to be square.
        
            Returns:
                the diagonal vector from this matrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.NonSquareMatrixException`: if the matrix is not square
        
        
        """
        ...
    def getEntry(self, int: int, int2: int) -> float:
        """
            Gets the entry at the specified row and column.
        
            Row and column indices start at 0.
        
            Parameters:
                row (int): the row index of entry to be fetched
                column (int): the column index of entry to be fetched
        
            Returns:
                the matrix entry at the specified row and column
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the row or column index is not valid
        
        
        """
        ...
    def getFrobeniusNorm(self) -> float:
        """
            Returns the ` Frobenius norm <http://mathworld.wolfram.com/FrobeniusNorm.html>` of the matrix.
        
            Returns:
                the Frobenius norm of the matrix
        
        
        """
        ...
    @typing.overload
    def getInverse(self) -> 'RealMatrix':
        """
            Gets the inverse (or pseudo-inverse) of this matrix using the default decomposition.
        
            The default decomposition builder can be changed using the
            :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setDefaultDecomposition` method.
        
            Returns:
                the inverse matrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.SingularMatrixException`: if the matrix is singular
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getDefaultDecomposition`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setDefaultDecomposition`
        
        :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` getInverse(`Function <http://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`,:class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`> decompositionBuilder)
        
            Gets the inverse (or pseudo-inverse) of this matrix using the given decomposition algorithm.
        
            The decomposition builder is a function capable of generating new instances of the decomposition algorithm to be used
            for the computation of the inverse matrix (like the :class:`~fr.cnes.sirius.patrius.math.linear.QRDecomposition` or the
            :class:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition`, for instance).
        
            Parameters:
                decompositionBuilder (`Function <http://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`,:class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`> decompositionBuilder): the decomposition builder to use
        
            Returns:
                the inverse matrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.SingularMatrixException`: if the matrix is singular
        
        
        """
        ...
    @typing.overload
    def getInverse(self, function: typing.Union[java.util.function.Function['RealMatrix', typing.Union[Decomposition, typing.Callable]], typing.Callable[['RealMatrix'], typing.Union[Decomposition, typing.Callable]]]) -> 'RealMatrix': ...
    @typing.overload
    def getMax(self, boolean: bool) -> float:
        """
            Returns the maximum value of the matrix.
        
            Parameters:
                absValue (boolean): Indicates if the absolute maximum value should be returned
        
            Returns:
                the maximum value of the matrix
        
        
        """
        ...
    @typing.overload
    def getMax(self) -> float:
        """
            Returns the maximum value of the matrix.
        
            Returns:
                the maximum value of the matrix
        
        """
        ...
    @typing.overload
    def getMin(self, boolean: bool) -> float:
        """
            Returns the minimum value of the matrix.
        
            Parameters:
                absValue (boolean): Indicates if the absolute minimum value should be returned
        
            Returns:
                the minimum value of the matrix
        
        
        """
        ...
    @typing.overload
    def getMin(self) -> float:
        """
            Returns the minimum value of the matrix.
        
            Returns:
                the minimum value of the matrix
        
        """
        ...
    def getNorm(self) -> float:
        """
            Returns the ` maximum absolute row sum norm <http://mathworld.wolfram.com/MaximumAbsoluteRowSumNorm.html>` of the
            matrix.
        
            Returns:
                the maximum absolute row sum norm of the matrix
        
        
        """
        ...
    def getRow(self, int: int) -> typing.MutableSequence[float]:
        """
            Gets the entries of a given row.
        
            Row indices start at 0.
        
            Parameters:
                row (int): the index of the row to be fetched
        
            Returns:
                the extracted row data
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified row index is invalid
        
        
        """
        ...
    def getRowMatrix(self, int: int) -> 'RealMatrix':
        """
            Gets the entries of a given row as a row matrix.
        
            Row indices start at 0.
        
            Parameters:
                row (int): the index of the row to be fetched
        
            Returns:
                the extracted row matrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified row index is invalid
        
        
        """
        ...
    def getRowVector(self, int: int) -> RealVector:
        """
            Gets the entries of a given row as a vector.
        
            Row indices start at 0.
        
            Parameters:
                row (int): the index of the row to be fetched
        
            Returns:
                the extracted row vector
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified row index is invalid
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> 'RealMatrix':
        """
            Gets a submatrix.
        
            Rows and columns are indicated counting from 0 to n-1.
        
            Parameters:
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
        
            Returns:
                the submatrix containing the data of the specified rows and columns
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the row/column indices are not valid
                :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooSmallException`: if :code:`endRow < startRow` or :code:`endColumn < startColumn`.
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> 'RealMatrix':
        """
            Gets a submatrix.
        
            Rows and columns are indicated counting from 0 to n-1.
        
            Parameters:
                selectedRows (int[]): the selected row indices
                selectedColumns (int[]): the selected column indices
        
            Returns:
                the submatrix containing the data in the specified rows and columns
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if the row or column selections are :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if the row or column selections are empty (zero length)
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the selected indices are not valid
        
        
        """
        ...
    def getTrace(self) -> float:
        """
            Returns the ` trace <http://mathworld.wolfram.com/MatrixTrace.html>` of the matrix (the sum of the elements on the main
            diagonal).
        
            *The trace of the matrix is only defined for square matrices.*
        
            Returns:
                the trace of the matrix
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.NonSquareMatrixException`: if the matrix is not square
        
        
        """
        ...
    def isAntisymmetric(self, double: float, double2: float) -> bool:
        """
            Is this a antisymmetric matrix?
        
            This method indicates if the matrix is antisymmetric.
        
        
            To do so, the method checks that symmetric off-diagonal elements have numerically equal values but opposite signs, and
            that diagonal elements are numerically equal to zero. Two off-diagonal elements are considered to have different values
            if their absolute and relative differences are both above the specified tolerances. Diagonal elements are considered to
            be different from zero if their absolute value is greater than the specified absolute tolerance.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Parameters:
                relativeTolerance (double): the relative tolerance to take into account when comparing off-diagonal elements
                absoluteTolerance (double): the absolute tolerance to take into account when comparing off-diagonal elements, and when checking if diagonal elements
                    are equal to zero
        
            Returns:
                :code:`true` if this is an antisymmetric matrix, :code:`false` otherwise
        
        
        """
        ...
    def isDiagonal(self, double: float) -> bool:
        """
            Is this a diagonal matrix?
        
            This method indicates if the matrix is diagonal, taking into account the specified tolerance.
        
        
            To do so, the method checks if the off-diagonal elements are numerically equal to zero.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Parameters:
                absoluteTolerance (double): the absolute threshold above which the absolute value of an off-diagonal element is considered to be strictly positive
        
            Returns:
                :code:`true` if this is a diagonal matrix, :code:`false` otherwise
        
        
        """
        ...
    def isInvertible(self, double: float) -> bool:
        """
            Is this an invertible matrix?
        
            This method indicates if the matrix is invertible, taking into account the specified tolerance.
        
        
            To do so, the method checks the linear independence between the column vectors of the matrix. Two columns are considered
            to be linearly dependent if their dot product is numerically equal to the product of their norm.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Parameters:
                relativeTolerance (double): the relative tolerance to take into account when checking the independence of the column vectors
        
            Returns:
                :code:`true` if this is an invertible matrix, :code:`false` otherwise
        
        
        """
        ...
    def isOrthogonal(self, double: float, double2: float) -> bool:
        """
            Is this an orthogonal matrix?
        
            This method indicates if this matrix is orthogonal, taking into account the specified tolerances.
        
        
            To do so, the method checks if the columns of the matrix form an orthonormal set (that is, the column vectors are
            orthogonal to each other and their norm is numerically equal to 1).
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Parameters:
                normalityThreshold (double): the relative tolerance to take into account when checking the normality of the the column vectors
                orthogonalityThreshold (double): the absolute tolerance to take into account when checking the mutual orthogonality of the the column vectors
        
            Returns:
                :code:`true` if this is an orthogonal matrix, :code:`false` otherwise
        
        
        """
        ...
    @typing.overload
    def isSymmetric(self) -> bool:
        """
            Is this a symmetric matrix?
        
            This method indicates if the matrix is symmetric.
        
        
            To do so, the method checks that symmetric off-diagonal elements are numerically equal. Two elements are considered to
            have different values if their absolute and relative differences are both above the default tolerances.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Returns:
                :code:`true` if this is a symmetric matrix, :code:`false` otherwise
        
        """
        ...
    @typing.overload
    def isSymmetric(self, double: float) -> bool:
        """
            Is this a symmetric matrix?
        
            This method indicates if the matrix is symmetric.
        
        
            To do so, the method checks that symmetric off-diagonal elements are numerically equal. Two elements are considered to
            have different values if their relative difference is above the specified tolerance.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Parameters:
                relativeTolerance (double): the relative tolerance to take into account when comparing off-diagonal elements
        
            Returns:
                :code:`true` if this is a symmetric matrix, :code:`false` otherwise
        
            Is this a symmetric matrix?
        
            This method indicates if the matrix is symmetric.
        
        
            To do so, the method checks that symmetric off-diagonal elements are numerically equal. Two elements are considered to
            have different values if their absolute and relative differences are both above the specified tolerances.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Parameters:
                relativeTolerance (double): the relative tolerance to take into account when comparing off-diagonal elements
                absoluteTolerance (double): the absolute tolerance to take into account when comparing off-diagonal elements
        
            Returns:
                :code:`true` if this is a symmetric matrix, :code:`false` otherwise
        
        
        """
        ...
    @typing.overload
    def isSymmetric(self, double: float, double2: float) -> bool: ...
    @typing.overload
    def multiply(self, realMatrix: 'RealMatrix') -> 'RealMatrix':
        """
            Returns the result of postmultiplying this matrix by the matrix :code:`m`.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix by which to postmultiply this matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`m`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the matrices are not multiplication compatible
        
            Returns the result of postmultiplying this matrix by the matrix :code:`m` or its transpose :code:`m` :sup:`T` .
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix by which to postmultiply this matrix by
                toTranspose (boolean): whether to compute the product :code:`this`×:code:`m` (:code:`toTranspose=false` ), or the product
                    :code:`this`×:code:`m` :sup:`T` (:code:`toTranspose=true`)
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`m` or :code:`this` ×:code:`m` :sup:`T`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the matrices are not multiplication compatible
        
            Returns the result of postmultiplying this matrix by the matrix :code:`m` or its transpose :code:`m` :sup:`T` , then by
            the scalar :code:`d`.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix by which to multiply this matrix by
                toTranspose (boolean): whether to compute the product :code:`this`×:code:`m`×:code:`d` ( :code:`toTranspose=false`), or the product
                    :code:`this`×:code:`m` :sup:`T` ×:code:`d` (:code:`toTranspose=true`)
                d (double): the scalar by which to multiply the resulting matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`m`×:code:`d` or :code:`this`×:code:`m` :sup:`T` ×:code:`d`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the matrices are not multiplication compatible
        
        
        """
        ...
    @typing.overload
    def multiply(self, realMatrix: 'RealMatrix', boolean: bool) -> 'RealMatrix': ...
    @typing.overload
    def multiply(self, realMatrix: 'RealMatrix', boolean: bool, double: float) -> 'RealMatrix': ...
    def multiplyEntry(self, int: int, int2: int, double: float) -> None:
        """
            Multiplies (in place) the specified entry of :code:`this` matrix by a given value.
        
            Row and column indices start at 0.
        
            Parameters:
                row (int): the row index of the entry to be modified
                column (int): the column index of the entry to be modified
                factor (double): the multiplication factor for the matrix entry
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the row or column index is not valid
        
            Since:
                2.0
        
        
        """
        ...
    @typing.overload
    def operate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
            Returns the result of postmultiplying this matrix by the vector :code:`v`.
        
            Parameters:
                v (double[]): the vector by which to multiply this matrix by
        
            Returns:
                the column vector resulting from the product :code:`this`×:code:`v`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the length of provided array does not match the column dimension of this matrix
        
            Returns the result of postmultiplying this matrix by the vector :code:`v`.
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the vector by which to multiply this matrix by
        
            Returns:
                the column vector resulting from the product :code:`this`×:code:`v`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the dimension of the provided vector does not match the column dimension of this matrix
        
        
        """
        ...
    @typing.overload
    def operate(self, realVector: RealVector) -> RealVector: ...
    def power(self, int: int) -> 'RealMatrix':
        """
            Returns the the result of multiplying this matrix with itself :code:`p` times.
        
            The exponent :code:`p` must be positive or equal to zero.
        
        
            This operation is only supported for square matrices.
        
        
            Depending on the underlying storage, numerical instabilities might occur for high powers.
        
            Parameters:
                p (int): the exponent :code:`p` to which this matrix is to be raised
        
            Returns:
                the matrix resulting from raising this matrix to the power of :code:`p`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NotPositiveException`: if the exponent :code:`p` is negative
                :class:`~fr.cnes.sirius.patrius.math.linear.NonSquareMatrixException`: if this matrix is not square
        
        
        """
        ...
    @typing.overload
    def preMultiply(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
            Returns the result of premultiplying this matrix by the matrix :code:`m`.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix M by which to premultiply this matrix by
        
            Returns:
                the matrix resulting from the product :code:`m`×:code:`this`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the matrices are not multiplication compatible
        
            Returns the result of premultiplying this matrix by the vector :code:`v`.
        
            Parameters:
                v (double[]): the row vector by which to premultiply this matrix by
        
            Returns:
                the row vector resulting from the product :code:`v`×:code:`this`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the length of the provided array does not match the row dimension of this matrix
        
            Returns the result of premultiplying this matrix by the vector :code:`v`.
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the vector by which to premultiply this matrix by
        
            Returns:
                the row vector resulting from the product :code:`v`×:code:`this`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the dimension of the provided vector does not match the row dimension of this matrix
        
        
        """
        ...
    @typing.overload
    def preMultiply(self, realMatrix: 'RealMatrix') -> 'RealMatrix': ...
    @typing.overload
    def preMultiply(self, realVector: RealVector) -> RealVector: ...
    def scalarAdd(self, double: float) -> 'RealMatrix':
        """
            Returns the result of adding a scalar :code:`d` to the entries of this matrix.
        
            Parameters:
                d (double): the scalar value to be added to the entries of this matrix
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`d`
        
        
        """
        ...
    def scalarMultiply(self, double: float) -> 'RealMatrix':
        """
            Returns the result of multiplying the entries of this matrix by the scalar :code:`d`.
        
            Parameters:
                d (double): the scalar value by which to multiply the entries of this matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`d`
        
        
        """
        ...
    def setColumn(self, int: int, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Replaces the entries of a given column with the entries of the specified data array.
        
            Column indices start at 0.
        
        
            The size of the provided data array must match the row dimension of this matrix.
        
            Parameters:
                column (int): the index of the column to be replaced
                array (double[]): the column data array to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified column index is invalid
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the length of the provided data array does not match the row dimension of this matrix
        
        
        """
        ...
    def setColumnMatrix(self, int: int, realMatrix: 'RealMatrix') -> None:
        """
            Replaces the entries of a given column with the entries of the specified column matrix.
        
            Column indices start at 0.
        
        
            The provided matrix must have one column and the same number of rows as this matrix.
        
            Parameters:
                column (int): the index of the column to be replaced
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the column matrix to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified column index is invalid
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the column dimension of the provided matrix is not 1, or if its row dimension does not match the row dimension of
                    this matrix
        
        
        """
        ...
    def setColumnVector(self, int: int, realVector: RealVector) -> None:
        """
            Replaces the entries of a given column with the entries of the specified vector.
        
            Column indices start at 0.
        
        
            The size of the provided vector must match the row dimension of this matrix.
        
            Parameters:
                column (int): the index of the column to be replaced
                vector (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the column vector to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified column index is invalid
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the dimension of the provided vector does not match the row dimension of this matrix
        
        
        """
        ...
    def setDefaultDecomposition(self, function: typing.Union[java.util.function.Function['RealMatrix', typing.Union[Decomposition, typing.Callable]], typing.Callable[['RealMatrix'], typing.Union[Decomposition, typing.Callable]]]) -> None: ...
    def setEntry(self, int: int, int2: int, double: float) -> None:
        """
            Sets the entry at the specified row and column to a new value.
        
            Row and column indices start at 0.
        
            Parameters:
                row (int): the row index of entry to be set
                column (int): the column index of entry to be set
                value (double): the new value of the entry
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the row or column index is not valid
        
            Since:
                2.0
        
        
        """
        ...
    def setRow(self, int: int, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Replaces the entries of a given row with the entries of the specified data array.
        
            Row indices start at 0.
        
        
            The size of the provided data array must match the column dimension of this matrix.
        
            Parameters:
                row (int): the index of the row to be replaced
                array (double[]): the row data array to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified row index is invalid
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the length of the provided data array does not match the column dimension of this matrix
        
        
        """
        ...
    def setRowMatrix(self, int: int, realMatrix: 'RealMatrix') -> None:
        """
            Replaces the entries of a given row with the entries of the specified row matrix.
        
            Row indices start at 0.
        
        
            The provided matrix must have one row and the same number of columns as this matrix.
        
            Parameters:
                row (int): the index of the row to be replaced
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the row matrix to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified row index is invalid
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the row dimension of the provided matrix is not 1, or if its column dimension does not match the column dimension of
                    this matrix
        
        
        """
        ...
    def setRowVector(self, int: int, realVector: RealVector) -> None:
        """
            Replaces the entries of a given row with the entries of the specified vector.
        
            Row indices start at 0.
        
        
            The size of the provided vector must match the column dimension of this matrix.
        
            Parameters:
                row (int): the index of the row to be replaced
                vector (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the row vector to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified row index is invalid
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the dimension of the provided vector does not match the column dimension of this matrix
        
        
        """
        ...
    def setSubMatrix(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int: int, int2: int) -> None:
        """
            Replaces part of the matrix with a given submatrix, starting at the specified row and column.
        
            Rows and columns are indicated counting from 0 to n-1.
        
        
            **Usage example:**
        
            .. code-block: java
            
            
             // Initial matrix
             matrix = [a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                      [a :sub:`10` , a :sub:`11` , a :sub:`21` ]
                      [a :sub:`20` , a :sub:`21` , a :sub:`22` ]
             // Submatrix
             subMatrix = [b :sub:`00` , b :sub:`01` ]
                         [b :sub:`10` , b :sub:`11` ]
                        
             // Replace part of the initial matrix 
             matrix.setSubMatrix(subMatrix, 1, 1) =>[a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                                                    [a :sub:`10` , b :sub:`00` , b :sub:`01` ]
                                                    [a :sub:`20` , b :sub:`10` , b :sub:`11` ]
             
        
            Parameters:
                subMatrix (double[][]): the array containing the submatrix replacement data
                row (int): the row coordinate of the top, left element to be replaced
                column (int): the column coordinate of the top, left element to be replaced
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NullArgumentException`: if the input submatrix array is :code:`null`
                :class:`~fr.cnes.sirius.patrius.math.exception.NoDataException`: if the input submatrix array is empty
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the rows of the input submatrix array have different lengths
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the input submatrix array does not fit into this matrix when starting from the specified top, left element
        
            Since:
                2.0
        
        
        """
        ...
    def subtract(self, realMatrix: 'RealMatrix') -> 'RealMatrix':
        """
            Returns the result of subtracting the matrix :code:`m` from this matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be subtracted
        
            Returns:
                the matrix resulting from the subtraction :code:`this`-:code:`m`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the matrix :code:`m` is not the same size as this matrix
        
        
        """
        ...
    def toString(self, realMatrixFormat: RealMatrixFormat) -> str:
        """
            Gets a string representation of this matrix using the specified format.
        
            Several predefined matrix formats are available in :class:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils`.
        
            Parameters:
                realMatrixFormat (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixFormat`): the matrix format to be used
        
            Returns:
                a string representation of this matrix
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils.JAVA_FORMAT`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils.OCTAVE_FORMAT`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils.VISUAL_FORMAT`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils.SUMMARY_FORMAT`
        
        
        """
        ...
    @typing.overload
    def transpose(self) -> 'RealMatrix':
        """
            Returns the transpose of this matrix.
        
            Returns:
                the transpose of this matrix
        
        """
        ...
    @typing.overload
    def transpose(self, boolean: bool) -> 'RealMatrix':
        """
            Returns the transpose of this matrix.
        
            If :code:`forceCopy` is :code:`true`, the returned matrix is guaranteed to be a new instance, which can be modified
            without any risk of impacting the current instance. Otherwise, this method may simply return the current instance when
            the matrix is its own transpose (symmetric matrix).
        
            Parameters:
                forceCopy (boolean): if :code:`true`, the transpose of the matrix is systematically stored in a new matrix; otherwise the method may return
                    the current instance when the matrix is its own transpose
        
            Returns:
                the transpose of this matrix
        
        
        """
        ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visits (and possibly change) all matrix entries in column order.
        
            Column order starts at upper left element, iterating through all elements of a column from top to bottom before going to
            the topmost element of the next column.
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) all matrix entries in column order.
        
            Column order starts at upper left element, iterating through all elements of a column from top to bottom before going to
            the topmost element of the next column.
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (and possibly change) some matrix entries in column order.
        
            Column order starts at upper left element, iterating through all elements of a column from top to bottom before going to
            the topmost element of the next column.
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified indices are not valid
                :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooSmallException`: if :code:`endRow < startRow` or :code:`endColumn < startColumn`
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) some matrix entries in column order.
        
            Column order starts at upper left element, iterating through all elements of a column from top to bottom before going to
            the topmost element of the next column.
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified indices are not valid
                :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooSmallException`: if :code:`endRow < startRow` or :code:`endColumn < startColumn`
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visits (and possibly change) all matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) all matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (and possibly change) some matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified indices are not valid
                :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooSmallException`: if :code:`endRow < startRow` or :code:`endColumn < startColumn`
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) some matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified indices are not valid
                :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooSmallException`: if :code:`endRow < startRow` or :code:`endColumn < startColumn`
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visits (and possibly change) all matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) all matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (and possibly change) some matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified indices are not valid
                :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooSmallException`: if :code:`endRow < startRow` or :code:`endColumn < startColumn`
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) some matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified indices are not valid
                :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooSmallException`: if :code:`endRow < startRow` or :code:`endColumn < startColumn`
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...

class SingularValueDecomposition(Decomposition):
    """
    public class SingularValueDecomposition extends `Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`
    
        Calculates the compact Singular Value Decomposition of a matrix.
    
        The Singular Value Decomposition of matrix A is a set of three matrices: U, Σ and V such that A = U × Σ × V :sup:`T`
        . Let A be a m × n matrix, then U is a m × p orthogonal matrix, Σ is a p × p diagonal matrix with positive or null
        elements, V is a p × n orthogonal matrix (hence V :sup:`T` is also orthogonal) where p=min(m,n).
    
        This class is similar to the class with similar name from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library,
        with the following changes:
    
          - the :code:`norm2` method which has been renamed as
            :meth:`~fr.cnes.sirius.patrius.math.linear.SingularValueDecomposition.getNorm`,
          - the :code:`cond` method which has been renamed as
            :meth:`~fr.cnes.sirius.patrius.math.linear.SingularValueDecomposition.getConditionNumber`,
          - the :code:`rank` method which has been renamed as
            :meth:`~fr.cnes.sirius.patrius.math.linear.SingularValueDecomposition.getRank`,
          - a :meth:`~fr.cnes.sirius.patrius.math.linear.SingularValueDecomposition.getUT` method has been added,
          - a :meth:`~fr.cnes.sirius.patrius.math.linear.SingularValueDecomposition.getVT` method has been added,
          - a :meth:`~fr.cnes.sirius.patrius.math.linear.SingularValueDecomposition.getSolver` method has been added,
          - a :meth:`~fr.cnes.sirius.patrius.math.linear.SingularValueDecomposition.getCovariance` method has been added.
    
    
        This class is up-to-date with commons-math 3.6.1.
    
        Since:
            2.0 (changed to concrete class in 3.0)
    
        Also see:
            `MathWorld <http://mathworld.wolfram.com/SingularValueDecomposition.html>`, `Wikipedia
            <http://en.wikipedia.org/wiki/Singular_value_decomposition>`
    """
    def __init__(self, realMatrix: RealMatrix): ...
    @staticmethod
    def decompositionBuilder() -> java.util.function.Function[RealMatrix, Decomposition]: ...
    def getConditionNumber(self) -> float:
        """
            Return the condition number of the matrix.
        
            Returns:
                condition number of the matrix
        
        
        """
        ...
    def getCovariance(self, double: float) -> RealMatrix:
        """
            Returns the n × n covariance matrix.
        
            The covariance matrix is V × J × V :sup:`T` where J is the diagonal matrix of the inverse of the squares of the
            singular values.
        
            Parameters:
                minSingularValue (double): value below which singular values are ignored (a 0 or negative value implies all singular value will be used)
        
            Returns:
                covariance matrix
        
            Raises:
                : if minSingularValue is larger than the largest singular value, meaning all singular values are ignored
        
        
        """
        ...
    def getInverseConditionNumber(self) -> float:
        """
            Computes the inverse of the condition number. In cases of rank deficiency, the
            :meth:`~fr.cnes.sirius.patrius.math.linear.SingularValueDecomposition.getConditionNumber` will become undefined.
        
            Returns:
                the inverse of the condition number.
        
        
        """
        ...
    def getNorm(self) -> float:
        """
            Returns the L :sub:`2` norm of the matrix.
        
            The L :sub:`2` norm is max(|A × u| :sub:`2` / |u| :sub:`2` ), where |.| :sub:`2` denotes the vectorial 2-norm (i.e. the
            traditional euclidian norm).
        
            Returns:
                norm
        
        
        """
        ...
    def getRank(self) -> int:
        """
            Return the effective numerical matrix rank.
        
            The effective numerical rank is the number of non-negligible singular values. The threshold used to identify
            non-negligible terms is max(m,n) × ulp(s :sub:`1` ) where ulp(s :sub:`1` ) is the least significant bit of the largest
            singular value.
        
            Returns:
                effective numerical matrix rank
        
        
        """
        ...
    def getS(self) -> RealMatrix:
        """
            Returns the diagonal matrix Σ of the decomposition.
        
            Σ is a diagonal matrix. The singular values are provided in non-increasing order, for compatibility with Jama.
        
            Returns:
                the Σ matrix
        
        
        """
        ...
    def getSingularValues(self) -> typing.MutableSequence[float]:
        """
            Returns the diagonal elements of the matrix Σ of the decomposition.
        
            The singular values are provided in non-increasing order, for compatibility with Jama.
        
            Returns:
                the diagonal elements of the Σ matrix
        
        
        """
        ...
    def getSolver(self) -> DecompositionSolver:
        """
            Gets a solver for finding the A × X = B solution in exact linear sense.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.Decomposition.getSolver` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`
        
            Returns:
                the decomposition solver.
        
        
        """
        ...
    def getU(self) -> RealMatrix:
        """
            Returns the matrix U of the decomposition.
        
            U is an orthogonal matrix, i.e. its transpose is also its inverse.
        
            Returns:
                the U matrix
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SingularValueDecomposition.getUT`
        
        
        """
        ...
    def getUT(self) -> RealMatrix:
        """
            Returns the transpose of the matrix U of the decomposition.
        
            U is an orthogonal matrix, i.e. its transpose is also its inverse.
        
            Returns:
                the transpose of the U matrix
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SingularValueDecomposition.getU`
        
        
        """
        ...
    def getV(self) -> RealMatrix:
        """
            Returns the matrix V of the decomposition.
        
            V is an orthogonal matrix, i.e. its transpose is also its inverse.
        
            Returns:
                the V matrix (or null if decomposed matrix is singular)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SingularValueDecomposition.getVT`
        
        
        """
        ...
    def getVT(self) -> RealMatrix:
        """
            Returns the transpose of the matrix V of the decomposition.
        
            V is an orthogonal matrix, i.e. its transpose is also its inverse.
        
            Returns:
                the V matrix
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SingularValueDecomposition.getV`
        
        
        """
        ...

class UDDecompositionImpl(UDDecomposition, Decomposition):
    DEFAULT_RELATIVE_SYMMETRY_THRESHOLD: typing.ClassVar[float] = ...
    DEFAULT_ABSOLUTE_POSITIVITY_THRESHOLD: typing.ClassVar[float] = ...
    @typing.overload
    def __init__(self, realMatrix: RealMatrix): ...
    @typing.overload
    def __init__(self, realMatrix: RealMatrix, double: float, double2: float): ...
    @staticmethod
    def decompositionBuilder(double: float, double2: float) -> java.util.function.Function[RealMatrix, Decomposition]: ...
    def getD(self) -> RealMatrix: ...
    def getDeterminant(self) -> float: ...
    def getSolver(self) -> DecompositionSolver: ...
    def getU(self) -> RealMatrix: ...
    def getUT(self) -> RealMatrix: ...

_AbstractFieldMatrix__T = typing.TypeVar('_AbstractFieldMatrix__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
class AbstractFieldMatrix(FieldMatrix[_AbstractFieldMatrix__T], typing.Generic[_AbstractFieldMatrix__T]):
    def add(self, fieldMatrix: FieldMatrix[_AbstractFieldMatrix__T]) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def addToEntry(self, int: int, int2: int, t: _AbstractFieldMatrix__T) -> None: ...
    def copy(self) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def copySubMatrix(self, int: int, int2: int, int3: int, int4: int, tArray: typing.Union[typing.List[typing.MutableSequence[_AbstractFieldMatrix__T]], jpype.JArray]) -> None: ...
    @typing.overload
    def copySubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray], tArray: typing.Union[typing.List[typing.MutableSequence[_AbstractFieldMatrix__T]], jpype.JArray]) -> None: ...
    def createMatrix(self, int: int, int2: int) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getColumn(self, int: int) -> typing.MutableSequence[_AbstractFieldMatrix__T]: ...
    def getColumnDimension(self) -> int: ...
    def getColumnMatrix(self, int: int) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def getColumnVector(self, int: int) -> FieldVector[_AbstractFieldMatrix__T]: ...
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[_AbstractFieldMatrix__T]]: ...
    def getEntry(self, int: int, int2: int) -> _AbstractFieldMatrix__T: ...
    def getField(self) -> fr.cnes.sirius.patrius.math.Field[_AbstractFieldMatrix__T]: ...
    def getRow(self, int: int) -> typing.MutableSequence[_AbstractFieldMatrix__T]: ...
    def getRowDimension(self) -> int: ...
    def getRowMatrix(self, int: int) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def getRowVector(self, int: int) -> FieldVector[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def getTrace(self) -> _AbstractFieldMatrix__T: ...
    def hashCode(self) -> int: ...
    def isSquare(self) -> bool: ...
    def multiply(self, fieldMatrix: FieldMatrix[_AbstractFieldMatrix__T]) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def multiplyEntry(self, int: int, int2: int, t: _AbstractFieldMatrix__T) -> None: ...
    @typing.overload
    def operate(self, tArray: typing.Union[typing.List[_AbstractFieldMatrix__T], jpype.JArray]) -> typing.MutableSequence[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def operate(self, fieldVector: FieldVector[_AbstractFieldMatrix__T]) -> FieldVector[_AbstractFieldMatrix__T]: ...
    def power(self, int: int) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, tArray: typing.Union[typing.List[_AbstractFieldMatrix__T], jpype.JArray]) -> typing.MutableSequence[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldMatrix: FieldMatrix[_AbstractFieldMatrix__T]) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldVector: FieldVector[_AbstractFieldMatrix__T]) -> FieldVector[_AbstractFieldMatrix__T]: ...
    def scalarAdd(self, t: _AbstractFieldMatrix__T) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def scalarMultiply(self, t: _AbstractFieldMatrix__T) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def setColumn(self, int: int, tArray: typing.Union[typing.List[_AbstractFieldMatrix__T], jpype.JArray]) -> None: ...
    def setColumnMatrix(self, int: int, fieldMatrix: FieldMatrix[_AbstractFieldMatrix__T]) -> None: ...
    def setColumnVector(self, int: int, fieldVector: FieldVector[_AbstractFieldMatrix__T]) -> None: ...
    def setEntry(self, int: int, int2: int, t: _AbstractFieldMatrix__T) -> None: ...
    def setRow(self, int: int, tArray: typing.Union[typing.List[_AbstractFieldMatrix__T], jpype.JArray]) -> None: ...
    def setRowMatrix(self, int: int, fieldMatrix: FieldMatrix[_AbstractFieldMatrix__T]) -> None: ...
    def setRowVector(self, int: int, fieldVector: FieldVector[_AbstractFieldMatrix__T]) -> None: ...
    def setSubMatrix(self, tArray: typing.Union[typing.List[typing.MutableSequence[_AbstractFieldMatrix__T]], jpype.JArray], int: int, int2: int) -> None: ...
    def subtract(self, fieldMatrix: FieldMatrix[_AbstractFieldMatrix__T]) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def toString(self) -> str: ...
    def transpose(self) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_AbstractFieldMatrix__T]) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_AbstractFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_AbstractFieldMatrix__T]) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_AbstractFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_AbstractFieldMatrix__T]) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_AbstractFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_AbstractFieldMatrix__T]) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_AbstractFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_AbstractFieldMatrix__T]) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_AbstractFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_AbstractFieldMatrix__T]) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_AbstractFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _AbstractFieldMatrix__T: ...

class AbstractRealMatrix(RealLinearOperator, RealMatrix):
    """
    public abstract class AbstractRealMatrix extends :class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator` implements :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
    
        Basic implementation of :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` methods regardless of the underlying
        storage.
    
        All the methods implemented here use :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getEntry` to access
        matrix elements. Derived class can provide faster implementations.
    
        This class is up-to-date with commons-math 3.6.1.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    def add(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Returns the result of adding the matrix :code:`m` to this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.add` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be added
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`m`
        
        
        """
        ...
    def addToEntry(self, int: int, int2: int, double: float) -> None:
        """
            Adds (in place) a given value to the specified entry of this matrix.
        
            Row and column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.addToEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                row (int): the row index of the entry to be modified
                column (int): the column index of the entry to be modified
                increment (double): the value to add to the matrix entry
        
        
        """
        ...
    @typing.overload
    def concatenateDiagonally(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Diagonally concatenates this matrix and another matrix :code:`m`, placing it in the lower right part of the concatenated
            matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.concatenateDiagonally` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
        
            Returns:
                the concatenated matrix
        
            Diagonally concatenates this matrix and another matrix :code:`m`, placing it in the lower right or upper left part of
            the concatenated matrix.
        
            The way the two matrices are concatenated depends on the provided argument:
        
        
            The matrix :code:`m` is placed in the lower right part of the concatenated matrix if :code:`lowerRightConcatenation` is
            set to :code:`true`, and in its upper left part if it is set to :code:`false`.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             this.concatenateDiagonally(m, true)  => [this, 0] 
                                                     [   0, m]
                
             this.concatenateDiagonally(m, false) => [m,    0]
                                                     [0, this]
             
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.concatenateDiagonally` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
                lowerRightConcatenation (boolean): whether the matrix :code:`m` is to be placed in the lower right (:code:`true`) or upper left (:code:`false`) part of the
                    concatenated matrix
        
            Returns:
                the concatenated matrix
        
            Diagonally or anti-diagonally concatenates this matrix and another matrix :code:`m`.
        
            The way the two matrices are concatenated depends on the provided arguments:
        
        
            The matrix :code:`m` is placed in the right part of the concatenated matrix if :code:`rightConcatenation` is set to
            :code:`true`, and in its left part if it is set to :code:`false`. Similarly, the matrix :code:`m` is placed in the lower
            part of the concatenated matrix if :code:`lowerConcatenation` is set to :code:`true`, and in its upper part if it is set
            to :code:`false`. This matrix is then placed in the opposite part of the concatenated matrix (as an example, if the
            provided matrix is placed in the upper left part, this matrix will be placed in the lower right part, the remaining
            parts being filled with zeros).
        
            **Usage examples:**
        
            .. code-block: java
            
            
             // Diagonal concatenation
             this.concatenateDiagonally(m, true, true)   => [this, 0] 
                                                            [   0, m]
                                                          
             this.concatenateDiagonally(m, false, false) => [m,    0]
                                                            [0, this]
                                      
             // Anti-diagonal concatenation
             this.concatenateDiagonally(m, false, true)  => [0, this]
                                                            [m,    0]
                                                           
             this.concatenateDiagonally(m, true, false)  => [   0, m]
                                                            [this, 0]
             
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.concatenateDiagonally` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
                rightConcatenation (boolean): whether the matrix :code:`m` is to be placed in the right (:code:`true`) or left ( :code:`false`) part of the
                    concatenated matrix
                lowerConcatenation (boolean): whether the matrix :code:`m` is to be placed in the lower (:code:`true`) or upper ( :code:`false`) part of the
                    concatenated matrix
        
            Returns:
                the concatenated matrix
        
        
        """
        ...
    @typing.overload
    def concatenateDiagonally(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    @typing.overload
    def concatenateDiagonally(self, realMatrix: RealMatrix, boolean: bool, boolean2: bool) -> RealMatrix: ...
    @typing.overload
    def concatenateHorizontally(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Horizontally concatenates this matrix and another matrix :code:`m`, placing it in the right part of the concatenated
            matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.concatenateHorizontally` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
        
            Returns:
                the concatenated matrix
        
            Horizontally concatenates this matrix and another matrix :code:`m`, , placing it in the left or right part of the
            concatenated matrix.
        
            The way the two matrices are concatenated depends on the provided argument:
        
        
            The matrix :code:`m` is placed in the right part of the concatenated matrix if :code:`rightConcatenation` is set to
            :code:`true`, and in its left part if it is set to :code:`false`.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             this.concatenateHorizontally(m, true)  => [this, m] 
             
             this.concatenateHorizontally(m, false) => [m, this]
             
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.concatenateHorizontally` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
                rightConcatenation (boolean): whether the matrix :code:`m` is to be placed in the right (:code:`true`) or left ( :code:`false`) part of the
                    concatenated matrix
        
            Returns:
                the concatenated matrix
        
        
        """
        ...
    @typing.overload
    def concatenateHorizontally(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    @typing.overload
    def concatenateVertically(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Vertically concatenates this matrix and another matrix :code:`m`, placing it in the lower part of the concatenated
            matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.concatenateVertically` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
        
            Returns:
                the concatenated matrix
        
            Vertically concatenates this matrix and another matrix :code:`m`, placing it in the lower or upper part of the
            concatenated matrix.
        
            The way the two matrices are concatenated depends on the provided argument:
        
        
            The matrix :code:`m` is placed in the lower part of the concatenated matrix if :code:`lowerConcatenation` is set to
            :code:`true`, and in its upper part if it is set to :code:`false`.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             this.concatenateVertically(m, true)  => [this] 
                                                     [   m]
                                                          
             this.concatenateVertically(m, false) => [   m]
                                                     [this]
             
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.concatenateVertically` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
                lowerConcatenation (boolean): whether the matrix :code:`m` is to be placed in the lower (:code:`true`) or upper ( :code:`false`) part of the
                    concatenated matrix
        
            Returns:
                the concatenated matrix
        
        
        """
        ...
    @typing.overload
    def concatenateVertically(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    def copy(self) -> RealMatrix:
        """
            Returns a deep copy of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.copy` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Returns:
                a deep copy of this matrix
        
        
        """
        ...
    @typing.overload
    def copySubMatrix(self, int: int, int2: int, int3: int, int4: int, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None:
        """
            Copies a submatrix into a given 2D array.
        
            Rows and columns are indicated counting from 0 to n-1. The submatrix data is copied in the upper-left part of the
            destination array. Elements which are not overwritten by the submatrix data are left unchanged (for example, if the
            destination array is larger than the size of the extracted submatrix).
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
                destination (double[][]): the 2D array where the submatrix data should be copied
        
            Copies a submatrix into a given 2D array.
        
            Rows and columns are indicated counting from 0 to n-1. The submatrix data is copied in the upper-left part of the
            destination array, starting at the specified row/column indices. Elements which are not overwritten by the submatrix
            data are left unchanged (for example, if the destination array is larger than the size of the extracted submatrix).
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
                destination (double[][]): the 2D array where the submatrix data should be copied
                startRowDest (int): the initial row index of the destination array
                startColumnDest (int): the initial column index of the destination array
        
            Copies a submatrix into a given 2D array.
        
            Rows and columns are indicated counting from 0 to n-1. The submatrix data is copied in the upper-left part of the
            destination array, starting at the specified row/column indices. Elements which are not overwritten by the submatrix
            data are left unchanged (for example, if the destination array is larger than the size of the extracted submatrix).
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                selectedRows (int[]): the selected row indices
                selectedColumns (int[]): the selected column indices
                destination (double[][]): the 2D array where the submatrix data should be copied
                startRowDest (int): the initial row index of the destination array
                startColumnDest (int): the initial column index of the destination array
        
        
        """
        ...
    @typing.overload
    def copySubMatrix(self, int: int, int2: int, int3: int, int4: int, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int5: int, int6: int) -> None: ...
    @typing.overload
    def copySubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray], doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None:
        """
            Copies a submatrix into a given 2D array.
        
            Rows and columns are indicated counting from 0 to n-1. The submatrix data is copied in the upper-left part of the
            destination array. Elements which are not overwritten by the submatrix data are left unchanged (for example, if the
            destination array is larger than the size of the extracted submatrix).
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                selectedRows (int[]): the selected row indices
                selectedColumns (int[]): the selected column indices
                destination (double[][]): the 2D array where the submatrix data should be copied
        
        """
        ...
    @typing.overload
    def copySubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray], doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int3: int, int4: int) -> None: ...
    def createMatrix(self, int: int, int2: int) -> RealMatrix:
        """
            Creates a new matrix of the same type as this matrix.
        
            The returned matrix is filled with zeros. Its size is determined by the specified row and column dimensions, which must
            both be strictly positive. Additional constraints on the dimensions may apply depending on the implementation (for
            example, symmetric matrices must be square, which implies that the row and column dimensions must be equal).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.createMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                rowDimension (int): the number of rows in the new matrix
                columnDimension (int): the number of columns in the new matrix
        
            Returns:
                a new matrix of the same type as this matrix
        
        
        """
        ...
    @typing.overload
    def equals(self, realMatrix: RealMatrix, double: float, double2: float) -> bool:
        """
            Is this matrix numerically equivalent to another matrix?
        
            This method indicates if this matrix is equal to another matrix.
        
        
            To do so, the method checks that the two matrices have the same row/column dimensions, and that all entries are
            numerically equal. Two elements are considered to have different values if their absolute and relative differences are
            both above the specified tolerances.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.equals` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be tested for equality
                relativeThreshold (double): the relative tolerance to take into account when comparing the entries of the matrices
                absoluteThreshold (double): the absolute tolerance to take into account when comparing the entries of the matrices
        
            Returns:
                :code:`true` if the tested matrix is numerically equivalent to this matrix, :code:`false` otherwise
        
        
        """
        ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool:
        """
            Returns :code:`true` if the provided object is a :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` instance with
            the same dimensions as this matrix, whose entries are strictly equal to the entries of this matrix (no absolute or
            relative tolerance is taken into account when comparing the entries).
        
            Overrides:
                 in class 
        
            Parameters:
                object (`Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`): the object to be tested for equality
        
            Returns:
                :code:`true` if the provided object is equal to this matrix
        
        """
        ...
    def getAbs(self) -> RealMatrix:
        """
            Returns the corresponding absolute values matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getAbs` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Returns:
                the corresponding absolute values matrix
        
        
        """
        ...
    def getColumn(self, int: int) -> typing.MutableSequence[float]:
        """
            Gets the entries of a given column.
        
            Column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getColumn` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                column (int): the index of the column to be fetched
        
            Returns:
                the extracted column data
        
        
        """
        ...
    def getColumnDimension(self) -> int:
        """
            Returns the dimension of the domain of this operator.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix.getColumnDimension` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator.getColumnDimension` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`
        
            Returns:
                the number of columns of the underlying matrix
        
        
        """
        ...
    def getColumnMatrix(self, int: int) -> RealMatrix:
        """
            Gets the entries of a given column as a column matrix.
        
            Column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getColumnMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                column (int): the index of the column to be fetched
        
            Returns:
                the extracted column matrix
        
        
        """
        ...
    def getColumnVector(self, int: int) -> RealVector:
        """
            Gets the entries of a given column as a vector.
        
            Column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getColumnVector` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                column (int): the index of the column to be fetched
        
            Returns:
                the extracted column vector
        
        
        """
        ...
    @typing.overload
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Returns a 2D array containing the entries of the matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getData` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Returns:
                a 2D array containing the entries of the matrix
        
        """
        ...
    @typing.overload
    def getData(self, boolean: bool) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Returns a 2D array containing the entries of the matrix.
        
            If :code:`forceCopy` is :code:`true`, the returned array is guaranteed to be free of references to any internal data
            array (thus, can be safely modified). Otherwise, the returned array may contain references to internal data arrays (for
            optimization purposes). Note that setting :code:`forceCopy` to :code:`false` does not guarantee the returned array
            references an internal data array. For instance, implementations that do not store the entries of the matrix in a 2D
            array have to rebuild a new array each time this method is called, regardless of this parameter.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getData` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                forceCopy (boolean): if :code:`true`, the entries of the matrix are systematically stored in a new array; otherwise the returned array may
                    reference internal data arrays
        
            Returns:
                a 2D array containing entries of the matrix
        
        
        """
        ...
    def getDefaultDecomposition(self) -> java.util.function.Function[RealMatrix, Decomposition]: ...
    def getDiagonal(self) -> typing.MutableSequence[float]:
        """
            Gets the diagonal vector from this matrix.
        
            **Note:** The matrix needs to be square.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getDiagonal` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Returns:
                the diagonal vector from this matrix
        
        
        """
        ...
    def getEntry(self, int: int, int2: int) -> float:
        """
            Gets the entry at the specified row and column.
        
            Row and column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                row (int): the row index of entry to be fetched
                column (int): the column index of entry to be fetched
        
            Returns:
                the matrix entry at the specified row and column
        
        
        """
        ...
    def getFrobeniusNorm(self) -> float:
        """
            Returns the ` Frobenius norm <http://mathworld.wolfram.com/FrobeniusNorm.html>` of the matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getFrobeniusNorm` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Returns:
                the Frobenius norm of the matrix
        
        
        """
        ...
    @typing.overload
    def getInverse(self) -> RealMatrix:
        """
            Gets the inverse (or pseudo-inverse) of this matrix using the default decomposition.
        
            The default decomposition builder can be changed using the
            :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setDefaultDecomposition` method.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Returns:
                the inverse matrix
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getDefaultDecomposition`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setDefaultDecomposition`
        
        public :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` getInverse(`Function <http://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`,:class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`> decompositionBuilder)
        
            Gets the inverse (or pseudo-inverse) of this matrix using the given decomposition algorithm.
        
            The decomposition builder is a function capable of generating new instances of the decomposition algorithm to be used
            for the computation of the inverse matrix (like the :class:`~fr.cnes.sirius.patrius.math.linear.QRDecomposition` or the
            :class:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition`, for instance).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                decompositionBuilder (`Function <http://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`,:class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`> decompositionBuilder): the decomposition builder to use
        
            Returns:
                the inverse matrix
        
        
        """
        ...
    @typing.overload
    def getInverse(self, function: typing.Union[java.util.function.Function[RealMatrix, typing.Union[Decomposition, typing.Callable]], typing.Callable[[RealMatrix], typing.Union[Decomposition, typing.Callable]]]) -> RealMatrix: ...
    @typing.overload
    def getMax(self) -> float: ...
    @typing.overload
    def getMax(self, boolean: bool) -> float:
        """
            Returns the maximum value of the matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getMax` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                absValue (boolean): Indicates if the absolute maximum value should be returned
        
            Returns:
                the maximum value of the matrix
        
        
        """
        ...
    @typing.overload
    def getMin(self) -> float: ...
    @typing.overload
    def getMin(self, boolean: bool) -> float:
        """
            Returns the minimum value of the matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getMin` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                absValue (boolean): Indicates if the absolute minimum value should be returned
        
            Returns:
                the minimum value of the matrix
        
        
        """
        ...
    def getNorm(self) -> float:
        """
            Returns the ` maximum absolute row sum norm <http://mathworld.wolfram.com/MaximumAbsoluteRowSumNorm.html>` of the
            matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getNorm` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Returns:
                the maximum absolute row sum norm of the matrix
        
        
        """
        ...
    def getRow(self, int: int) -> typing.MutableSequence[float]:
        """
            Gets the entries of a given row.
        
            Row indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getRow` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                row (int): the index of the row to be fetched
        
            Returns:
                the extracted row data
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
            Returns the dimension of the codomain of this operator.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix.getRowDimension` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator.getRowDimension` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`
        
            Returns:
                the number of rows of the underlying matrix
        
        
        """
        ...
    def getRowMatrix(self, int: int) -> RealMatrix:
        """
            Gets the entries of a given row as a row matrix.
        
            Row indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getRowMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                row (int): the index of the row to be fetched
        
            Returns:
                the extracted row matrix
        
        
        """
        ...
    def getRowVector(self, int: int) -> RealVector:
        """
            Gets the entries of a given row as a vector.
        
            Row indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getRowVector` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                row (int): the index of the row to be fetched
        
            Returns:
                the extracted row vector
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> RealMatrix:
        """
            Gets a submatrix.
        
            Rows and columns are indicated counting from 0 to n-1.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getSubMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
        
            Returns:
                the submatrix containing the data of the specified rows and columns
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> RealMatrix:
        """
            Gets a submatrix.
        
            Rows and columns are indicated counting from 0 to n-1.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                selectedRows (int[]): the selected row indices
                selectedColumns (int[]): the selected column indices
        
            Returns:
                the submatrix containing the data in the specified rows and columns
        
        
        """
        ...
    def getTrace(self) -> float:
        """
            Returns the ` trace <http://mathworld.wolfram.com/MatrixTrace.html>` of the matrix (the sum of the elements on the main
            diagonal).
        
            *The trace of the matrix is only defined for square matrices.*
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getTrace` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Returns:
                the trace of the matrix
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code for the matrix.
        
            Overrides:
                 in class 
        
            Returns:
                hash code for matrix
        
        
        """
        ...
    def isAntisymmetric(self, double: float, double2: float) -> bool:
        """
            Is this a antisymmetric matrix?
        
            This method indicates if the matrix is antisymmetric.
        
        
            To do so, the method checks that symmetric off-diagonal elements have numerically equal values but opposite signs, and
            that diagonal elements are numerically equal to zero. Two off-diagonal elements are considered to have different values
            if their absolute and relative differences are both above the specified tolerances. Diagonal elements are considered to
            be different from zero if their absolute value is greater than the specified absolute tolerance.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isAntisymmetric` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                relativeTolerance (double): the relative tolerance to take into account when comparing off-diagonal elements
                absoluteTolerance (double): the absolute tolerance to take into account when comparing off-diagonal elements, and when checking if diagonal elements
                    are equal to zero
        
            Returns:
                :code:`true` if this is an antisymmetric matrix, :code:`false` otherwise
        
        
        """
        ...
    def isDiagonal(self, double: float) -> bool:
        """
            Is this a diagonal matrix?
        
            This method indicates if the matrix is diagonal, taking into account the specified tolerance.
        
        
            To do so, the method checks if the off-diagonal elements are numerically equal to zero.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isDiagonal` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                absoluteTolerance (double): the absolute threshold above which the absolute value of an off-diagonal element is considered to be strictly positive
        
            Returns:
                :code:`true` if this is a diagonal matrix, :code:`false` otherwise
        
        
        """
        ...
    def isInvertible(self, double: float) -> bool:
        """
            Is this an invertible matrix?
        
            This method indicates if the matrix is invertible, taking into account the specified tolerance.
        
        
            To do so, the method checks the linear independence between the column vectors of the matrix. Two columns are considered
            to be linearly dependent if their dot product is numerically equal to the product of their norm.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isInvertible` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                relativeTolerance (double): the relative tolerance to take into account when checking the independence of the column vectors
        
            Returns:
                :code:`true` if this is an invertible matrix, :code:`false` otherwise
        
        
        """
        ...
    def isOrthogonal(self, double: float, double2: float) -> bool:
        """
            Is this an orthogonal matrix?
        
            This method indicates if this matrix is orthogonal, taking into account the specified tolerances.
        
        
            To do so, the method checks if the columns of the matrix form an orthonormal set (that is, the column vectors are
            orthogonal to each other and their norm is numerically equal to 1).
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isOrthogonal` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                normalityThreshold (double): the relative tolerance to take into account when checking the normality of the the column vectors
                orthogonalityThreshold (double): the absolute tolerance to take into account when checking the mutual orthogonality of the the column vectors
        
            Returns:
                :code:`true` if this is an orthogonal matrix, :code:`false` otherwise
        
        
        """
        ...
    def isSquare(self) -> bool:
        """
            Is this a square matrix?
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix.isSquare` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`
        
            Returns:
                true if the matrix is square (rowDimension = columnDimension)
        
        
        """
        ...
    @typing.overload
    def isSymmetric(self) -> bool:
        """
            Is this a symmetric matrix?
        
            This method indicates if the matrix is symmetric.
        
        
            To do so, the method checks that symmetric off-diagonal elements are numerically equal. Two elements are considered to
            have different values if their absolute and relative differences are both above the default tolerances.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            The absolute and relative tolerances both default to
            :meth:`~fr.cnes.sirius.patrius.math.util.Precision.DOUBLE_COMPARISON_EPSILON`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isSymmetric` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Returns:
                :code:`true` if this is a symmetric matrix, :code:`false` otherwise
        
        """
        ...
    @typing.overload
    def isSymmetric(self, double: float) -> bool:
        """
            Is this a symmetric matrix?
        
            This method indicates if the matrix is symmetric.
        
        
            To do so, the method checks that symmetric off-diagonal elements are numerically equal. Two elements are considered to
            have different values if their relative difference is above the specified tolerance.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isSymmetric` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                relativeTolerance (double): the relative tolerance to take into account when comparing off-diagonal elements
        
            Returns:
                :code:`true` if this is a symmetric matrix, :code:`false` otherwise
        
            Is this a symmetric matrix?
        
            This method indicates if the matrix is symmetric.
        
        
            To do so, the method checks that symmetric off-diagonal elements are numerically equal. Two elements are considered to
            have different values if their absolute and relative differences are both above the specified tolerances.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isSymmetric` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                relativeTolerance (double): the relative tolerance to take into account when comparing off-diagonal elements
                absoluteTolerance (double): the absolute tolerance to take into account when comparing off-diagonal elements
        
            Returns:
                :code:`true` if this is a symmetric matrix, :code:`false` otherwise
        
        
        """
        ...
    @typing.overload
    def isSymmetric(self, double: float, double2: float) -> bool: ...
    @typing.overload
    def multiply(self, diagonalMatrix: 'DiagonalMatrix', double: float) -> RealMatrix:
        """
            Returns the result of postmultiplying this matrix by the matrix :code:`m` or its transpose :code:`m` :sup:`T` .
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.multiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix by which to postmultiply this matrix by
                toTranspose (boolean): whether to compute the product :code:`this`×:code:`m` (:code:`toTranspose=false` ), or the product
                    :code:`this`×:code:`m` :sup:`T` (:code:`toTranspose=true`)
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`m` or :code:`this` ×:code:`m` :sup:`T`
        
            Returns the result of postmultiplying this matrix by the matrix :code:`m` or its transpose :code:`m` :sup:`T` , then by
            the scalar :code:`d`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.multiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix by which to multiply this matrix by
                toTranspose (boolean): whether to compute the product :code:`this`×:code:`m`×:code:`d` ( :code:`toTranspose=false`), or the product
                    :code:`this`×:code:`m` :sup:`T` ×:code:`d` (:code:`toTranspose=true`)
                d (double): the scalar by which to multiply the resulting matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`m`×:code:`d` or :code:`this`×:code:`m` :sup:`T` ×:code:`d`
        
            Returns the result of postmultiplying this matrix by the diagonal matrix :code:`m`, then by the scalar :code:`d`.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix`): the diagonal matrix by which to multiply this matrix by
                d (double): the scalar by which to multiply the resulting matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`m`×:code:`d` or :code:`this`×:code:`m` :sup:`T` ×:code:`d`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the matrices are not multiplication compatible
        
        
        """
        ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Returns the result of postmultiplying this matrix by the matrix :code:`m`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.multiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix by which to postmultiply this matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`m`
        
        """
        ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix, boolean: bool, double: float) -> RealMatrix: ...
    def multiplyEntry(self, int: int, int2: int, double: float) -> None:
        """
            Multiplies (in place) the specified entry of :code:`this` matrix by a given value.
        
            Row and column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.multiplyEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                row (int): the row index of the entry to be modified
                column (int): the column index of the entry to be modified
                factor (double): the multiplication factor for the matrix entry
        
        
        """
        ...
    @typing.overload
    def operate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
            Returns the result of postmultiplying this matrix by the vector :code:`v`.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                v (double[]): the vector by which to multiply this matrix by
        
            Returns:
                the column vector resulting from the product :code:`this`×:code:`v`
        
            Returns the result of multiplying :code:`this` by the vector :code:`x`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.operate` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator.operate` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.RealLinearOperator`
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the vector to operate on
        
            Returns:
                the product of :code:`this` instance with :code:`x`
        
        
        """
        ...
    @typing.overload
    def operate(self, realVector: RealVector) -> RealVector: ...
    def power(self, int: int) -> RealMatrix:
        """
            Returns the the result of multiplying this matrix with itself :code:`p` times.
        
            The exponent :code:`p` must be positive or equal to zero.
        
        
            This operation is only supported for square matrices.
        
        
            Depending on the underlying storage, numerical instabilities might occur for high powers.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.power` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                p (int): the exponent :code:`p` to which this matrix is to be raised
        
            Returns:
                the matrix resulting from raising this matrix to the power of :code:`p`
        
        
        """
        ...
    @typing.overload
    def preMultiply(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
            Returns the result of premultiplying this matrix by the matrix :code:`m`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.preMultiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix M by which to premultiply this matrix by
        
            Returns:
                the matrix resulting from the product :code:`m`×:code:`this`
        
            Returns the result of premultiplying this matrix by the vector :code:`v`.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                v (double[]): the row vector by which to premultiply this matrix by
        
            Returns:
                the row vector resulting from the product :code:`v`×:code:`this`
        
            Returns the result of premultiplying this matrix by the vector :code:`v`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.preMultiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the vector by which to premultiply this matrix by
        
            Returns:
                the row vector resulting from the product :code:`v`×:code:`this`
        
        
        """
        ...
    @typing.overload
    def preMultiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def preMultiply(self, realVector: RealVector) -> RealVector: ...
    def scalarAdd(self, double: float) -> RealMatrix:
        """
            Returns the result of adding a scalar :code:`d` to the entries of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.scalarAdd` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                d (double): the scalar value to be added to the entries of this matrix
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`d`
        
        
        """
        ...
    def scalarMultiply(self, double: float) -> RealMatrix:
        """
            Returns the result of multiplying the entries of this matrix by the scalar :code:`d`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.scalarMultiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                d (double): the scalar value by which to multiply the entries of this matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`d`
        
        
        """
        ...
    def setColumn(self, int: int, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Replaces the entries of a given column with the entries of the specified data array.
        
            Column indices start at 0.
        
        
            The size of the provided data array must match the row dimension of this matrix.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                column (int): the index of the column to be replaced
                array (double[]): the column data array to be copied
        
        
        """
        ...
    def setColumnMatrix(self, int: int, realMatrix: RealMatrix) -> None:
        """
            Replaces the entries of a given column with the entries of the specified column matrix.
        
            Column indices start at 0.
        
        
            The provided matrix must have one column and the same number of rows as this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setColumnMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                column (int): the index of the column to be replaced
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the column matrix to be copied
        
        
        """
        ...
    def setColumnVector(self, int: int, realVector: RealVector) -> None:
        """
            Replaces the entries of a given column with the entries of the specified vector.
        
            Column indices start at 0.
        
        
            The size of the provided vector must match the row dimension of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setColumnVector` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                column (int): the index of the column to be replaced
                vector (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the column vector to be copied
        
        
        """
        ...
    def setDefaultDecomposition(self, function: typing.Union[java.util.function.Function[RealMatrix, typing.Union[Decomposition, typing.Callable]], typing.Callable[[RealMatrix], typing.Union[Decomposition, typing.Callable]]]) -> None: ...
    def setEntry(self, int: int, int2: int, double: float) -> None:
        """
            Sets the entry at the specified row and column to a new value.
        
            Row and column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                row (int): the row index of entry to be set
                column (int): the column index of entry to be set
                value (double): the new value of the entry
        
        
        """
        ...
    def setRow(self, int: int, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Replaces the entries of a given row with the entries of the specified data array.
        
            Row indices start at 0.
        
        
            The size of the provided data array must match the column dimension of this matrix.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                row (int): the index of the row to be replaced
                array (double[]): the row data array to be copied
        
        
        """
        ...
    def setRowMatrix(self, int: int, realMatrix: RealMatrix) -> None:
        """
            Replaces the entries of a given row with the entries of the specified row matrix.
        
            Row indices start at 0.
        
        
            The provided matrix must have one row and the same number of columns as this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setRowMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                row (int): the index of the row to be replaced
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the row matrix to be copied
        
        
        """
        ...
    def setRowVector(self, int: int, realVector: RealVector) -> None:
        """
            Replaces the entries of a given row with the entries of the specified vector.
        
            Row indices start at 0.
        
        
            The size of the provided vector must match the column dimension of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setRowVector` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                row (int): the index of the row to be replaced
                vector (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the row vector to be copied
        
        
        """
        ...
    def setSubMatrix(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int: int, int2: int) -> None:
        """
            Replaces part of the matrix with a given submatrix, starting at the specified row and column.
        
            Rows and columns are indicated counting from 0 to n-1.
        
        
            **Usage example:**
        
            .. code-block: java
            
            
             // Initial matrix
             matrix = [a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                      [a :sub:`10` , a :sub:`11` , a :sub:`21` ]
                      [a :sub:`20` , a :sub:`21` , a :sub:`22` ]
             // Submatrix
             subMatrix = [b :sub:`00` , b :sub:`01` ]
                         [b :sub:`10` , b :sub:`11` ]
                        
             // Replace part of the initial matrix 
             matrix.setSubMatrix(subMatrix, 1, 1) =>[a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                                                    [a :sub:`10` , b :sub:`00` , b :sub:`01` ]
                                                    [a :sub:`20` , b :sub:`10` , b :sub:`11` ]
             
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                subMatrix (double[][]): the array containing the submatrix replacement data
                row (int): the row coordinate of the top, left element to be replaced
                column (int): the column coordinate of the top, left element to be replaced
        
        
        """
        ...
    def subtract(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Returns the result of subtracting the matrix :code:`m` from this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.subtract` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be subtracted
        
            Returns:
                the matrix resulting from the subtraction :code:`this`-:code:`m`
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str:
        """
            Get a string representation for this matrix.
        
            Default format is :meth:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils.VISUAL_FORMAT`.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation for this matrix
        
        """
        ...
    @typing.overload
    def toString(self, realMatrixFormat: RealMatrixFormat) -> str:
        """
            Gets a string representation of this matrix using the specified format.
        
            Several predefined matrix formats are available in :class:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.toString` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                realMatrixFormat (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixFormat`): the matrix format to be used
        
            Returns:
                a string representation of this matrix
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils.JAVA_FORMAT`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils.OCTAVE_FORMAT`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils.VISUAL_FORMAT`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.MatrixUtils.SUMMARY_FORMAT`
        
        
        """
        ...
    @typing.overload
    def transpose(self) -> RealMatrix:
        """
            Returns the transpose of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Returns:
                the transpose of this matrix
        
        """
        ...
    @typing.overload
    def transpose(self, boolean: bool) -> RealMatrix:
        """
            Returns the transpose of this matrix.
        
            If :code:`forceCopy` is :code:`true`, the returned matrix is guaranteed to be a new instance, which can be modified
            without any risk of impacting the current instance. Otherwise, this method may simply return the current instance when
            the matrix is its own transpose (symmetric matrix).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                forceCopy (boolean): if :code:`true`, the transpose of the matrix is systematically stored in a new matrix; otherwise the method may return
                    the current instance when the matrix is its own transpose
        
            Returns:
                the transpose of this matrix
        
        
        """
        ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visits (and possibly change) all matrix entries in column order.
        
            Column order starts at upper left element, iterating through all elements of a column from top to bottom before going to
            the topmost element of the next column.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) all matrix entries in column order.
        
            Column order starts at upper left element, iterating through all elements of a column from top to bottom before going to
            the topmost element of the next column.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (and possibly change) some matrix entries in column order.
        
            Column order starts at upper left element, iterating through all elements of a column from top to bottom before going to
            the topmost element of the next column.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) some matrix entries in column order.
        
            Column order starts at upper left element, iterating through all elements of a column from top to bottom before going to
            the topmost element of the next column.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visits (and possibly change) all matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) all matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (and possibly change) some matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) some matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visits (and possibly change) all matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) all matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (and possibly change) some matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) some matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...

class ConjugateGradient(PreconditionedIterativeLinearSolver):
    OPERATOR: typing.ClassVar[str] = ...
    VECTOR: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, iterationManager: fr.cnes.sirius.patrius.math.util.IterationManager, double: float, boolean: bool): ...
    @typing.overload
    def __init__(self, int: int, double: float, boolean: bool): ...
    def getCheck(self) -> bool: ...
    @typing.overload
    def solveInPlace(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...
    @typing.overload
    def solveInPlace(self, realLinearOperator: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...

class SymmLQ(PreconditionedIterativeLinearSolver):
    @typing.overload
    def __init__(self, iterationManager: fr.cnes.sirius.patrius.math.util.IterationManager, double: float, boolean: bool): ...
    @typing.overload
    def __init__(self, int: int, double: float, boolean: bool): ...
    def getCheck(self) -> bool: ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector) -> RealVector: ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector, boolean: bool, double: float) -> RealVector: ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realVector: RealVector) -> RealVector: ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realVector: RealVector, boolean: bool, double: float) -> RealVector: ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...
    @typing.overload
    def solveInPlace(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...
    @typing.overload
    def solveInPlace(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector, realVector2: RealVector, boolean: bool, double: float) -> RealVector: ...
    @typing.overload
    def solveInPlace(self, realLinearOperator: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...

class SymmetricMatrix(RealMatrix):
    """
    public interface SymmetricMatrix extends :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
    
        Interface for symmetric matrices.
    """
    @typing.overload
    def add(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Returns the result of adding the symmetric matrix :code:`m` to this matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`): the matrix to be added
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`m`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the matrix :code:`m` is not the same size as this matrix
        
        
        """
        ...
    @typing.overload
    def add(self, symmetricMatrix: 'SymmetricMatrix') -> 'SymmetricMatrix': ...
    def copy(self) -> 'SymmetricMatrix':
        """
            Returns a deep copy of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.copy` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Returns:
                a deep copy of this matrix
        
        
        """
        ...
    def createMatrix(self, int: int, int2: int) -> 'SymmetricMatrix':
        """
            Creates a new matrix of the same type as this matrix.
        
            The returned matrix is filled with zeros. Its size is determined by the specified row and column dimensions, which must
            both be strictly positive. Additional constraints on the dimensions may apply depending on the implementation (for
            example, symmetric matrices must be square, which implies that the row and column dimensions must be equal).
        
            *Since the matrix build is a symmetric matrix, the row and column dimensions are expected to be equal.*
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.createMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                rowDimension (int): the number of rows in the new matrix
                columnDimension (int): the number of columns in the new matrix
        
            Returns:
                a new matrix of the same type as this matrix
        
        
        """
        ...
    def equals(self, realMatrix: RealMatrix, double: float, double2: float) -> bool: ...
    def getDiagonal(self) -> typing.MutableSequence[float]:
        """
            Gets the diagonal vector from this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getDiagonal` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Returns:
                the diagonal vector from this matrix
        
        
        """
        ...
    @typing.overload
    def getInverse(self) -> 'SymmetricMatrix':
        """
            Gets the inverse (or pseudo-inverse) of this matrix using the default decomposition.
        
            The default decomposition builder can be changed using the
            :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setDefaultDecomposition` method.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Returns:
                the inverse matrix
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getDefaultDecomposition`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setDefaultDecomposition`
        
        :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix` getInverse(`Function <http://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`,:class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`> decompositionBuilder)
        
            Gets the inverse (or pseudo-inverse) of this matrix using the given decomposition algorithm.
        
            The decomposition builder is a function capable of generating new instances of the decomposition algorithm to be used
            for the computation of the inverse matrix (like the :class:`~fr.cnes.sirius.patrius.math.linear.QRDecomposition` or the
            :class:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition`, for instance).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                decompositionBuilder (`Function <http://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`,:class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`> decompositionBuilder): the decomposition builder to use
        
            Returns:
                the inverse matrix
        
        
        """
        ...
    @typing.overload
    def getInverse(self, function: typing.Union[java.util.function.Function[RealMatrix, typing.Union[Decomposition, typing.Callable]], typing.Callable[[RealMatrix], typing.Union[Decomposition, typing.Callable]]]) -> 'SymmetricMatrix': ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> RealMatrix: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> RealMatrix:
        """
            Extracts the submatrix corresponding to the specified indices.
        
            This method uses the same start/end indices to select the rows and columns to be extracted. These indices must be valid
            indices with respect to the dimensions of the matrix (valid indices range from 0 to n-1, with n the row/column dimension
            of the matrix). Calling this method is equivalent to calling
            :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getSubMatrix` using the same start/end indices for the rows and
            columns. The extracted submatrix is guaranteed to be symmetric. It will also remain positive semi-definite if the
            initial matrix originally is.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             // Initial matrix
             matrix = [a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                      [a :sub:`10` , a :sub:`11` , a :sub:`21` ]
                      [a :sub:`20` , a :sub:`21` , a :sub:`22` ]
             
             // Submatrix extraction
             matrix.getSubMatrix(1, 2) => [a :sub:`11` , a :sub:`21` ]
                                          [a :sub:`21` , a :sub:`22` ]
             
        
            Parameters:
                startIndex (int): the initial row/column index
                endIndex (int): the final row/column index (inclusive)
        
            Returns:
                the extracted submatrix
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int) -> 'SymmetricMatrix': ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray]) -> 'SymmetricMatrix':
        """
            Extracts the submatrix corresponding to the specified indices.
        
            This method uses a single index array to select the rows and columns to be extracted. All indices must be valid indices
            with respect to the dimensions of the matrix (valid indices range from 0 to n-1, with n the row/column dimension of the
            matrix). The provided index array is allowed to contain duplicates. Calling this method is equivalent to calling
            RealMatrix.getSubMatrix(int[], int[]) using the provided index array for the selected rows and columns. This method can
            be used to extract any submatrix and perform a symmetric reordering of its rows/columns. The extracted submatrix is
            guaranteed to be symmetric. It will also remain positive semi-definite if the initial matrix originally is.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             // Initial matrix
             matrix = [a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                      [a :sub:`10` , a :sub:`11` , a :sub:`21` ]
                      [a :sub:`20` , a :sub:`21` , a :sub:`22` ]
             
             // Submatrix extraction
             matrix.getSubMatrix([1, 2]) => [a :sub:`11` , a :sub:`21` ]
                                            [a :sub:`21` , a :sub:`22` ]
             
             // Rows/Columns permutation
             matrix.getSubMatrix([1, 2, 0]) => [a :sub:`11` , a :sub:`21` , a :sub:`10` ]
                                               [a :sub:`21` , a :sub:`22` , a :sub:`20` ]
                                               [a :sub:`10` , a :sub:`20` , a :sub:`00` ]
             
             // Submatrix extraction (with duplicated indices)
             matrix.getSubMatrix([1, 2, 0, 1, 0]) 
                  => [a :sub:`11` , a :sub:`21` , a :sub:`10` , a :sub:`11` , a :sub:`10` ]
                     [a :sub:`21` , a :sub:`22` , a :sub:`20` , a :sub:`21` , a :sub:`20` ]
                     [a :sub:`10` , a :sub:`20` , a :sub:`00` , a :sub:`10` , a :sub:`00` ]
                     [a :sub:`11` , a :sub:`21` , a :sub:`10` , a :sub:`11` , a :sub:`10` ]
                     [a :sub:`10` , a :sub:`20` , a :sub:`00` , a :sub:`10` , a :sub:`00` ]
             
        
            Parameters:
                indices (int[]): the selected indices
        
            Returns:
                the extracted submatrix
        
        
        """
        ...
    def power(self, int: int) -> 'SymmetricMatrix':
        """
            Returns the the result of multiplying this matrix with itself :code:`p` times.
        
            The exponent :code:`p` must be positive or equal to zero.
        
        
            This operation is only supported for square matrices.
        
        
            Depending on the underlying storage, numerical instabilities might occur for high powers.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.power` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                p (int): the exponent :code:`p` to which this matrix is to be raised
        
            Returns:
                the matrix resulting from raising this matrix to the power of :code:`p`
        
        
        """
        ...
    @typing.overload
    def quadraticMultiplication(self, realMatrix: RealMatrix) -> 'SymmetricMatrix':
        """
            Returns the result of the quadratic multiplication M×:code:`this`×M :sup:`T` , where M is the provided matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix M
        
            Returns:
                the matrix resulting from the quadratic multiplication M×:code:`this` ×M :sup:`T`
        
            Returns the result of the quadratic multiplication M×:code:`this`×M :sup:`T` , where M or M :sup:`T` is the provided
            matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix M or the matrix M :sup:`T`
                isTranspose (boolean): if :code:`true`, assumes the provided matrix is M :sup:`T` , otherwise assumes it is M
        
            Returns:
                the matrix resulting from the quadratic multiplication M×:code:`this` ×M :sup:`T`
        
        
        """
        ...
    @typing.overload
    def quadraticMultiplication(self, realMatrix: RealMatrix, boolean: bool) -> 'SymmetricMatrix': ...
    def scalarAdd(self, double: float) -> 'SymmetricMatrix':
        """
            Returns the result of adding a scalar :code:`d` to the entries of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.scalarAdd` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                d (double): the scalar value to be added to the entries of this matrix
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`d`
        
        
        """
        ...
    def scalarMultiply(self, double: float) -> 'SymmetricMatrix':
        """
            Returns the result of multiplying the entries of this matrix by the scalar :code:`d`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.scalarMultiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                d (double): the scalar value by which to multiply the entries of this matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`d`
        
        
        """
        ...
    @typing.overload
    def subtract(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Returns the result of subtracting the symmetric matrix :code:`m` from this matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`): the matrix to be subtracted
        
            Returns:
                the matrix resulting from the subtraction :code:`this`-:code:`m`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the matrix :code:`m` is not the same size as this matrix
        
        
        """
        ...
    @typing.overload
    def subtract(self, symmetricMatrix: 'SymmetricMatrix') -> 'SymmetricMatrix': ...
    def toString(self, realMatrixFormat: RealMatrixFormat) -> str: ...
    @typing.overload
    def transpose(self) -> 'SymmetricMatrix':
        """
            Returns the transpose of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Returns:
                the transpose of this matrix
        
        """
        ...
    @typing.overload
    def transpose(self, boolean: bool) -> 'SymmetricMatrix':
        """
            Returns the transpose of this matrix.
        
            If :code:`forceCopy` is :code:`true`, the returned matrix is guaranteed to be a new instance, which can be modified
            without any risk of impacting the current instance. Otherwise, this method may simply return the current instance when
            the matrix is its own transpose (symmetric matrix).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Parameters:
                forceCopy (boolean): if :code:`true`, the transpose of the matrix is systematically stored in a new matrix; otherwise the method may return
                    the current instance when the matrix is its own transpose
        
            Returns:
                the transpose of this matrix
        
        
        """
        ...

_Array2DRowFieldMatrix__T = typing.TypeVar('_Array2DRowFieldMatrix__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
class Array2DRowFieldMatrix(AbstractFieldMatrix[_Array2DRowFieldMatrix__T], java.io.Serializable, typing.Generic[_Array2DRowFieldMatrix__T]):
    @typing.overload
    def __init__(self, field: fr.cnes.sirius.patrius.math.Field[_Array2DRowFieldMatrix__T]): ...
    @typing.overload
    def __init__(self, field: fr.cnes.sirius.patrius.math.Field[_Array2DRowFieldMatrix__T], tArray: typing.Union[typing.List[_Array2DRowFieldMatrix__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, field: fr.cnes.sirius.patrius.math.Field[_Array2DRowFieldMatrix__T], tArray: typing.Union[typing.List[typing.MutableSequence[_Array2DRowFieldMatrix__T]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, field: fr.cnes.sirius.patrius.math.Field[_Array2DRowFieldMatrix__T], tArray: typing.Union[typing.List[typing.MutableSequence[_Array2DRowFieldMatrix__T]], jpype.JArray], boolean: bool): ...
    @typing.overload
    def __init__(self, field: fr.cnes.sirius.patrius.math.Field[_Array2DRowFieldMatrix__T], int: int, int2: int): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_Array2DRowFieldMatrix__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[typing.MutableSequence[_Array2DRowFieldMatrix__T]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[typing.MutableSequence[_Array2DRowFieldMatrix__T]], jpype.JArray], boolean: bool): ...
    @typing.overload
    def add(self, array2DRowFieldMatrix: 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]) -> 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def add(self, fieldMatrix: FieldMatrix[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    def addToEntry(self, int: int, int2: int, t: _Array2DRowFieldMatrix__T) -> None: ...
    def copy(self) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    def createMatrix(self, int: int, int2: int) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    def getColumnDimension(self) -> int: ...
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[_Array2DRowFieldMatrix__T]]: ...
    def getDataRef(self) -> typing.MutableSequence[typing.MutableSequence[_Array2DRowFieldMatrix__T]]: ...
    def getEntry(self, int: int, int2: int) -> _Array2DRowFieldMatrix__T: ...
    def getRowDimension(self) -> int: ...
    @typing.overload
    def multiply(self, array2DRowFieldMatrix: 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]) -> 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def multiply(self, fieldMatrix: FieldMatrix[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    def multiplyEntry(self, int: int, int2: int, t: _Array2DRowFieldMatrix__T) -> None: ...
    @typing.overload
    def operate(self, tArray: typing.Union[typing.List[_Array2DRowFieldMatrix__T], jpype.JArray]) -> typing.MutableSequence[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def operate(self, fieldVector: FieldVector[_Array2DRowFieldMatrix__T]) -> FieldVector[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, tArray: typing.Union[typing.List[_Array2DRowFieldMatrix__T], jpype.JArray]) -> typing.MutableSequence[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldMatrix: FieldMatrix[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldVector: FieldVector[_Array2DRowFieldMatrix__T]) -> FieldVector[_Array2DRowFieldMatrix__T]: ...
    def setEntry(self, int: int, int2: int, t: _Array2DRowFieldMatrix__T) -> None: ...
    def setSubMatrix(self, tArray: typing.Union[typing.List[typing.MutableSequence[_Array2DRowFieldMatrix__T]], jpype.JArray], int: int, int2: int) -> None: ...
    @typing.overload
    def subtract(self, array2DRowFieldMatrix: 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]) -> 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def subtract(self, fieldMatrix: FieldMatrix[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_Array2DRowFieldMatrix__T]) -> _Array2DRowFieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_Array2DRowFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _Array2DRowFieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_Array2DRowFieldMatrix__T]) -> _Array2DRowFieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_Array2DRowFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _Array2DRowFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_Array2DRowFieldMatrix__T]) -> _Array2DRowFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_Array2DRowFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _Array2DRowFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_Array2DRowFieldMatrix__T]) -> _Array2DRowFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_Array2DRowFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _Array2DRowFieldMatrix__T: ...

class Array2DRowRealMatrix(AbstractRealMatrix):
    """
    public class Array2DRowRealMatrix extends :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
    
        Implementation of :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` using a :code:`double[][]` array to store
        entries.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], boolean: bool): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    @typing.overload
    def add(self, array2DRowRealMatrix: 'Array2DRowRealMatrix') -> 'Array2DRowRealMatrix':
        """
            Returns the result of adding a matrix M to this matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix`): the matrix M to be added
        
            Returns:
                the matrix resulting from the sum :code:`this` + M
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the matrix M is not the same size as this matrix
        
        
        """
        ...
    @typing.overload
    def add(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def addToEntry(self, int: int, int2: int, double: float) -> None:
        """
            Adds (in place) a given value to the specified entry of this matrix.
        
            Row and column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.addToEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.addToEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the row index of the entry to be modified
                column (int): the column index of the entry to be modified
                increment (double): the value to add to the matrix entry
        
        
        """
        ...
    def copy(self) -> RealMatrix:
        """
            Returns a deep copy of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.copy` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.copy` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                a deep copy of this matrix
        
        
        """
        ...
    @typing.overload
    def copySubMatrix(self, int: int, int2: int, int3: int, int4: int, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int5: int, int6: int) -> None: ...
    @typing.overload
    def copySubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray], doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int3: int, int4: int) -> None:
        """
            Copies a submatrix into a given 2D array.
        
            Rows and columns are indicated counting from 0 to n-1. The submatrix data is copied in the upper-left part of the
            destination array. Elements which are not overwritten by the submatrix data are left unchanged (for example, if the
            destination array is larger than the size of the extracted submatrix).
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
                destination (double[][]): the 2D array where the submatrix data should be copied
        
        """
        ...
    @typing.overload
    def copySubMatrix(self, int: int, int2: int, int3: int, int4: int, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None: ...
    @typing.overload
    def copySubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray], doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None:
        """
            Copies a submatrix into a given 2D array.
        
            Rows and columns are indicated counting from 0 to n-1. The submatrix data is copied in the upper-left part of the
            destination array. Elements which are not overwritten by the submatrix data are left unchanged (for example, if the
            destination array is larger than the size of the extracted submatrix).
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                selectedRows (int[]): the selected row indices
                selectedColumns (int[]): the selected column indices
                destination (double[][]): the 2D array where the submatrix data should be copied
        
        
        """
        ...
    def createMatrix(self, int: int, int2: int) -> RealMatrix:
        """
            Creates a new matrix of the same type as this matrix.
        
            The returned matrix is filled with zeros. Its size is determined by the specified row and column dimensions, which must
            both be strictly positive. Additional constraints on the dimensions may apply depending on the implementation (for
            example, symmetric matrices must be square, which implies that the row and column dimensions must be equal).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.createMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.createMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                rowDimension (int): the number of rows in the new matrix
                columnDimension (int): the number of columns in the new matrix
        
            Returns:
                a new matrix of the same type as this matrix
        
        
        """
        ...
    def getColumnDimension(self) -> int:
        """
            Returns the dimension of the domain of this operator.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix.getColumnDimension` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getColumnDimension` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the number of columns of the underlying matrix
        
        
        """
        ...
    @typing.overload
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Returns a 2D array containing the entries of the matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getData` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getData` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                a 2D array containing the entries of the matrix
        
        """
        ...
    @typing.overload
    def getData(self, boolean: bool) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Returns a 2D array containing the entries of the matrix.
        
            If :code:`forceCopy` is :code:`true`, the returned array is guaranteed to be free of references to any internal data
            array (thus, can be safely modified). Otherwise, the returned array may contain references to internal data arrays (for
            optimization purposes). Note that setting :code:`forceCopy` to :code:`false` does not guarantee the returned array
            references an internal data array. For instance, implementations that do not store the entries of the matrix in a 2D
            array have to rebuild a new array each time this method is called, regardless of this parameter.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getData` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getData` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                forceCopy (boolean): if :code:`true`, the entries of the matrix are systematically stored in a new array; otherwise the returned array may
                    reference internal data arrays
        
            Returns:
                a 2D array containing entries of the matrix
        
        
        """
        ...
    def getDataRef(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Gets a direct reference to the underlying data array storing the entries of the matrix.
        
            Returns:
                the underlying data array storing the entries of the matrix
        
        
        """
        ...
    def getEntry(self, int: int, int2: int) -> float:
        """
            Gets the entry at the specified row and column.
        
            Row and column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the row index of entry to be fetched
                column (int): the column index of entry to be fetched
        
            Returns:
                the matrix entry at the specified row and column
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
            Returns the dimension of the codomain of this operator.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix.getRowDimension` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getRowDimension` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the number of rows of the underlying matrix
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> RealMatrix:
        """
            Gets a submatrix.
        
            Rows and columns are indicated counting from 0 to n-1.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getSubMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getSubMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
        
            Returns:
                the submatrix containing the data of the specified rows and columns
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> RealMatrix:
        """
            Gets a submatrix.
        
            Rows and columns are indicated counting from 0 to n-1.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                selectedRows (int[]): the selected row indices
                selectedColumns (int[]): the selected column indices
        
            Returns:
                the submatrix containing the data in the specified rows and columns
        
        
        """
        ...
    @typing.overload
    def multiply(self, array2DRowRealMatrix: 'Array2DRowRealMatrix') -> 'Array2DRowRealMatrix':
        """
            Returns the result of postmultiplying this matrix by the matrix :code:`m` or its transpose :code:`m` :sup:`T` , then by
            the scalar :code:`d`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.multiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.multiply` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix by which to multiply this matrix by
                toTranspose (boolean): whether to compute the product :code:`this`×:code:`m`×:code:`d` ( :code:`toTranspose=false`), or the product
                    :code:`this`×:code:`m` :sup:`T` ×:code:`d` (:code:`toTranspose=true`)
                d (double): the scalar by which to multiply the resulting matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`m`×:code:`d` or :code:`this`×:code:`m` :sup:`T` ×:code:`d`
        
            Returns the result of postmultiplying this matrix by a matrix M.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix`): the matrix M by which to multiply this matrix by
        
            Returns:
                the matrix resulting from the product :code:`this` × M
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the matrices are not multiplication compatible
        
            Returns the result of postmultiplying this matrix by a matrix M or by its transpose M :sup:`T` .
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix`): the matrix M by which to multiply this matrix by
                toTranspose (boolean): whether to compute the product :code:`this` × M (:code:`toTranspose=false`), or the product :code:`this` × M :sup:`T`
                    (:code:`toTranspose=true`)
        
            Returns:
                the matrix resulting from the product :code:`this` × M or :code:`this` × M :sup:`T`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the matrices are not multiplication compatible
        
            Returns the result of postmultiplying this matrix by a matrix M or by its transpose M :sup:`T` , then by a scalar
            :code:`d`.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix`): the matrix M by which to multiply this matrix by
                toTranspose (boolean): whether to compute the product :code:`this` × M ×:code:`d` ( :code:`toTranspose=false`), or the product :code:`this`
                    × M :sup:`T` × :code:`d` (:code:`toTranspose=true`)
                d (double): the scalar by which to multiply the resulting matrix by
        
            Returns:
                the matrix resulting from the product :code:`this` × M × :code:`d` or :code:`this` × M :sup:`T` × :code:`d`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if the matrices are not multiplication compatible
        
        
        """
        ...
    @typing.overload
    def multiply(self, array2DRowRealMatrix: 'Array2DRowRealMatrix', boolean: bool) -> 'Array2DRowRealMatrix': ...
    @typing.overload
    def multiply(self, array2DRowRealMatrix: 'Array2DRowRealMatrix', boolean: bool, double: float) -> 'Array2DRowRealMatrix': ...
    @typing.overload
    def multiply(self, diagonalMatrix: 'DiagonalMatrix', double: float) -> RealMatrix: ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix, boolean: bool, double: float) -> RealMatrix: ...
    def multiplyEntry(self, int: int, int2: int, double: float) -> None:
        """
            Multiplies (in place) the specified entry of :code:`this` matrix by a given value.
        
            Row and column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.multiplyEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.multiplyEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the row index of the entry to be modified
                column (int): the column index of the entry to be modified
                factor (double): the multiplication factor for the matrix entry
        
        
        """
        ...
    @typing.overload
    def operate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
            Returns the result of postmultiplying this matrix by the vector :code:`v`.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                v (double[]): the vector by which to multiply this matrix by
        
            Returns:
                the column vector resulting from the product :code:`this`×:code:`v`
        
        
        """
        ...
    @typing.overload
    def operate(self, realVector: RealVector) -> RealVector: ...
    @typing.overload
    def preMultiply(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
            Returns the result of premultiplying this matrix by the vector :code:`v`.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                v (double[]): the row vector by which to premultiply this matrix by
        
            Returns:
                the row vector resulting from the product :code:`v`×:code:`this`
        
        
        """
        ...
    @typing.overload
    def preMultiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def preMultiply(self, realVector: RealVector) -> RealVector: ...
    def setEntry(self, int: int, int2: int, double: float) -> None:
        """
            Sets the entry at the specified row and column to a new value.
        
            Row and column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.setEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the row index of entry to be set
                column (int): the column index of entry to be set
                value (double): the new value of the entry
        
        
        """
        ...
    def setSubMatrix(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int: int, int2: int) -> None:
        """
            Replaces part of the matrix with a given submatrix, starting at the specified row and column.
        
            Rows and columns are indicated counting from 0 to n-1.
        
        
            **Usage example:**
        
            .. code-block: java
            
            
             // Initial matrix
             matrix = [a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                      [a :sub:`10` , a :sub:`11` , a :sub:`21` ]
                      [a :sub:`20` , a :sub:`21` , a :sub:`22` ]
             // Submatrix
             subMatrix = [b :sub:`00` , b :sub:`01` ]
                         [b :sub:`10` , b :sub:`11` ]
                        
             // Replace part of the initial matrix 
             matrix.setSubMatrix(subMatrix, 1, 1) =>[a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                                                    [a :sub:`10` , b :sub:`00` , b :sub:`01` ]
                                                    [a :sub:`20` , b :sub:`10` , b :sub:`11` ]
             
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                subMatrix (double[][]): the array containing the submatrix replacement data
                row (int): the row coordinate of the top, left element to be replaced
                column (int): the column coordinate of the top, left element to be replaced
        
        
        """
        ...
    @typing.overload
    def subtract(self, array2DRowRealMatrix: 'Array2DRowRealMatrix') -> 'Array2DRowRealMatrix':
        """
            Returns the result of subtracting a matrix M from this matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix`): matrix to be subtracted
        
            Returns:
                the matrix resulting from the subtraction :code:`this` - M
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the matrix M is not the same size as this matrix
        
        
        """
        ...
    @typing.overload
    def subtract(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def transpose(self) -> RealMatrix:
        """
            Returns the transpose of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.transpose` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the transpose of this matrix
        
        
        """
        ...
    @typing.overload
    def transpose(self, boolean: bool) -> RealMatrix: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visits (and possibly change) all matrix entries in column order.
        
            Column order starts at upper left element, iterating through all elements of a column from top to bottom before going to
            the topmost element of the next column.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInColumnOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) all matrix entries in column order.
        
            Column order starts at upper left element, iterating through all elements of a column from top to bottom before going to
            the topmost element of the next column.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInColumnOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (and possibly change) some matrix entries in column order.
        
            Column order starts at upper left element, iterating through all elements of a column from top to bottom before going to
            the topmost element of the next column.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInColumnOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) some matrix entries in column order.
        
            Column order starts at upper left element, iterating through all elements of a column from top to bottom before going to
            the topmost element of the next column.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInColumnOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visits (and possibly change) all matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInRowOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) all matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInRowOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (and possibly change) some matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInRowOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) some matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInRowOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...

class ArrayRowSymmetricMatrix(AbstractRealMatrix, SymmetricMatrix):
    @typing.overload
    def __init__(self, symmetryType: 'ArrayRowSymmetricMatrix.SymmetryType', doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, symmetryType: 'ArrayRowSymmetricMatrix.SymmetryType', doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], double2: float, double3: float): ...
    @typing.overload
    def __init__(self, symmetryType: 'ArrayRowSymmetricMatrix.SymmetryType', realMatrix: RealMatrix): ...
    @typing.overload
    def __init__(self, symmetryType: 'ArrayRowSymmetricMatrix.SymmetryType', realMatrix: RealMatrix, double: float, double2: float): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def add(self, diagonalMatrix: 'DiagonalMatrix') -> 'ArrayRowSymmetricMatrix': ...
    @typing.overload
    def add(self, symmetricMatrix: SymmetricMatrix) -> 'ArrayRowSymmetricMatrix': ...
    @typing.overload
    def add(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def addToEntry(self, int: int, int2: int, double: float) -> None: ...
    @typing.overload
    def concatenateDiagonally(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def concatenateDiagonally(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    @typing.overload
    def concatenateDiagonally(self, realMatrix: RealMatrix, boolean: bool, boolean2: bool) -> RealMatrix: ...
    @typing.overload
    def concatenateHorizontally(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def concatenateHorizontally(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    @typing.overload
    def concatenateVertically(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def concatenateVertically(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    def copy(self) -> 'ArrayRowSymmetricMatrix': ...
    @staticmethod
    def createIdentityMatrix(int: int) -> 'ArrayRowSymmetricMatrix': ...
    def createMatrix(self, int: int, int2: int) -> 'ArrayRowSymmetricMatrix': ...
    @typing.overload
    def equals(self, realMatrix: RealMatrix, double: float, double2: float) -> bool: ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool: ...
    def getColumnDimension(self) -> int: ...
    def getColumnMatrix(self, int: int) -> RealMatrix: ...
    @staticmethod
    def getDefaultAbsoluteSymmetryThreshold() -> float: ...
    @staticmethod
    def getDefaultRelativeSymmetryThreshold() -> float: ...
    def getEntry(self, int: int, int2: int) -> float: ...
    @typing.overload
    def getInverse(self) -> 'ArrayRowSymmetricMatrix': ...
    @typing.overload
    def getInverse(self, function: typing.Union[java.util.function.Function[RealMatrix, typing.Union[Decomposition, typing.Callable]], typing.Callable[[RealMatrix], typing.Union[Decomposition, typing.Callable]]]) -> 'ArrayRowSymmetricMatrix': ...
    def getRowDimension(self) -> int: ...
    def getRowMatrix(self, int: int) -> RealMatrix: ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int) -> 'ArrayRowSymmetricMatrix': ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray]) -> 'ArrayRowSymmetricMatrix': ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> RealMatrix: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> RealMatrix: ...
    def hashCode(self) -> int: ...
    def isSquare(self) -> bool: ...
    @typing.overload
    def isSymmetric(self) -> bool: ...
    @typing.overload
    def isSymmetric(self, double: float) -> bool: ...
    @typing.overload
    def isSymmetric(self, double: float, double2: float) -> bool: ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    @typing.overload
    def multiply(self, diagonalMatrix: 'DiagonalMatrix', double: float) -> RealMatrix: ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix, boolean: bool, double: float) -> RealMatrix: ...
    def multiplyEntry(self, int: int, int2: int, double: float) -> None: ...
    def power(self, int: int) -> 'ArrayRowSymmetricMatrix': ...
    @typing.overload
    def quadraticMultiplication(self, realMatrix: RealMatrix) -> 'ArrayRowSymmetricMatrix': ...
    @typing.overload
    def quadraticMultiplication(self, realMatrix: RealMatrix, boolean: bool) -> 'ArrayRowSymmetricMatrix': ...
    def scalarAdd(self, double: float) -> 'ArrayRowSymmetricMatrix': ...
    def scalarMultiply(self, double: float) -> 'ArrayRowSymmetricMatrix': ...
    @staticmethod
    def setDefaultAbsoluteSymmetryThreshold(double: float) -> None: ...
    @staticmethod
    def setDefaultRelativeSymmetryThreshold(double: float) -> None: ...
    def setEntry(self, int: int, int2: int, double: float) -> None: ...
    def setSubMatrix(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int: int, int2: int) -> None: ...
    @typing.overload
    def subtract(self, diagonalMatrix: 'DiagonalMatrix') -> 'ArrayRowSymmetricMatrix': ...
    @typing.overload
    def subtract(self, symmetricMatrix: SymmetricMatrix) -> 'ArrayRowSymmetricMatrix': ...
    @typing.overload
    def subtract(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def transpose(self) -> 'ArrayRowSymmetricMatrix': ...
    @typing.overload
    def transpose(self, boolean: bool) -> 'ArrayRowSymmetricMatrix': ...
    class SymmetryType(java.lang.Enum['ArrayRowSymmetricMatrix.SymmetryType']):
        LOWER: typing.ClassVar['ArrayRowSymmetricMatrix.SymmetryType'] = ...
        UPPER: typing.ClassVar['ArrayRowSymmetricMatrix.SymmetryType'] = ...
        MEAN: typing.ClassVar['ArrayRowSymmetricMatrix.SymmetryType'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'ArrayRowSymmetricMatrix.SymmetryType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['ArrayRowSymmetricMatrix.SymmetryType']: ...

_BlockFieldMatrix__T = typing.TypeVar('_BlockFieldMatrix__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
class BlockFieldMatrix(AbstractFieldMatrix[_BlockFieldMatrix__T], java.io.Serializable, typing.Generic[_BlockFieldMatrix__T]):
    BLOCK_SIZE: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, field: fr.cnes.sirius.patrius.math.Field[_BlockFieldMatrix__T], int: int, int2: int): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[typing.MutableSequence[_BlockFieldMatrix__T]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, int: int, int2: int, tArray: typing.Union[typing.List[typing.MutableSequence[_BlockFieldMatrix__T]], jpype.JArray], boolean: bool): ...
    @typing.overload
    def add(self, blockFieldMatrix: 'BlockFieldMatrix'[_BlockFieldMatrix__T]) -> 'BlockFieldMatrix'[_BlockFieldMatrix__T]: ...
    @typing.overload
    def add(self, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    def addToEntry(self, int: int, int2: int, t: _BlockFieldMatrix__T) -> None: ...
    def copy(self) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    _createBlocksLayout__T = typing.TypeVar('_createBlocksLayout__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
    @staticmethod
    def createBlocksLayout(field: fr.cnes.sirius.patrius.math.Field[_createBlocksLayout__T], int: int, int2: int) -> typing.MutableSequence[typing.MutableSequence[_createBlocksLayout__T]]: ...
    def createMatrix(self, int: int, int2: int) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    def getColumn(self, int: int) -> typing.MutableSequence[_BlockFieldMatrix__T]: ...
    def getColumnDimension(self) -> int: ...
    def getColumnMatrix(self, int: int) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    def getColumnVector(self, int: int) -> FieldVector[_BlockFieldMatrix__T]: ...
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[_BlockFieldMatrix__T]]: ...
    def getEntry(self, int: int, int2: int) -> _BlockFieldMatrix__T: ...
    def getRow(self, int: int) -> typing.MutableSequence[_BlockFieldMatrix__T]: ...
    def getRowDimension(self) -> int: ...
    def getRowMatrix(self, int: int) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    def getRowVector(self, int: int) -> FieldVector[_BlockFieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    @typing.overload
    def multiply(self, blockFieldMatrix: 'BlockFieldMatrix'[_BlockFieldMatrix__T]) -> 'BlockFieldMatrix'[_BlockFieldMatrix__T]: ...
    @typing.overload
    def multiply(self, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    def multiplyEntry(self, int: int, int2: int, t: _BlockFieldMatrix__T) -> None: ...
    @typing.overload
    def operate(self, tArray: typing.Union[typing.List[_BlockFieldMatrix__T], jpype.JArray]) -> typing.MutableSequence[_BlockFieldMatrix__T]: ...
    @typing.overload
    def operate(self, fieldVector: FieldVector[_BlockFieldMatrix__T]) -> FieldVector[_BlockFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, tArray: typing.Union[typing.List[_BlockFieldMatrix__T], jpype.JArray]) -> typing.MutableSequence[_BlockFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldVector: FieldVector[_BlockFieldMatrix__T]) -> FieldVector[_BlockFieldMatrix__T]: ...
    def scalarAdd(self, t: _BlockFieldMatrix__T) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    def scalarMultiply(self, t: _BlockFieldMatrix__T) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    def setColumn(self, int: int, tArray: typing.Union[typing.List[_BlockFieldMatrix__T], jpype.JArray]) -> None: ...
    @typing.overload
    def setColumnMatrix(self, int: int, blockFieldMatrix: 'BlockFieldMatrix'[_BlockFieldMatrix__T]) -> None: ...
    @typing.overload
    def setColumnMatrix(self, int: int, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> None: ...
    def setColumnVector(self, int: int, fieldVector: FieldVector[_BlockFieldMatrix__T]) -> None: ...
    def setEntry(self, int: int, int2: int, t: _BlockFieldMatrix__T) -> None: ...
    def setRow(self, int: int, tArray: typing.Union[typing.List[_BlockFieldMatrix__T], jpype.JArray]) -> None: ...
    @typing.overload
    def setRowMatrix(self, int: int, blockFieldMatrix: 'BlockFieldMatrix'[_BlockFieldMatrix__T]) -> None: ...
    @typing.overload
    def setRowMatrix(self, int: int, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> None: ...
    def setRowVector(self, int: int, fieldVector: FieldVector[_BlockFieldMatrix__T]) -> None: ...
    def setSubMatrix(self, tArray: typing.Union[typing.List[typing.MutableSequence[_BlockFieldMatrix__T]], jpype.JArray], int: int, int2: int) -> None: ...
    @typing.overload
    def subtract(self, blockFieldMatrix: 'BlockFieldMatrix'[_BlockFieldMatrix__T]) -> 'BlockFieldMatrix'[_BlockFieldMatrix__T]: ...
    @typing.overload
    def subtract(self, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    _toBlocksLayout__T = typing.TypeVar('_toBlocksLayout__T', bound=fr.cnes.sirius.patrius.math.FieldElement)  # <T>
    @staticmethod
    def toBlocksLayout(tArray: typing.Union[typing.List[typing.MutableSequence[_toBlocksLayout__T]], jpype.JArray]) -> typing.MutableSequence[typing.MutableSequence[_toBlocksLayout__T]]: ...
    def transpose(self) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_BlockFieldMatrix__T]) -> _BlockFieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_BlockFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _BlockFieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_BlockFieldMatrix__T]) -> _BlockFieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_BlockFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _BlockFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_BlockFieldMatrix__T]) -> _BlockFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_BlockFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _BlockFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_BlockFieldMatrix__T]) -> _BlockFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_BlockFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _BlockFieldMatrix__T: ...

class BlockRealMatrix(AbstractRealMatrix):
    """
    public class BlockRealMatrix extends :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
    
        Cache-friendly implementation of RealMatrix using a flat arrays to store square blocks of the matrix.
    
        This implementation is specially designed to be cache-friendly. Square blocks are stored as small arrays and allow
        efficient traversal of data both in row major direction and columns major direction, one block at a time. This greatly
        increases performances for algorithms that use crossed directions loops like multiplication or transposition.
    
        The size of square blocks is a static parameter. It may be tuned according to the cache size of the target computer
        processor. As a rule of thumbs, it should be the largest value that allows three blocks to be simultaneously cached
        (this is necessary for example for matrix multiplication). The default value is to use 52x52 blocks which is well suited
        for processors with 64k L1 cache (one block holds 2704 values or 21632 bytes). This value could be lowered to 36x36 for
        processors with 32k L1 cache.
    
        The regular blocks represent :meth:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix.BLOCK_SIZE` x
        :meth:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix.BLOCK_SIZE` squares. Blocks at right hand side and bottom
        side which may be smaller to fit matrix dimensions. The square blocks are flattened in row major order in single
        dimension arrays which are therefore :meth:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix.BLOCK_SIZE` :sup:`2`
        elements long for regular blocks. The blocks are themselves organized in row major order.
    
        As an example, for a block size of 52x52, a 100x60 matrix would be stored in 4 blocks. Block 0 would be a double[2704]
        array holding the upper left 52x52 square, block 1 would be a double[416] array holding the upper right 52x8 rectangle,
        block 2 would be a double[2496] array holding the lower left 48x52 rectangle and block 3 would be a double[384] array
        holding the lower right 48x8 rectangle.
    
        The layout complexity overhead versus simple mapping of matrices to java arrays is negligible for small matrices (about
        1%). The gain from cache efficiency leads to up to 3-fold improvements for matrices of moderate to large size.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    BLOCK_SIZE: typing.ClassVar[int] = ...
    """
    public static final int BLOCK_SIZE
    
        Block size.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], boolean: bool): ...
    @typing.overload
    def add(self, blockRealMatrix: 'BlockRealMatrix') -> 'BlockRealMatrix':
        """
            Returns the result of adding the matrix :code:`m` to this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.add` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.add` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be added
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`m`
        
            Compute the sum of this matrix and :code:`m`.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix`): Matrix to be added.
        
            Returns:
                :code:`this` + m.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if :code:`m` is not the same size as this matrix.
        
        
        """
        ...
    @typing.overload
    def add(self, realMatrix: RealMatrix) -> 'BlockRealMatrix': ...
    def addToEntry(self, int: int, int2: int, double: float) -> None:
        """
            Adds (in place) a given value to the specified entry of this matrix.
        
            Row and column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.addToEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.addToEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the row index of the entry to be modified
                column (int): the column index of the entry to be modified
                increment (double): the value to add to the matrix entry
        
        
        """
        ...
    def copy(self) -> 'BlockRealMatrix':
        """
            Returns a deep copy of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.copy` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.copy` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                a deep copy of this matrix
        
        
        """
        ...
    @staticmethod
    def createBlocksLayout(int: int, int2: int) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Create a data array in blocks layout.
        
            This method can be used to create the array argument of the null constructor.
        
            Parameters:
                rows (int): Number of rows in the new matrix.
                columns (int): Number of columns in the new matrix.
        
            Returns:
                a new data array in blocks layout.
        
            Also see:
                null, null
        
        
        """
        ...
    def createMatrix(self, int: int, int2: int) -> 'BlockRealMatrix':
        """
            Creates a new matrix of the same type as this matrix.
        
            The returned matrix is filled with zeros. Its size is determined by the specified row and column dimensions, which must
            both be strictly positive. Additional constraints on the dimensions may apply depending on the implementation (for
            example, symmetric matrices must be square, which implies that the row and column dimensions must be equal).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.createMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.createMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                rowDimension (int): the number of rows in the new matrix
                columnDimension (int): the number of columns in the new matrix
        
            Returns:
                a new matrix of the same type as this matrix
        
        
        """
        ...
    def getColumn(self, int: int) -> typing.MutableSequence[float]:
        """
            Gets the entries of a given column.
        
            Column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getColumn` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getColumn` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                column (int): the index of the column to be fetched
        
            Returns:
                the extracted column data
        
        
        """
        ...
    def getColumnDimension(self) -> int:
        """
            Returns the dimension of the domain of this operator.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix.getColumnDimension` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getColumnDimension` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the number of columns of the underlying matrix
        
        
        """
        ...
    def getColumnMatrix(self, int: int) -> 'BlockRealMatrix':
        """
            Gets the entries of a given column as a column matrix.
        
            Column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getColumnMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getColumnMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                column (int): the index of the column to be fetched
        
            Returns:
                the extracted column matrix
        
        
        """
        ...
    def getColumnVector(self, int: int) -> RealVector:
        """
            Gets the entries of a given column as a vector.
        
            Column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getColumnVector` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getColumnVector` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                column (int): the index of the column to be fetched
        
            Returns:
                the extracted column vector
        
        
        """
        ...
    @typing.overload
    def getData(self, boolean: bool) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Returns a 2D array containing the entries of the matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getData` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getData` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                a 2D array containing the entries of the matrix
        
        
        """
        ...
    def getEntry(self, int: int, int2: int) -> float:
        """
            Gets the entry at the specified row and column.
        
            Row and column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the row index of entry to be fetched
                column (int): the column index of entry to be fetched
        
            Returns:
                the matrix entry at the specified row and column
        
        
        """
        ...
    def getFrobeniusNorm(self) -> float:
        """
            Returns the ` Frobenius norm <http://mathworld.wolfram.com/FrobeniusNorm.html>` of the matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getFrobeniusNorm` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getFrobeniusNorm` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the Frobenius norm of the matrix
        
        
        """
        ...
    def getNorm(self) -> float:
        """
            Returns the ` maximum absolute row sum norm <http://mathworld.wolfram.com/MaximumAbsoluteRowSumNorm.html>` of the
            matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getNorm` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getNorm` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the maximum absolute row sum norm of the matrix
        
        
        """
        ...
    def getRow(self, int: int) -> typing.MutableSequence[float]:
        """
            Gets the entries of a given row.
        
            Row indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getRow` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getRow` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the index of the row to be fetched
        
            Returns:
                the extracted row data
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
            Returns the dimension of the codomain of this operator.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix.getRowDimension` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getRowDimension` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the number of rows of the underlying matrix
        
        
        """
        ...
    def getRowMatrix(self, int: int) -> 'BlockRealMatrix':
        """
            Gets the entries of a given row as a row matrix.
        
            Row indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getRowMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getRowMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the index of the row to be fetched
        
            Returns:
                the extracted row matrix
        
        
        """
        ...
    def getRowVector(self, int: int) -> RealVector:
        """
            Gets the entries of a given row as a vector.
        
            Row indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getRowVector` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getRowVector` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the index of the row to be fetched
        
            Returns:
                the extracted row vector
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> 'BlockRealMatrix':
        """
            Gets a submatrix.
        
            Rows and columns are indicated counting from 0 to n-1.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getSubMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getSubMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
        
            Returns:
                the submatrix containing the data of the specified rows and columns
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> RealMatrix: ...
    @typing.overload
    def multiply(self, blockRealMatrix: 'BlockRealMatrix') -> 'BlockRealMatrix':
        """
            Returns the result of postmultiplying this matrix by the matrix :code:`m` or its transpose :code:`m` :sup:`T` , then by
            the scalar :code:`d`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.multiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.multiply` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix by which to multiply this matrix by
                toTranspose (boolean): whether to compute the product :code:`this`×:code:`m`×:code:`d` ( :code:`toTranspose=false`), or the product
                    :code:`this`×:code:`m` :sup:`T` ×:code:`d` (:code:`toTranspose=true`)
                d (double): the scalar by which to multiply the resulting matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`m`×:code:`d` or :code:`this`×:code:`m` :sup:`T` ×:code:`d`
        
            Returns the result of postmultiplying :code:`this` by :code:`m`.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix`): matrix to postmultiply by
        
            Returns:
                :code:`this * m`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if matrices are not multiplication compatible
        
            Returns the result of postmultiplying this &times m (if :code:`toTranspose = false`) or this &times m :sup:`T` (if
            :code:`toTranspose = true`)
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix`): matrix to postmultiply by
                toTranspose (boolean): indication value, true if we expect the :code:`m` matrix to be transposed
        
            Returns:
                this &times m or this &times m :sup:`T`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if matrices are not multiplication compatible
        
            Returns the result of postmultiplying d &times; this &times m (if :code:`toTranspose = false` ) or
            d &times; this &times m :sup:`T` (if :code:`toTranspose = true`)
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix`): matrix to postmultiply by
                toTranspose (boolean): indication value, true if we expect the :code:`m` matrix to be transposed
                d (double): value to multiply all entries by
        
            Returns:
                d &times; this &times m or d &times; this &times m :sup:`T`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if matrices are not multiplication compatible
        
        
        """
        ...
    @typing.overload
    def multiply(self, blockRealMatrix: 'BlockRealMatrix', boolean: bool) -> 'BlockRealMatrix': ...
    @typing.overload
    def multiply(self, blockRealMatrix: 'BlockRealMatrix', boolean: bool, double: float) -> 'BlockRealMatrix': ...
    @typing.overload
    def multiply(self, diagonalMatrix: 'DiagonalMatrix', double: float) -> RealMatrix: ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix, boolean: bool, double: float) -> RealMatrix: ...
    def multiplyEntry(self, int: int, int2: int, double: float) -> None:
        """
            Multiplies (in place) the specified entry of :code:`this` matrix by a given value.
        
            Row and column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.multiplyEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.multiplyEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the row index of the entry to be modified
                column (int): the column index of the entry to be modified
                factor (double): the multiplication factor for the matrix entry
        
        
        """
        ...
    @typing.overload
    def operate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
            Returns the result of postmultiplying this matrix by the vector :code:`v`.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                v (double[]): the vector by which to multiply this matrix by
        
            Returns:
                the column vector resulting from the product :code:`this`×:code:`v`
        
        
        """
        ...
    @typing.overload
    def operate(self, realVector: RealVector) -> RealVector: ...
    @typing.overload
    def preMultiply(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
            Returns the result of premultiplying this matrix by the vector :code:`v`.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                v (double[]): the row vector by which to premultiply this matrix by
        
            Returns:
                the row vector resulting from the product :code:`v`×:code:`this`
        
        
        """
        ...
    @typing.overload
    def preMultiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def preMultiply(self, realVector: RealVector) -> RealVector: ...
    def scalarAdd(self, double: float) -> 'BlockRealMatrix':
        """
            Returns the result of adding a scalar :code:`d` to the entries of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.scalarAdd` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.scalarAdd` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                d (double): the scalar value to be added to the entries of this matrix
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`d`
        
        
        """
        ...
    def scalarMultiply(self, double: float) -> 'BlockRealMatrix':
        """
            Returns the result of multiplying the entries of this matrix by the scalar :code:`d`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.scalarMultiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.scalarMultiply` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                d (double): the scalar value by which to multiply the entries of this matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`d`
        
        
        """
        ...
    def setColumn(self, int: int, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Replaces the entries of a given column with the entries of the specified data array.
        
            Column indices start at 0.
        
        
            The size of the provided data array must match the row dimension of this matrix.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                column (int): the index of the column to be replaced
                array (double[]): the column data array to be copied
        
        
        """
        ...
    @typing.overload
    def setColumnMatrix(self, int: int, blockRealMatrix: 'BlockRealMatrix') -> None:
        """
            Replaces the entries of a given column with the entries of the specified column matrix.
        
            Column indices start at 0.
        
        
            The provided matrix must have one column and the same number of rows as this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setColumnMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.setColumnMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                column (int): the index of the column to be replaced
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the column matrix to be copied
        
            Sets the entries in column number :code:`column` as a column matrix. Column indices start at 0.
        
            Parameters:
                column (int): the column to be set
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix`): column matrix (must have one column and the same number of rows as the instance)
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified column index is invalid.
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the matrix dimensions do not match one instance column.
        
        
        """
        ...
    @typing.overload
    def setColumnMatrix(self, int: int, realMatrix: RealMatrix) -> None: ...
    def setColumnVector(self, int: int, realVector: RealVector) -> None:
        """
            Replaces the entries of a given column with the entries of the specified vector.
        
            Column indices start at 0.
        
        
            The size of the provided vector must match the row dimension of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setColumnVector` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.setColumnVector` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                column (int): the index of the column to be replaced
                vector (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the column vector to be copied
        
        
        """
        ...
    def setEntry(self, int: int, int2: int, double: float) -> None:
        """
            Sets the entry at the specified row and column to a new value.
        
            Row and column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.setEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the row index of entry to be set
                column (int): the column index of entry to be set
                value (double): the new value of the entry
        
        
        """
        ...
    def setRow(self, int: int, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Replaces the entries of a given row with the entries of the specified data array.
        
            Row indices start at 0.
        
        
            The size of the provided data array must match the column dimension of this matrix.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the index of the row to be replaced
                array (double[]): the row data array to be copied
        
        
        """
        ...
    @typing.overload
    def setRowMatrix(self, int: int, blockRealMatrix: 'BlockRealMatrix') -> None:
        """
            Replaces the entries of a given row with the entries of the specified row matrix.
        
            Row indices start at 0.
        
        
            The provided matrix must have one row and the same number of columns as this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setRowMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.setRowMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the index of the row to be replaced
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the row matrix to be copied
        
            Sets the entries in row number :code:`row` as a row matrix. Row indices start at 0.
        
            Parameters:
                row (int): the row to be set
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix`): row matrix (must have one row and the same number of columns as the instance)
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.OutOfRangeException`: if the specified row index is invalid.
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the matrix dimensions do not match one instance row.
        
        
        """
        ...
    @typing.overload
    def setRowMatrix(self, int: int, realMatrix: RealMatrix) -> None: ...
    def setRowVector(self, int: int, realVector: RealVector) -> None:
        """
            Replaces the entries of a given row with the entries of the specified vector.
        
            Row indices start at 0.
        
        
            The size of the provided vector must match the column dimension of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setRowVector` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.setRowVector` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the index of the row to be replaced
                vector (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the row vector to be copied
        
        
        """
        ...
    def setSubMatrix(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int: int, int2: int) -> None:
        """
            Replaces part of the matrix with a given submatrix, starting at the specified row and column.
        
            Rows and columns are indicated counting from 0 to n-1.
        
        
            **Usage example:**
        
            .. code-block: java
            
            
             // Initial matrix
             matrix = [a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                      [a :sub:`10` , a :sub:`11` , a :sub:`21` ]
                      [a :sub:`20` , a :sub:`21` , a :sub:`22` ]
             // Submatrix
             subMatrix = [b :sub:`00` , b :sub:`01` ]
                         [b :sub:`10` , b :sub:`11` ]
                        
             // Replace part of the initial matrix 
             matrix.setSubMatrix(subMatrix, 1, 1) =>[a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                                                    [a :sub:`10` , b :sub:`00` , b :sub:`01` ]
                                                    [a :sub:`20` , b :sub:`10` , b :sub:`11` ]
             
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                subMatrix (double[][]): the array containing the submatrix replacement data
                row (int): the row coordinate of the top, left element to be replaced
                column (int): the column coordinate of the top, left element to be replaced
        
        
        """
        ...
    @typing.overload
    def subtract(self, blockRealMatrix: 'BlockRealMatrix') -> 'BlockRealMatrix':
        """
            Returns the result of subtracting the matrix :code:`m` from this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.subtract` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.subtract` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be subtracted
        
            Returns:
                the matrix resulting from the subtraction :code:`this`-:code:`m`
        
            Subtract :code:`m` from this matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix`): Matrix to be subtracted.
        
            Returns:
                :code:`this` - m.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if :code:`m` is not the same size as this matrix.
        
        
        """
        ...
    @typing.overload
    def subtract(self, realMatrix: RealMatrix) -> 'BlockRealMatrix': ...
    @staticmethod
    def toBlocksLayout(doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Convert a data array from raw layout to blocks layout.
        
            Raw layout is the straightforward layout where element at row i and column j is in array element :code:`rawData[i][j]`.
            Blocks layout is the layout used in :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` instances, where the
            matrix is split in square blocks (except at right and bottom side where blocks may be rectangular to fit matrix size)
            and each block is stored in a flattened one-dimensional array.
        
            This method creates an array in blocks layout from an input array in raw layout. It can be used to provide the array
            argument of the null constructor.
        
            Parameters:
                rawData (double[][]): Data array in raw layout.
        
            Returns:
                a new data array containing the same entries but in blocks layout.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.DimensionMismatchException`: if :code:`rawData` is not rectangular.
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix.createBlocksLayout`, null
        
        
        """
        ...
    @typing.overload
    def transpose(self) -> 'BlockRealMatrix':
        """
            Returns the transpose of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.transpose` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the transpose of this matrix
        
        
        """
        ...
    @typing.overload
    def transpose(self, boolean: bool) -> RealMatrix: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visits (and possibly change) all matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInOptimizedOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) all matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInOptimizedOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (and possibly change) some matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInOptimizedOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) some matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInOptimizedOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visits (and possibly change) all matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInRowOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) all matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInRowOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (and possibly change) some matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInRowOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (but don't change) some matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInRowOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...

class DiagonalMatrix(AbstractRealMatrix, SymmetricMatrix):
    """
    public class DiagonalMatrix extends :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix` implements :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
    
        Diagonal matrix.
    
        This implementation only stores the diagonal elements of the matrix. Setting any off-diagonal element to a value that is
        not 0 is forbidden (otherwise the matrix would not be diagonal anymore) and attempting to do so will systematically
        result in a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException` being thrown. As a result,
        any method which modifies the entries of the matrix (setRow, setColumn, setSubMatrix, etc) will most likely fail, unless
        only the diagonal elements are actually modified.
    
        This class is up-to-date with commons-math 3.6.1, but has been mostly rewritten since.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], boolean: bool): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def add(self, diagonalMatrix: 'DiagonalMatrix') -> 'DiagonalMatrix':
        """
            Returns the result of adding the matrix :code:`m` to this matrix.
        
            The returned matrix is, in order of priority:
        
              - A :class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix` if the provided matrix is a
                :class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix`;
              - An :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix` if it is any other type of
                :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`;
              - An :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix` or a
                :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` if it is any other type of
                :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`.
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.add` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.add` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be added
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`m`
        
            Returns the result of adding the symmetric matrix :code:`m` to this matrix.
        
            The returned matrix is, in order of priority:
        
              - A :class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix` if the provided matrix is a
                :class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix`;
              - An :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix` if it is any other type of
                :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`.
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.add` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`): the matrix to be added
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`m`
        
            Returns the result of adding the diagonal matrix :code:`m` to this matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix`): the matrix to be added
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`m`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the matrix :code:`m` is not the same size as this matrix
        
        
        """
        ...
    @typing.overload
    def add(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def add(self, symmetricMatrix: SymmetricMatrix) -> SymmetricMatrix: ...
    def addToEntry(self, int: int, int2: int, double: float) -> None:
        """
            Adds (in place) a given value to the specified entry of this matrix.
        
            Row and column indices start at 0.
        
            **Important:**
        
        
            This method throws a :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooLargeException` when asked to add a
            non-zero value to an extra-diagonal element, since this operation is not allowed when dealing with diagonal matrices
            (the properties of the matrix are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.addToEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.addToEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the row index of the entry to be modified
                column (int): the column index of the entry to be modified
                increment (double): the value to add to the matrix entry
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooLargeException`: if the method is asked to add a non-zero value to an extra-diagonal element
        
        
        """
        ...
    @typing.overload
    def concatenateDiagonally(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Diagonally or anti-diagonally concatenates this matrix and another matrix :code:`m`.
        
            The way the two matrices are concatenated depends on the provided arguments:
        
        
            The matrix :code:`m` is placed in the right part of the concatenated matrix if :code:`rightConcatenation` is set to
            :code:`true`, and in its left part if it is set to :code:`false`. Similarly, the matrix :code:`m` is placed in the lower
            part of the concatenated matrix if :code:`lowerConcatenation` is set to :code:`true`, and in its upper part if it is set
            to :code:`false`. This matrix is then placed in the opposite part of the concatenated matrix (as an example, if the
            provided matrix is placed in the upper left part, this matrix will be placed in the lower right part, the remaining
            parts being filled with zeros).
        
            **Usage examples:**
        
            .. code-block: java
            
            
             // Diagonal concatenation
             this.concatenateDiagonally(m, true, true)   => [this, 0] 
                                                            [   0, m]
                                                          
             this.concatenateDiagonally(m, false, false) => [m,    0]
                                                            [0, this]
                                      
             // Anti-diagonal concatenation
             this.concatenateDiagonally(m, false, true)  => [0, this]
                                                            [m,    0]
                                                           
             this.concatenateDiagonally(m, true, false)  => [   0, m]
                                                            [this, 0]
             
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.concatenateDiagonally` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.concatenateDiagonally` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
                rightConcatenation (boolean): whether the matrix :code:`m` is to be placed in the right (:code:`true`) or left ( :code:`false`) part of the
                    concatenated matrix
                lowerConcatenation (boolean): whether the matrix :code:`m` is to be placed in the lower (:code:`true`) or upper ( :code:`false`) part of the
                    concatenated matrix
        
            Returns:
                the concatenated matrix
        
        
        """
        ...
    @typing.overload
    def concatenateDiagonally(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    @typing.overload
    def concatenateDiagonally(self, realMatrix: RealMatrix, boolean: bool, boolean2: bool) -> RealMatrix: ...
    @typing.overload
    def concatenateHorizontally(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Horizontally concatenates this matrix and another matrix :code:`m`, , placing it in the left or right part of the
            concatenated matrix.
        
            The way the two matrices are concatenated depends on the provided argument:
        
        
            The matrix :code:`m` is placed in the right part of the concatenated matrix if :code:`rightConcatenation` is set to
            :code:`true`, and in its left part if it is set to :code:`false`.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             this.concatenateHorizontally(m, true)  => [this, m] 
             
             this.concatenateHorizontally(m, false) => [m, this]
             
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.concatenateHorizontally` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.concatenateHorizontally` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
                rightConcatenation (boolean): whether the matrix :code:`m` is to be placed in the right (:code:`true`) or left ( :code:`false`) part of the
                    concatenated matrix
        
            Returns:
                the concatenated matrix
        
        
        """
        ...
    @typing.overload
    def concatenateHorizontally(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    @typing.overload
    def concatenateVertically(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Vertically concatenates this matrix and another matrix :code:`m`, placing it in the lower or upper part of the
            concatenated matrix.
        
            The way the two matrices are concatenated depends on the provided argument:
        
        
            The matrix :code:`m` is placed in the lower part of the concatenated matrix if :code:`lowerConcatenation` is set to
            :code:`true`, and in its upper part if it is set to :code:`false`.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             this.concatenateVertically(m, true)  => [this] 
                                                     [   m]
                                                          
             this.concatenateVertically(m, false) => [   m]
                                                     [this]
             
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.concatenateVertically` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.concatenateVertically` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
                lowerConcatenation (boolean): whether the matrix :code:`m` is to be placed in the lower (:code:`true`) or upper ( :code:`false`) part of the
                    concatenated matrix
        
            Returns:
                the concatenated matrix
        
        
        """
        ...
    @typing.overload
    def concatenateVertically(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    def copy(self) -> 'DiagonalMatrix':
        """
            Returns a deep copy of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.copy` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.copy` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.copy` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                a deep copy of this matrix
        
        
        """
        ...
    @staticmethod
    def createIdentityMatrix(int: int) -> 'DiagonalMatrix':
        """
            Creates an identity matrix of the specified dimension.
        
            Parameters:
                n (int): the dimension of the identity matrix
        
            Returns:
                the identity matrix built
        
        
        """
        ...
    def createMatrix(self, int: int, int2: int) -> 'DiagonalMatrix':
        """
            Creates a new matrix of the same type as this matrix.
        
            The returned matrix is filled with zeros. Its size is determined by the specified row and column dimensions, which must
            both be strictly positive. Additional constraints on the dimensions may apply depending on the implementation (for
            example, symmetric matrices must be square, which implies that the row and column dimensions must be equal).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.createMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.createMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.createMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                rowDimension (int): the number of rows in the new matrix
                columnDimension (int): the number of columns in the new matrix
        
            Returns:
                a new matrix of the same type as this matrix
        
        
        """
        ...
    @typing.overload
    def equals(self, realMatrix: RealMatrix, double: float, double2: float) -> bool: ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool:
        """
            Returns :code:`true` if the provided object is a :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` instance with
            the same dimensions as this matrix, whose entries are strictly equal to the entries of this matrix (no absolute or
            relative tolerance is taken into account when comparing the entries).
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.equals` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                object (`Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`): the object to be tested for equality
        
            Returns:
                :code:`true` if the provided object is equal to this matrix
        
        
        """
        ...
    def getAbs(self) -> RealMatrix:
        """
            Returns the corresponding absolute values matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getAbs` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getAbs` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the corresponding absolute values matrix
        
        
        """
        ...
    def getColumn(self, int: int) -> typing.MutableSequence[float]:
        """
            Gets the entries of a given column.
        
            Column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getColumn` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getColumn` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                column (int): the index of the column to be fetched
        
            Returns:
                the extracted column data
        
        
        """
        ...
    def getColumnDimension(self) -> int:
        """
            Returns the dimension of the domain of this operator.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix.getColumnDimension` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getColumnDimension` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the number of columns of the underlying matrix
        
        
        """
        ...
    def getColumnMatrix(self, int: int) -> RealMatrix:
        """
            Gets the entries of a given column as a column matrix.
        
            Column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getColumnMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getColumnMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                column (int): the index of the column to be fetched
        
            Returns:
                the extracted column matrix
        
        
        """
        ...
    def getColumnVector(self, int: int) -> RealVector:
        """
            Gets the entries of a given column as a vector.
        
            Column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getColumnVector` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getColumnVector` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                column (int): the index of the column to be fetched
        
            Returns:
                the extracted column vector
        
        
        """
        ...
    @typing.overload
    def getData(self, boolean: bool) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Returns a 2D array containing the entries of the matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getData` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getData` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                a 2D array containing the entries of the matrix
        
        
        """
        ...
    def getDataRef(self) -> typing.MutableSequence[float]:
        """
            Gets a reference to the internal data array storing the diagonal elements of the matrix.
        
            *This method is only provided for optimization purposes. Any modification made on the returned array will change the
            values of this matrix.*
        
            Returns:
                a direct reference to the internal data array storing the diagonal elements of the matrix
        
        
        """
        ...
    def getDiagonal(self) -> typing.MutableSequence[float]:
        """
            Gets the diagonal vector from this matrix.
        
            **Note:** The matrix needs to be square.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getDiagonal` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.getDiagonal` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getDiagonal` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the diagonal vector from this matrix
        
        
        """
        ...
    def getEntry(self, int: int, int2: int) -> float:
        """
            Gets the entry at the specified row and column.
        
            Row and column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the row index of entry to be fetched
                column (int): the column index of entry to be fetched
        
            Returns:
                the matrix entry at the specified row and column
        
        
        """
        ...
    def getFrobeniusNorm(self) -> float:
        """
            Returns the ` Frobenius norm <http://mathworld.wolfram.com/FrobeniusNorm.html>` of the matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getFrobeniusNorm` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getFrobeniusNorm` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the Frobenius norm of the matrix
        
        
        """
        ...
    @typing.overload
    def getInverse(self) -> 'DiagonalMatrix':
        """
            Gets the inverse (or pseudo-inverse) of this matrix using the default decomposition.
        
            The default decomposition builder can be changed using the
            :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setDefaultDecomposition` method.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getInverse` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the inverse matrix
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getDefaultDecomposition`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setDefaultDecomposition`
        
        public :class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix` getInverse(`Function <http://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`,:class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`> decompositionBuilder)
        
            Gets the inverse (or pseudo-inverse) of this matrix using the given decomposition algorithm.
        
            The decomposition builder is a function capable of generating new instances of the decomposition algorithm to be used
            for the computation of the inverse matrix (like the :class:`~fr.cnes.sirius.patrius.math.linear.QRDecomposition` or the
            :class:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition`, for instance).
        
            *The provided decomposition algorithm is never used, since the computation of the inverse is straightforward for
            diagonal matrices.*
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getInverse` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                decompositionBuilder (`Function <http://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`,:class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`> decompositionBuilder): the decomposition builder to use
        
            Returns:
                the inverse matrix
        
        
        """
        ...
    @typing.overload
    def getInverse(self, function: typing.Union[java.util.function.Function[RealMatrix, typing.Union[Decomposition, typing.Callable]], typing.Callable[[RealMatrix], typing.Union[Decomposition, typing.Callable]]]) -> 'DiagonalMatrix': ...
    @typing.overload
    def getMax(self) -> float: ...
    @typing.overload
    def getMax(self, boolean: bool) -> float:
        """
            Returns the maximum value of the matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getMax` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getMax` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                absValue (boolean): Indicates if the absolute maximum value should be returned
        
            Returns:
                the maximum value of the matrix
        
        
        """
        ...
    @typing.overload
    def getMin(self) -> float: ...
    @typing.overload
    def getMin(self, boolean: bool) -> float:
        """
            Returns the minimum value of the matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getMin` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getMin` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                absValue (boolean): Indicates if the absolute minimum value should be returned
        
            Returns:
                the minimum value of the matrix
        
        
        """
        ...
    def getNorm(self) -> float:
        """
            Returns the ` maximum absolute row sum norm <http://mathworld.wolfram.com/MaximumAbsoluteRowSumNorm.html>` of the
            matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getNorm` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getNorm` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the maximum absolute row sum norm of the matrix
        
        
        """
        ...
    def getRow(self, int: int) -> typing.MutableSequence[float]:
        """
            Gets the entries of a given row.
        
            Row indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getRow` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getRow` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the index of the row to be fetched
        
            Returns:
                the extracted row data
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
            Returns the dimension of the codomain of this operator.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix.getRowDimension` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getRowDimension` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the number of rows of the underlying matrix
        
        
        """
        ...
    def getRowMatrix(self, int: int) -> RealMatrix:
        """
            Gets the entries of a given row as a row matrix.
        
            Row indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getRowMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getRowMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the index of the row to be fetched
        
            Returns:
                the extracted row matrix
        
        
        """
        ...
    def getRowVector(self, int: int) -> RealVector:
        """
            Gets the entries of a given row as a vector.
        
            Row indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getRowVector` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getRowVector` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the index of the row to be fetched
        
            Returns:
                the extracted row vector
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray]) -> ArrayRowSymmetricMatrix:
        """
            Gets a submatrix.
        
            Rows and columns are indicated counting from 0 to n-1.
        
            The returned matrix is a :class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix` if the selected rows and columns
            are the same, and an :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix` or a
            :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` otherwise.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getSubMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getSubMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
        
            Returns:
                the submatrix containing the data of the specified rows and columns
        
            Extracts the submatrix corresponding to the specified indices.
        
            This method uses the same start/end indices to select the rows and columns to be extracted. These indices must be valid
            indices with respect to the dimensions of the matrix (valid indices range from 0 to n-1, with n the row/column dimension
            of the matrix). Calling this method is equivalent to calling
            :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getSubMatrix` using the same start/end indices for the rows and
            columns. The extracted submatrix is guaranteed to be symmetric. It will also remain positive semi-definite if the
            initial matrix originally is.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             // Initial matrix
             matrix = [a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                      [a :sub:`10` , a :sub:`11` , a :sub:`21` ]
                      [a :sub:`20` , a :sub:`21` , a :sub:`22` ]
             
             // Submatrix extraction
             matrix.getSubMatrix(1, 2) => [a :sub:`11` , a :sub:`21` ]
                                          [a :sub:`21` , a :sub:`22` ]
             
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.getSubMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Parameters:
                startIndex (int): the initial row/column index
                endIndex (int): the final row/column index (inclusive)
        
            Returns:
                the extracted submatrix
        
            Extracts the submatrix corresponding to the specified indices.
        
            This method uses a single index array to select the rows and columns to be extracted. All indices must be valid indices
            with respect to the dimensions of the matrix (valid indices range from 0 to n-1, with n the row/column dimension of the
            matrix). The provided index array is allowed to contain duplicates. Calling this method is equivalent to calling
            RealMatrix.getSubMatrix(int[], int[]) using the provided index array for the selected rows and columns. This method can
            be used to extract any submatrix and perform a symmetric reordering of its rows/columns. The extracted submatrix is
            guaranteed to be symmetric. It will also remain positive semi-definite if the initial matrix originally is.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             // Initial matrix
             matrix = [a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                      [a :sub:`10` , a :sub:`11` , a :sub:`21` ]
                      [a :sub:`20` , a :sub:`21` , a :sub:`22` ]
             
             // Submatrix extraction
             matrix.getSubMatrix([1, 2]) => [a :sub:`11` , a :sub:`21` ]
                                            [a :sub:`21` , a :sub:`22` ]
             
             // Rows/Columns permutation
             matrix.getSubMatrix([1, 2, 0]) => [a :sub:`11` , a :sub:`21` , a :sub:`10` ]
                                               [a :sub:`21` , a :sub:`22` , a :sub:`20` ]
                                               [a :sub:`10` , a :sub:`20` , a :sub:`00` ]
             
             // Submatrix extraction (with duplicated indices)
             matrix.getSubMatrix([1, 2, 0, 1, 0]) 
                  => [a :sub:`11` , a :sub:`21` , a :sub:`10` , a :sub:`11` , a :sub:`10` ]
                     [a :sub:`21` , a :sub:`22` , a :sub:`20` , a :sub:`21` , a :sub:`20` ]
                     [a :sub:`10` , a :sub:`20` , a :sub:`00` , a :sub:`10` , a :sub:`00` ]
                     [a :sub:`11` , a :sub:`21` , a :sub:`10` , a :sub:`11` , a :sub:`10` ]
                     [a :sub:`10` , a :sub:`20` , a :sub:`00` , a :sub:`10` , a :sub:`00` ]
             
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Parameters:
                indices (int[]): the selected indices
        
            Returns:
                the extracted submatrix
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int) -> 'DiagonalMatrix':
        """
            Gets a submatrix.
        
            Rows and columns are indicated counting from 0 to n-1.
        
            The returned matrix is an :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix` if the selected rows and
            columns are the same (same indices, same order), and an
            :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix` or a
            :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` otherwise.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                selectedRows (int[]): the selected row indices
                selectedColumns (int[]): the selected column indices
        
            Returns:
                the submatrix containing the data in the specified rows and columns
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> RealMatrix: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> RealMatrix: ...
    def getTrace(self) -> float:
        """
            Returns the ` trace <http://mathworld.wolfram.com/MatrixTrace.html>` of the matrix (the sum of the elements on the main
            diagonal).
        
            *The trace of the matrix is only defined for square matrices.*
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getTrace` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getTrace` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the trace of the matrix
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code for the matrix.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.hashCode` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                hash code for matrix
        
        
        """
        ...
    @typing.overload
    def isAntisymmetric(self, double: float) -> bool:
        """
            Checks if this is an antisymmetric matrix.
        
            A diagonal matrix can only be antisymmetric if its diagonal elements are all equal to zero.
        
        
            The specified absolute threshold is taken into account to assess if this is the case or not.
        
            Parameters:
                absoluteTolerance (double): the absolute threshold to take into account when checking if the diagonal elements are equal to zero
        
            Returns:
                :code:`true` if the matrix is antisymmetric, :code:`false` otherwise
        
            Is this a antisymmetric matrix?
        
            This method indicates if the matrix is antisymmetric.
        
        
            To do so, the method checks that symmetric off-diagonal elements have numerically equal values but opposite signs, and
            that diagonal elements are numerically equal to zero. Two off-diagonal elements are considered to have different values
            if their absolute and relative differences are both above the specified tolerances. Diagonal elements are considered to
            be different from zero if their absolute value is greater than the specified absolute tolerance.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            A diagonal matrix can only be antisymmetric if its diagonal elements are all equal to zero.
        
        
            Only the absolute threshold is taken into account to assess if this is the case or not.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isAntisymmetric` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.isAntisymmetric` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                relativeTolerance (double): the relative tolerance to take into account when comparing off-diagonal elements
                absoluteTolerance (double): the absolute tolerance to take into account when comparing off-diagonal elements, and when checking if diagonal elements
                    are equal to zero
        
            Returns:
                :code:`true` if this is an antisymmetric matrix, :code:`false` otherwise
        
        
        """
        ...
    @typing.overload
    def isAntisymmetric(self, double: float, double2: float) -> bool: ...
    def isDiagonal(self, double: float) -> bool:
        """
            Is this a diagonal matrix?
        
            This method indicates if the matrix is diagonal, taking into account the specified tolerance.
        
        
            To do so, the method checks if the off-diagonal elements are numerically equal to zero.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isDiagonal` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.isDiagonal` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                threshold (double): the absolute threshold above which the absolute value of an off-diagonal element is considered to be strictly positive
        
            Returns:
                :code:`true` if this is a diagonal matrix, :code:`false` otherwise
        
        
        """
        ...
    @typing.overload
    def isInvertible(self) -> bool:
        """
            Checks if the matrix is invertible.
        
            A diagonal matrix is invertible if its diagonal elements are all different from zero.
        
        
            The default absolute tolerance (:meth:`~fr.cnes.sirius.patrius.math.util.Precision.SAFE_MIN`) is taken into account when
            checking the values.
        
            Returns:
                :code:`true` if the matrix is invertible, :code:`false` otherwise
        
        """
        ...
    @typing.overload
    def isInvertible(self, double: float) -> bool:
        """
            Checks if the matrix is invertible.
        
            A diagonal matrix is invertible if its diagonal elements are all different from zero.
        
        
            The specified absolute tolerance is taken into account when checking the values.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isInvertible` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.isInvertible` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                absoluteTolerance (double): the absolute tolerance to take into account when checking if an element is equal to 0
        
            Returns:
                :code:`true` if the matrix is invertible, :code:`false` otherwise
        
        
        """
        ...
    def isOrthogonal(self, double: float, double2: float) -> bool:
        """
            Is this an orthogonal matrix?
        
            This method indicates if this matrix is orthogonal, taking into account the specified tolerances.
        
        
            To do so, the method checks if the columns of the matrix form an orthonormal set (that is, the column vectors are
            orthogonal to each other and their norm is numerically equal to 1).
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            A diagonal matrix can only be orthogonal if its diagonal elements are all equal to +1 or -1.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isOrthogonal` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.isOrthogonal` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                thresholdNorm (double): the relative tolerance to take into account when checking the normality of the the column vectors
                thresholdOrthogonality (double): the absolute tolerance to take into account when checking the mutual orthogonality of the the column vectors
        
            Returns:
                :code:`true` if this is an orthogonal matrix, :code:`false` otherwise
        
        
        """
        ...
    @typing.overload
    def isSingular(self) -> bool:
        """
            Checks whether this diagonal matrix is singular or not.
        
            A diagonal matrix is singular if any of its diagonal elements is equal to 0.
        
        
            The default absolute tolerance (:meth:`~fr.cnes.sirius.patrius.math.util.Precision.SAFE_MIN`) is taken into account when
            checking the values.
        
            Returns:
                :code:`true` if the matrix is singular, :code:`false` otherwise
        
        """
        ...
    @typing.overload
    def isSingular(self, double: float) -> bool:
        """
            Checks whether this diagonal matrix is singular or not.
        
            A diagonal matrix is singular if any of its diagonal elements is equal to 0.
        
        
            The specified absolute tolerance is taken into account when checking the values.
        
            Parameters:
                absoluteTolerance (double): the absolute tolerance to take into account when checking if an element is equal to 0
        
            Returns:
                :code:`true` if the matrix is singular, :code:`false` otherwise
        
        
        """
        ...
    def isSquare(self) -> bool:
        """
            Is this a square matrix?
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix.isSquare` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.isSquare` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                true if the matrix is square (rowDimension = columnDimension)
        
        
        """
        ...
    @typing.overload
    def isSymmetric(self) -> bool:
        """
            Is this a symmetric matrix?
        
            This method indicates if the matrix is symmetric.
        
        
            To do so, the method checks that symmetric off-diagonal elements are numerically equal. Two elements are considered to
            have different values if their absolute and relative differences are both above the default tolerances.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            The absolute and relative tolerances both default to
            :meth:`~fr.cnes.sirius.patrius.math.util.Precision.DOUBLE_COMPARISON_EPSILON`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isSymmetric` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.isSymmetric` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                :code:`true` if this is a symmetric matrix, :code:`false` otherwise
        
        """
        ...
    @typing.overload
    def isSymmetric(self, double: float) -> bool:
        """
            Is this a symmetric matrix?
        
            This method indicates if the matrix is symmetric.
        
        
            To do so, the method checks that symmetric off-diagonal elements are numerically equal. Two elements are considered to
            have different values if their relative difference is above the specified tolerance.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isSymmetric` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.isSymmetric` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                relativeTolerance (double): the relative tolerance to take into account when comparing off-diagonal elements
        
            Returns:
                :code:`true` if this is a symmetric matrix, :code:`false` otherwise
        
            Is this a symmetric matrix?
        
            This method indicates if the matrix is symmetric.
        
        
            To do so, the method checks that symmetric off-diagonal elements are numerically equal. Two elements are considered to
            have different values if their absolute and relative differences are both above the specified tolerances.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isSymmetric` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.isSymmetric` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                relativeTolerance (double): the relative tolerance to take into account when comparing off-diagonal elements
                absoluteTolerance (double): the absolute tolerance to take into account when comparing off-diagonal elements
        
            Returns:
                :code:`true` if this is a symmetric matrix, :code:`false` otherwise
        
        
        """
        ...
    @typing.overload
    def isSymmetric(self, double: float, double2: float) -> bool: ...
    @typing.overload
    def multiply(self, diagonalMatrix: 'DiagonalMatrix', double: float) -> 'DiagonalMatrix':
        """
            Returns the result of postmultiplying this matrix by the matrix :code:`m` or its transpose :code:`m` :sup:`T` , then by
            the scalar :code:`d`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.multiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.multiply` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix by which to multiply this matrix by
                toTranspose (boolean): whether to compute the product :code:`this`×:code:`m`×:code:`d` ( :code:`toTranspose=false`), or the product
                    :code:`this`×:code:`m` :sup:`T` ×:code:`d` (:code:`toTranspose=true`)
                d (double): the scalar by which to multiply the resulting matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`m`×:code:`d` or :code:`this`×:code:`m` :sup:`T` ×:code:`d`
        
            Returns the result of postmultiplying this matrix by the diagonal matrix :code:`m`, then by the scalar :code:`d`.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.multiply` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix`): the diagonal matrix by which to multiply this matrix by
                d (double): the scalar by which to multiply the resulting matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`m`×:code:`d` or :code:`this`×:code:`m` :sup:`T` ×:code:`d`
        
        
        """
        ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix, boolean: bool, double: float) -> RealMatrix: ...
    def multiplyEntry(self, int: int, int2: int, double: float) -> None:
        """
            Multiplies (in place) the specified entry of :code:`this` matrix by a given value.
        
            Row and column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.multiplyEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.multiplyEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the row index of the entry to be modified
                column (int): the column index of the entry to be modified
                factor (double): the multiplication factor for the matrix entry
        
        
        """
        ...
    @typing.overload
    def operate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
            Returns the result of postmultiplying this matrix by the vector :code:`v`.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                v (double[]): the vector by which to multiply this matrix by
        
            Returns:
                the column vector resulting from the product :code:`this`×:code:`v`
        
            Returns the result of multiplying :code:`this` by the vector :code:`x`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.operate` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.operate` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the vector to operate on
        
            Returns:
                the product of :code:`this` instance with :code:`x`
        
        
        """
        ...
    @typing.overload
    def operate(self, realVector: RealVector) -> RealVector: ...
    def power(self, int: int) -> 'DiagonalMatrix':
        """
            Returns the the result of multiplying this matrix with itself :code:`p` times.
        
            The exponent :code:`p` must be positive or equal to zero.
        
        
            This operation is only supported for square matrices.
        
        
            Depending on the underlying storage, numerical instabilities might occur for high powers.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.power` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.power` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.power` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                p (int): the exponent :code:`p` to which this matrix is to be raised
        
            Returns:
                the matrix resulting from raising this matrix to the power of :code:`p`
        
        
        """
        ...
    @typing.overload
    def preMultiply(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
            Returns the result of premultiplying this matrix by the vector :code:`v`.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                v (double[]): the row vector by which to premultiply this matrix by
        
            Returns:
                the row vector resulting from the product :code:`v`×:code:`this`
        
            Returns the result of premultiplying this matrix by the vector :code:`v`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.preMultiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.preMultiply` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                v (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the vector by which to premultiply this matrix by
        
            Returns:
                the row vector resulting from the product :code:`v`×:code:`this`
        
        
        """
        ...
    @typing.overload
    def preMultiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def preMultiply(self, realVector: RealVector) -> RealVector: ...
    @typing.overload
    def quadraticMultiplication(self, realMatrix: RealMatrix) -> ArrayRowSymmetricMatrix:
        """
            Returns the result of the quadratic multiplication M×:code:`this`×M :sup:`T` , where M is the provided matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.quadraticMultiplication` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix M
        
            Returns:
                the matrix resulting from the quadratic multiplication M×:code:`this` ×M :sup:`T`
        
            Returns the result of the quadratic multiplication M×:code:`this`×M :sup:`T` , where M or M :sup:`T` is the provided
            matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.quadraticMultiplication` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix M or the matrix M :sup:`T`
                isTranspose (boolean): if :code:`true`, assumes the provided matrix is M :sup:`T` , otherwise assumes it is M
        
            Returns:
                the matrix resulting from the quadratic multiplication M×:code:`this` ×M :sup:`T`
        
        
        """
        ...
    @typing.overload
    def quadraticMultiplication(self, realMatrix: RealMatrix, boolean: bool) -> ArrayRowSymmetricMatrix: ...
    def scalarAdd(self, double: float) -> ArrayRowSymmetricMatrix:
        """
            Returns the result of adding a scalar :code:`d` to the entries of this matrix.
        
            The returned matrix is an :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.scalarAdd` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.scalarAdd` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.scalarAdd` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                d (double): the scalar value to be added to the entries of this matrix
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`d`
        
        
        """
        ...
    def scalarMultiply(self, double: float) -> 'DiagonalMatrix':
        """
            Returns the result of multiplying the entries of this matrix by the scalar :code:`d`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.scalarMultiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.scalarMultiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.scalarMultiply` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                d (double): the scalar value by which to multiply the entries of this matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`d`
        
        
        """
        ...
    def setEntry(self, int: int, int2: int, double: float) -> None:
        """
            Sets the entry at the specified row and column to a new value.
        
            Row and column indices start at 0.
        
            **Important:**
        
        
            This method throws a :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooLargeException` when asked to set an
            extra-diagonal element to a non-zero value, since this operation is not allowed when dealing with diagonal matrices (the
            properties of the matrix are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.setEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the row index of entry to be set
                column (int): the column index of entry to be set
                value (double): the new value of the entry
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.NumberIsTooLargeException`: if the method is asked to set an extra-diagonal element to a non-zero value
        
        
        """
        ...
    def setSubMatrix(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int: int, int2: int) -> None:
        """
            Replaces part of the matrix with a given submatrix, starting at the specified row and column.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with diagonal matrices (the properties of the matrix are not guaranteed to
            be preserved).
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                subMatrix (double[][]): the array containing the replacement data of the targeted submatrix
                row (int): the row coordinate of the top, left element to be replaced
                column (int): the column coordinate of the top, left element to be replaced
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    @typing.overload
    def subtract(self, diagonalMatrix: 'DiagonalMatrix') -> 'DiagonalMatrix':
        """
            Returns the result of subtracting the matrix :code:`m` from this matrix.
        
            The returned matrix is, in order of priority:
        
              - A :class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix` if the provided matrix is a
                :class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix`;
              - An :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix` if it is any other type of
                :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`;
              - An :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix` or a
                :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` if it is any other type of
                :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`.
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.subtract` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.subtract` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be subtracted
        
            Returns:
                the matrix resulting from the subtraction :code:`this`-:code:`m`
        
            Returns the result of subtracting the symmetric matrix :code:`m` from this matrix.
        
            The returned matrix is, in order of priority:
        
              - A :class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix` if the provided matrix is a
                :class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix`;
              - An :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix` if it is any other type of
                :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`.
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.subtract` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`): the matrix to be subtracted
        
            Returns:
                the matrix resulting from the subtraction :code:`this`-:code:`m`
        
            Returns the result of subtracting the diagonal matrix :code:`m` from this matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix`): the matrix to be subtracted
        
            Returns:
                the matrix resulting from the subtraction :code:`this` - :code:`m`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the matrix :code:`m` is not the same size as this matrix
        
        
        """
        ...
    @typing.overload
    def subtract(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def subtract(self, symmetricMatrix: SymmetricMatrix) -> SymmetricMatrix: ...
    @typing.overload
    def transpose(self) -> 'DiagonalMatrix':
        """
            Returns the transpose of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.transpose` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the transpose of this matrix
        
        """
        ...
    @typing.overload
    def transpose(self, boolean: bool) -> 'DiagonalMatrix':
        """
            Returns the transpose of this matrix.
        
            If :code:`forceCopy` is :code:`true`, the returned matrix is guaranteed to be a new instance, which can be modified
            without any risk of impacting the current instance. Otherwise, this method may simply return the current instance when
            the matrix is its own transpose (symmetric matrix).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.transpose` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                forceCopy (boolean): if :code:`true`, the transpose of the matrix is systematically stored in a new matrix; otherwise the method may return
                    the current instance when the matrix is its own transpose
        
            Returns:
                the transpose of this matrix
        
        
        """
        ...

class SymmetricPositiveMatrix(SymmetricMatrix):
    """
    public interface SymmetricPositiveMatrix extends :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
    
        Interface for symmetric positive semi-definite matrices.
    """
    @typing.overload
    def add(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Returns the result of adding the symmetric positive semi-definite matrix :code:`m` to this matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`): the symmetric positive semi-definite matrix to be added
        
            Returns:
                the symmetric positive semi-definite matrix resulting from the addition :code:`this`+ :code:`m`
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.MatrixDimensionMismatchException`: if the matrix :code:`m` is not the same size as this matrix
        
        
        """
        ...
    @typing.overload
    def add(self, symmetricMatrix: SymmetricMatrix) -> SymmetricMatrix: ...
    @typing.overload
    def add(self, symmetricPositiveMatrix: 'SymmetricPositiveMatrix') -> 'SymmetricPositiveMatrix': ...
    def copy(self) -> 'SymmetricPositiveMatrix':
        """
            Returns a deep copy of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.copy` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.copy` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Returns:
                a deep copy of this matrix
        
        
        """
        ...
    def createMatrix(self, int: int, int2: int) -> 'SymmetricPositiveMatrix':
        """
            Creates a new matrix of the same type as this matrix.
        
            The returned matrix is filled with zeros. Its size is determined by the specified row and column dimensions, which must
            both be strictly positive. Additional constraints on the dimensions may apply depending on the implementation (for
            example, symmetric matrices must be square, which implies that the row and column dimensions must be equal).
        
            *Since the matrix build is a symmetric matrix, the row and column dimensions are expected to be equal.*
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.createMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.createMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Parameters:
                rowDimension (int): the number of rows in the new matrix
                columnDimension (int): the number of columns in the new matrix
        
            Returns:
                a new matrix of the same type as this matrix
        
        
        """
        ...
    def equals(self, realMatrix: RealMatrix, double: float, double2: float) -> bool: ...
    @typing.overload
    def getInverse(self) -> 'SymmetricPositiveMatrix':
        """
            Gets the inverse (or pseudo-inverse) of this matrix using the default decomposition.
        
            The default decomposition builder can be changed using the
            :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setDefaultDecomposition` method.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Returns:
                the inverse matrix
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getDefaultDecomposition`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setDefaultDecomposition`
        
        :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix` getInverse(`Function <http://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`,:class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`> decompositionBuilder)
        
            Gets the inverse (or pseudo-inverse) of this matrix using the given decomposition algorithm.
        
            The decomposition builder is a function capable of generating new instances of the decomposition algorithm to be used
            for the computation of the inverse matrix (like the :class:`~fr.cnes.sirius.patrius.math.linear.QRDecomposition` or the
            :class:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition`, for instance).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Parameters:
                decompositionBuilder (`Function <http://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`,:class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`> decompositionBuilder): the decomposition builder to use
        
            Returns:
                the inverse matrix
        
        
        """
        ...
    @typing.overload
    def getInverse(self, function: typing.Union[java.util.function.Function[RealMatrix, typing.Union[Decomposition, typing.Callable]], typing.Callable[[RealMatrix], typing.Union[Decomposition, typing.Callable]]]) -> 'SymmetricPositiveMatrix': ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> RealMatrix: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> RealMatrix:
        """
            Extracts the submatrix corresponding to the specified indices.
        
            This method uses the same start/end indices to select the rows and columns to be extracted. These indices must be valid
            indices with respect to the dimensions of the matrix (valid indices range from 0 to n-1, with n the row/column dimension
            of the matrix). Calling this method is equivalent to calling
            :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getSubMatrix` using the same start/end indices for the rows and
            columns. The extracted submatrix is guaranteed to be symmetric. It will also remain positive semi-definite if the
            initial matrix originally is.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             // Initial matrix
             matrix = [a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                      [a :sub:`10` , a :sub:`11` , a :sub:`21` ]
                      [a :sub:`20` , a :sub:`21` , a :sub:`22` ]
             
             // Submatrix extraction
             matrix.getSubMatrix(1, 2) => [a :sub:`11` , a :sub:`21` ]
                                          [a :sub:`21` , a :sub:`22` ]
             
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.getSubMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Parameters:
                startIndex (int): the initial row/column index
                endIndex (int): the final row/column index (inclusive)
        
            Returns:
                the extracted submatrix
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int) -> 'SymmetricPositiveMatrix': ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray]) -> 'SymmetricPositiveMatrix':
        """
            Extracts the submatrix corresponding to the specified indices.
        
            This method uses a single index array to select the rows and columns to be extracted. All indices must be valid indices
            with respect to the dimensions of the matrix (valid indices range from 0 to n-1, with n the row/column dimension of the
            matrix). The provided index array is allowed to contain duplicates. Calling this method is equivalent to calling
            RealMatrix.getSubMatrix(int[], int[]) using the provided index array for the selected rows and columns. This method can
            be used to extract any submatrix and perform a symmetric reordering of its rows/columns. The extracted submatrix is
            guaranteed to be symmetric. It will also remain positive semi-definite if the initial matrix originally is.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             // Initial matrix
             matrix = [a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                      [a :sub:`10` , a :sub:`11` , a :sub:`21` ]
                      [a :sub:`20` , a :sub:`21` , a :sub:`22` ]
             
             // Submatrix extraction
             matrix.getSubMatrix([1, 2]) => [a :sub:`11` , a :sub:`21` ]
                                            [a :sub:`21` , a :sub:`22` ]
             
             // Rows/Columns permutation
             matrix.getSubMatrix([1, 2, 0]) => [a :sub:`11` , a :sub:`21` , a :sub:`10` ]
                                               [a :sub:`21` , a :sub:`22` , a :sub:`20` ]
                                               [a :sub:`10` , a :sub:`20` , a :sub:`00` ]
             
             // Submatrix extraction (with duplicated indices)
             matrix.getSubMatrix([1, 2, 0, 1, 0]) 
                  => [a :sub:`11` , a :sub:`21` , a :sub:`10` , a :sub:`11` , a :sub:`10` ]
                     [a :sub:`21` , a :sub:`22` , a :sub:`20` , a :sub:`21` , a :sub:`20` ]
                     [a :sub:`10` , a :sub:`20` , a :sub:`00` , a :sub:`10` , a :sub:`00` ]
                     [a :sub:`11` , a :sub:`21` , a :sub:`10` , a :sub:`11` , a :sub:`10` ]
                     [a :sub:`10` , a :sub:`20` , a :sub:`00` , a :sub:`10` , a :sub:`00` ]
             
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Parameters:
                indices (int[]): the selected indices
        
            Returns:
                the extracted submatrix
        
        
        """
        ...
    def positiveScalarAdd(self, double: float) -> 'SymmetricPositiveMatrix':
        """
            Returns the result of adding a positive scalar :code:`d` to the entries of this matrix.
        
            Parameters:
                d (double): the positive scalar value to be added to the entries of this matrix
        
            Returns:
                the symmetric positive semi-definite matrix resulting from the addition :code:`this`+ :code:`d`
        
        
        """
        ...
    def positiveScalarMultiply(self, double: float) -> 'SymmetricPositiveMatrix':
        """
            Returns the result of multiplying the entries of this matrix by a positive scalar :code:`d`.
        
            Parameters:
                d (double): the positive scalar value by which to multiply the entries of this matrix by
        
            Returns:
                the symmetric positive semi-definite matrix resulting from the product :code:`d` ×:code:`this`
        
        
        """
        ...
    def power(self, int: int) -> 'SymmetricPositiveMatrix':
        """
            Returns the the result of multiplying this matrix with itself :code:`p` times.
        
            The exponent :code:`p` must be positive or equal to zero.
        
        
            This operation is only supported for square matrices.
        
        
            Depending on the underlying storage, numerical instabilities might occur for high powers.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.power` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.power` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Parameters:
                p (int): the exponent :code:`p` to which this matrix is to be raised
        
            Returns:
                the matrix resulting from raising this matrix to the power of :code:`p`
        
        
        """
        ...
    @typing.overload
    def quadraticMultiplication(self, realMatrix: RealMatrix) -> 'SymmetricPositiveMatrix':
        """
            Returns the result of the quadratic multiplication M×:code:`this`×M :sup:`T` , where M is the provided matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.quadraticMultiplication` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix M
        
            Returns:
                the matrix resulting from the quadratic multiplication M×:code:`this` ×M :sup:`T`
        
            Returns the result of the quadratic multiplication M×:code:`this`×M :sup:`T` , where M or M :sup:`T` is the provided
            matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.quadraticMultiplication` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix M or the matrix M :sup:`T`
                isTranspose (boolean): if :code:`true`, assumes the provided matrix is M :sup:`T` , otherwise assumes it is M
        
            Returns:
                the matrix resulting from the quadratic multiplication M×:code:`this` ×M :sup:`T`
        
        
        """
        ...
    @typing.overload
    def quadraticMultiplication(self, realMatrix: RealMatrix, boolean: bool) -> 'SymmetricPositiveMatrix': ...
    def toString(self, realMatrixFormat: RealMatrixFormat) -> str: ...
    @typing.overload
    def transpose(self) -> 'SymmetricPositiveMatrix':
        """
            Returns the transpose of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Returns:
                the transpose of this matrix
        
        """
        ...
    @typing.overload
    def transpose(self, boolean: bool) -> 'SymmetricPositiveMatrix':
        """
            Returns the transpose of this matrix.
        
            If :code:`forceCopy` is :code:`true`, the returned matrix is guaranteed to be a new instance, which can be modified
            without any risk of impacting the current instance. Otherwise, this method may simply return the current instance when
            the matrix is its own transpose (symmetric matrix).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Parameters:
                forceCopy (boolean): if :code:`true`, the transpose of the matrix is systematically stored in a new matrix; otherwise the method may return
                    the current instance when the matrix is its own transpose
        
            Returns:
                the transpose of this matrix
        
        
        """
        ...

class ArrayRowSymmetricPositiveMatrix(ArrayRowSymmetricMatrix, SymmetricPositiveMatrix):
    """
    public class ArrayRowSymmetricPositiveMatrix extends :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix` implements :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
    
        Symmetric positive semi-definite matrix defined by its lower triangular part.
    
        This implementation stores the elements of the lower triangular part of a symmetric matrix. These elements are stored in
        a 1D array, row after row. For example, for a 3 by 3 matrix we have:
    
    
        (1) = s :sub:`1,1` ;
    
    
        (2) = s :sub:`2,1` ; (3) = s :sub:`2,2` ;
    
    
        (4) = s :sub:`3,1` ; (5) = s :sub:`3,2` ; (6) = s :sub:`3,3` ;
    
    
    
        The elements actually stored depends on the type of symmetry specified at construction:
        :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.SymmetryType.LOWER` or
        :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.SymmetryType.UPPER` implies the symmetry is enforced
        by keeping only the lower or upper triangular part of the matrix, while
        :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.SymmetryType.MEAN` enforces the symmetry by computing
        the mean of the lower and upper elements. The symmetry of the provided matrix is not checked by default, meaning that
        the symmetry is enforced regardless of the inputs. However, such a check can be triggered by setting the default
        absolute or relative symmetry threshold to a non-null value, or by specifying any of these thresholds at construction.
        Note that the default values for these symmetry thresholds are shared with
        :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`.
    
        In contrast, the positivity of the symmetrized matrix is always checked by default. This check can be disabled by
        setting the absolute and relative positivity thresholds to :code:`null`, either by changing the default values or by
        overriding them at construction. A symmetric matrix is considered to be positive semi-definite if all its pivots are
        strictly positive, or if the pivot and the associated row/column are equal to zero. Possible numerical errors are taken
        into account by adding a small value (which depends on the specified tolerances) to the diagonal elements of the matrix.
        The relative tolerance is relative to the maximum row sum norm of the matrix.
    
        **Important:**
    
    
        Since it might induce a loss of positivity or definiteness, modifying any element of the matrix is forbidden.
    
        Also see:
            :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, symmetryType: ArrayRowSymmetricMatrix.SymmetryType, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, symmetryType: ArrayRowSymmetricMatrix.SymmetryType, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], double2: float, double3: float, double4: float, double5: float): ...
    @typing.overload
    def __init__(self, symmetryType: ArrayRowSymmetricMatrix.SymmetryType, realMatrix: RealMatrix): ...
    @typing.overload
    def __init__(self, symmetryType: ArrayRowSymmetricMatrix.SymmetryType, realMatrix: RealMatrix, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def add(self, diagonalMatrix: DiagonalMatrix) -> ArrayRowSymmetricMatrix:
        """
            Returns the result of adding the symmetric matrix :code:`m` to this matrix.
        
            The returned matrix is, in order of priority:
        
              - An :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricPositiveMatrix` if it is a
                :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`;
              - An :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix` if it is any other type of
                :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`.
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.add` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.add` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`): the matrix to be added
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`m`
        
            Returns the result of adding the symmetric positive semi-definite matrix :code:`m` to this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.add` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`): the symmetric positive semi-definite matrix to be added
        
            Returns:
                the symmetric positive semi-definite matrix resulting from the addition :code:`this`+ :code:`m`
        
        
        """
        ...
    @typing.overload
    def add(self, symmetricMatrix: SymmetricMatrix) -> ArrayRowSymmetricMatrix: ...
    @typing.overload
    def add(self, symmetricPositiveMatrix: SymmetricPositiveMatrix) -> 'ArrayRowSymmetricPositiveMatrix': ...
    @typing.overload
    def add(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def addToEntry(self, int: int, int2: int, double: float) -> None:
        """
            Adds (in place) a given value to the specified entry of this matrix.
        
            Row and column indices start at 0.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.addToEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.addToEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                row (int): the row index of the entry to be modified
                column (int): the column index of the entry to be modified
                increment (double): the value to add to the matrix entry
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    def copy(self) -> 'ArrayRowSymmetricPositiveMatrix':
        """
            Returns a deep copy of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.copy` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.copy` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.copy` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.copy` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Returns:
                a deep copy of this matrix
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createIdentityMatrix(int: int) -> ArrayRowSymmetricMatrix:
        """
            Creates an identity matrix of the specified dimension.
        
            Parameters:
                dim (int): the dimension of the identity matrix
        
            Returns:
                the identity matrix built
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createIdentityMatrix(int: int) -> 'ArrayRowSymmetricPositiveMatrix': ...
    def createMatrix(self, int: int, int2: int) -> 'ArrayRowSymmetricPositiveMatrix':
        """
            Creates a new matrix of the same type as this matrix.
        
            The returned matrix is filled with zeros. Its size is determined by the specified row and column dimensions, which must
            both be strictly positive. Additional constraints on the dimensions may apply depending on the implementation (for
            example, symmetric matrices must be square, which implies that the row and column dimensions must be equal).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.createMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.createMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.createMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.createMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                rowDimension (int): the number of rows in the new matrix
                columnDimension (int): the number of columns in the new matrix
        
            Returns:
                a new matrix of the same type as this matrix
        
        
        """
        ...
    @typing.overload
    def equals(self, realMatrix: RealMatrix, double: float, double2: float) -> bool: ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool:
        """
            Returns :code:`true` if the provided object is a :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix` instance with
            the same dimensions as this matrix, whose entries are strictly equal to the entries of this matrix (no absolute or
            relative tolerance is taken into account when comparing the entries).
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.equals` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                object (`Object <http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true>`): the object to be tested for equality
        
            Returns:
                :code:`true` if the provided object is equal to this matrix
        
        
        """
        ...
    @staticmethod
    def getDefaultAbsolutePositivityThreshold() -> float:
        """
            Gets the default absolute positivity threshold, above which a value is considered to be strictly positive.
        
            Returns:
                the default absolute positivity threshold (≥0 or :code:`null`)
        
        
        """
        ...
    @staticmethod
    def getDefaultRelativePositivityThreshold() -> float:
        """
            Gets the default relative positivity threshold, above which a value is considered to be numerically significant when
            compared to another value.
        
            Returns:
                the default relative positivity threshold (≥0 or :code:`null`)
        
        
        """
        ...
    @typing.overload
    def getInverse(self) -> 'ArrayRowSymmetricPositiveMatrix':
        """
            Gets the inverse (or pseudo-inverse) of this matrix using the default decomposition.
        
            The default decomposition builder can be changed using the
            :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setDefaultDecomposition` method.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.getInverse` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Returns:
                the inverse matrix
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getDefaultDecomposition`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setDefaultDecomposition`
        
        public :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricPositiveMatrix` getInverse(`Function <http://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`,:class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`> decompositionBuilder)
        
            Gets the inverse (or pseudo-inverse) of this matrix using the given decomposition algorithm.
        
            The decomposition builder is a function capable of generating new instances of the decomposition algorithm to be used
            for the computation of the inverse matrix (like the :class:`~fr.cnes.sirius.patrius.math.linear.QRDecomposition` or the
            :class:`~fr.cnes.sirius.patrius.math.linear.EigenDecomposition`, for instance).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.getInverse` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                decompositionBuilder (`Function <http://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`,:class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`> decompositionBuilder): the decomposition builder to use
        
            Returns:
                the inverse matrix
        
        
        """
        ...
    @typing.overload
    def getInverse(self, function: typing.Union[java.util.function.Function[RealMatrix, typing.Union[Decomposition, typing.Callable]], typing.Callable[[RealMatrix], typing.Union[Decomposition, typing.Callable]]]) -> 'ArrayRowSymmetricPositiveMatrix': ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int) -> 'ArrayRowSymmetricPositiveMatrix':
        """
            Gets a submatrix.
        
            Rows and columns are indicated counting from 0 to n-1.
        
            The returned matrix is an :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix` if the selected indices
            are the same for the rows and the columns, and an :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix` or a
            :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` otherwise.
        
            The returned matrix is an :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricPositiveMatrix` if the selected
            indices are the same for the rows and the columns, and an
            :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix` or a
            :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` otherwise.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getSubMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.getSubMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
        
            Returns:
                the submatrix containing the data of the specified rows and columns
        
            Gets a submatrix.
        
            Rows and columns are indicated counting from 0 to n-1.
        
            The returned matrix is an :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix` if the selected indices
            are the same for the rows and the columns (same indices, same order), and an
            :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix` or a
            :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` otherwise.
        
            The returned matrix is an :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricPositiveMatrix` if the selected
            indices are the same for the rows and the columns (same indices, same order), and an
            :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix` or a
            :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` otherwise.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                selectedRows (int[]): the selected row indices
                selectedColumns (int[]): the selected column indices
        
            Returns:
                the submatrix containing the data in the specified rows and columns
        
            Extracts the submatrix corresponding to the specified indices.
        
            This method uses the same start/end indices to select the rows and columns to be extracted. These indices must be valid
            indices with respect to the dimensions of the matrix (valid indices range from 0 to n-1, with n the row/column dimension
            of the matrix). Calling this method is equivalent to calling
            :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getSubMatrix` using the same start/end indices for the rows and
            columns. The extracted submatrix is guaranteed to be symmetric. It will also remain positive semi-definite if the
            initial matrix originally is.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             // Initial matrix
             matrix = [a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                      [a :sub:`10` , a :sub:`11` , a :sub:`21` ]
                      [a :sub:`20` , a :sub:`21` , a :sub:`22` ]
             
             // Submatrix extraction
             matrix.getSubMatrix(1, 2) => [a :sub:`11` , a :sub:`21` ]
                                          [a :sub:`21` , a :sub:`22` ]
             
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.getSubMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.getSubMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.getSubMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                startIndex (int): the initial row/column index
                endIndex (int): the final row/column index (inclusive)
        
            Returns:
                the extracted submatrix
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray]) -> 'ArrayRowSymmetricPositiveMatrix':
        """
            Extracts the submatrix corresponding to the specified indices.
        
            This method uses a single index array to select the rows and columns to be extracted. All indices must be valid indices
            with respect to the dimensions of the matrix (valid indices range from 0 to n-1, with n the row/column dimension of the
            matrix). The provided index array is allowed to contain duplicates. Calling this method is equivalent to calling
            RealMatrix.getSubMatrix(int[], int[]) using the provided index array for the selected rows and columns. This method can
            be used to extract any submatrix and perform a symmetric reordering of its rows/columns. The extracted submatrix is
            guaranteed to be symmetric. It will also remain positive semi-definite if the initial matrix originally is.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             // Initial matrix
             matrix = [a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                      [a :sub:`10` , a :sub:`11` , a :sub:`21` ]
                      [a :sub:`20` , a :sub:`21` , a :sub:`22` ]
             
             // Submatrix extraction
             matrix.getSubMatrix([1, 2]) => [a :sub:`11` , a :sub:`21` ]
                                            [a :sub:`21` , a :sub:`22` ]
             
             // Rows/Columns permutation
             matrix.getSubMatrix([1, 2, 0]) => [a :sub:`11` , a :sub:`21` , a :sub:`10` ]
                                               [a :sub:`21` , a :sub:`22` , a :sub:`20` ]
                                               [a :sub:`10` , a :sub:`20` , a :sub:`00` ]
             
             // Submatrix extraction (with duplicated indices)
             matrix.getSubMatrix([1, 2, 0, 1, 0]) 
                  => [a :sub:`11` , a :sub:`21` , a :sub:`10` , a :sub:`11` , a :sub:`10` ]
                     [a :sub:`21` , a :sub:`22` , a :sub:`20` , a :sub:`21` , a :sub:`20` ]
                     [a :sub:`10` , a :sub:`20` , a :sub:`00` , a :sub:`10` , a :sub:`00` ]
                     [a :sub:`11` , a :sub:`21` , a :sub:`10` , a :sub:`11` , a :sub:`10` ]
                     [a :sub:`10` , a :sub:`20` , a :sub:`00` , a :sub:`10` , a :sub:`00` ]
             
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                index (int[]): the selected indices
        
            Returns:
                the extracted submatrix
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> RealMatrix: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> RealMatrix: ...
    def hashCode(self) -> int:
        """
            Computes a hash code for the matrix.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.hashCode` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Returns:
                hash code for matrix
        
        
        """
        ...
    @typing.overload
    def isPositiveSemiDefinite(self, double: float) -> bool:
        """
            Determines if this matrix is positive semi-definite or not.
        
            A symmetric matrix is considered to be positive semi-definite if its pivots are either strictly positive, or if the
            whole row is equal to zero after reduction (pivot included). In order to take into account possible numerical errors,
            the specified tolerance is added to the diagonal elements of the initial matrix.
        
            Parameters:
                absoluteTolerance (double): the absolute tolerance to take into account
        
            Returns:
                :code:`true` if this matrix is positive semi-definite, :code:`false` otherwise
        
            Determines if a symmetric matrix is positive semi-definite or not.
        
            A symmetric matrix is considered to be positive semi-definite if its pivots are either strictly positive, or if the
            whole row is equal to zero after reduction (pivot included). In order to take into account possible numerical errors,
            the specified tolerance is added to the diagonal elements of the initial matrix.
        
            Parameters:
                symmetricMatrix (:class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`): the symmetric matrix to be checked
                absoluteTolerance (double): the absolute tolerance to take into account
        
            Returns:
                :code:`true` if the provided matrix is positive semi-definite, :code:`false` otherwise
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def isPositiveSemiDefinite(symmetricMatrix: SymmetricMatrix, double: float) -> bool: ...
    def multiplyEntry(self, int: int, int2: int, double: float) -> None:
        """
            Multiplies (in place) the specified entry of :code:`this` matrix by a given value.
        
            Row and column indices start at 0.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.multiplyEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.multiplyEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                row (int): the row index of the entry to be modified
                column (int): the column index of the entry to be modified
                factor (double): the multiplication factor for the matrix entry
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    def positiveScalarAdd(self, double: float) -> 'ArrayRowSymmetricPositiveMatrix':
        """
            Returns the result of adding a positive scalar :code:`d` to the entries of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.positiveScalarAdd` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Parameters:
                d (double): the positive scalar value to be added to the entries of this matrix
        
            Returns:
                the symmetric positive semi-definite matrix resulting from the addition :code:`this`+ :code:`d`
        
        
        """
        ...
    def positiveScalarMultiply(self, double: float) -> 'ArrayRowSymmetricPositiveMatrix':
        """
            Returns the result of multiplying the entries of this matrix by a positive scalar :code:`d`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.positiveScalarMultiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Parameters:
                d (double): the positive scalar value by which to multiply the entries of this matrix by
        
            Returns:
                the symmetric positive semi-definite matrix resulting from the product :code:`d` ×:code:`this`
        
        
        """
        ...
    def power(self, int: int) -> 'ArrayRowSymmetricPositiveMatrix':
        """
            Returns the the result of multiplying this matrix with itself :code:`p` times.
        
            The exponent :code:`p` must be positive or equal to zero.
        
        
            This operation is only supported for square matrices.
        
        
            Depending on the underlying storage, numerical instabilities might occur for high powers.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.power` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.power` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.power` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.power` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                p (int): the exponent :code:`p` to which this matrix is to be raised
        
            Returns:
                the matrix resulting from raising this matrix to the power of :code:`p`
        
        
        """
        ...
    @typing.overload
    def quadraticMultiplication(self, realMatrix: RealMatrix) -> 'ArrayRowSymmetricPositiveMatrix':
        """
            Returns the result of the quadratic multiplication M×:code:`this`×M :sup:`T` , where M is the provided matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.quadraticMultiplication` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.quadraticMultiplication` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.quadraticMultiplication` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix M
        
            Returns:
                the matrix resulting from the quadratic multiplication M×:code:`this` ×M :sup:`T`
        
            Returns the result of the quadratic multiplication M×:code:`this`×M :sup:`T` , where M or M :sup:`T` is the provided
            matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.quadraticMultiplication` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.quadraticMultiplication` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.quadraticMultiplication` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix M or the matrix M :sup:`T`
                isTranspose (boolean): if :code:`true`, assumes the provided matrix is M :sup:`T` , otherwise assumes it is M
        
            Returns:
                the matrix resulting from the quadratic multiplication M×:code:`this` ×M :sup:`T`
        
        
        """
        ...
    @typing.overload
    def quadraticMultiplication(self, realMatrix: RealMatrix, boolean: bool) -> 'ArrayRowSymmetricPositiveMatrix': ...
    def scalarAdd(self, double: float) -> ArrayRowSymmetricMatrix:
        """
            Returns the result of adding a scalar :code:`d` to the entries of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.scalarAdd` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.scalarAdd` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.scalarAdd` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                d (double): the scalar value to be added to the entries of this matrix
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`d`
        
        
        """
        ...
    def scalarMultiply(self, double: float) -> ArrayRowSymmetricMatrix:
        """
            Returns the result of multiplying the entries of this matrix by the scalar :code:`d`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.scalarMultiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.scalarMultiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.scalarMultiply` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                d (double): the scalar value by which to multiply the entries of this matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`d`
        
        
        """
        ...
    def setColumn(self, int: int, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Replaces the entries of a given column with the entries of the specified data array.
        
            Column indices start at 0.
        
        
            The size of the provided data array must match the row dimension of this matrix.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                column (int): the index of the column to be replaced
                array (double[]): the column data array to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    def setColumnMatrix(self, int: int, realMatrix: RealMatrix) -> None:
        """
            Replaces the entries of a given column with the entries of the specified column matrix.
        
            Column indices start at 0.
        
        
            The provided matrix must have one column and the same number of rows as this matrix.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setColumnMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.setColumnMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                column (int): the index of the column to be replaced
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the column matrix to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    def setColumnVector(self, int: int, realVector: RealVector) -> None:
        """
            Replaces the entries of a given column with the entries of the specified vector.
        
            Column indices start at 0.
        
        
            The size of the provided vector must match the row dimension of this matrix.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setColumnVector` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.setColumnVector` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                column (int): the index of the column to be replaced
                vector (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the column vector to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    @staticmethod
    def setDefaultAbsolutePositivityThreshold(double: float) -> None:
        """
            Sets the default absolute positivity threshold, above which a value is considered to be positive.
        
            Parameters:
                threshold (`Double <http://docs.oracle.com/javase/8/docs/api/java/lang/Double.html?is-external=true>`): the new default absolute positivity threshold (≥0 or :code:`null`)
        
            Raises:
                : if the provided threshold is :code:`NaN` or is strictly negative
        
        
        """
        ...
    @staticmethod
    def setDefaultRelativePositivityThreshold(double: float) -> None:
        """
            Sets the default relative positivity threshold, above which a value is considered to be numerically significant when
            compared to another value.
        
            Parameters:
                threshold (`Double <http://docs.oracle.com/javase/8/docs/api/java/lang/Double.html?is-external=true>`): the new default relative positivity threshold (≥0 or :code:`null`)
        
            Raises:
                : if the provided threshold is :code:`NaN` or is strictly negative
        
        
        """
        ...
    def setEntry(self, int: int, int2: int, double: float) -> None:
        """
            Sets the entry at the specified row and column to a new value.
        
            Row and column indices start at 0.
        
            *This method automatically modify the symmetric element to ensure the symmetry of the matrix is preserved.*
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.setEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                row (int): the row index of entry to be set
                column (int): the column index of entry to be set
                value (double): the new value of the entry
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically (this operation is forbidden)
        
        
        """
        ...
    def setRow(self, int: int, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Replaces the entries of a given row with the entries of the specified data array.
        
            Row indices start at 0.
        
        
            The size of the provided data array must match the column dimension of this matrix.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the index of the row to be replaced
                array (double[]): the row data array to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    def setRowMatrix(self, int: int, realMatrix: RealMatrix) -> None:
        """
            Replaces the entries of a given row with the entries of the specified row matrix.
        
            Row indices start at 0.
        
        
            The provided matrix must have one row and the same number of columns as this matrix.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setRowMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.setRowMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the index of the row to be replaced
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the row matrix to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    def setRowVector(self, int: int, realVector: RealVector) -> None:
        """
            Replaces the entries of a given row with the entries of the specified vector.
        
            Row indices start at 0.
        
        
            The size of the provided vector must match the column dimension of this matrix.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setRowVector` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.setRowVector` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the index of the row to be replaced
                vector (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the row vector to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    def setSubMatrix(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int: int, int2: int) -> None:
        """
            Replaces part of the matrix with a given submatrix, starting at the specified row and column.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                subMatrix (double[][]): the array containing the replacement data of the targeted submatrix
                row (int): the row coordinate of the top, left element to be replaced
                column (int): the column coordinate of the top, left element to be replaced
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    @typing.overload
    def transpose(self) -> 'ArrayRowSymmetricPositiveMatrix':
        """
            Returns the transpose of this matrix..
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.transpose` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Returns:
                the transpose of this matrix
        
        """
        ...
    @typing.overload
    def transpose(self, boolean: bool) -> 'ArrayRowSymmetricPositiveMatrix':
        """
            Returns the transpose of this matrix.
        
            If :code:`forceCopy` is :code:`true`, the returned matrix is guaranteed to be a new instance, which can be modified
            without any risk of impacting the current instance. Otherwise, this method may simply return the current instance when
            the matrix is its own transpose (symmetric matrix).
            .
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix.transpose` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`
        
            Parameters:
                forceCopy (boolean): if :code:`true`, the transpose of the matrix is systematically stored in a new matrix; otherwise the method may return
                    the current instance when the matrix is its own transpose
        
            Returns:
                the transpose of this matrix
        
        
        """
        ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float:
        """
            Visits (and possibly change) all matrix entries in column order.
        
            Column order starts at upper left element, iterating through all elements of a column from top to bottom before going to
            the topmost element of the next column.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInColumnOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically (this operation is forbidden)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (and possibly change) some matrix entries in column order.
        
            Column order starts at upper left element, iterating through all elements of a column from top to bottom before going to
            the topmost element of the next column.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInColumnOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically (this operation is forbidden)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float:
        """
            Visits (and possibly change) all matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInOptimizedOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically (this operation is forbidden)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (and possibly change) some matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInOptimizedOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically (this operation is forbidden)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float:
        """
            Visits (and possibly change) all matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInRowOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically (this operation is forbidden)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (and possibly change) some matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInRowOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically (this operation is forbidden)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...

class DecomposedSymmetricPositiveMatrix(AbstractRealMatrix, SymmetricPositiveMatrix):
    """
    public class DecomposedSymmetricPositiveMatrix extends :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix` implements :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
    
        Stores a symmetric positive semi-definite matrix as A = B×B :sup:`T` .
    
        The matrix A is symmetric positive semi-definite by definition for any matrix B. Although the matrix A is always a NxN
        matrix, this is not necessarily the case for the matrix B: any NxM matrix multiplied by its transpose will yield a NxN
        matrix.
    
        The decomposition matrix B is not unique and building it is left to the user. Typically, this matrix is computed through
        a Cholesky decomposition A = L×L :sup:`T` , where L is a lower-triangular matrix. The matrix yielded by this
        decomposition is unique for positive definite matrices, but is not for positive semi-definite matrices (the
        implementation :class:`~fr.cnes.sirius.patrius.math.linear.CholeskyDecomposition` does not even support the latter). It
        can also be obtained through a LDL decomposition (A = L×D×L :sup:`T` ), or through an eigen decomposition
        (A = V×D×V :sup:`T` ).
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], boolean: bool): ...
    @typing.overload
    def __init__(self, realMatrix: RealMatrix): ...
    @typing.overload
    def __init__(self, realMatrix: RealMatrix, boolean: bool): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def add(self, decomposedSymmetricPositiveMatrix: 'DecomposedSymmetricPositiveMatrix') -> 'DecomposedSymmetricPositiveMatrix':
        """
            Returns the result of adding the matrix :code:`m` to this matrix.
        
            The returned matrix is, in order of priority:
        
              - A :class:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix` if the provided matrix is a
                :class:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix`;
              - An :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricPositiveMatrix` if it is any other type of
                :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`;
              - An :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix` if it is any other type of
                :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`;
              - An :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix` or a
                :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` if it is any other type of
                :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`.
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.add` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.add` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be added
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`m`
        
            Returns the result of adding the symmetric matrix :code:`m` to this matrix.
        
            The returned matrix is, in order of priority:
        
              - A :class:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix` if the provided matrix is a
                :class:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix`;
              - An :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricPositiveMatrix` if it is any other type of
                :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`;
              - An :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix` if it is any other type of
                :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`.
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.add` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`): the matrix to be added
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`m`
        
            Returns the result of adding the symmetric positive semi-definite matrix :code:`m` to this matrix.
        
            The returned matrix is, in order of priority:
        
              - A :class:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix` if the provided matrix is a
                :class:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix`;
              - An :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricPositiveMatrix` if it is any other type of
                :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`;
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.add` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`): the symmetric positive semi-definite matrix to be added
        
            Returns:
                the symmetric positive semi-definite matrix resulting from the addition :code:`this`+ :code:`m`
        
            Adds another :class:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix` to this matrix.
        
            Adding another :class:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix` amounts to concatenating
            their B matrices horizontally. As a result, the number of column of the matrix B increases with each addition. The
            concatenated matrix B is automatically resized afterward to ensure it is a NxN matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix`): the matrix to add
        
            Returns:
                the sum of the two matrices
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix.add`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix.resizeB`
        
            Adds another :class:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix` to this matrix.
        
            Adding another :class:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix` amounts to concatenating
            their B matrices horizontally. As a result, the number of column of the matrix B increases with each addition. Setting
            :code:`resize` to :code:`true` triggers a reduction or an extension of the matrix B afterward to ensure it is a NxN
            matrix.
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix`): the matrix to add
                resize (boolean): if :code:`true`, the matrix B is resized afterward to ensure it is NxN
        
            Returns:
                the sum of the two matrices
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix.resizeB`
        
        
        """
        ...
    @typing.overload
    def add(self, decomposedSymmetricPositiveMatrix: 'DecomposedSymmetricPositiveMatrix', boolean: bool) -> 'DecomposedSymmetricPositiveMatrix': ...
    @typing.overload
    def add(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def add(self, symmetricMatrix: SymmetricMatrix) -> SymmetricMatrix: ...
    @typing.overload
    def add(self, symmetricPositiveMatrix: SymmetricPositiveMatrix) -> SymmetricPositiveMatrix: ...
    def addToEntry(self, int: int, int2: int, double: float) -> None:
        """
            Adds (in place) a given value to the specified entry of this matrix.
        
            Row and column indices start at 0.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.addToEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.addToEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the row index of the entry to be modified
                column (int): the column index of the entry to be modified
                increment (double): the value to add to the matrix entry
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically (this operation is forbidden)
        
        
        """
        ...
    @staticmethod
    def castOrTransform(symmetricPositiveMatrix: SymmetricPositiveMatrix) -> 'DecomposedSymmetricPositiveMatrix':
        """
            Cast or transform the provided matrix into a
            :class:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix`.
        
            The transformation is performed thanks to a :class:`~fr.cnes.sirius.patrius.math.linear.CholeskyDecomposition`. In this
            case, the input matrix must be positive definite otherwise an exception is thrown).
        
            Parameters:
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`): The symmetric positive matrix to cast or transform
        
            Returns:
                the decomposed symmetric matrix (might be the same instance as the input if only a cast was performed)
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.linear.NonPositiveDefiniteMatrixException`: if a transformation is necessary and the matrix is not positive definite
        
        
        """
        ...
    @typing.overload
    def concatenateDiagonally(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Diagonally or anti-diagonally concatenates this matrix and another matrix :code:`m`.
        
            The way the two matrices are concatenated depends on the provided arguments:
        
        
            The matrix :code:`m` is placed in the right part of the concatenated matrix if :code:`rightConcatenation` is set to
            :code:`true`, and in its left part if it is set to :code:`false`. Similarly, the matrix :code:`m` is placed in the lower
            part of the concatenated matrix if :code:`lowerConcatenation` is set to :code:`true`, and in its upper part if it is set
            to :code:`false`. This matrix is then placed in the opposite part of the concatenated matrix (as an example, if the
            provided matrix is placed in the upper left part, this matrix will be placed in the lower right part, the remaining
            parts being filled with zeros).
        
            **Usage examples:**
        
            .. code-block: java
            
            
             // Diagonal concatenation
             this.concatenateDiagonally(m, true, true)   => [this, 0] 
                                                            [   0, m]
                                                          
             this.concatenateDiagonally(m, false, false) => [m,    0]
                                                            [0, this]
                                      
             // Anti-diagonal concatenation
             this.concatenateDiagonally(m, false, true)  => [0, this]
                                                            [m,    0]
                                                           
             this.concatenateDiagonally(m, true, false)  => [   0, m]
                                                            [this, 0]
             
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.concatenateDiagonally` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.concatenateDiagonally` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
                rightConcatenation (boolean): whether the matrix :code:`m` is to be placed in the right (:code:`true`) or left ( :code:`false`) part of the
                    concatenated matrix
                lowerConcatenation (boolean): whether the matrix :code:`m` is to be placed in the lower (:code:`true`) or upper ( :code:`false`) part of the
                    concatenated matrix
        
            Returns:
                the concatenated matrix
        
        
        """
        ...
    @typing.overload
    def concatenateDiagonally(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    @typing.overload
    def concatenateDiagonally(self, realMatrix: RealMatrix, boolean: bool, boolean2: bool) -> RealMatrix: ...
    @typing.overload
    def concatenateHorizontally(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Horizontally concatenates this matrix and another matrix :code:`m`, , placing it in the left or right part of the
            concatenated matrix.
        
            The way the two matrices are concatenated depends on the provided argument:
        
        
            The matrix :code:`m` is placed in the right part of the concatenated matrix if :code:`rightConcatenation` is set to
            :code:`true`, and in its left part if it is set to :code:`false`.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             this.concatenateHorizontally(m, true)  => [this, m] 
             
             this.concatenateHorizontally(m, false) => [m, this]
             
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.concatenateHorizontally` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.concatenateHorizontally` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
                rightConcatenation (boolean): whether the matrix :code:`m` is to be placed in the right (:code:`true`) or left ( :code:`false`) part of the
                    concatenated matrix
        
            Returns:
                the concatenated matrix
        
        
        """
        ...
    @typing.overload
    def concatenateHorizontally(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    @typing.overload
    def concatenateVertically(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Vertically concatenates this matrix and another matrix :code:`m`, placing it in the lower or upper part of the
            concatenated matrix.
        
            The way the two matrices are concatenated depends on the provided argument:
        
        
            The matrix :code:`m` is placed in the lower part of the concatenated matrix if :code:`lowerConcatenation` is set to
            :code:`true`, and in its upper part if it is set to :code:`false`.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             this.concatenateVertically(m, true)  => [this] 
                                                     [   m]
                                                          
             this.concatenateVertically(m, false) => [   m]
                                                     [this]
             
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.concatenateVertically` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.concatenateVertically` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be concatenated with this matrix
                lowerConcatenation (boolean): whether the matrix :code:`m` is to be placed in the lower (:code:`true`) or upper ( :code:`false`) part of the
                    concatenated matrix
        
            Returns:
                the concatenated matrix
        
        
        """
        ...
    @typing.overload
    def concatenateVertically(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    def copy(self) -> 'DecomposedSymmetricPositiveMatrix':
        """
            Returns a deep copy of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.copy` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.copy` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.copy` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.copy` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                a deep copy of this matrix
        
        
        """
        ...
    @staticmethod
    def createIdentityMatrix(int: int) -> 'DecomposedSymmetricPositiveMatrix':
        """
            Creates an identity matrix of the specified dimension.
        
            Parameters:
                dim (int): the dimension of the identity matrix
        
            Returns:
                the identity matrix built
        
        
        """
        ...
    def createMatrix(self, int: int, int2: int) -> 'DecomposedSymmetricPositiveMatrix':
        """
            Creates a new matrix of the same type as this matrix.
        
            The returned matrix is filled with zeros. Its size is determined by the specified row and column dimensions, which must
            both be strictly positive. Additional constraints on the dimensions may apply depending on the implementation (for
            example, symmetric matrices must be square, which implies that the row and column dimensions must be equal).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.createMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.createMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.createMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.createMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                rowDimension (int): the number of rows in the new matrix
                columnDimension (int): the number of columns in the new matrix
        
            Returns:
                a new matrix of the same type as this matrix
        
        
        """
        ...
    def getB(self) -> RealMatrix:
        """
            Gets the matrix B of the decomposition A = B×B :sup:`T` of this matrix.
        
            This method returns a copy of the B :sup:`T` matrix stored internally.
        
            Returns:
                the matrix B
        
        
        """
        ...
    @typing.overload
    def getBT(self) -> RealMatrix:
        """
            Gets the matrix B :sup:`T` of the decomposition A = B×B :sup:`T` of this matrix.
        
            Returns:
                the matrix B :sup:`T` (copy)
        
        """
        ...
    @typing.overload
    def getBT(self, boolean: bool) -> RealMatrix:
        """
            Gets the matrix B :sup:`T` of the decomposition A = B×B :sup:`T` of this matrix.
        
            This method returns a copy of the matrix B :sup:`T` if :code:`copyMatrix` is set to :code:`true`. Otherwise, it returns
            a direct reference to the matrix stored internally. Access to the internal matrix is provided for optimization purposes
            only. Modifying the returned matrix is strongly discouraged, as any change made on it will also apply to this matrix.
        
            Parameters:
                copyMatrix (boolean): whether to return a copy of the B :sup:`T` matrix (:code:`true`) or its reference ( :code:`false`)
        
            Returns:
                the matrix B :sup:`T` (copy or reference)
        
        
        """
        ...
    def getColumnDimension(self) -> int:
        """
            Returns the dimension of the domain of this operator.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix.getColumnDimension` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getColumnDimension` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the number of columns of the underlying matrix
        
        
        """
        ...
    def getColumnMatrix(self, int: int) -> RealMatrix:
        """
            Gets the entries of a given column as a column matrix.
        
            Column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getColumnMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getColumnMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                column (int): the index of the column to be fetched
        
            Returns:
                the extracted column matrix
        
        
        """
        ...
    def getEntry(self, int: int, int2: int) -> float:
        """
            Gets the entry at the specified row and column.
        
            Row and column indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the row index of entry to be fetched
                column (int): the column index of entry to be fetched
        
            Returns:
                the matrix entry at the specified row and column
        
        
        """
        ...
    @typing.overload
    def getInverse(self) -> 'DecomposedSymmetricPositiveMatrix':
        """
            Gets the inverse of the matrix.
        
            The inverse matrix is calculated using the default decomposition as follows:
        
        
            If A :sub:`1`  = B :sub:`1`  &times B :sub:`1` :sup:`T` and A :sub:`2`  = B :sub:`2`  &times B :sub:`2` :sup:`T`
              = A :sub:`1` :sup:`-1` , then we have B :sub:`2` :sup:`T`  = B :sub:`1` :sup:`-1` .
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getInverse` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the inverse matrix
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getDefaultDecomposition`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setDefaultDecomposition`
        
        public :class:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix` getInverse(`Function <http://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`,:class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`> decompositionBuilder)
        
            Gets the inverse of the matrix.
        
            The inverse of B :sub:`1` is computed using the provided decomposition as follows:
        
        
            If A :sub:`1`  = B :sub:`1`  &times B :sub:`1` :sup:`T` and A :sub:`2`  = B :sub:`2`  &times B :sub:`2` :sup:`T`
              = A :sub:`1` :sup:`-1` , then we have B :sub:`2` :sup:`T`  = B :sub:`1` :sup:`-1` .
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.getInverse` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getInverse` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                decompositionBuilder (`Function <http://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html?is-external=true>`<:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`,:class:`~fr.cnes.sirius.patrius.math.linear.Decomposition`> decompositionBuilder): the decomposition algorithm to use
        
            Returns:
                the inverse matrix
        
        
        """
        ...
    @typing.overload
    def getInverse(self, function: typing.Union[java.util.function.Function[RealMatrix, typing.Union[Decomposition, typing.Callable]], typing.Callable[[RealMatrix], typing.Union[Decomposition, typing.Callable]]]) -> 'DecomposedSymmetricPositiveMatrix': ...
    def getResizedB(self) -> RealMatrix:
        """
            Gets the matrix B after reducing or extending it to match this matrix's dimensions.
        
            If the matrix B has more columns than rows, this method returns the transpose of the matrix R resulting from the QR
            decomposition of B :sup:`T` , after truncating it to its first N rows (where N is the dimension of this matrix). If the
            matrix B has less columns than rows, this methods simply adds columns filled with zero to match its row dimensions.
        
            Returns:
                the resized matrix B
        
        
        """
        ...
    def getResizedBT(self) -> RealMatrix:
        """
            Gets the matrix B :sup:`T` after reducing or extending it to match this matrix's dimensions.
        
            If the matrix B has more columns than rows, this method returns the matrix R resulting from the QR decomposition of B
            :sup:`T` , after truncating it to its first N rows (where N is the dimension of this matrix). If the matrix B has less
            columns than rows, this methods simply adds columns filled with zero to match its row dimensions.
        
            Returns:
                the resized matrix B :sup:`T`
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
            Returns the dimension of the codomain of this operator.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix.getRowDimension` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getRowDimension` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the number of rows of the underlying matrix
        
        
        """
        ...
    def getRowMatrix(self, int: int) -> RealMatrix:
        """
            Gets the entries of a given row as a row matrix.
        
            Row indices start at 0.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getRowMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getRowMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the index of the row to be fetched
        
            Returns:
                the extracted row matrix
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int) -> 'DecomposedSymmetricPositiveMatrix':
        """
            Gets a submatrix.
        
            Rows and columns are indicated counting from 0 to n-1.
        
            The returned matrix is an :class:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix` if the selected
            indices are the same for the rows and the columns, and an
            :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix` or a
            :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` otherwise.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getSubMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.getSubMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
        
            Returns:
                the submatrix containing the data of the specified rows and columns
        
            Gets a submatrix.
        
            Rows and columns are indicated counting from 0 to n-1.
        
            The returned matrix is a :class:`~fr.cnes.sirius.patrius.math.linear.DecomposedSymmetricPositiveMatrix` if the selected
            indices are the same for the rows and the columns (same indices, same order), and an
            :class:`~fr.cnes.sirius.patrius.math.linear.Array2DRowRealMatrix` or a
            :class:`~fr.cnes.sirius.patrius.math.linear.BlockRealMatrix` otherwise.
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                selectedRows (int[]): the selected row indices
                selectedColumns (int[]): the selected column indices
        
            Returns:
                the submatrix containing the data in the specified rows and columns
        
            Extracts the submatrix corresponding to the specified indices.
        
            This method uses the same start/end indices to select the rows and columns to be extracted. These indices must be valid
            indices with respect to the dimensions of the matrix (valid indices range from 0 to n-1, with n the row/column dimension
            of the matrix). Calling this method is equivalent to calling
            :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.getSubMatrix` using the same start/end indices for the rows and
            columns. The extracted submatrix is guaranteed to be symmetric. It will also remain positive semi-definite if the
            initial matrix originally is.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             // Initial matrix
             matrix = [a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                      [a :sub:`10` , a :sub:`11` , a :sub:`21` ]
                      [a :sub:`20` , a :sub:`21` , a :sub:`22` ]
             
             // Submatrix extraction
             matrix.getSubMatrix(1, 2) => [a :sub:`11` , a :sub:`21` ]
                                          [a :sub:`21` , a :sub:`22` ]
             
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.getSubMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.getSubMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Parameters:
                startIndex (int): the initial row/column index
                endIndex (int): the final row/column index (inclusive)
        
            Returns:
                the extracted submatrix
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray]) -> 'DecomposedSymmetricPositiveMatrix':
        """
            Extracts the submatrix corresponding to the specified indices.
        
            This method uses a single index array to select the rows and columns to be extracted. All indices must be valid indices
            with respect to the dimensions of the matrix (valid indices range from 0 to n-1, with n the row/column dimension of the
            matrix). The provided index array is allowed to contain duplicates. Calling this method is equivalent to calling
            RealMatrix.getSubMatrix(int[], int[]) using the provided index array for the selected rows and columns. This method can
            be used to extract any submatrix and perform a symmetric reordering of its rows/columns. The extracted submatrix is
            guaranteed to be symmetric. It will also remain positive semi-definite if the initial matrix originally is.
        
            **Usage examples:**
        
            .. code-block: java
            
            
             // Initial matrix
             matrix = [a :sub:`00` , a :sub:`10` , a :sub:`20` ]
                      [a :sub:`10` , a :sub:`11` , a :sub:`21` ]
                      [a :sub:`20` , a :sub:`21` , a :sub:`22` ]
             
             // Submatrix extraction
             matrix.getSubMatrix([1, 2]) => [a :sub:`11` , a :sub:`21` ]
                                            [a :sub:`21` , a :sub:`22` ]
             
             // Rows/Columns permutation
             matrix.getSubMatrix([1, 2, 0]) => [a :sub:`11` , a :sub:`21` , a :sub:`10` ]
                                               [a :sub:`21` , a :sub:`22` , a :sub:`20` ]
                                               [a :sub:`10` , a :sub:`20` , a :sub:`00` ]
             
             // Submatrix extraction (with duplicated indices)
             matrix.getSubMatrix([1, 2, 0, 1, 0]) 
                  => [a :sub:`11` , a :sub:`21` , a :sub:`10` , a :sub:`11` , a :sub:`10` ]
                     [a :sub:`21` , a :sub:`22` , a :sub:`20` , a :sub:`21` , a :sub:`20` ]
                     [a :sub:`10` , a :sub:`20` , a :sub:`00` , a :sub:`10` , a :sub:`00` ]
                     [a :sub:`11` , a :sub:`21` , a :sub:`10` , a :sub:`11` , a :sub:`10` ]
                     [a :sub:`10` , a :sub:`20` , a :sub:`00` , a :sub:`10` , a :sub:`00` ]
             
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Parameters:
                indices (int[]): the selected indices
        
            Returns:
                the extracted submatrix
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> RealMatrix: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> RealMatrix: ...
    def getTransparentDimension(self) -> int:
        """
            Gets this matrix's transparent dimension (i.e. the number of columns of the matrix B).
        
            Returns:
                this matrix's transparent dimension
        
        
        """
        ...
    def isSquare(self) -> bool:
        """
            Is this a square matrix?
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix.isSquare` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.AnyMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.isSquare` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                true if the matrix is square (rowDimension = columnDimension)
        
        
        """
        ...
    @typing.overload
    def isSymmetric(self) -> bool:
        """
            Is this a symmetric matrix?
        
            This method indicates if the matrix is symmetric.
        
        
            To do so, the method checks that symmetric off-diagonal elements are numerically equal. Two elements are considered to
            have different values if their absolute and relative differences are both above the default tolerances.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            The absolute and relative tolerances both default to
            :meth:`~fr.cnes.sirius.patrius.math.util.Precision.DOUBLE_COMPARISON_EPSILON`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isSymmetric` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.isSymmetric` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                :code:`true` if this is a symmetric matrix, :code:`false` otherwise
        
        """
        ...
    @typing.overload
    def isSymmetric(self, double: float) -> bool:
        """
            Is this a symmetric matrix?
        
            This method indicates if the matrix is symmetric.
        
        
            To do so, the method checks that symmetric off-diagonal elements are numerically equal. Two elements are considered to
            have different values if their relative difference is above the specified tolerance.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isSymmetric` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.isSymmetric` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                relativeTolerance (double): the relative tolerance to take into account when comparing off-diagonal elements
        
            Returns:
                :code:`true` if this is a symmetric matrix, :code:`false` otherwise
        
            Is this a symmetric matrix?
        
            This method indicates if the matrix is symmetric.
        
        
            To do so, the method checks that symmetric off-diagonal elements are numerically equal. Two elements are considered to
            have different values if their absolute and relative differences are both above the specified tolerances.
        
            *This method systematically returns :code:`false` for non-square matrices.*
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.isSymmetric` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.isSymmetric` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                relativeTolerance (double): the relative tolerance to take into account when comparing off-diagonal elements
                absoluteTolerance (double): the absolute tolerance to take into account when comparing off-diagonal elements
        
            Returns:
                :code:`true` if this is a symmetric matrix, :code:`false` otherwise
        
        
        """
        ...
    @typing.overload
    def isSymmetric(self, double: float, double2: float) -> bool: ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Returns the result of postmultiplying this matrix by the matrix :code:`m` or its transpose :code:`m` :sup:`T` , then by
            the scalar :code:`d`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.multiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.multiply` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix by which to multiply this matrix by
                toTranspose (boolean): whether to compute the product :code:`this`×:code:`m`×:code:`d` ( :code:`toTranspose=false`), or the product
                    :code:`this`×:code:`m` :sup:`T` ×:code:`d` (:code:`toTranspose=true`)
                d (double): the scalar by which to multiply the resulting matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`m`×:code:`d` or :code:`this`×:code:`m` :sup:`T` ×:code:`d`
        
            Returns the result of postmultiplying this matrix by the diagonal matrix :code:`m`, then by the scalar :code:`d`.
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.multiply` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.DiagonalMatrix`): the diagonal matrix by which to multiply this matrix by
                d (double): the scalar by which to multiply the resulting matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`m`×:code:`d` or :code:`this`×:code:`m` :sup:`T` ×:code:`d`
        
        
        """
        ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix, boolean: bool) -> RealMatrix: ...
    @typing.overload
    def multiply(self, diagonalMatrix: DiagonalMatrix, double: float) -> RealMatrix: ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix, boolean: bool, double: float) -> RealMatrix: ...
    def multiplyEntry(self, int: int, int2: int, double: float) -> None:
        """
            Multiplies (in place) the specified entry of :code:`this` matrix by a given value.
        
            Row and column indices start at 0.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.multiplyEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.multiplyEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the row index of the entry to be modified
                column (int): the column index of the entry to be modified
                factor (double): the multiplication factor for the matrix entry
        
        
        """
        ...
    def positiveScalarAdd(self, double: float) -> 'DecomposedSymmetricPositiveMatrix':
        """
            Returns the result of adding a positive scalar :code:`d` to the entries of this matrix.
        
            The scalar addition is computed by doing a vertical concatenation between the B :sup:`T` matrix and a row matrix storing
            the square root of the scalar to add.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.positiveScalarAdd` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Parameters:
                d (double): the positive scalar value to be added to the entries of this matrix
        
            Returns:
                the symmetric positive semi-definite matrix resulting from the addition :code:`this`+ :code:`d`
        
        
        """
        ...
    def positiveScalarMultiply(self, double: float) -> 'DecomposedSymmetricPositiveMatrix':
        """
             Returns the result of multiplying the entries of this matrix by a positive scalar :code:`d`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.positiveScalarMultiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Parameters:
                d (double): the positive scalar value by which to multiply the entries of this matrix by
        
            Returns:
                the symmetric positive semi-definite matrix resulting from the product :code:`d` ×:code:`this`
        
        
        """
        ...
    def power(self, int: int) -> 'DecomposedSymmetricPositiveMatrix':
        """
            Returns the the result of multiplying this matrix with itself :code:`p` times.
        
            The exponent :code:`p` must be positive or equal to zero.
        
        
            This operation is only supported for square matrices.
        
        
            Depending on the underlying storage, numerical instabilities might occur for high powers.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.power` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.power` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.power` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.power` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                p (int): the exponent :code:`p` to which this matrix is to be raised
        
            Returns:
                the matrix resulting from raising this matrix to the power of :code:`p`
        
        
        """
        ...
    @typing.overload
    def quadraticMultiplication(self, realMatrix: RealMatrix) -> 'DecomposedSymmetricPositiveMatrix':
        """
            Returns the result of the quadratic multiplication M×:code:`this`×M :sup:`T` , where M is the provided matrix..
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.quadraticMultiplication` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.quadraticMultiplication` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix M
        
            Returns:
                the matrix resulting from the quadratic multiplication M×:code:`this` ×M :sup:`T`
        
            Returns the result of the quadratic multiplication M×:code:`this`×M :sup:`T` , where M or M :sup:`T` is the provided
            matrix..
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.quadraticMultiplication` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.quadraticMultiplication` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix M or the matrix M :sup:`T`
                isTranspose (boolean): if :code:`true`, assumes the provided matrix is M :sup:`T` , otherwise assumes it is M
        
            Returns:
                the matrix resulting from the quadratic multiplication M×:code:`this` ×M :sup:`T`
        
        
        """
        ...
    @typing.overload
    def quadraticMultiplication(self, realMatrix: RealMatrix, boolean: bool) -> 'DecomposedSymmetricPositiveMatrix': ...
    def resizeB(self) -> 'DecomposedSymmetricPositiveMatrix':
        """
            Reduces or extends the matrix B to ensure it is a NxN matrix.
        
            If the matrix B has more columns than rows, this method replaces the current matrix B by the matrix R resulting from the
            QR decomposition of B :sup:`T` , after truncating it to its first N rows (where N is the dimension of this matrix). If
            it has less columns than rows, it simply adds new columns filled with zero.
        
            Returns:
                this matrix
        
        
        """
        ...
    def scalarAdd(self, double: float) -> SymmetricMatrix:
        """
            Returns the result of adding a scalar :code:`d` to the entries of this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.scalarAdd` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.scalarAdd` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.scalarAdd` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                d (double): the scalar value to be added to the entries of this matrix
        
            Returns:
                the matrix resulting from the addition :code:`this`+:code:`d`
        
        
        """
        ...
    def scalarMultiply(self, double: float) -> SymmetricMatrix:
        """
            Returns the result of multiplying the entries of this matrix by the scalar :code:`d`.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.scalarMultiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.scalarMultiply` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.scalarMultiply` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                d (double): the scalar value by which to multiply the entries of this matrix by
        
            Returns:
                the matrix resulting from the product :code:`this`×:code:`d`
        
        
        """
        ...
    def setColumn(self, int: int, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Replaces the entries of a given column with the entries of the specified data array.
        
            Column indices start at 0.
        
        
            The size of the provided data array must match the row dimension of this matrix.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                column (int): the index of the column to be replaced
                array (double[]): the column data array to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    def setColumnMatrix(self, int: int, realMatrix: RealMatrix) -> None:
        """
            Replaces the entries of a given column with the entries of the specified column matrix.
        
            Column indices start at 0.
        
        
            The provided matrix must have one column and the same number of rows as this matrix.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setColumnMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.setColumnMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                column (int): the index of the column to be replaced
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the column matrix to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    def setColumnVector(self, int: int, realVector: RealVector) -> None:
        """
            Replaces the entries of a given column with the entries of the specified vector.
        
            Column indices start at 0.
        
        
            The size of the provided vector must match the row dimension of this matrix.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setColumnVector` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.setColumnVector` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                column (int): the index of the column to be replaced
                vector (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the column vector to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    def setEntry(self, int: int, int2: int, double: float) -> None:
        """
            Sets the entry for the specified row and column.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setEntry` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.setEntry` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the row index of entry to be set.
                column (int): the column index of entry to be set.
                value (double): the new value of the entry.
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    def setRow(self, int: int, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Replaces the entries of a given row with the entries of the specified data array.
        
            Row indices start at 0.
        
        
            The size of the provided data array must match the column dimension of this matrix.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the index of the row to be replaced
                array (double[]): the row data array to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    def setRowMatrix(self, int: int, realMatrix: RealMatrix) -> None:
        """
            Replaces the entries of a given row with the entries of the specified row matrix.
        
            Row indices start at 0.
        
        
            The provided matrix must have one row and the same number of columns as this matrix.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setRowMatrix` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.setRowMatrix` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the index of the row to be replaced
                matrix (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the row matrix to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    def setRowVector(self, int: int, realVector: RealVector) -> None:
        """
            Replaces the entries of a given row with the entries of the specified vector.
        
            Row indices start at 0.
        
        
            The size of the provided vector must match the column dimension of this matrix.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.setRowVector` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.setRowVector` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                row (int): the index of the row to be replaced
                vector (:class:`~fr.cnes.sirius.patrius.math.linear.RealVector`): the row vector to be copied
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    def setSubMatrix(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int: int, int2: int) -> None:
        """
            Replaces part of the matrix with a given submatrix, starting at the specified row and column.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                 in interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                 in class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                subMatrix (double[][]): the array containing the replacement data of the targeted submatrix
                row (int): the row coordinate of the top, left element to be replaced
                column (int): the column coordinate of the top, left element to be replaced
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically, since this operation is not supported
        
        
        """
        ...
    @typing.overload
    def subtract(self, symmetricMatrix: SymmetricMatrix) -> ArrayRowSymmetricMatrix:
        """
            Returns the result of subtracting the matrix :code:`m` from this matrix.
        
            The returned matrix is, in order of priority:
        
              - An :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricPositiveMatrix` if it is a
                :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`;
              - An :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix` if it is any other type of
                :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`.
        
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.subtract` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.subtract` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`): the matrix to be subtracted
        
            Returns:
                the matrix resulting from the subtraction :code:`this`-:code:`m`
        
            Returns the result of subtracting the symmetric matrix :code:`m` from this matrix.
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.subtract` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Parameters:
                m (:class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`): the matrix to be subtracted
        
            Returns:
                the matrix resulting from the subtraction :code:`this`-:code:`m`
        
        
        """
        ...
    @typing.overload
    def subtract(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def toArrayRowSymmetricMatrix(self) -> ArrayRowSymmetricMatrix:
        """
            Gets the matrix A = B×B :sup:`T` represented by this instance, stored in a new
            :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix`.
        
            Returns:
                a new :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricMatrix` instance storing the matrix A represented by
                this instance
        
        
        """
        ...
    def toArrayRowSymmetricPositiveMatrix(self) -> ArrayRowSymmetricPositiveMatrix:
        """
            Gets the matrix A = B×B :sup:`T` represented by this instance, stored in a new
            :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricPositiveMatrix`.
        
            Returns:
                a new :class:`~fr.cnes.sirius.patrius.math.linear.ArrayRowSymmetricPositiveMatrix` instance storing the matrix A
                represented by this instance
        
        
        """
        ...
    @typing.overload
    def transpose(self) -> 'DecomposedSymmetricPositiveMatrix':
        """
            Returns the transpose of this matrix..
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.transpose` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Returns:
                the transpose of this matrix
        
        """
        ...
    @typing.overload
    def transpose(self, boolean: bool) -> 'DecomposedSymmetricPositiveMatrix':
        """
            Returns the transpose of this matrix.
        
            If :code:`forceCopy` is :code:`true`, the returned matrix is guaranteed to be a new instance, which can be modified
            without any risk of impacting the current instance. Otherwise, this method may simply return the current instance when
            the matrix is its own transpose (symmetric matrix).
            .
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricMatrix`
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix.transpose` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.SymmetricPositiveMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.transpose` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                forceCopy (boolean): if :code:`true`, the transpose of the matrix is systematically stored in a new matrix; otherwise the method may return
                    the current instance when the matrix is its own transpose
        
            Returns:
                the transpose of this matrix
        
        
        """
        ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float:
        """
            Visits (and possibly change) all matrix entries in column order.
        
            Column order starts at upper left element, iterating through all elements of a column from top to bottom before going to
            the topmost element of the next column.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInColumnOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically (this operation is forbidden)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (and possibly change) some matrix entries in column order.
        
            Column order starts at upper left element, iterating through all elements of a column from top to bottom before going to
            the topmost element of the next column.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInColumnOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically (this operation is forbidden)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float:
        """
            Visits (and possibly change) all matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInOptimizedOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically (this operation is forbidden)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (and possibly change) some matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInOptimizedOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index (inclusive)
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically (this operation is forbidden)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float:
        """
            Visits (and possibly change) all matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInRowOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically (this operation is forbidden)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
            Visits (and possibly change) some matrix entries in row order.
        
            Row order starts at upper left element, iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            **Important:**
        
        
            This method systematically throws a :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`
            since this operation is not safe when dealing with symmetric positive definite matrices (the properties of the matrix
            are not guaranteed to be preserved).
        
            Specified by:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder` in
                interface :class:`~fr.cnes.sirius.patrius.math.linear.RealMatrix`
        
            Overrides:
                :meth:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix.walkInRowOrder` in
                class :class:`~fr.cnes.sirius.patrius.math.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor`): the visitor used to process all matrix entries
                startRow (int): the initial row index
                endRow (int): the final row index (inclusive)
                startColumn (int): the initial column index
                endColumn (int): the final column index
        
            Returns:
                the value returned by :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~fr.cnes.sirius.patrius.math.exception.MathUnsupportedOperationException`: systematically (this operation is forbidden)
        
            Also see:
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInRowOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~fr.cnes.sirius.patrius.math.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("fr.cnes.sirius.patrius.math.linear")``.

    AbstractFieldMatrix: typing.Type[AbstractFieldMatrix]
    AbstractRealMatrix: typing.Type[AbstractRealMatrix]
    AnyMatrix: typing.Type[AnyMatrix]
    Array2DRowFieldMatrix: typing.Type[Array2DRowFieldMatrix]
    Array2DRowRealMatrix: typing.Type[Array2DRowRealMatrix]
    ArrayFieldVector: typing.Type[ArrayFieldVector]
    ArrayRealVector: typing.Type[ArrayRealVector]
    ArrayRowSymmetricMatrix: typing.Type[ArrayRowSymmetricMatrix]
    ArrayRowSymmetricPositiveMatrix: typing.Type[ArrayRowSymmetricPositiveMatrix]
    BlockFieldMatrix: typing.Type[BlockFieldMatrix]
    BlockRealMatrix: typing.Type[BlockRealMatrix]
    CholeskyDecomposition: typing.Type[CholeskyDecomposition]
    ConjugateGradient: typing.Type[ConjugateGradient]
    DecomposedSymmetricPositiveMatrix: typing.Type[DecomposedSymmetricPositiveMatrix]
    Decomposition: typing.Type[Decomposition]
    DecompositionSolver: typing.Type[DecompositionSolver]
    DefaultFieldMatrixChangingVisitor: typing.Type[DefaultFieldMatrixChangingVisitor]
    DefaultFieldMatrixPreservingVisitor: typing.Type[DefaultFieldMatrixPreservingVisitor]
    DefaultIterativeLinearSolverEvent: typing.Type[DefaultIterativeLinearSolverEvent]
    DefaultRealMatrixChangingVisitor: typing.Type[DefaultRealMatrixChangingVisitor]
    DefaultRealMatrixPreservingVisitor: typing.Type[DefaultRealMatrixPreservingVisitor]
    DiagonalMatrix: typing.Type[DiagonalMatrix]
    EigenDecomposition: typing.Type[EigenDecomposition]
    FieldDecompositionSolver: typing.Type[FieldDecompositionSolver]
    FieldLUDecomposition: typing.Type[FieldLUDecomposition]
    FieldMatrix: typing.Type[FieldMatrix]
    FieldMatrixChangingVisitor: typing.Type[FieldMatrixChangingVisitor]
    FieldMatrixPreservingVisitor: typing.Type[FieldMatrixPreservingVisitor]
    FieldVector: typing.Type[FieldVector]
    IllConditionedOperatorException: typing.Type[IllConditionedOperatorException]
    IterativeLinearSolver: typing.Type[IterativeLinearSolver]
    IterativeLinearSolverEvent: typing.Type[IterativeLinearSolverEvent]
    JacobiPreconditioner: typing.Type[JacobiPreconditioner]
    LUDecomposition: typing.Type[LUDecomposition]
    MatrixDimensionMismatchException: typing.Type[MatrixDimensionMismatchException]
    MatrixUtils: typing.Type[MatrixUtils]
    NonPositiveDefiniteMatrixException: typing.Type[NonPositiveDefiniteMatrixException]
    NonPositiveDefiniteOperatorException: typing.Type[NonPositiveDefiniteOperatorException]
    NonSelfAdjointOperatorException: typing.Type[NonSelfAdjointOperatorException]
    NonSquareMatrixException: typing.Type[NonSquareMatrixException]
    NonSquareOperatorException: typing.Type[NonSquareOperatorException]
    NonSymmetricMatrixException: typing.Type[NonSymmetricMatrixException]
    PreconditionedIterativeLinearSolver: typing.Type[PreconditionedIterativeLinearSolver]
    QRDecomposition: typing.Type[QRDecomposition]
    RealLinearOperator: typing.Type[RealLinearOperator]
    RealMatrix: typing.Type[RealMatrix]
    RealMatrixChangingVisitor: typing.Type[RealMatrixChangingVisitor]
    RealMatrixFormat: typing.Type[RealMatrixFormat]
    RealMatrixPreservingVisitor: typing.Type[RealMatrixPreservingVisitor]
    RealVector: typing.Type[RealVector]
    RealVectorChangingVisitor: typing.Type[RealVectorChangingVisitor]
    RealVectorFormat: typing.Type[RealVectorFormat]
    RealVectorPreservingVisitor: typing.Type[RealVectorPreservingVisitor]
    RectangularCholeskyDecomposition: typing.Type[RectangularCholeskyDecomposition]
    SingularMatrixException: typing.Type[SingularMatrixException]
    SingularOperatorException: typing.Type[SingularOperatorException]
    SingularValueDecomposition: typing.Type[SingularValueDecomposition]
    SymmLQ: typing.Type[SymmLQ]
    SymmetricMatrix: typing.Type[SymmetricMatrix]
    SymmetricPositiveMatrix: typing.Type[SymmetricPositiveMatrix]
    UDDecomposition: typing.Type[UDDecomposition]
    UDDecompositionImpl: typing.Type[UDDecompositionImpl]
