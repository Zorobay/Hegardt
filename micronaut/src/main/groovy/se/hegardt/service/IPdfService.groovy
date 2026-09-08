package se.hegardt.service

import se.hegardt.domain.PdfReference

interface IPdfService {

    List<PdfReference> findAll()

}
