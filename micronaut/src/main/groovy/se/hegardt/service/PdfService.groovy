package se.hegardt.service

import groovy.transform.CompileStatic
import jakarta.inject.Singleton
import se.hegardt.domain.PdfReference
import se.hegardt.repository.PdfReferenceRespository

@Singleton
@CompileStatic
class PdfService implements IPdfService {
    private final PdfReferenceRespository repository

    PdfService(PdfReferenceRespository repository) {
        this.repository = repository
    }

    List<PdfReference> findAll() {
        return repository.findAll()
    }
}
