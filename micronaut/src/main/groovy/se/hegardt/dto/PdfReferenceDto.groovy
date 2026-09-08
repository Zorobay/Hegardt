package se.hegardt.dto

import groovy.transform.CompileStatic
import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.PdfReference

@Serdeable
@CompileStatic
class PdfReferenceDto {
    Long id
    Integer pdfPage
    Double x0
    Double y0
    Double width
    Double height

    static PdfReferenceDto from(PdfReference pdfReference) {
        return new PdfReferenceDto(
            id: pdfReference.id,
            pdfPage: pdfReference.pdfPage,
            x0: pdfReference.x0,
            y0: pdfReference.y0,
            width: pdfReference.width,
            height: pdfReference.height
        )
    }
}
