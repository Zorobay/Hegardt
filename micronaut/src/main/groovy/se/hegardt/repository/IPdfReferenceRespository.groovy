package se.hegardt.repository

import groovy.transform.CompileStatic
import io.micronaut.data.annotation.Repository
import io.micronaut.data.jpa.repository.JpaRepository
import se.hegardt.domain.PdfReference

@CompileStatic
interface IPdfReferenceRespository extends JpaRepository<PdfReference, Long> {

    Optional<PdfReference> findByPersonId(Long personId)
}
