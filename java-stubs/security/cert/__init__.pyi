
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java
import java.io
import java.lang
import java.math
import java.net
import java.security
import java.util
import javax.security.auth.x500
import jpype
import typing



class CRL:
    def getType(self) -> str: ...
    def isRevoked(self, certificate: 'Certificate') -> bool: ...
    def toString(self) -> str: ...

class CRLException(java.security.GeneralSecurityException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class CRLReason(java.lang.Enum['CRLReason']):
    UNSPECIFIED: typing.ClassVar['CRLReason'] = ...
    KEY_COMPROMISE: typing.ClassVar['CRLReason'] = ...
    CA_COMPROMISE: typing.ClassVar['CRLReason'] = ...
    AFFILIATION_CHANGED: typing.ClassVar['CRLReason'] = ...
    SUPERSEDED: typing.ClassVar['CRLReason'] = ...
    CESSATION_OF_OPERATION: typing.ClassVar['CRLReason'] = ...
    CERTIFICATE_HOLD: typing.ClassVar['CRLReason'] = ...
    UNUSED: typing.ClassVar['CRLReason'] = ...
    REMOVE_FROM_CRL: typing.ClassVar['CRLReason'] = ...
    PRIVILEGE_WITHDRAWN: typing.ClassVar['CRLReason'] = ...
    AA_COMPROMISE: typing.ClassVar['CRLReason'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'CRLReason': ...
    @staticmethod
    def values() -> typing.MutableSequence['CRLReason']: ...

class CRLSelector(java.lang.Cloneable):
    def clone(self) -> typing.Any: ...
    def match(self, cRL: CRL) -> bool: ...

class CertPath(java.io.Serializable):
    def equals(self, object: typing.Any) -> bool: ...
    def getCertificates(self) -> java.util.List['Certificate']: ...
    @typing.overload
    def getEncoded(self) -> typing.MutableSequence[int]: ...
    @typing.overload
    def getEncoded(self, string: str) -> typing.MutableSequence[int]: ...
    def getEncodings(self) -> java.util.Iterator[str]: ...
    def getType(self) -> str: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class CertPathBuilder:
    def build(self, certPathParameters: typing.Union['CertPathParameters', typing.Callable]) -> 'CertPathBuilderResult': ...
    def getAlgorithm(self) -> str: ...
    @staticmethod
    def getDefaultType() -> str: ...
    @typing.overload
    @staticmethod
    def getInstance(string: str) -> 'CertPathBuilder': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, string2: str) -> 'CertPathBuilder': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, provider: java.security.Provider) -> 'CertPathBuilder': ...
    def getProvider(self) -> java.security.Provider: ...
    def getRevocationChecker(self) -> 'CertPathChecker': ...

class CertPathBuilderException(java.security.GeneralSecurityException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class CertPathBuilderResult(java.lang.Cloneable):
    def clone(self) -> typing.Any: ...
    def getCertPath(self) -> CertPath: ...

class CertPathBuilderSpi:
    def __init__(self): ...
    def engineBuild(self, certPathParameters: typing.Union['CertPathParameters', typing.Callable]) -> CertPathBuilderResult: ...
    def engineGetRevocationChecker(self) -> 'CertPathChecker': ...

class CertPathChecker:
    def check(self, certificate: 'Certificate') -> None: ...
    def init(self, boolean: bool) -> None: ...
    def isForwardCheckingSupported(self) -> bool: ...

class CertPathParameters(java.lang.Cloneable):
    def clone(self) -> typing.Any: ...

class CertPathValidator:
    def getAlgorithm(self) -> str: ...
    @staticmethod
    def getDefaultType() -> str: ...
    @typing.overload
    @staticmethod
    def getInstance(string: str) -> 'CertPathValidator': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, string2: str) -> 'CertPathValidator': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, provider: java.security.Provider) -> 'CertPathValidator': ...
    def getProvider(self) -> java.security.Provider: ...
    def getRevocationChecker(self) -> CertPathChecker: ...
    def validate(self, certPath: CertPath, certPathParameters: typing.Union[CertPathParameters, typing.Callable]) -> 'CertPathValidatorResult': ...

class CertPathValidatorResult(java.lang.Cloneable):
    def clone(self) -> typing.Any: ...

class CertPathValidatorSpi:
    def __init__(self): ...
    def engineGetRevocationChecker(self) -> CertPathChecker: ...
    def engineValidate(self, certPath: CertPath, certPathParameters: typing.Union[CertPathParameters, typing.Callable]) -> CertPathValidatorResult: ...

class CertSelector(java.lang.Cloneable):
    def clone(self) -> typing.Any: ...
    def match(self, certificate: 'Certificate') -> bool: ...

class CertStore:
    def getCRLs(self, cRLSelector: CRLSelector) -> java.util.Collection[CRL]: ...
    def getCertStoreParameters(self) -> 'CertStoreParameters': ...
    def getCertificates(self, certSelector: CertSelector) -> java.util.Collection['Certificate']: ...
    @staticmethod
    def getDefaultType() -> str: ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, certStoreParameters: typing.Union['CertStoreParameters', typing.Callable]) -> 'CertStore': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, certStoreParameters: typing.Union['CertStoreParameters', typing.Callable], string2: str) -> 'CertStore': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, certStoreParameters: typing.Union['CertStoreParameters', typing.Callable], provider: java.security.Provider) -> 'CertStore': ...
    def getProvider(self) -> java.security.Provider: ...
    def getType(self) -> str: ...

class CertStoreException(java.security.GeneralSecurityException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class CertStoreParameters(java.lang.Cloneable):
    def clone(self) -> typing.Any: ...

class CertStoreSpi:
    def __init__(self, certStoreParameters: typing.Union[CertStoreParameters, typing.Callable]): ...
    def engineGetCRLs(self, cRLSelector: CRLSelector) -> java.util.Collection[CRL]: ...
    def engineGetCertificates(self, certSelector: CertSelector) -> java.util.Collection['Certificate']: ...

class Certificate(java.io.Serializable):
    def equals(self, object: typing.Any) -> bool: ...
    def getEncoded(self) -> typing.MutableSequence[int]: ...
    def getPublicKey(self) -> java.security.PublicKey: ...
    def getType(self) -> str: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    @typing.overload
    def verify(self, publicKey: java.security.PublicKey) -> None: ...
    @typing.overload
    def verify(self, publicKey: java.security.PublicKey, string: str) -> None: ...
    @typing.overload
    def verify(self, publicKey: java.security.PublicKey, provider: java.security.Provider) -> None: ...

class CertificateException(java.security.GeneralSecurityException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class CertificateFactory:
    def generateCRL(self, inputStream: java.io.InputStream) -> CRL: ...
    def generateCRLs(self, inputStream: java.io.InputStream) -> java.util.Collection[CRL]: ...
    @typing.overload
    def generateCertPath(self, inputStream: java.io.InputStream) -> CertPath: ...
    @typing.overload
    def generateCertPath(self, inputStream: java.io.InputStream, string: str) -> CertPath: ...
    @typing.overload
    def generateCertPath(self, list: java.util.List[Certificate]) -> CertPath: ...
    def generateCertificate(self, inputStream: java.io.InputStream) -> Certificate: ...
    def generateCertificates(self, inputStream: java.io.InputStream) -> java.util.Collection[Certificate]: ...
    def getCertPathEncodings(self) -> java.util.Iterator[str]: ...
    @typing.overload
    @staticmethod
    def getInstance(string: str) -> 'CertificateFactory': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, string2: str) -> 'CertificateFactory': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, provider: java.security.Provider) -> 'CertificateFactory': ...
    def getProvider(self) -> java.security.Provider: ...
    def getType(self) -> str: ...

class CertificateFactorySpi:
    def __init__(self): ...
    def engineGenerateCRL(self, inputStream: java.io.InputStream) -> CRL: ...
    def engineGenerateCRLs(self, inputStream: java.io.InputStream) -> java.util.Collection[CRL]: ...
    @typing.overload
    def engineGenerateCertPath(self, inputStream: java.io.InputStream) -> CertPath: ...
    @typing.overload
    def engineGenerateCertPath(self, inputStream: java.io.InputStream, string: str) -> CertPath: ...
    @typing.overload
    def engineGenerateCertPath(self, list: java.util.List[Certificate]) -> CertPath: ...
    def engineGenerateCertificate(self, inputStream: java.io.InputStream) -> Certificate: ...
    def engineGenerateCertificates(self, inputStream: java.io.InputStream) -> java.util.Collection[Certificate]: ...
    def engineGetCertPathEncodings(self) -> java.util.Iterator[str]: ...

class Extension:
    def encode(self, outputStream: java.io.OutputStream) -> None: ...
    def getId(self) -> str: ...
    def getValue(self) -> typing.MutableSequence[int]: ...
    def isCritical(self) -> bool: ...

class PolicyNode:
    def getChildren(self) -> java.util.Iterator['PolicyNode']: ...
    def getDepth(self) -> int: ...
    def getExpectedPolicies(self) -> java.util.Set[str]: ...
    def getParent(self) -> 'PolicyNode': ...
    def getPolicyQualifiers(self) -> java.util.Set['PolicyQualifierInfo']: ...
    def getValidPolicy(self) -> str: ...
    def isCritical(self) -> bool: ...

class PolicyQualifierInfo:
    def __init__(self, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]): ...
    def getEncoded(self) -> typing.MutableSequence[int]: ...
    def getPolicyQualifier(self) -> typing.MutableSequence[int]: ...
    def getPolicyQualifierId(self) -> str: ...
    def toString(self) -> str: ...

class TrustAnchor:
    @typing.overload
    def __init__(self, string: str, publicKey: java.security.PublicKey, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]): ...
    @typing.overload
    def __init__(self, x509Certificate: 'X509Certificate', byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]): ...
    @typing.overload
    def __init__(self, x500Principal: javax.security.auth.x500.X500Principal, publicKey: java.security.PublicKey, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]): ...
    def getCA(self) -> javax.security.auth.x500.X500Principal: ...
    def getCAName(self) -> str: ...
    def getCAPublicKey(self) -> java.security.PublicKey: ...
    def getNameConstraints(self) -> typing.MutableSequence[int]: ...
    def getTrustedCert(self) -> 'X509Certificate': ...
    def toString(self) -> str: ...

class X509Extension:
    def getCriticalExtensionOIDs(self) -> java.util.Set[str]: ...
    def getExtensionValue(self, string: str) -> typing.MutableSequence[int]: ...
    def getNonCriticalExtensionOIDs(self) -> java.util.Set[str]: ...
    def hasUnsupportedCriticalExtension(self) -> bool: ...

class CertificateEncodingException(CertificateException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class CertificateExpiredException(CertificateException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class CertificateNotYetValidException(CertificateException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class CertificateParsingException(CertificateException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class CertificateRevokedException(CertificateException):
    def __init__(self, date: java.util.Date, cRLReason: CRLReason, x500Principal: javax.security.auth.x500.X500Principal, map: typing.Union[java.util.Map[str, Extension], typing.Mapping[str, Extension]]): ...
    def getAuthorityName(self) -> javax.security.auth.x500.X500Principal: ...
    def getExtensions(self) -> java.util.Map[str, Extension]: ...
    def getInvalidityDate(self) -> java.util.Date: ...
    def getMessage(self) -> str: ...
    def getRevocationDate(self) -> java.util.Date: ...
    def getRevocationReason(self) -> CRLReason: ...

class CollectionCertStoreParameters(CertStoreParameters):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any]]): ...
    def clone(self) -> typing.Any: ...
    def getCollection(self) -> java.util.Collection[typing.Any]: ...
    def toString(self) -> str: ...

class LDAPCertStoreParameters(CertStoreParameters):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, int: int): ...
    def clone(self) -> typing.Any: ...
    def getPort(self) -> int: ...
    def getServerName(self) -> str: ...
    def toString(self) -> str: ...

class PKIXCertPathChecker(CertPathChecker, java.lang.Cloneable):
    @typing.overload
    def check(self, certificate: Certificate, collection: typing.Union[java.util.Collection[str], typing.Sequence[str], typing.Set[str]]) -> None: ...
    @typing.overload
    def check(self, certificate: Certificate) -> None: ...
    def clone(self) -> typing.Any: ...
    def getSupportedExtensions(self) -> java.util.Set[str]: ...
    def init(self, boolean: bool) -> None: ...
    def isForwardCheckingSupported(self) -> bool: ...

class PKIXCertPathValidatorResult(CertPathValidatorResult):
    def __init__(self, trustAnchor: TrustAnchor, policyNode: PolicyNode, publicKey: java.security.PublicKey): ...
    def clone(self) -> typing.Any: ...
    def getPolicyTree(self) -> PolicyNode: ...
    def getPublicKey(self) -> java.security.PublicKey: ...
    def getTrustAnchor(self) -> TrustAnchor: ...
    def toString(self) -> str: ...

class PKIXParameters(CertPathParameters):
    @typing.overload
    def __init__(self, keyStore: java.security.KeyStore): ...
    @typing.overload
    def __init__(self, set: java.util.Set[TrustAnchor]): ...
    def addCertPathChecker(self, pKIXCertPathChecker: PKIXCertPathChecker) -> None: ...
    def addCertStore(self, certStore: CertStore) -> None: ...
    def clone(self) -> typing.Any: ...
    def getCertPathCheckers(self) -> java.util.List[PKIXCertPathChecker]: ...
    def getCertStores(self) -> java.util.List[CertStore]: ...
    def getDate(self) -> java.util.Date: ...
    def getInitialPolicies(self) -> java.util.Set[str]: ...
    def getPolicyQualifiersRejected(self) -> bool: ...
    def getSigProvider(self) -> str: ...
    def getTargetCertConstraints(self) -> CertSelector: ...
    def getTrustAnchors(self) -> java.util.Set[TrustAnchor]: ...
    def isAnyPolicyInhibited(self) -> bool: ...
    def isExplicitPolicyRequired(self) -> bool: ...
    def isPolicyMappingInhibited(self) -> bool: ...
    def isRevocationEnabled(self) -> bool: ...
    def setAnyPolicyInhibited(self, boolean: bool) -> None: ...
    def setCertPathCheckers(self, list: java.util.List[PKIXCertPathChecker]) -> None: ...
    def setCertStores(self, list: java.util.List[CertStore]) -> None: ...
    def setDate(self, date: java.util.Date) -> None: ...
    def setExplicitPolicyRequired(self, boolean: bool) -> None: ...
    def setInitialPolicies(self, set: java.util.Set[str]) -> None: ...
    def setPolicyMappingInhibited(self, boolean: bool) -> None: ...
    def setPolicyQualifiersRejected(self, boolean: bool) -> None: ...
    def setRevocationEnabled(self, boolean: bool) -> None: ...
    def setSigProvider(self, string: str) -> None: ...
    def setTargetCertConstraints(self, certSelector: CertSelector) -> None: ...
    def setTrustAnchors(self, set: java.util.Set[TrustAnchor]) -> None: ...
    def toString(self) -> str: ...

class URICertStoreParameters(CertStoreParameters):
    def __init__(self, uRI: java.net.URI): ...
    def clone(self) -> 'URICertStoreParameters': ...
    def equals(self, object: typing.Any) -> bool: ...
    def getURI(self) -> java.net.URI: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class X509CRL(CRL, X509Extension):
    def equals(self, object: typing.Any) -> bool: ...
    def getEncoded(self) -> typing.MutableSequence[int]: ...
    def getIssuerDN(self) -> java.security.Principal: ...
    def getIssuerX500Principal(self) -> javax.security.auth.x500.X500Principal: ...
    def getNextUpdate(self) -> java.util.Date: ...
    @typing.overload
    def getRevokedCertificate(self, bigInteger: java.math.BigInteger) -> 'X509CRLEntry': ...
    @typing.overload
    def getRevokedCertificate(self, x509Certificate: 'X509Certificate') -> 'X509CRLEntry': ...
    def getRevokedCertificates(self) -> java.util.Set['X509CRLEntry']: ...
    def getSigAlgName(self) -> str: ...
    def getSigAlgOID(self) -> str: ...
    def getSigAlgParams(self) -> typing.MutableSequence[int]: ...
    def getSignature(self) -> typing.MutableSequence[int]: ...
    def getTBSCertList(self) -> typing.MutableSequence[int]: ...
    def getThisUpdate(self) -> java.util.Date: ...
    def getVersion(self) -> int: ...
    def hashCode(self) -> int: ...
    @typing.overload
    def verify(self, publicKey: java.security.PublicKey) -> None: ...
    @typing.overload
    def verify(self, publicKey: java.security.PublicKey, string: str) -> None: ...
    @typing.overload
    def verify(self, publicKey: java.security.PublicKey, provider: java.security.Provider) -> None: ...

class X509CRLEntry(X509Extension):
    def __init__(self): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getCertificateIssuer(self) -> javax.security.auth.x500.X500Principal: ...
    def getEncoded(self) -> typing.MutableSequence[int]: ...
    def getRevocationDate(self) -> java.util.Date: ...
    def getRevocationReason(self) -> CRLReason: ...
    def getSerialNumber(self) -> java.math.BigInteger: ...
    def hasExtensions(self) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class X509CRLSelector(CRLSelector):
    def __init__(self): ...
    def addIssuer(self, x500Principal: javax.security.auth.x500.X500Principal) -> None: ...
    @typing.overload
    def addIssuerName(self, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> None: ...
    @typing.overload
    def addIssuerName(self, string: str) -> None: ...
    def clone(self) -> typing.Any: ...
    def getCertificateChecking(self) -> 'X509Certificate': ...
    def getDateAndTime(self) -> java.util.Date: ...
    def getIssuerNames(self) -> java.util.Collection[typing.Any]: ...
    def getIssuers(self) -> java.util.Collection[javax.security.auth.x500.X500Principal]: ...
    def getMaxCRL(self) -> java.math.BigInteger: ...
    def getMinCRL(self) -> java.math.BigInteger: ...
    def match(self, cRL: CRL) -> bool: ...
    def setCertificateChecking(self, x509Certificate: 'X509Certificate') -> None: ...
    def setDateAndTime(self, date: java.util.Date) -> None: ...
    def setIssuerNames(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any]]) -> None: ...
    def setIssuers(self, collection: typing.Union[java.util.Collection[javax.security.auth.x500.X500Principal], typing.Sequence[javax.security.auth.x500.X500Principal], typing.Set[javax.security.auth.x500.X500Principal]]) -> None: ...
    def setMaxCRLNumber(self, bigInteger: java.math.BigInteger) -> None: ...
    def setMinCRLNumber(self, bigInteger: java.math.BigInteger) -> None: ...
    def toString(self) -> str: ...

class X509CertSelector(CertSelector):
    def __init__(self): ...
    @typing.overload
    def addPathToName(self, int: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> None: ...
    @typing.overload
    def addPathToName(self, int: int, string: str) -> None: ...
    @typing.overload
    def addSubjectAlternativeName(self, int: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> None: ...
    @typing.overload
    def addSubjectAlternativeName(self, int: int, string: str) -> None: ...
    def clone(self) -> typing.Any: ...
    def getAuthorityKeyIdentifier(self) -> typing.MutableSequence[int]: ...
    def getBasicConstraints(self) -> int: ...
    def getCertificate(self) -> 'X509Certificate': ...
    def getCertificateValid(self) -> java.util.Date: ...
    def getExtendedKeyUsage(self) -> java.util.Set[str]: ...
    def getIssuer(self) -> javax.security.auth.x500.X500Principal: ...
    def getIssuerAsBytes(self) -> typing.MutableSequence[int]: ...
    def getIssuerAsString(self) -> str: ...
    def getKeyUsage(self) -> typing.MutableSequence[bool]: ...
    def getMatchAllSubjectAltNames(self) -> bool: ...
    def getNameConstraints(self) -> typing.MutableSequence[int]: ...
    def getPathToNames(self) -> java.util.Collection[java.util.List[typing.Any]]: ...
    def getPolicy(self) -> java.util.Set[str]: ...
    def getPrivateKeyValid(self) -> java.util.Date: ...
    def getSerialNumber(self) -> java.math.BigInteger: ...
    def getSubject(self) -> javax.security.auth.x500.X500Principal: ...
    def getSubjectAlternativeNames(self) -> java.util.Collection[java.util.List[typing.Any]]: ...
    def getSubjectAsBytes(self) -> typing.MutableSequence[int]: ...
    def getSubjectAsString(self) -> str: ...
    def getSubjectKeyIdentifier(self) -> typing.MutableSequence[int]: ...
    def getSubjectPublicKey(self) -> java.security.PublicKey: ...
    def getSubjectPublicKeyAlgID(self) -> str: ...
    def match(self, certificate: Certificate) -> bool: ...
    def setAuthorityKeyIdentifier(self, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> None: ...
    def setBasicConstraints(self, int: int) -> None: ...
    def setCertificate(self, x509Certificate: 'X509Certificate') -> None: ...
    def setCertificateValid(self, date: java.util.Date) -> None: ...
    def setExtendedKeyUsage(self, set: java.util.Set[str]) -> None: ...
    @typing.overload
    def setIssuer(self, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> None: ...
    @typing.overload
    def setIssuer(self, string: str) -> None: ...
    @typing.overload
    def setIssuer(self, x500Principal: javax.security.auth.x500.X500Principal) -> None: ...
    def setKeyUsage(self, booleanArray: typing.Union[typing.List[bool], jpype.JArray]) -> None: ...
    def setMatchAllSubjectAltNames(self, boolean: bool) -> None: ...
    def setNameConstraints(self, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> None: ...
    def setPathToNames(self, collection: typing.Union[java.util.Collection[java.util.List[typing.Any]], typing.Sequence[java.util.List[typing.Any]], typing.Set[java.util.List[typing.Any]]]) -> None: ...
    def setPolicy(self, set: java.util.Set[str]) -> None: ...
    def setPrivateKeyValid(self, date: java.util.Date) -> None: ...
    def setSerialNumber(self, bigInteger: java.math.BigInteger) -> None: ...
    @typing.overload
    def setSubject(self, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> None: ...
    @typing.overload
    def setSubject(self, string: str) -> None: ...
    @typing.overload
    def setSubject(self, x500Principal: javax.security.auth.x500.X500Principal) -> None: ...
    def setSubjectAlternativeNames(self, collection: typing.Union[java.util.Collection[java.util.List[typing.Any]], typing.Sequence[java.util.List[typing.Any]], typing.Set[java.util.List[typing.Any]]]) -> None: ...
    def setSubjectKeyIdentifier(self, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> None: ...
    @typing.overload
    def setSubjectPublicKey(self, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> None: ...
    @typing.overload
    def setSubjectPublicKey(self, publicKey: java.security.PublicKey) -> None: ...
    def setSubjectPublicKeyAlgID(self, string: str) -> None: ...
    def toString(self) -> str: ...

class X509Certificate(Certificate, X509Extension):
    @typing.overload
    def checkValidity(self) -> None: ...
    @typing.overload
    def checkValidity(self, date: java.util.Date) -> None: ...
    def getBasicConstraints(self) -> int: ...
    def getExtendedKeyUsage(self) -> java.util.List[str]: ...
    def getIssuerAlternativeNames(self) -> java.util.Collection[java.util.List[typing.Any]]: ...
    def getIssuerDN(self) -> java.security.Principal: ...
    def getIssuerUniqueID(self) -> typing.MutableSequence[bool]: ...
    def getIssuerX500Principal(self) -> javax.security.auth.x500.X500Principal: ...
    def getKeyUsage(self) -> typing.MutableSequence[bool]: ...
    def getNotAfter(self) -> java.util.Date: ...
    def getNotBefore(self) -> java.util.Date: ...
    def getSerialNumber(self) -> java.math.BigInteger: ...
    def getSigAlgName(self) -> str: ...
    def getSigAlgOID(self) -> str: ...
    def getSigAlgParams(self) -> typing.MutableSequence[int]: ...
    def getSignature(self) -> typing.MutableSequence[int]: ...
    def getSubjectAlternativeNames(self) -> java.util.Collection[java.util.List[typing.Any]]: ...
    def getSubjectDN(self) -> java.security.Principal: ...
    def getSubjectUniqueID(self) -> typing.MutableSequence[bool]: ...
    def getSubjectX500Principal(self) -> javax.security.auth.x500.X500Principal: ...
    def getTBSCertificate(self) -> typing.MutableSequence[int]: ...
    def getVersion(self) -> int: ...
    @typing.overload
    def verify(self, publicKey: java.security.PublicKey) -> None: ...
    @typing.overload
    def verify(self, publicKey: java.security.PublicKey, string: str) -> None: ...
    @typing.overload
    def verify(self, publicKey: java.security.PublicKey, provider: java.security.Provider) -> None: ...

class PKIXBuilderParameters(PKIXParameters):
    @typing.overload
    def __init__(self, keyStore: java.security.KeyStore, certSelector: CertSelector): ...
    @typing.overload
    def __init__(self, set: java.util.Set[TrustAnchor], certSelector: CertSelector): ...
    def getMaxPathLength(self) -> int: ...
    def setMaxPathLength(self, int: int) -> None: ...
    def toString(self) -> str: ...

class PKIXCertPathBuilderResult(PKIXCertPathValidatorResult, CertPathBuilderResult):
    def __init__(self, certPath: CertPath, trustAnchor: TrustAnchor, policyNode: PolicyNode, publicKey: java.security.PublicKey): ...
    def getCertPath(self) -> CertPath: ...
    def toString(self) -> str: ...

class PKIXRevocationChecker(PKIXCertPathChecker):
    def clone(self) -> 'PKIXRevocationChecker': ...
    def getOcspExtensions(self) -> java.util.List[Extension]: ...
    def getOcspResponder(self) -> java.net.URI: ...
    def getOcspResponderCert(self) -> X509Certificate: ...
    def getOcspResponses(self) -> java.util.Map[X509Certificate, typing.MutableSequence[int]]: ...
    def getOptions(self) -> java.util.Set['PKIXRevocationChecker.Option']: ...
    def getSoftFailExceptions(self) -> java.util.List['CertPathValidatorException']: ...
    def setOcspExtensions(self, list: java.util.List[Extension]) -> None: ...
    def setOcspResponder(self, uRI: java.net.URI) -> None: ...
    def setOcspResponderCert(self, x509Certificate: X509Certificate) -> None: ...
    def setOcspResponses(self, map: typing.Union[java.util.Map[X509Certificate, typing.Union[typing.List[int], jpype.JArray, bytes]], typing.Mapping[X509Certificate, typing.Union[typing.List[int], jpype.JArray, bytes]]]) -> None: ...
    def setOptions(self, set: java.util.Set['PKIXRevocationChecker.Option']) -> None: ...
    class Option(java.lang.Enum['PKIXRevocationChecker.Option']):
        ONLY_END_ENTITY: typing.ClassVar['PKIXRevocationChecker.Option'] = ...
        PREFER_CRLS: typing.ClassVar['PKIXRevocationChecker.Option'] = ...
        NO_FALLBACK: typing.ClassVar['PKIXRevocationChecker.Option'] = ...
        SOFT_FAIL: typing.ClassVar['PKIXRevocationChecker.Option'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'PKIXRevocationChecker.Option': ...
        @staticmethod
        def values() -> typing.MutableSequence['PKIXRevocationChecker.Option']: ...

class CertPathValidatorException(java.security.GeneralSecurityException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, certPath: CertPath, int: int): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, certPath: CertPath, int: int, reason: 'CertPathValidatorException.Reason'): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...
    def getCertPath(self) -> CertPath: ...
    def getIndex(self) -> int: ...
    def getReason(self) -> 'CertPathValidatorException.Reason': ...
    class BasicReason(java.lang.Enum['CertPathValidatorException.BasicReason'], java.security.cert.CertPathValidatorException.Reason):
        UNSPECIFIED: typing.ClassVar['CertPathValidatorException.BasicReason'] = ...
        EXPIRED: typing.ClassVar['CertPathValidatorException.BasicReason'] = ...
        NOT_YET_VALID: typing.ClassVar['CertPathValidatorException.BasicReason'] = ...
        REVOKED: typing.ClassVar['CertPathValidatorException.BasicReason'] = ...
        UNDETERMINED_REVOCATION_STATUS: typing.ClassVar['CertPathValidatorException.BasicReason'] = ...
        INVALID_SIGNATURE: typing.ClassVar['CertPathValidatorException.BasicReason'] = ...
        ALGORITHM_CONSTRAINED: typing.ClassVar['CertPathValidatorException.BasicReason'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'CertPathValidatorException.BasicReason': ...
        @staticmethod
        def values() -> typing.MutableSequence['CertPathValidatorException.BasicReason']: ...
    class Reason(java.io.Serializable): ...

class PKIXReason(java.lang.Enum['PKIXReason'], CertPathValidatorException.Reason):
    NAME_CHAINING: typing.ClassVar['PKIXReason'] = ...
    INVALID_KEY_USAGE: typing.ClassVar['PKIXReason'] = ...
    INVALID_POLICY: typing.ClassVar['PKIXReason'] = ...
    NO_TRUST_ANCHOR: typing.ClassVar['PKIXReason'] = ...
    UNRECOGNIZED_CRIT_EXT: typing.ClassVar['PKIXReason'] = ...
    NOT_CA_CERT: typing.ClassVar['PKIXReason'] = ...
    PATH_TOO_LONG: typing.ClassVar['PKIXReason'] = ...
    INVALID_NAME: typing.ClassVar['PKIXReason'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PKIXReason': ...
    @staticmethod
    def values() -> typing.MutableSequence['PKIXReason']: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.security.cert")``.

    CRL: typing.Type[CRL]
    CRLException: typing.Type[CRLException]
    CRLReason: typing.Type[CRLReason]
    CRLSelector: typing.Type[CRLSelector]
    CertPath: typing.Type[CertPath]
    CertPathBuilder: typing.Type[CertPathBuilder]
    CertPathBuilderException: typing.Type[CertPathBuilderException]
    CertPathBuilderResult: typing.Type[CertPathBuilderResult]
    CertPathBuilderSpi: typing.Type[CertPathBuilderSpi]
    CertPathChecker: typing.Type[CertPathChecker]
    CertPathParameters: typing.Type[CertPathParameters]
    CertPathValidator: typing.Type[CertPathValidator]
    CertPathValidatorException: typing.Type[CertPathValidatorException]
    CertPathValidatorResult: typing.Type[CertPathValidatorResult]
    CertPathValidatorSpi: typing.Type[CertPathValidatorSpi]
    CertSelector: typing.Type[CertSelector]
    CertStore: typing.Type[CertStore]
    CertStoreException: typing.Type[CertStoreException]
    CertStoreParameters: typing.Type[CertStoreParameters]
    CertStoreSpi: typing.Type[CertStoreSpi]
    Certificate: typing.Type[Certificate]
    CertificateEncodingException: typing.Type[CertificateEncodingException]
    CertificateException: typing.Type[CertificateException]
    CertificateExpiredException: typing.Type[CertificateExpiredException]
    CertificateFactory: typing.Type[CertificateFactory]
    CertificateFactorySpi: typing.Type[CertificateFactorySpi]
    CertificateNotYetValidException: typing.Type[CertificateNotYetValidException]
    CertificateParsingException: typing.Type[CertificateParsingException]
    CertificateRevokedException: typing.Type[CertificateRevokedException]
    CollectionCertStoreParameters: typing.Type[CollectionCertStoreParameters]
    Extension: typing.Type[Extension]
    LDAPCertStoreParameters: typing.Type[LDAPCertStoreParameters]
    PKIXBuilderParameters: typing.Type[PKIXBuilderParameters]
    PKIXCertPathBuilderResult: typing.Type[PKIXCertPathBuilderResult]
    PKIXCertPathChecker: typing.Type[PKIXCertPathChecker]
    PKIXCertPathValidatorResult: typing.Type[PKIXCertPathValidatorResult]
    PKIXParameters: typing.Type[PKIXParameters]
    PKIXReason: typing.Type[PKIXReason]
    PKIXRevocationChecker: typing.Type[PKIXRevocationChecker]
    PolicyNode: typing.Type[PolicyNode]
    PolicyQualifierInfo: typing.Type[PolicyQualifierInfo]
    TrustAnchor: typing.Type[TrustAnchor]
    URICertStoreParameters: typing.Type[URICertStoreParameters]
    X509CRL: typing.Type[X509CRL]
    X509CRLEntry: typing.Type[X509CRLEntry]
    X509CRLSelector: typing.Type[X509CRLSelector]
    X509CertSelector: typing.Type[X509CertSelector]
    X509Certificate: typing.Type[X509Certificate]
    X509Extension: typing.Type[X509Extension]
