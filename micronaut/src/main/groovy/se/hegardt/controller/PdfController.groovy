package se.hegardt.controller

import groovy.transform.CompileStatic
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import se.hegardt.domain.PdfReference
import se.hegardt.dto.PdfReferenceDto
import se.hegardt.service.IPdfService

@Controller('/pdf')
@CompileStatic
class PdfController {

    private final IPdfService pdfService

    PdfController(IPdfService pdfReferenceService) {
        this.pdfService = pdfReferenceService
    }

    @Get("/getAllReferences")
    HttpResponse<Map<Integer, List<PdfReferenceDto>>> getAllReferences() {
        return HttpResponse.ok(pdfService.findAll()
            .groupBy { PdfReference ref -> ref.pdfPage }
            .collectEntries { Integer page, List<PdfReference> refs -> [page, refs.collect { PdfReferenceDto.from(it) }] })
    }
}
