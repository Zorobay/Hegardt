package se.hegardt.repository

import groovy.transform.CompileStatic
import io.micronaut.data.annotation.Repository
import io.micronaut.data.jpa.repository.JpaRepository
import se.hegardt.domain.PdfReference
import se.hegardt.dto.PdfReferenceDto


@Repository
@CompileStatic
abstract class PdfReferenceRespository implements JpaRepository<PdfReference, Long>{

}
