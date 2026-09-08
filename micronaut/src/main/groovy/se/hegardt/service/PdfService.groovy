package se.hegardt.service

import groovy.transform.CompileStatic
import jakarta.inject.Singleton
import se.hegardt.domain.PdfReference
import se.hegardt.repository.PdfReferenceRespository

@Singleton
@CompileStatic
class PdfService implements IPdfService {
    private final PdfReferenceRespository repository

    PdfService(PdfReferenceRespository respository) {
        this.repository = respository
    }

    List<PdfReference> findAll() {
        repository.findAll()
    }
}
