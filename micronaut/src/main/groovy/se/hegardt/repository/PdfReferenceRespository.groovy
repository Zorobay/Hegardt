package se.hegardt.repository

import groovy.transform.CompileStatic
import io.micronaut.data.annotation.Repository

@SuppressWarnings(['AbstractClassWithoutAbstractMethod'])
@Repository
@CompileStatic
abstract class PdfReferenceRespository implements IPdfReferenceRespository {

}
